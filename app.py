import io
import sys
import numpy as np
from PIL import Image
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, File, UploadFile , HTTPException , Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from fastapi.templating import Jinja2Templates

# --- Model and Constants ---
model_path = r"E:\New folder\chest-xray-pneumonia-detection\model\chest_xray_model.keras"  # Path to the trained Keras model
image_size = (150, 150)  # Input image size
THRESHOLD = 0.6  # Threshold to classify Pneumonia
class_names = ["NORMAL", "PNEUMONIA"]  # Class labels

# Load the model
try:
    model = load_model(model_path)  # Load Keras model
    print(f"Model loaded successfully: {model_path}")
except Exception as e:
    print(f"ERROR: Model not loaded. Detail: {e}")  # Print error if loading fails

# Initialize FastAPI app
app = FastAPI( 
    title="Chest X-Ray Pneumonia Detection System",  # App title
    description="* AI-powered system that analyzes chest X-rays *",  # App description
    version="1.0.0"
)

# Allowed origins for CORS
origins = [
           
           "http://127.0.0.1:8800",  # Localhost
           "http://localhost:8800" 
           
           ] 

# Templates directory
templates = Jinja2Templates(directory= "templates")  # HTML templates folder

# Middleware for CORS
app.add_middleware(CORSMiddleware, 
                   allow_origins=origins,  # Allowed origins
                   allow_credentials=True, 
                   allow_methods=["*"], 
                   allow_headers=["*"])

# Image preprocessing function
def preprocessing_image(image_data):
    try:
        img = Image.open(io.BytesIO(image_data)).convert("RGB")  # Open image and convert to RGB
        img = img.resize(image_size)  # Resize to model input size
        image_array = np.array(img, dtype=np.float32) / 255.0  # Normalize pixel values
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
        return image_array
    except Exception as e:
        print(f"Error in image processing: {e}")  # Print error if preprocessing fails
        return None


# Home page route
@app.get("/" , response_class=HTMLResponse )
async def server_ui(request : Request):
    return templates.TemplateResponse("index.html" , {"request" : request})  # Render HTML template


# Prediction endpoint
@app.post("/PREDICTION")
async def prediction(file: UploadFile = File(...)):
    image_data = await file.read()  # Read uploaded file
    processed_image = preprocessing_image(image_data)  # Preprocess image

    if processed_image is None:
        return JSONResponse(status_code=400, content={"Error": "Invalid image file or processing failed."})
        # Return error if image is invalid

    try:
        raw_prediction = model.predict(processed_image)  # Make prediction using model
        score = float(raw_prediction[0][0])  # Confidence score
        Diagnosis = class_names[1] if score >= THRESHOLD else class_names[0]  # Determine diagnosis
        return {
            "Prediction": raw_prediction.tolist(),  # Raw prediction output
            "Diagnosis": Diagnosis,  # Predicted class
            "Confidance_Score_PNEUMONIA": score,  # Confidence score for Pneumonia
            "THRESHOLD": THRESHOLD  # Threshold used
        }
    except Exception as e:
        print(f"Prediction failed: {e}", file=sys.stderr)  # Print error if prediction fails
        return JSONResponse(status_code=500, content={"Error": "Prediction failed internally."})

# Run FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8800)  # Run local server