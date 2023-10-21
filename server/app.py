from flask import Flask, request , render_template
import pandas as pd
import json
app = Flask('__name__')

@app.route('/', methods=['POST', 'GET'])
def api():
    link = request.form['link']
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)
    print(link)
    table = df.to_html(classes="table")
    return link

if __name__ == "__main__":
    app.run()