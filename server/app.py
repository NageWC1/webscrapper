from flask import Flask, request , render_template, redirect
import requests
import pandas as pd
from bs4 import BeautifulSoup

import json
app = Flask('__name__', template_folder='../')

@app.route('/<link>', methods=['POST', 'GET'])
def api(link):
    url = request.form[link]
    # check whether website givig permision to scrape their data
    per = check_permission(url)

    # if per == "ok":
    # #     table = scrap_table(url)
    # # else:
    # #     table = "nothing"
    print(url)
    return per
def scrap_table(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    table_headers = []
    print(link)
    for i in table.find_all('tr'):
        for x in i.find_all('th'):
            print(x.text.strip())
            table_headers.append(x.text)
    table_headers = list(dict.fromkeys(table_headers))

    row_data = []
    for i in table.find_all("tr")[1:]:
        td_tags = i.find_all('td')
        td_val = [y.text for y in td_tags]
        print(td_val)
        row_data.append(td_val)

    df = pd.DataFrame(row_data,columns=table_headers)
    # table = df.to_html(classes="table")
    # return df.to_html(classes="table table-striped table-dark")
    # return str(table)
    # return table_headers
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