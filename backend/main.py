from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import detect_food,multi_detect_food

app = FastAPI(title="Food Recipe Generator")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_api_route("/detect", detect_food, methods=["POST"]  )
app.add_api_route("/multi_detect", multi_detect_food, methods=["POST"])
# @app.post("/text_recipe")
# def text_recipe(food: str = ""):
#     prompt = f"Simple and tasty recipe for {food}. Include ingredients and steps."
#     response = llm.invoke([HumanMessage(content=prompt)])
#     return {"recipe": response.content}





















# from fastapi import FastAPI,File,UploadFile
# from fastapi.middleware.cors import CORSMiddleware
# from PIL import Image
# from langchain_groq import ChatGroq
# from transformers import pipeline
# import os, shutil

# app=FastAPI(title="Food Predictor and Recipe Generator")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_methods=['*'],
#     allow_headers=['*']
# )

# classifier = pipeline("image-classification", model="nateraw/food")

# llm=ChatGroq(model="llama-3.3-70b-versatile",api_key='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')



# UPLOAD_DIR="../uploads"
# os.makedirs(UPLOAD_DIR,exist_ok=True)


# @app.post('/detect')
# async def detect_food(file: UploadFile=File(...)):
#     path=os.path.join(UPLOAD_DIR, file.filename)
#     with open(path, 'wb') as f:
#         shutil.copyfileobj(file.file, f)
#     image=Image.open(path)
#     results=classifier(image, top_k=1)
#     food=results[0]['label'].replace("_", " ").title()
#     confidence=results[0]['score']
#     prompt=f"Give a simple, delicious food recipe of {food}... "
#     response=llm.invoke(prompt)
#     recipe=response.content
#     return {"Detected Food": food, "Confidence": f"{confidence:.1%}", "Recipe": recipe
#             }