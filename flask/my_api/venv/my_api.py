from flask import Flask, jsonify, request
import json
app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    return jsonify({'id':id,'nome':'Yan'})

@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma':total})

if __name__ == '__main__':
    app.run(debug=True)

