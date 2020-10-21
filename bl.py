from werkzeug.utils import secure_filename
import backend
def handle_new_excel(f):
    print('bl was here')
    f.save('./uploads/'+secure_filename(f.filename))    
    backend.select_from_db()
    return 'True'