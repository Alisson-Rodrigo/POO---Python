#Exercicio classe da netflix:
class Cliente:
    def __init__(self,name,email,plano_cliente):
        self.name = name
        self.email = email
        self.lista_planos = ['basic','premium']
        if plano_cliente in self.lista_planos:
            self.plano_cliente = plano_cliente
        else:
            print ("Plano inválido")
            exit()
    def novoPlano(self,novo_plano):
        if novo_plano in self.lista_planos:
            self.plano_cliente = novo_plano
        else:
            print("Plano inválido!")
        
cliente = Cliente(input("Digite seu nome: "),input("Digite seu email: "),input("Qual o seu plano: [basic or premium]: ").strip().lower())
print (f'{cliente.name}\n{cliente.email}\n{cliente.plano_cliente}')
aux = input("Deseja trocar de plano? [S/N]: ").upper().strip()
if aux == 'S':
    cliente.novoPlano(input("Qual o novo plano: ").lower().strip())
    print (cliente.plano_cliente)
if aux == 'N':
    exit()
    
        