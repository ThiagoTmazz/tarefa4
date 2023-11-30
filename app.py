from flask import Flask, request, jsonify

app = Flask(__name__)

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def calcular_fibonacci(numero):
    if numero <= 0:
        return "O número deve ser maior que zero."
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < numero:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
        return fibonacci_sequence

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()

    print("Recebendo solicitação:", data)

    if 'operacao' not in data:
        return jsonify({'error': 'O campo "operacao" é obrigatório.'}), 400

    if data['operacao'] == 'fatorial':
        if 'numero' not in data:
            return jsonify({'error': 'O campo "numero" é obrigatório para a operação de fatorial.'}), 400

        resultado = calcular_fatorial(data['numero'])
        response = {'resultado': resultado}
        print("Enviando resposta:", response)
        return jsonify(response)

    elif data['operacao'] == 'fibonacci':
        if 'numero' not in data:
            return jsonify({'error': 'O campo "numero" é obrigatório para a operação de Fibonacci.'}), 400

        resultado = calcular_fibonacci(data['numero'])
        response = {'resultado': resultado}
        print("Enviando resposta:", response)
        return jsonify(response)

    else:
        return jsonify({'error': 'Operação inválida. Escolha entre "fatorial" ou "fibonacci".'}), 400

if __name__ == '__main__':
    app.run(debug=True)
