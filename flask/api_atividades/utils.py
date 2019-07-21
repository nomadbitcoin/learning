from models import Pessoas, Usuarios

#insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Luiz',idade=25)
    print(pessoa)
    pessoa.save()

#realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Yan').first()
    print(pessoa.idade)
    '''
    for p in pessoa:
        print(p)
    '''

#altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Luiz').first()
    pessoa.idade = 21
    pessoa.nome = 'Coito'
    pessoa.save()

#exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Coito').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    #insere_usuario('rafael', '1234')
    #insere_usuario('galeanni', '4321')
    insere_usuario('yaaanhue', 'hehe')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()