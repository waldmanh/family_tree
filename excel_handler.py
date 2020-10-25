import excel2json
import json
import csv

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

def create_csv_from_result(result):
    with open('result.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['id','first_name', 'last_name'])
        for arr in result:
            filewriter.writerow([arr[0],arr[1],arr[2]])
            
    return "true"

        
        
