from flask import Flask;

app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>BEM VINDO AO MUNDO... DEVOPS.!!! UHUL -- Version: 0.3</h1></center>'

@app.route('/msg')
def msg():
    return '<center><h1>Usando os conceitos de deploy DEV..!!!</h1></center>'

#app.run();
