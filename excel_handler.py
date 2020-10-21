import excel2json
import json
def convert_excel_to_json(file_path):
    excel2json.convert_from_file(file_path)
    with open('d:/projects/python/familytree/uploads/Sheet1.json') as f:
        json_file=json.load(f)
    data = convert_json(json_file)    
    return data

def convert_json(json_file):
    data = []
    for item in json_file:
        data.append({
            "idnum":str(int(item["id"])),
            "date":item["date"]
            })
    return data

def convert_cursor_to_csv(cursor):
    # import csv
    # with open('names.csv', 'w', newline='') as csvfile:
    #     fieldnames = ['id','first_name', 'last_name']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for row in cursor: 
    #         writer.writerow({'id':row[0],'first_name': row[1], 'last_name': row[2]})
    res=""
    for row in cursor:
        res += str(row) + ","
    res = "["+res[0:-1]+"]"
    return str(res)
        
        
