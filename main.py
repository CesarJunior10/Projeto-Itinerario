from flask import Flask, jsonify, request
from bd import livros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

#Consultar(todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
#Consultar(id)
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
        return jsonify(livro)
    return jsonify({'error': 'Not found'}), 404
#Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'error': 'Not found'}), 404
#Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    for livro in livros:
        if novo_livro.get('id') != livro.get('id'):
            livros.append(novo_livro)
        return jsonify(livros), 201
#Excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):   
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
#Status code error
@app.errorhandler(404)
def handler_404_error(_error):
    return jsonify({'error': 'Not found'}), 404

app.run(port=5000,host='localhost',debug=True)