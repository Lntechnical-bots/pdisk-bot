from flask import Flask , render_template , request
from werkzeug.utils import secure_filename
from flask import send_file
app = Flask(__name__)

		
@app.route('/<message_id>')
def upload_fil(file_name):
   try:
   	path = f"/app/downloads/{message_id}"
   	return send_file(path, as_attachment=True)
   except:
   	return "404"
   


if __name__ == "__main__":
    app.run( debug=True)
