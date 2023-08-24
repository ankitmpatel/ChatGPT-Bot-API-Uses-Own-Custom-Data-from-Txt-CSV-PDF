from flask import Flask, request, jsonify
from llama_index import GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
import os
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'user'
app.config['BASIC_AUTH_PASSWORD'] = 'user123*'

basic_auth = BasicAuth(app)

def load_index():
    os.environ["OPENAI_API_KEY"] = "sk-lJz3s2Lqa0oMN3p4gk2pT3suhkFJcnce0JbRt9ubmbQ3goEk"
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    return index

@app.route('/ask_ai', methods=['post'])
@basic_auth.required
def ask_ai():
    try:
        data = request.get_json()
        query = data.get('query', '')
        if query:
            index = load_index()
            response = index.query(query)
            return jsonify({'response': response.response})
        else:
            return jsonify({'error': 'Invalid input'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5001)