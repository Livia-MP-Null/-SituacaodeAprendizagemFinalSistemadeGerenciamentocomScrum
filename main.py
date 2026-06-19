import os
import time
import re
from datetime import datetime

# ═══════════════════════════════════════════════════════════
#  STOCKFLOW V5 - Sistema de Estoque e Cardapio de Restaurante
# ═══════════════════════════════════════════════════════════

# --- Cores ANSI ---
RESET, BOLD = "\033[0m", "\033[1m"
VERMELHO, VERDE, AMARELO, AZUL, CIANO = (
    "\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[96m")
PISCA = "\033[5m"

# --- Limites de validacao ---
LIMITE_COMPRA_KG     = 300        # max 300 kg (ou 300.000 g) por compra
LIMITE_COMPRA_UN     = 300        # max 300 unidades por compra
ANOS_MAX_VALIDADE    = 200        # validade nao pode estar a mais de 200 anos
EXCECOES_LONGA_VAL   = {"Queijo"} # itens que podem ter validade muito longa

# --- Dados do sistema ---
ADMINS = {"admin": "1234"}

estoque = {
    "Arroz":       {"qtd": 3000, "un": "g",  "validade": "30/06/2026", "custo": 0.005},
    "Feijao":      {"qtd": 1500, "un": "g",  "validade": "01/06/2026", "custo": 0.008},
    "Frango":      {"qtd": 2000, "un": "g",  "validade": "15/07/2026", "custo": 0.020},
    "Macarrao":    {"qtd": 2000, "un": "g",  "validade": "31/12/2026", "custo": 0.004},
    "Carne":       {"qtd": 1500, "un": "g",  "validade": "10/06/2026", "custo": 0.030},
    "Batata":      {"qtd": 2000, "un": "g",  "validade": "20/06/2026", "custo": 0.003},
    "Alface":      {"qtd": 800,  "un": "g",  "validade": "05/06/2026", "custo": 0.010},
    "Ovo":         {"qtd": 30,   "un": "un", "validade": "20/06/2026", "custo": 0.800},
    "Queijo":      {"qtd": 500,  "un": "g",  "validade": "25/06/2026", "custo": 0.040},
    "MolhoTomate": {"qtd": 1000, "un": "g",  "validade": "31/10/2026", "custo": 0.006},
}

cardapio = {
    "1": {"nome": "PF Tradicional",      "preco": 18.0, "ingr": {"Arroz": 200, "Feijao": 100, "Carne": 150}},
    "2": {"nome": "Parmegiana",          "preco": 22.0, "ingr": {"Arroz": 150, "Frango": 200, "MolhoTomate": 100, "Queijo": 50}},
    "3": {"nome": "Espaguete Bolonhesa", "preco": 20.0, "ingr": {"Macarrao": 200, "Carne": 150, "MolhoTomate": 150}},
    "4": {"nome": "Salada Caesar",       "preco": 14.0, "ingr": {"Alface": 150, "Queijo": 30, "Frango": 100}},
    "5": {"nome": "Omelete",             "preco": 12.0, "ingr": {"Ovo": 3, "Queijo": 40}},
    "6": {"nome": "Batata Frita",        "preco": 10.0, "ingr": {"Batata": 200}},
    "7": {"nome": "Frango Grelhado",     "preco": 19.0, "ingr": {"Frango": 250, "Batata": 150}},
    "8": {"nome": "Feijoadinha",         "preco": 16.0, "ingr": {"Feijao": 200, "Arroz": 150, "Carne": 100}},
}

pedidos, compras = [], []
ALERTA_MINIMO = 300

# --- Utilitarios ---
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input(f"\n  {CIANO}Pressione ENTER para continuar...{RESET}")

def data(txt):
    return datetime.strptime(txt, "%d/%m/%Y")

def agora():
    return datetime.now().strftime("%d/%m/%Y %H:%M")

def cabecalho(titulo):
    print(f"{BOLD}{AZUL}╔{'═'*52}╗")
    print(f"║{titulo.center(52)}║")
    print(f"╚{'═'*52}╝{RESET}")

def pedir_num(msg, minimo=0.0, maximo=None):
    while True:
        try:
            v = float(input(msg).strip().replace(",", "."))
            if v < minimo:
                print(f"  {AMARELO}Valor minimo: {minimo}{RESET}")
                continue
            if maximo is not None and v > maximo:
                print(f"  {AMARELO}Valor maximo permitido: {maximo}{RESET}")
                continue
            return v
        except ValueError:
            print(f"  {AMARELO}Digite um numero valido.{RESET}")

