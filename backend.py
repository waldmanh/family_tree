import pyodbc 
import json
# import excel_handler

def select_from_db(data):
    with open('d:/projects/python/familytree/config.json') as f:
        config_data=json.load(f)
    query_where=''
    for item in data:
        query_where+="'"+item["idnum"]+"',"
    query_where=query_where[0:-1]
    print(query_where)
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server='+config_data["server_name"]+';'
                          'Database='+config_data["database_name"]+';'
                          'Trusted_Connection=yes;')
    
    cursor = conn.cursor()
    cursor.execute('SELECT * \
                   FROM '+config_data["database_name"]+'.dbo.person p\
                   WHERE p.id in('+query_where+')')
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(list(row))
    print(result)
    # for row in cursor:
    #     print(row)    
    return result