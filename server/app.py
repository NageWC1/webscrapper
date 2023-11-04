from flask import Flask, request , jsonify
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

app = Flask('__name__', template_folder='../')
import re
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

def data_cleaning(dataframe,count):
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
    dataframe.to_csv('./../src/components/result/csv/data table'+{count}+'.csv', index=False)
    dataframe.to_excel('./../src/components/result/excel/data table'+{count}+'.xlsx', index=False)
    return dataframe

@app.route('/data_types', methods=['GET'])
def identify_data_types_auto( threshold=0.9):
    dataframe = pd.read_csv('./../src/components/result/data.csv')
    data_types_list = []
    data_types_list.append(["Column Names", "Data Type"])
    for column in dataframe.columns:
        column_data = dataframe[column]

        # Initialize counters for each data type
        num_int = 0
        num_float = 0
        num_str = 0

        # Analyze the content of the column
        for value in column_data:
            if pd.notna(value):
                if str(value).replace(".", "").isdigit():
                    if "." in str(value):
                        num_float += 1
                    else:
                        num_int += 1
                else:
                    num_str += 1

        # Calculate the ratio of non-null values that match each data type
        ratio_int = num_int / len(column_data)
        ratio_float = num_float / len(column_data)
        ratio_str = num_str / len(column_data)

        # Determine the most likely data type for the column based on the threshold
        if ratio_int >= threshold:
            data_type = 'int'
        elif ratio_float >= threshold:
            data_type = 'float'
        elif ratio_str >= threshold:
            data_type = 'string'
        else:
            data_type = 'mixed'

        data_types_list.append([column, data_type])

    return jsonify({'data_types_list': data_types_list})   

@app.route('/scrape_tables', methods=['POST'])
def scrape_tables():
    # Get the URL from the request
    url =  request.json.get('link')

    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content with Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the tables on the webpage
        tables = soup.find_all('table')

        # Extract table data and store in a list
        table_data = []
        for table in tables:
            rows = []
            headers = [header.text.strip() for header in table.find_all('th')]  # Extract table headers
            for row in table.find_all('tr'):
                cell_data = [cell.text.strip() for cell in row.find_all('td')]
                rows.append(cell_data)
            table_data.append({'headers': headers, 'data': rows})  # Include headers in the response
       
        # Specify the location for the output JSON file
        output_file = './../src/components/result/json/output.json'
        with open(output_file, 'w') as json_file:
            json.dump({'tables': table_data}, json_file, indent=4)

        return jsonify({'tables': table_data})

    except Exception as e:
        return jsonify({'error': str(e)})

# New API endpoint to analyze tables and detect data types
@app.route('/analyze_tables', methods=['POST'])
def analyze_tables():
    try:
        # Get the tables from the request
        tables = request.json.get('tables')

        # Analyze the data types of columns
        analyzed_tables = []
        for table in tables:
            analyzed_table = []
            for row in table:
                analyzed_row = []
                for cell in row:
                    # Detect data type (float, number, or string)
                    data_type = 'string'
                    if re.match(r'^-?\d+\.?\d*$', cell):  # Match numbers and floats
                        if '.' in cell:
                            data_type = 'float'
                        else:
                            data_type = 'number'
                    analyzed_row.append({'value': cell, 'data_type': data_type})
                analyzed_table.append(analyzed_row)
            analyzed_tables.append(analyzed_table)

        return jsonify({'analyzed_tables': analyzed_tables})

    except Exception as e:
        return jsonify({'error': str(e)})
        
if __name__ == "__main__":
    app.run()