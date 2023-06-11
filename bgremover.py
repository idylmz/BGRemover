# Importing Required Modules
from rembg import remove
from PIL import Image
import sys


logf = open("app.log", "w")

try:
# Store path of the image in the variable input_path
    input_path =  sys.argv[1]
    print(input_path)  
    logf.writelines(input_path)
    # Store path of the output image in the variable output_path
    output_path = sys.argv[2]
    print(output_path)  
    logf.writelines(output_path)
    
    # Processing the image
    input = Image.open(input_path)
    
    # Removing the background from the given Image
    output = remove(input)
    
    #Saving the image in the given path
    output.save(output_path)
except Exception as e:
    logf.writelines(str(e))