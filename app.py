from flask import Flask, send_file, render_template, request
# Importing Required Modules
from rembg import remove
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD'] = "."



@app.route('/')
def home():
    return render_template('./home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['img']
    print(file.filename)
    filename = secure_filename(file.filename)
    file.save(filename)
    res = remove_bg(filename)
    
    return send_file(res, mimetype="image/png")
    


def remove_bg(filename):
    # Store path of the image in the variable input_path
    input_path =  "./TEST.jpg"
  
    # Store path of the output image in the variable output_path
    output_path = "./TESTout.png"
  
    # Processing the image
    input = Image.open(filename)

  
    # Removing the background from the given Image
    output = remove(input)
  
    #Saving the image in the given path
    output.save(output_path)
    return output
    