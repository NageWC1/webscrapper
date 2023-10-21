from flask import Flask, request , render_template
import requests
import pandas as pd
from bs4 import BeautifulSoup

import json
app = Flask('__name__')

@app.route('/', methods=['POST', 'GET'])
def api():
    url = request.form['link']
    # check whether website givig permision to scrape their data
    per = check_permission(url)

    if per == "ok":
        table = scrap_table(url)
    else:
        table = "nothing"
        
    return table

def scrap_table(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "lxml")
    table = soup.find("table")
    headers = table.find_all("th")
    titles = []
    for i in headers:
        text = i.text
        titles.append(text)
    df = pd.DataFrame(columns=titles)
    # table = df.to_html(classes="table")
    return df.to_html()

def check_permission(link):
    permision = requests.get(link)

    
    if permision.status_code == 200:
        per = "ok"
    else:
        per = "nope"
    return per

if __name__ == "__main__":
    app.run()