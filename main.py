from flask import Flask, request, jsonify
from fastapi.responses import RedirectResponse
from fastapi import FastAPI

app = FastAPI(title="Api de PTC")

@app.get('/',include_in_schema=False)
def index():
    return RedirectResponse("/docs", status_code=300)

@app.get("/api")
def receber_formulario():
    data = request.get_json()

    # Aqui você pode tratar os dados recebidos do formulário
    # e realizar as operações necessárias, como adicionar ao dataset, treinamento do modelo, etc.

    # Exemplo de exibição dos dados recebidos no console
    print('Dados do formulário recebidos:')
    print('Tipo de Crime:', data['tipoCrime'])
    print('Data:', data['data'])
    # Outros campos do formulário

    # Retorne uma resposta de sucesso ao frontend.
    return jsonify({'message': 'Formulário recebido com sucesso.'})

#if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=5000, debug=True)
