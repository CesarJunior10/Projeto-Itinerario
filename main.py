import mysql.connector
from flask import Flask, jsonify, request, make_response, abort, redirect
import os
mydb = mysql.connector.connect(
    host='localhost',
    user='MainUser',
    password='MainPassword',
    database='Backoffice',
    autocommit = True
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Status code error 404
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Status code error 403
@app.errorhandler(403)
def not_found(error):
    return make_response(jsonify({'error': 'Forbidden - Book exists'}), 403)

# Status code error 400
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM Livros')
    meus_livros = my_cursor.fetchall()

    livros = list()
    for livro in meus_livros:
        livros.append(
            {
                'id': livro[0],
                'autor': livro[1],
                'titulo': livro[2]
            }
        )
    return jsonify({'Livros': livros})

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    try:
        my_cursor = mydb.cursor()
        sql = f'SELECT * FROM Livros WHERE id = {id}'
        my_cursor.execute(sql)
        meu_livro = my_cursor.fetchone()
        return jsonify({
                'id': meu_livro[0],
                'autor': meu_livro[1],
                'titulo': meu_livro[2]
            })

    except:
        abort(404)
        
# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    if ("autor" not in request.json):
        abort(400)
    if ("titulo" not in request.json):
        abort(400)

    try:
        livro = request.json

        my_cursor = mydb.cursor()
        sql = f"SELECT * FROM Livros WHERE titulo = '{livro['titulo']}'"
        my_cursor.execute(sql)
        meus_livros = my_cursor.fetchall()

        sql = f"INSERT INTO Livros (autor, titulo) VALUES ('{livro['autor']}', '{livro['titulo']}')"
        my_cursor.execute(sql)
        return jsonify(livro), 201
    except:
        abort(403)

# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    if ("autor" not in request.json):
        abort(400)
    if ("titulo" not in request.json):
        abort(400)

    try:
        livro = request.json

        my_cursor = mydb.cursor()
        sql = f"UPDATE Livros SET autor = '{livro['autor']}', titulo = '{livro['titulo']}' WHERE id = {id}"
        my_cursor.execute(sql)
        return jsonify(livro)
    except:
        abort(404)

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    try:
        my_cursor = mydb.cursor()
        sql = f"DELETE FROM Livros WHERE id = {id}"
        my_cursor.execute(sql) 
        return jsonify({'Excluido com sucesso!': True}) 
    except:
        abort(404)

@app.route('/upload', methods=['POST'])
def upload():
    arquivo = request.files.get('imagem')
    nome_arquivo = arquivo.filename.replace(" ","-")
    arquivo.save(os.path.join('../imagem/', nome_arquivo))
    return redirect('/livros')

app.run(debug=True)