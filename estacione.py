import textwrap
from datetime import datetime, timedelta

class Veiculo:
    def __init__(self, nome, placa):
        self.nome = nome
        self.placa = placa
        self.data_entrada = datetime.now()
        
    def __str__(self):
        data_entrada_formatada = self.data_entrada.strftime("%d/%m/%Y %H:%M:%S")
       
        return f"""\
                Data:{data_entrada_formatada}
                Veículo:{self.nome}
                Placa:{self.placa}
                """
            
def menu():
    menu = """\n
    ================ MENU ================
    
    [a] Adicionar carro
    [d] Excluir carro
    [e] Exibir relatório
    [q] Sair
    
    => """
    return input(textwrap.dedent(menu))

def filtrar_placa(placa, carros):
    carros_filtrados = [carro for carro in carros if carro.placa == placa]
    return carros_filtrados[0] if carros_filtrados else None

def adicionar_carro(carros):
    placa = input("Informe a placa do veículo: ")
    carro = filtrar_placa(placa, carros)
    
    if carro:
        print("Veículo já cadastrado!")
        return
    

    nome = input("Informe o nome do veículo: ")
    placa = input("Ionforme a placa do veiculo: ")
    
    carro = Veiculo(nome=nome, placa=placa)
    carros.append(carro)
   
    print("Veículo cadastrado com sucesso!")
    
def excluir_carro(carros):
    placa = input("Informe a placa do veículo: ")
    carro = filtrar_placa(placa, carros)
    
    if carro.placa == placa:
        carros.remove(carro)

        print(f"Veiculo placa {placa} removido com sucesso!")
    
def listar_carros(carros):
    for carro in carros:
        print("=" * 20)
        print(textwrap.dedent(str(carro)))

def main():
    carros = []

    while True:
        opcao = menu()

        if opcao == "a":
            adicionar_carro(carros)
            
        elif opcao == "d":
            excluir_carro(carros)
            
        elif opcao == "e":
            listar_carros(carros)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Opção inválida. @@@")


if __name__ == "__main__":
    main()

