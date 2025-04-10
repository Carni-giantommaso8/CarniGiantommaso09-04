from flask import Flask, render_template,request,redirect,url_for
lista = []
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modifica')
def modifica():
    return render_template('modifica.html')

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    nome = request.form.get('nome')
    cognome = request.form.get('cognome')
    scuola = request.form.get('scuola')
    hobby = request.form.get('hobby')
    
    if nome and scuola and hobby:
        persone.append({'nome': nome,'cognome': cognome, 'scuola': scuola, 'hobby': hobby}) 
    return redirect('/')
  
if __name__ == '__main__':
    app.run(debug=True)