from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import io
import numpy as np
import tensorflow as tf
import tensorflow.image as tfi
from tensorflow.keras.utils import img_to_array
from PIL import Image, ImageEnhance
from keras.models import load_model

# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model during application startup
model = load_model('pix2pix_1000epoch.h5')

# Endpoint to colorize uploaded images
@app.post("/colourizer/")
async def get_colorized_image(file: UploadFile = File(...)):
    """
    Colorize an uploaded image.

    Parameters:
    - file: UploadFile - The image file to be colorized.

    Returns:
    - StreamingResponse: The colorized image as a streaming response.
    """
    try:
        # Read the uploaded image
        image = await file.read()

        # Process and colorize the image
        processed_image = process_image(image)
        colorized_image = colorize_image(processed_image)

        # Save the colorized image to a byte buffer
        colorized_image_bytes = save_image_to_bytes(colorized_image)

        # Return the colorized image as a streaming response
        return StreamingResponse(colorized_image_bytes, media_type="image/jpeg")

    except Exception as e:
        # Return an error response in case of an exception
        return {"error": str(e)}

# Function to preprocess the image
def process_image(image):
    """
    Preprocess the image.

    Parameters:
    - image: bytes - The raw image data.

    Returns:
    - np.ndarray: Processed image as a NumPy array.
    """
    img_array = np.zeros(shape=(1, 256, 256, 3), dtype=np.float32)

    # Convert image bytes to NumPy array
    img = np.array(Image.open(io.BytesIO(image)).convert('RGB'), dtype=np.float32)    
    img_array[0] = (tfi.resize(img, (256, 256))) / 255.0

    return img_array[0]

# Function to colorize the image using the pre-trained model
def colorize_image(image):
    """
    Colorize the image using a pre-trained model.

    Parameters:
    - image: np.ndarray - The preprocessed image.

    Returns:
    - PIL.Image.Image: Colorized image as a PIL Image.
    """
    # Feed image to model and get output
    pred_out = model.predict(tf.expand_dims(image, axis=0))[0]
    pred_out = (pred_out - np.min(pred_out)) / (np.max(pred_out) - np.min(pred_out))
    pred_out = (pred_out * 255).astype(np.uint8)

    # Convert numpy array to PIL Image
    pred_pil = Image.fromarray(pred_out)

    # Enhance color and contrast
    enhancer = ImageEnhance.Color(pred_pil)
    enhanced_pil = enhancer.enhance(1.3)

    enhancer = ImageEnhance.Contrast(enhanced_pil)
    enhanced_pil = enhancer.enhance(1.1)

    return enhanced_pil

# Function to save the PIL Image to a byte buffer
def save_image_to_bytes(image):
    """
    Save a PIL Image to a byte buffer.

    Parameters:
    - image: PIL.Image.Image - The image to be saved.

    Returns:
    - io.BytesIO: Byte buffer containing the image data.
    """
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='JPEG')
    image_bytes.seek(0)
    return image_bytes

# Run the FastAPI application using Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.4", port=8000)
