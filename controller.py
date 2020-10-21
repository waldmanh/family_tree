from flask import Flask, render_template, request
import bl
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload')
def upload_file():
   return render_template('./upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
      result = bl.handle_new_excel(request.files['file'])
      if result=='FALSE':
          return 'error handling file'
      return result
		
if __name__ == '__main__':
   app.run(debug = True)