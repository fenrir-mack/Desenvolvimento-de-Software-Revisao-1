from abc import ABC, abstractmethod
from datetime import date


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)


class Conta:
    def __init__(self, cliente, numero: int, agencia: str = "0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self) -> float:
        return self.saldo

    @staticmethod
    def nova_conta(cliente, numero: int):
        return Conta(cliente, numero)

    def sacar(self, valor: float) -> bool:
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            return True
        return False


class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, limite: float, limite_saques: int, agencia: str = "0001"):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor: float) -> bool:
        if self._saques_realizados >= self.limite_saques:
            print("Limite de saques atingido.")
            return False
        if valor > (self.saldo + self.limite):
            print("Saldo insuficiente (considerando limite).")
            return False
        if super().sacar(valor):
            self._saques_realizados += 1
            return True
        return False


class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


# --------------------------
# Example usage
# --------------------------
if __name__ == "__main__":
    cliente = PessoaFisica("Rua A, 123", "12345678900", "João", date(1990, 5, 20))
    conta = ContaCorrente(cliente, numero=1, limite=500, limite_saques=3)

    cliente.adicionar_conta(conta)

    # Deposit
    cliente.realizar_transacao(conta, Deposito(1000))
    print("Saldo após depósito:", conta.saldo_atual())

    # Withdraw
    cliente.realizar_transacao(conta, Saque(300))
    print("Saldo após saque:", conta.saldo_atual())

    # History
    print("Transações registradas:", [type(t).__name__ for t in conta.historico.transacoes])
