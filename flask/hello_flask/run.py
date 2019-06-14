from flask import Flask
app = Flask(__name__)

@app.route('/<numero>', methods=['GET','POST'])
def hello(numero):
    return 'Hello Word. {}'.format(numero)  #recebe um numero como parametro na chamada e o retorna

if __name__=='__main__':    #a chamada so eh atendida se vier de run.py
    app.run(debug=True)