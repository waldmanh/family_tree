from flask import Flask, render_template, request, send_from_directory
import bl
import os
# import glob
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload')
def upload_file():
    return render_template('./upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        result = bl.handle_new_excel(request.files['file'])
        if result == 'false':
            return 'error handling file'
        os.remove('./uploads/Sheet1.json')
        # files = glob.glob('/uploads/*')
        # for fileitem in files:
        # os.remove(fileitem)
        try:
            return send_from_directory('./', 'result.csv', as_attachment=True)
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True)
