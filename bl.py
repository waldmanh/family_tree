from werkzeug.utils import secure_filename
import dal
import excel_handler


def script1(uploaded_file):
    print('script 1 func')
    file_path = save_uploaded_file(uploaded_file)
    is_success = handle_new_excel(file_path)
    if(is_success == "true"):
        return "true"
    else:
        return "false"


def script2(uploaded_file):
    file_path = save_uploaded_file(uploaded_file)
    with open('result.txt', 'w+') as txtfile:
        txtfile.write("uploaded " + file_path)
    return file_path


def save_uploaded_file(uploaded_file):
    file_path = './uploads/'+secure_filename(uploaded_file.filename)
    uploaded_file.save(file_path)
    return file_path


def handle_new_excel(file_path):
    data = excel_handler.convert_excel_to_json(file_path)
    result = dal.select_from_db(data)
    is_success = excel_handler.create_csv_from_result(result)
    return is_success
