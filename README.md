# Generative Adversarial Network (GAN) - FastAPI Image Colorizer

This is a FastAPI application that colorizes images using a GAN pre-trained model.

## Requirements

Make sure you have Python and pip installed on your machine. You may also consider using a virtual environment for isolation.

```bash
# Install virtual environment (optional)
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Unix or MacOS
# or
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt or pip install tensorflow, python-multipart, pillow, and fastapi.
```

## How to Run
1. Activate Virtual Environment (if used):
```bash
source venv/bin/activate  # Unix or MacOS
# or
.\venv\Scripts\activate   # Windows
```
## How to Deactivate Virtual Environment
To deactivate the virtual environment, run the command
```bash
deactivate  # Unix or MacOS
# or
.\venv\Scripts\deactivate  # Windows
```

2. Run FastAPI:
```bash
uvicorn main:app --reload
```
Replace `main` with the actual name of your Python file and app with the name of your FastAPI instance if it's different. 

3. Access the API:
Once the server is running, you can access the API at [http://127.0.0.1:8000/](url). Use tools like curl, Postman, or a web browser using swagger [http://127.0.0.1:8000/docs](url)  to interact with the endpoints. Navigate to the /colourizer/ endpoint, click on "Try it out," and upload an image file.

4. Accessing through the HTML file
If you're testing through the frontend html file, the web browser may disallow requests from being processed from the originating domain to the server. If this happens, you can use a CORS handler extension to toggle the restriction off and proceed.


