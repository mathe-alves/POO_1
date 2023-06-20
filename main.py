def criar_conta(numero, titular, saldo, limite):
    conta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite
    }
    return conta


def depositar(conta, valor):
    conta['saldo'] += valor


def saque(conta, valor):
    conta['saldo'] -= valor


def extratos(conta):
    print(f'Número da conta: {conta["numero"]}')
    print(f'Titular: {conta["titular"]}')
    print(f'Saldo: {conta["saldo"]}')
    print(f'Limite: {conta["limite"]}')
    print('=' * 30)