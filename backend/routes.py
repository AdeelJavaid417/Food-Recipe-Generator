from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from PIL import Image
from models import load_classifier, load_llm, get_yolo_model
from langchain_core.messages import HumanMessage

classifier=load_classifier()
yolo_model = get_yolo_model()
llm=load_llm()
UPLOAD_DIR = "../uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def detect_food(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    image = Image.open(path)
    
    # Classify the food
    results = classifier(image, top_k=1)
    food_name = results[0]['label'].replace("_", " ").title()
    confidence = results[0]['score']
    
    # Generate recipe
    prompt = f"Give a simple, delicious recipe for {food_name}. Include ingredients for 2-4 people and step-by-step instructions. Keep it under 300 words."
    response = llm.invoke([HumanMessage(content=prompt)])
    recipe = response.content
    
    return {
        "detected_food": food_name,
        "confidence": f"{confidence:.1%}",
        "recipe": recipe
    }
async def multi_detect_food(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    
    results = yolo_model(path)
    
    if len(results) == 0:
        return {"message": "No detection results."}
    
    result = results[0]
    

    detected = set()
    for box in result.boxes:
        conf = float(box.conf)
        if conf > 0.2:
            label = result.names[int(box.cls)]
            detected.add(label.title())
    
    ingredients = list(detected)
    
    if not ingredients:
        return {"message": "No items detected with high confidence. Try better lighting or closer shot!"}
    
    # prompt: Ask for 3 different dishes
    prompt = f"""
I have these ingredients at home: {', '.join(ingredients)}.

Please suggest 3 different simple and tasty dishes I can make using as many of these ingredients as possible.

For each dish, include:
- A catchy title
- List of ingredients used (only from what I have)
- Easy step-by-step instructions for 2 people

Separate the 3 dishes clearly with numbers: Dish 1, Dish 2, Dish 3.

Make them creative but realistic!
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    recipes_text = response.content
    
    return {
        "detected_ingredients": ingredients,
        "dishes": recipes_text  # Contains all 3 dish suggestions
    }
def health():
    return{
        "STATUS": "OK",
        "VERSION": os.getenv("MODEL_VERSION"),
        "MODEL_LOADED": all([
            classifier is not None,
            yolo_model is not None,
            llm is not None
        ])
    }