def pedir_txt(msg, vazio=False):
    while True:
        v = input(msg).strip()
        if v or vazio:
            return v
        print(f"  {AMARELO}Campo obrigatorio.{RESET}")

# --- Validacao do nome do cliente ---
# Aceita SOMENTE letras (incl. acentuadas) e espacos. Nada de numeros/simbolos.
REGEX_NOME = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ ]+$")

def pedir_nome_cliente():
    while True:
        nome = input("  Digite seu nome: ").strip()
        if not nome:
            print(f"  {AMARELO}Nome obrigatorio.{RESET}")
            continue
        if not REGEX_NOME.match(nome):
            print(f"  {VERMELHO}Nome invalido! Use apenas letras e espacos "
                  f"(sem numeros ou simbolos como @!#$%&*...).{RESET}")
            continue
        if len(nome) < 2:
            print(f"  {AMARELO}Nome muito curto.{RESET}")
            continue
        # Capitaliza cada palavra
        return " ".join(p.capitalize() for p in nome.split())

# --- Telas de erro CLI dedicadas ---
def tela_erro(titulo, linhas):
    """Abre uma 'nova tela' CLI vermelha com a mensagem de erro."""
    for _ in range(3):  # pisca a tela 3x
        limpar()
        print(f"\n{VERMELHO}{BOLD}{'█'*60}{RESET}")
        print(f"{VERMELHO}{BOLD}{PISCA}{titulo.center(60)}{RESET}")
        print(f"{VERMELHO}{BOLD}{'█'*60}{RESET}\n")
        for l in linhas:
            print(f"  {VERMELHO}{l}{RESET}")
        print(f"\n{VERMELHO}{BOLD}{'█'*60}{RESET}")
        time.sleep(0.4)
    pausar()

# --- Validacao da quantidade comprada ---
def validar_quantidade_compra(item, qtd, unidade):
    """
    Retorna (ok, mensagem). Limite de 300 kg / 300 unidades por compra.
    'g'  -> max 300000 g  (300 kg)
    'kg' -> max 300 kg
    'un' -> max 300 unidades
    """
    un = unidade.lower()
    if un == "g":
        limite = LIMITE_COMPRA_KG * 1000
    elif un == "kg":
        limite = LIMITE_COMPRA_KG
    elif un == "un":
        limite = LIMITE_COMPRA_UN
    else:
        limite = LIMITE_COMPRA_KG * 1000  # fallback seguro
    if qtd <= 0:
        return False, "Quantidade deve ser maior que zero."
    if qtd > limite:
        return False, f"Compra acima do limite ({limite} {un}). Maximo permitido por compra."
    return True, ""

# --- Validacao da data de validade ---
def validar_validade(item, data_str):
    """
    - Tem que ser uma data valida no formato DD/MM/AAAA
    - Nao pode estar vencida (data passada)
    - Nao pode estar a mais de ANOS_MAX_VALIDADE anos (exceto Queijo)
    Retorna (ok, motivo).
    """
    try:
        d = data(data_str)
    except ValueError:
        return False, "Data invalida. Use o formato DD/MM/AAAA."

    hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    if d < hoje:
        return False, "ALIMENTO VENCIDO - nao pode ser comprado."

    dias = (d - hoje).days
    if item not in EXCECOES_LONGA_VAL and dias > ANOS_MAX_VALIDADE * 365:
        return False, (f"Validade absurda: mais de {ANOS_MAX_VALIDADE} anos no futuro. "
                       f"Apenas {', '.join(EXCECOES_LONGA_VAL)} pode passar disso.")
    return True, ""

# --- Consultas de estoque ---
def custo_prato(ingr):
    return sum(estoque[i]["custo"] * q for i, q in ingr.items() if i in estoque)

def tem_estoque(ingr):
    return all(estoque.get(i) and estoque[i]["qtd"] >= q for i, q in ingr.items())

def estoque_para_carrinho(carrinho):
    necessario = {}
    for pid, qtd in carrinho.items():
        for ing, q in cardapio[pid]["ingr"].items():
            necessario[ing] = necessario.get(ing, 0) + q * qtd
    return all(estoque.get(i, {}).get("qtd", 0) >= q for i, q in necessario.items())

