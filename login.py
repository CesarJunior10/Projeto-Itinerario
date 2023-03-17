import mysql.connector
from flask import Flask, redirect, request
mydb = mysql.connector.connect(
    host='localhost',
    user='MainUser',
    password='MainPassword',
    database='Backoffice',
    autocommit = True
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 't10'

@app.route('/cadastro', methods=['POST'])
def cadastro():
    email = request.form.get('email')
    senha = request.form.get('password')
    
    my_cursor = mydb.cursor()
    my_cursor.execute(f"INSERT INTO USUARIO VALUES (default, '{email}', '{senha}')")
    
    return redirect('/login')
    
@app.route('/login', methods=['POST'])
def login():

    email = request.form.get('email')
    senha = request.form.get('password')

    my_cursor = mydb.cursor()
   
    cont = 0   

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM Usuarios')
    usuarioBD = my_cursor.fetchall()
        
    for usuario in usuarioBD:
        cont += 1
        usuarioNome = str(usuario[1])
        usuarioSenha = str(usuario[2])

        if usuarioNome['email'] == email and usuarioSenha['password'] == senha:
            return redirect('/livros')
        if cont >= len(usuarioBD):
            return redirect('/')

app.run(debug=True)