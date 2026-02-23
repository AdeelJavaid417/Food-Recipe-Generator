from transformers import pipeline
from langchain_groq import ChatGroq
from ultralytics import YOLO
from dotenv import load_dotenv
import os
load_dotenv()
def load_classifier():
    return pipeline("image-classification", model="nateraw/food")

def load_llm():
    api_key = os.getenv("GROQ_API_KEY")
    return ChatGroq(model="llama-3.3-70b-versatile",api_key=api_key)
yolo_model = YOLO("yolo_model.pt")

def get_yolo_model():
    return yolo_model