def alertas():
    hoje = datetime.now()
    zerados = [n for n, d in estoque.items() if d["qtd"] <= 0]
    baixos = [n for n, d in estoque.items() if 0 < d["qtd"] <= ALERTA_MINIMO]
    vencendo = [(n, (data(d["validade"]) - hoje).days)
                for n, d in estoque.items() if (data(d["validade"]) - hoje).days <= 3]
    return zerados, baixos, vencendo

def mostrar_alertas():
    zerados, baixos, vencendo = alertas()
    if not (zerados or baixos or vencendo):
        print(f"  {VERDE}Nenhum alerta no momento.{RESET}")
        pausar()
        return
    for _ in range(6):
        limpar()
        print(f"\n  {VERMELHO}{BOLD}{PISCA}{'*** ALERTA CRITICO DE ESTOQUE ***'.center(50)}{RESET}\n")
        for n in zerados:
            print(f"    {VERMELHO}[ZERADO]  {n} -- estoque vazio{RESET}")
        for n in baixos:
            print(f"    {AMARELO}[BAIXO]   {n} -- {estoque[n]['qtd']}{estoque[n]['un']} restante(s){RESET}")
        for n, dias in vencendo:
            txt = "VENCIDO!" if dias <= 0 else f"vence em {dias} dia(s)"
            print(f"    {AMARELO}[VALIDADE] {n} -- {txt}{RESET}")
        time.sleep(0.5)
    pausar()

# --- Modulo CLIENTE ---
def menu_cliente(nome):
    carrinho = {}
    while True:
        limpar()
        cabecalho(f"CARDAPIO  --  Ola, {nome}!")
        print(f"  {BOLD}┌────┬──────────────────────────┬───────────┬────────────┐{RESET}")
        print(f"  {BOLD}│ ID │ PRATO                    │   PRECO   │   STATUS   │{RESET}")
        print(f"  {BOLD}├────┼──────────────────────────┼───────────┼────────────┤{RESET}")
        for i, d in sorted(cardapio.items(), key=lambda x: int(x[0])):
            ok = tem_estoque(d["ingr"])
            cor = VERDE if ok else VERMELHO
            status = f"{cor}{('OK' if ok else 'ESGOTADO'):^10}{RESET}"
            preco = f"R$ {d['preco']:>6.2f}"
            print(f"  │ {i:<2} │ {d['nome']:<24} │ {preco:>9} │ {status} │")
        print(f"  └────┴──────────────────────────┴───────────┴────────────┘")

        if carrinho:
            print(f"\n  {CIANO}{BOLD}SEU CARRINHO{RESET}")
            print(f"  {BOLD}┌──────────────────────────┬──────┬──────────┐{RESET}")
            print(f"  {BOLD}│ PRATO                    │ QTD  │ SUBTOTAL │{RESET}")
            print(f"  {BOLD}├──────────────────────────┼──────┼──────────┤{RESET}")
            total = 0.0
            for pid, q in carrinho.items():
                sub = cardapio[pid]["preco"] * q
                total += sub
                print(f"  │ {cardapio[pid]['nome']:<24} │ {q:>4} │ R$ {sub:>6.2f} │")
            print(f"  └──────────────────────────┴──────┴──────────┘")
            print(f"  {VERDE}{BOLD}TOTAL: R$ {total:.2f}{RESET}")

        print("\n  Digite o ID/NOME para ADICIONAR  |  F = finalizar pedido  |  0 = sair")
        escolha = pedir_txt("  > ", vazio=True)

        if escolha == "0":
            break

        if escolha.lower() == "f":
            if not carrinho:
                print(f"  {AMARELO}Carrinho vazio. Adicione algum prato antes.{RESET}")
                pausar()
                continue
            for pid, q in carrinho.items():
                prato = cardapio[pid]
                for ing, qi in prato["ingr"].items():
                    estoque[ing]["qtd"] -= qi * q
                c = custo_prato(prato["ingr"])
                pedidos.append({"cliente": nome, "prato": prato["nome"], "qtd": q,
                                "venda": round(prato["preco"] * q, 2),
                                "custo": round(c * q, 2),
                                "lucro": round((prato["preco"] - c) * q, 2),
                                "hora": agora()})
            print(f"\n  {VERDE}Pedido confirmado! {sum(carrinho.values())} item(ns) em preparo. Bom apetite!{RESET}")
            carrinho = {}
            pausar()
            continue

        achou = next((i for i, d in cardapio.items()
                      if escolha == i or escolha.lower() == d["nome"].lower()), None)
        if not achou:
            print(f"  {AMARELO}Prato nao encontrado.{RESET}")
            pausar()
            continue
        prato = cardapio[achou]
        if not tem_estoque(prato["ingr"]):
            print(f"  {VERMELHO}{prato['nome']} indisponivel - ingredientes insuficientes.{RESET}")
            pausar()
            continue

        qtd = int(pedir_num(f"  Quantas unidades de '{prato['nome']}'? ", 1))
        teste = dict(carrinho)
        teste[achou] = teste.get(achou, 0) + qtd
        if not estoque_para_carrinho(teste):
            print(f"  {VERMELHO}Estoque insuficiente para essa quantidade.{RESET}")
            pausar()
            continue
        carrinho[achou] = teste[achou]
        print(f"  {VERDE}+{qtd}x {prato['nome']} adicionado(s) ao carrinho.{RESET}")
        pausar()

