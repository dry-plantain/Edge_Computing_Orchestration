import io
from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageOps
import numpy as np

app = Flask(__name__)

# Function to process the image by adding a value to every pixel
def process_image(image, value):
    
    #image = Image.open(io.BytesIO(image))
    #image_array=np.array(image)
    #height, width, channels = image_array.shape
    #processed_image_array = image_array
    # Convert the processed image to bytes
    #for y in range(height):
    #    for x in range(width):
    #        for c in range(channels):
    #            # Add the specified value to each channel of the pixel
    #            processed_image_array[y, x, c] = np.uint8(image_array[y, x, c] + value)
    #processed_image = Image.fromarray(processed_image_array)
    #output_buffer = io.BytesIO()
    #processed_image.save(output_buffer,format="JPEG")
    #return output_buffer.getvalue()
    
    image = Image.open(io.BytesIO(image))
    processed_image = ImageOps.autocontrast(image, cutoff=value)
    return processed_image

@app.route('/process_image', methods=['POST'])
def process_image_api():
    try:
        value = float(request.form['value'])  # Get the value to add to the pixels
        uploaded_image = request.files['image'].read()  # Read the uploaded image
        # Process the image and get the processed image as bytes
        processed_image = process_image(uploaded_image, value)
        ##return send_file(io.BytesIO(processed_image_bytes), mimetype='image/jpeg')
        output_buffer = io.BytesIO()
        processed_image.save(output_buffer, format="JPEG")
        output_buffer.seek(0)
        return send_file(output_buffer, mimetype='image/jpeg')
    except Exception as e:
        print("check point5")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
