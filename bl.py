from werkzeug.utils import secure_filename
import backend
import excel_handler
def handle_new_excel(f):
    print('bl was here')
    file_path = './uploads/'+secure_filename(f.filename)    
    f.save(file_path)
    data = excel_handler.convert_excel_to_json(file_path)
    result = backend.select_from_db(data) 
    is_success = excel_handler.create_csv_from_result(result)
    if(is_success=="true"):
        return "true"
    else:
        return "false"