from flask import Flask, request, jsonify
from fastapi.responses import RedirectResponse
from fastapi import FastAPI

app = FastAPI(title="Api de PTC")


@app.route("/api/denuncia", methods=["POST"])
def receber_formulario():
    data = request.json

    # Aqui você pode tratar os dados recebidos do formulário
    # e realizar as operações necessárias, como adicionar ao dataset, treinamento do modelo, etc.

    # Exemplo de exibição dos dados recebidos no console
    print('Dados do formulário recebidos:')
    print('Tipo de Crime:', data['tipoCrime'])
    print('Data:', data['data'])
    # Outros campos do formulário

    # Retorne uma resposta de sucesso ao frontend.
    return jsonify({'message': 'Formulário recebido com sucesso.'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
