
from flask import Flask ,render_template , request, jsonify
from flask_uploads import UploadSet , configure_uploads, IMAGES
from attention8kfinal import main
from flask_cors import CORS
import os



app = Flask(__name__)
CORS(app)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app , photos)

#*************************************************************************************************************************************#

@app.route('/')
def index():
	return render_template('index.htm')


@app.route('/prediction',methods=['POST','GET'])
def predictions():
	''' This method takes the image file from the front-end 
		and then forwards this file to the 
		ML Model for further processing...
	'''
	if request.method == 'POST':
		#print(request.files)
		if request.files['photo']:
			path = photos.save(request.files['photo'])
			path ='.\\static\\img\\'+path
			caption = main(path)
			os.remove(path);
			return caption
		else:
			return "No file"
	return "Failed"



#****************************************************************************************************************************************#

@app.route('/prediction1',methods = ['POST','GET'])
def prediction1():
	'''This function handles the local images of the app and does the same functionality as the above function...'''
	if request.method == "POST":
		json = request.get_json()
		path1 = json["path"]
		caption = main("."+path1)
		return caption


#***************************************************************************************************************************************#

if __name__ == "__main__":
	'''Run this function with host=0.0.0.0 to run this server for all the devices on your network...'''
	app.run(host='0.0.0.0',debug=True,threaded=True)