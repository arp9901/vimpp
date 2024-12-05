import base64
from io import BytesIO
import cv2
import numpy as np
from PIL import Image
from flask import jsonify

def handler(request):
    # Get the base64 image data from the frontend
    data = request.get_json()
    image_data = data['image']
    
    # Decode the base64 image data
    img_data = base64.b64decode(image_data.split(',')[1])
    img = Image.open(BytesIO(img_data))
    
    # Convert the image to a NumPy array for OpenCV processing
    img_np = np.array(img)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    
    # Convert the grayscale image back to RGB for display in frontend
    gray_image_rgb = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
    
    # Encode the processed image to base64
    _, buffer = cv2.imencode('.png', gray_image_rgb)
    gray_image_base64 = base64.b64encode(buffer).decode('utf-8')
    
    # Return the base64 image data to the frontend
    return jsonify(grayscale_image=f"data:image/png;base64,{gray_image_base64}")
