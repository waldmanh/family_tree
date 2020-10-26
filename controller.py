from flask import Flask, render_template, request, send_from_directory
import bl

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/upload')
def upload_file():
    return render_template('./upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    script_to_run = str(request.query_string[12:])
    script_to_run = script_to_run[2:-1]
    print(script_to_run)
    if request.method == 'POST':       
        if script_to_run == 'script1':
            result = bl.script1(request.files['file'])
            print('result='+result)
            if result == 'false':
                 return 'error handling file'
            try:
                 return send_from_directory('./', 'result.csv', as_attachment=True)
            except Exception as e:
                 return str(e)
        elif script_to_run == 'script2':
            print('script_to_run = '+script_to_run)            
            bl.script2(request.files['file'])
            return send_from_directory('./', 'result.txt', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
