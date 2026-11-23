
from datetime import datetime


class Cliente:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Telefone:", self.telefone)


class Quarto:
    def __init__(self, numero, preco):
        self.numero = numero
        self.preco = preco

    def exibir_dados(self):
        print("Quarto:", self.numero)
        print(f"Diária: R$ {self.preco:.2f}")


class QuartoSolteiro(Quarto):
    def exibir_dados(self):
        print("Tipo: Solteiro")
        super().exibir_dados()


class QuartoCasal(Quarto):
    def exibir_dados(self):
        print("Tipo: Casal")
        super().exibir_dados()


class Suite(Quarto):
    def exibir_dados(self):
        print("Tipo: Suíte")
        super().exibir_dados()
        print("Café da manhã incluso")


class Reserva:
    def __init__(self, cliente, quarto, entrada, saida):
        self.cliente = cliente
        self.quarto = quarto
        self.entrada = entrada
        self.saida = saida

    def exibir_dados(self):
        dias = (self.saida - self.entrada).days
        total = dias * self.quarto.preco

        print("Cliente:", self.cliente.nome)
        print("Quarto:", self.quarto.numero)
        print("Entrada:", self.entrada.strftime("%d/%m/%Y"))
        print("Saída:", self.saida.strftime("%d/%m/%Y"))
        print(f"Total: R$ {total:.2f}")


clientes = []
reservas = []

quartos = [
    QuartoSolteiro(101, 100),
    QuartoSolteiro(102, 100),
    QuartoCasal(201, 180),
    QuartoCasal(202, 180),
    Suite(301, 300)
]


def mostrar_menu():
    print("\n=== SISTEMA DE HOTEL ===")
    print("1 - Cadastrar cliente")
    print("2 - Listar quartos")
    print("3 - Realizar reserva")
    print("4 - Listar reservas")
    print("5 - Listar clientes")
    print("0 - Sair")


def cadastrar_cliente():
    print("\n=== Cadastro de Cliente ===")

    nome = input("Nome: ").strip()

    if not nome or not nome.replace(" ", "").isalpha():
        print("Nome inválido!")
        return

    cpf = input("CPF (11 números): ").strip()

    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido!")
        return

    for cliente in clientes:
        if cliente.cpf == cpf:
            print("CPF já cadastrado!")
            return

    telefone = input("Telefone com DDD: ").strip()

    if not telefone.isdigit() or len(telefone) not in (10, 11):
        print("Telefone inválido!")
        return

    cliente = Cliente(nome, cpf, telefone)
    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    print("\n=== Clientes ===")

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        cliente.exibir_dados()
        print("--------------------")


def listar_quartos():
    print("\n=== Quartos ===")

    for quarto in quartos:
        quarto.exibir_dados()
        print("--------------------")


def realizar_reserva():
    print("\n=== Nova Reserva ===")

    cpf = input("CPF do cliente: ")

    cliente_encontrado = None

    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("Cliente não encontrado!")
        return

    try:
        numero = int(input("Número do quarto: "))

        quarto_encontrado = None

        for quarto in quartos:
            if quarto.numero == numero:
                quarto_encontrado = quarto
                break

        if quarto_encontrado is None:
            print("Quarto não encontrado!")
            return

        entrada = input("Data de entrada (DD/MM/AAAA): ")
        saida = input("Data de saída (DD/MM/AAAA): ")

        entrada = datetime.strptime(entrada, "%d/%m/%Y")
        saida = datetime.strptime(saida, "%d/%m/%Y")

        if entrada.date() < datetime.today().date():
            print("A data de entrada já passou!")
            return

        if saida <= entrada:
            print("A data de saída deve ser depois da entrada!")
            return

        for reserva in reservas:
            if reserva.quarto.numero == numero:
                if entrada < reserva.saida and saida > reserva.entrada:
                    print("Quarto ocupado nesse período!")
                    return

        nova_reserva = Reserva(
            cliente_encontrado, quarto_encontrado, entrada, saida
        )

        reservas.append(nova_reserva)
        print("Reserva realizada com sucesso!")

    except ValueError:
        print("Número do quarto ou data inválida!")


def listar_reservas():
    print("\n=== Reservas ===")

    if len(reservas) == 0:
        print("Nenhuma reserva cadastrada.")
        return

    for reserva in reservas:
        reserva.exibir_dados()
        print("--------------------")


def main():
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()

        elif opcao == "2":
            listar_quartos()

        elif opcao == "3":
            realizar_reserva()

        elif opcao == "4":
            listar_reservas()

        elif opcao == "5":
            listar_clientes()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
