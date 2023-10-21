from flask import Flask, request , render_template

app = Flask('__name__')

@app.route('/', methods=['POST', 'GET'])
def api():
    data = request.form['link']
    return data