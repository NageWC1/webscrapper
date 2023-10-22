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
  
    data_cleaning(df)
    print("print list")
    print(row_data)
    return jsonify({'row_data': row_data})

def data_cleaning(dataframe):
    # Replace missing values with NaN
    dataframe = dataframe.fillna(pd.NA)
    
    # Remove duplicate rows
    dataframe = dataframe.drop_duplicates()
    
    # Remove leading and trailing whitespaces from column names
    dataframe.columns = dataframe.columns.str.strip()
    
    # Remove leading and trailing whitespaces from string columns
    string_columns = dataframe.select_dtypes(include=['object']).columns
    dataframe[string_columns] = dataframe[string_columns].apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Add more data cleaning steps as needed
    dataframe.to_csv('./../src/components/result/data.csv', index=False)
    dataframe.to_excel('./../src/components/result/data.xlsx', index=False)
    return dataframe
    
    
if __name__ == "__main__":
    app.run()