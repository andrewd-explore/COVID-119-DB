from chalice import Chalice
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Chalice(app_name='covid19')

username = "admin"
password = ""
host = "database-1.ccwgqdqrrmvt.eu-west-1.rds.amazonaws.com"
port = "1433"

engine = create_engine(
    'mssql+pymssql://' +
    username + ':' + password + '@' + host + ':' +
    str(port) + '/Corona'

)

@app.route('/')
def index():
    return 'Covid 19 rest API'

@app.route('/get_tests')
def get_tests():

    sql_query = "Select * from Tests"
    results_proxy = engine.execute(sql_query)

    d,a = {},[]
    for rowproxy in results_proxy:
        for column,value in rowproxy.items():
            d = {**d,**{column:value}}
        a.append(d)

    return a

@app.route('/get_table/{table_name}')
def get_table(table_name):

    table_name = table_name.replace('%22','')

    sql_query = "Select * from " + table_name
    results_proxy = engine.execute(sql_query)

    d,a = {},[]
    for rowproxy in results_proxy:
        for column,value in rowproxy.items():
            d = {**d,**{column:value}}
        a.append(d)

    return a
