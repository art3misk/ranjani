from flask import Flask, request, render_template
from google import genai
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        output = query_document(user_input)
        return render_template('index.html', output=output, input=user_input)
    return render_template('index.html')

def query_document(question):
    response = chat.send_message(f"Someone is on my personal website that I made, and this is the question they're asking: {question}. Make the answer short and succint, and highlight points from my resume. You can also extrapolate a little and add some personality to your response. But also make sure it's proffesional sounding, as if a collegue or employer or student is asking it. If they ask a personal question then make up a funny response (it doesnt have to be true, but don't be cringy). Also dont suggest more questions. Here is my resume: {content}")
    return response.text

if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        content = file.read()
    
    gemini_key = os.getenv("GENAIAPIKEY")

    client = genai.Client(api_key=gemini_key)
    chat = client.chats.create(model="gemini-2.0-flash")
    app.run(debug=True)