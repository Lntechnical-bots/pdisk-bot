from flask import Flask , render_template , request
from werkzeug.utils import secure_filename
from flask import send_file
app = Flask(__name__)

		
@app.route('/<file_name>')
def upload_fil(file_name):
   	path = f"downloads/{file_name}"
   	return send_file(path, as_attachment=True)
 


if __name__ == "__main__":
    app.run( debug=True)
