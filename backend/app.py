from flask import Flask, request, jsonify
from solver import solve_question
from ocr import extract_text_from_image

app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    question = data['question']
    answer = solve_question(question)
    return jsonify({'solution': answer})

@app.route('/image-upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    text = extract_text_from_image(file)
    answer = solve_question(text)
    return jsonify({'question': text, 'solution': answer})

if __name__ == '__main__':
    app.run(debug=True)
