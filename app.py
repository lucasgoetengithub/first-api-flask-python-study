from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id':1,
        'titulo' : 'Senhor dos aneis',
        'autor': 'J.R.R Tolkin'
    },
    {
        'id':2,
        'titulo' : 'Senhor dos aneis 2',
        'autor': 'J.R.R Tolkin'
    },
    {
        'id':3,
        'titulo' : 'Senhor dos aneis 3',
        'autor': 'J.R.R Tolkin'
    },
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
    
@app.route('/livros/alterar/<int:id>', methods=['PUT'])
def edit_livr_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)