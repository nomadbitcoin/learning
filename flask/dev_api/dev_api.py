from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id':'0',
        'nome':'Yan',
        'habilidades': ['Python', 'Flask']
     },
    {
        'id':'1',
        'nome':'Luiz',
        'habilidades':['Python', 'Django']
    }
]

@app.route('/dev/<int:id>/', methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            responda = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} nao existe'.format(id)
            responda = {'status':'error','mensagem':mensagem}
        except Exception:
            mensagem = 'erro desconhecido'
            responda = {'status':'erro','mensagem':mensagem}
        return jsonify(responda)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluido'})

#   Lista todos os desenvolvedore e e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolveores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao =len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
if __name__ == '__main__':
    app.run(debug=True)