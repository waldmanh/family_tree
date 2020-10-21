from werkzeug.utils import secure_filename
import backend
import excel_handler
def handle_new_excel(f):
    print('bl was here')
    file_path = './uploads/'+secure_filename(f.filename)    
    f.save(file_path)
    data = excel_handler.convert_excel_to_json(file_path)
    cursor = backend.select_from_db(data)
    result = excel_handler.convert_cursor_to_csv(cursor)
    return result