from flask import Flask , render_template , request
from werkzeug.utils import secure_filename
from flask import send_file
import os, os.path
app = Flask(__name__)

		
@app.route('/<file_name>')
def upload_fil(file_name):
   try:
   	DIR = '/storage/emulated/0/Download'
   	print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
   	path = f"/app/downloads/{file_name}"
   	return send_file(path, as_attachment=True)
   except:
   	return "404"
   	
   


if __name__ == "__main__":
    app.run( debug=True)
