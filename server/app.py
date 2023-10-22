from flask import Flask, request , jsonify
import requests
import pandas as pd
from bs4 import BeautifulSoup

import json
app = Flask('__name__', template_folder='../')

@app.route('/', methods=['POST', 'GET'])
def api():
    url =  request.json.get('link')
    print(url)
    permision = requests.get(url) 
    
    if permision.status_code == 200:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        table_headers = []
        print(url)
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
        row_data[0] = table_headers
    else:
        per = "nope"
  

    print("print list")
    print(row_data)
    return jsonify({'row_data': row_data})

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
    row_data[0] = table_headers
    html_table = df.to_json(orient='records')
   
    # print(html_table)
    
    return jsonify({'row_data': row_data})


def check_permission(link):
    permision = requests.get(link) 
    if permision.status_code == 200:
        per = "ok"
    else:
        per = "nope"
    return per

def scrape_website(link):
    try:
        # Send an HTTP GET request to the provided link
        response = requests.get(link)
        print(response)
        # Check if the request was successful
        if response.status_code == 200:
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the table on the webpage (you may need to adjust this based on the website's structure)
            table = soup.find('table')

            # Convert the table to an HTML string
            html_table = str(table) if table else "No table found on the webpage."

            return html_table
        else:
            return "Failed to fetch data from the website. Status code: " + str(response.status_code)
    except Exception as e:
        return str(e)

@app.route('/scrape', methods=['POST'])
def scrape():
    try:
        # Get the website link from the request
        link = request.json.get('link')

        if not link:
            return jsonify({'error': 'No link provided'})

        # Perform web scraping using the helper function
        html_table = scrape_website(link)

        # Send the HTML table as a response
        return jsonify({'tableData': html_table})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == "__main__":
    app.run()