# --- Modulo ADMIN ---
def login_admin():
    limpar()
    cabecalho("AREA RESTRITA - LOGIN ADMINISTRADOR")
    usuario = pedir_txt("\n  Usuario: ").lower()
    senha = pedir_txt("  Senha:   ")
    if ADMINS.get(usuario) == senha:
        print(f"\n  {VERDE}Acesso liberado, {usuario}!{RESET}")
        time.sleep(1)
        return usuario
    print(f"\n  {VERMELHO}Usuario ou senha invalidos.{RESET}")
    pausar()
    return None

def menu_admin(usuario):
    while True:
        limpar()
        z, b, v = alertas()
        total = len(z) + len(b) + len(v)
        cabecalho(f"PORTAL ADMINISTRATIVO - {usuario}")
        if total:
            print(f"  {VERMELHO}[!] {total} alerta(s) -- ver opcao 6{RESET}")
        for linha in ["1. Ver Estoque", "2. Repor/Comprar Estoque", "3. Cadastrar Prato",
                      "4. Remover Prato", "5. Pedidos e Lucro", "6. Alertas de Estoque",
                      "7. Historico de Compras", "0. Sair"]:
            print(f"  {linha}")
        op = pedir_txt("\n  > Opcao: ")

        if op == "1":
            limpar()
            hoje = datetime.now()
            print(f"\n  {BOLD}{'ITEM':<14}{'QTD':>8} {'UN':<4}{'VALIDADE':<12}{'CUSTO':>9}  STATUS{RESET}")
            print("  " + "─"*60)
            for n, d in sorted(estoque.items()):
                dias = (data(d["validade"]) - hoje).days
                if d["qtd"] <= 0:
                    st = f"{VERMELHO}[ZERADO]{RESET}"
                elif d["qtd"] <= ALERTA_MINIMO:
                    st = f"{AMARELO}[BAIXO]{RESET}"
                elif dias <= 3:
                    st = f"{AMARELO}[VENCE EM BREVE]{RESET}"
                else:
                    st = f"{VERDE}[OK]{RESET}"
                print(f"  {n:<14}{d['qtd']:>8.1f} {d['un']:<4}{d['validade']:<12}R${d['custo']:>7.4f}  {st}")
            pausar()

        elif op == "2":
            limpar()
            cabecalho("REPOR / COMPRAR ESTOQUE")
            itens = sorted(estoque)
            print(f"  {BOLD}┌────┬──────────────────┬────────────┬──────┬────────────┐{RESET}")
            print(f"  {BOLD}│ Nº │ ITEM             │ QTD ATUAL  │ UN   │ VALIDADE   │{RESET}")
            print(f"  {BOLD}├────┼──────────────────┼────────────┼──────┼────────────┤{RESET}")
            for n, nome_it in enumerate(itens, 1):
                d = estoque[nome_it]
                print(f"  │ {n:<2} │ {nome_it:<16} │ {d['qtd']:>10.1f} │ {d['un']:<4} │ {d['validade']:<10} │")
            print(f"  └────┴──────────────────┴────────────┴──────┴────────────┘")
            print(f"  {CIANO}[N] Cadastrar item NOVO{RESET}")
            sel = pedir_txt("\n  Numero do item (ou N para novo): ")

            # --- Identifica o item ---
            if sel.lower() == "n":
                item = pedir_txt("  Nome do item novo: ").capitalize()
                if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+$", item):
                    tela_erro("NOME DE ITEM INVALIDO",
                              ["Use apenas letras (sem numeros/simbolos)",
                               "para o nome do item novo."])
                    continue
                if item in estoque:
                    print(f"  {AMARELO}Item ja existe, sera atualizado.{RESET}")
                novo = True
            elif sel.isdigit() and 1 <= int(sel) <= len(itens):
                item = itens[int(sel) - 1]
                novo = False
            else:
                print(f"  {AMARELO}Opcao invalida.{RESET}")
                pausar()
                continue

            # --- Define unidade (precisa antes p/ validar quantidade) ---
            if novo and item not in estoque:
                un = pedir_txt("  Unidade (g/kg/un): ").lower()
                if un not in ("g", "kg", "un"):
                    tela_erro("UNIDADE INVALIDA",
                              ["Use somente: g, kg ou un."])
                    continue
            else:
                un = estoque[item]["un"]

            # --- Quantidade com validacao de teto ---
            limite_un = (LIMITE_COMPRA_KG * 1000 if un == "g"
                         else LIMITE_COMPRA_KG if un == "kg"
                         else LIMITE_COMPRA_UN)
            qtd = pedir_num(f"  Quantidade adicionada (max {limite_un} {un}): ",
                            0.001, maximo=limite_un)
            ok, msg = validar_quantidade_compra(item, qtd, un)
            if not ok:
                tela_erro("COMPRA RECUSADA - QUANTIDADE INVALIDA",
                          [msg,
                           f"Limite: ate {LIMITE_COMPRA_KG} kg (ou {LIMITE_COMPRA_KG*1000} g)",
                           f"        ate {LIMITE_COMPRA_UN} unidades por compra."])
                continue

            custo = pedir_num("  Custo total da compra (R$): ", 0.0)

            # --- Validade com validacao (vencimento + 200 anos) ---
            if item in estoque and not novo:
                val_default = estoque[item]["validade"]
                nova = pedir_txt(f"  Validade (DD/MM/AAAA) [{val_default}]: ", vazio=True) or val_default
            else:
                nova = pedir_txt("  Validade (DD/MM/AAAA): ")

            ok, motivo = validar_validade(item, nova)
            if not ok:
                if "VENCIDO" in motivo.upper():
                    tela_erro("!!! ALIMENTO VENCIDO !!!",
                              [f"O item '{item}' com validade {nova}",
                               "ISSO NAO PODE SER COMPRADO - ESTA VENCIDO.",
                               "",
                               "Verifique a data de validade do fornecedor",
                               "antes de registrar a compra."])
                else:
                    tela_erro("DATA DE VALIDADE INVALIDA",
                              [motivo,
                               "",
                               f"Itens (exceto {', '.join(EXCECOES_LONGA_VAL)}) nao podem",
                               f"ter validade superior a {ANOS_MAX_VALIDADE} anos."])
                continue

            # --- Aplica a compra ---
            if item in estoque:
                estoque[item]["qtd"] += qtd
                estoque[item]["validade"] = nova
                estoque[item]["custo"] = round(custo / qtd, 6)
            else:
                estoque[item] = {"qtd": qtd, "un": un, "validade": nova,
                                 "custo": round(custo / qtd, 6)}
            compras.append({"funcionario": usuario, "item": item, "qtd": qtd,
                            "custo": custo, "hora": agora()})
            print(f"  {VERDE}{item} atualizado! (+{qtd} {un}){RESET}")
            pausar()

        elif op == "3":
            limpar()
            cabecalho("CADASTRAR NOVO PRATO")
            nome = pedir_txt("\n  Nome do prato: ")
            if any(d["nome"].lower() == nome.lower() for d in cardapio.values()):
                print(f"  {AMARELO}Ja existe um prato com esse nome.{RESET}")
                pausar()
                continue
            preco = pedir_num("  Preco de venda (R$): ", 0.01)
            print(f"\n  Ingredientes: {', '.join(sorted(estoque))}")
            print("  Digite 'fim' para encerrar.")
            ingr = {}
            while True:
                entrada = pedir_txt("  Ingrediente (ou 'fim'): ", vazio=True)
                if entrada.lower() == "fim":
                    break
                # busca case-insensitive na chave real do estoque
                achou_ing = next((k for k in estoque if k.lower() == entrada.lower()), None)
                if not achou_ing:
                    print(f"  {AMARELO}'{entrada}' nao esta no estoque. Use um dos listados acima.{RESET}")
                    continue
                if achou_ing in ingr:
                    print(f"  {AMARELO}'{achou_ing}' ja foi adicionado. Pulando.{RESET}")
                    continue
                ingr[achou_ing] = pedir_num(f"  Qtd de {achou_ing} ({estoque[achou_ing]['un']}): ", 0.001)
            if not ingr:
                print(f"  {AMARELO}Prato sem ingredientes. Cancelado.{RESET}")
                pausar()
                continue
            novo_id = str(max(int(k) for k in cardapio) + 1)
            cardapio[novo_id] = {"nome": nome, "preco": preco, "ingr": ingr}
            print(f"  {VERDE}'{nome}' cadastrado (ID {novo_id}). Custo: R${custo_prato(ingr):.2f}{RESET}")
            pausar()

        elif op == "4":
            limpar()
            cabecalho("REMOVER PRATO")
            for i, d in sorted(cardapio.items(), key=lambda x: int(x[0])):
                print(f"  [{i}] {d['nome']}")
            busca = pedir_txt("\n  ID ou nome a remover: ")
            alvo = next((i for i, d in cardapio.items()
                         if busca == i or busca.lower() == d["nome"].lower()), None)
            if alvo and pedir_txt(f"  Remover '{cardapio[alvo]['nome']}'? (s/n): ").lower() == "s":
                print(f"  {VERDE}'{cardapio[alvo]['nome']}' removido.{RESET}")
                del cardapio[alvo]
            elif not alvo:
                print(f"  {AMARELO}Prato nao encontrado.{RESET}")
            pausar()

        elif op == "5":
            limpar()
            cabecalho("PEDIDOS E LUCRO")
            if not pedidos:
                print("  Nenhum pedido registrado.")
            else:
                print(f"\n  {BOLD}{'#':<3}{'CLIENTE':<12}{'PRATO':<22}{'QTD':>4}{'VENDA':>9}{'CUSTO':>9}{'LUCRO':>9}{RESET}")
                print("  " + "─"*68)
                for n, p in enumerate(pedidos, 1):
                    print(f"  {n:<3}{p['cliente']:<12}{p['prato']:<22}{p.get('qtd', 1):>4}  R${p['venda']:>6.2f} R${p['custo']:>6.2f} R${p['lucro']:>6.2f}")
                print("  " + "─"*68)
                print(f"  {VERDE}Receita: R${sum(p['venda'] for p in pedidos):.2f}  |  "
                      f"Lucro: R${sum(p['lucro'] for p in pedidos):.2f}{RESET}")
            pausar()

        elif op == "6":
            mostrar_alertas()

        elif op == "7":
            limpar()
            cabecalho("HISTORICO DE COMPRAS")
            if not compras:
                print("  Nenhuma compra registrada.")
            else:
                print(f"\n  {BOLD}{'#':<3}{'FUNC':<12}{'ITEM':<14}{'QTD':>8}{'CUSTO':>10}{RESET}")
                print("  " + "─"*50)
                for n, c in enumerate(compras, 1):
                    print(f"  {n:<3}{c['funcionario']:<12}{c['item']:<14}{c['qtd']:>8.1f}R${c['custo']:>8.2f}")
                print("  " + "─"*50)
                print(f"  {VERDE}Total investido: R${sum(c['custo'] for c in compras):.2f}{RESET}")
            pausar()

        elif op == "0":
            break

# --- Menu principal ---
def main():
    while True:
        limpar()
        cabecalho("STOCKFLOW V5  --  BEM-VINDO(A)!")
        print(f"  {VERDE}1.{RESET} Sou CLIENTE      (entra direto, so com o nome)")
        print(f"  {AZUL}2.{RESET} Sou ADMIN        (area separada com senha)")
        print(f"  0. Sair")
        op = pedir_txt("\n  > Perfil: ")
        if op == "1":
            limpar()
            cabecalho("AREA DO CLIENTE")
            print()
            nome = pedir_nome_cliente()  # entra direto, sem senha, nome validado
            menu_cliente(nome)
        elif op == "2":
            usuario = login_admin()
            if usuario:
                z, b, v = alertas()
                if z or b or v:
                    mostrar_alertas()
                menu_admin(usuario)
        elif op == "0":
            limpar()
            print(f"\n  {CIANO}Ate logo!{RESET}\n")
            break
        else:
            print(f"  {AMARELO}Opcao invalida.{RESET}")
            pausar()

if __name__ == "__main__":
    main()
