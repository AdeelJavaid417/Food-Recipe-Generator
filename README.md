# 🍽️ Food Recipe Generator

![App Workflow](App_Workflow.jpg)

A modern, dark-themed architecture diagram of a Food Recipe Generator application built with Streamlit (frontend) and FastAPI (backend). It shows two main paths: food classification using a ViT model (trained on Food-101) and ingredient/object detection using YOLOv11, both feeding detected items into Llama 3.3 70B to generate relevant recipes, with clean neon accents and a sleek AI-app layout.


---

## 🌟 Features

- *Food Recognition + Recipe Generation*  
  Upload any food photo → model detects what it is → LLM generates a complete recipe

- *Ingredient-based Dish Suggestions*  
  Upload a photo of fruits & vegetables → model identifies them → LLM suggests creative dishes you can make

- Modern, clean *Streamlit* user interface  
- Fast & production-ready *FastAPI* backend  
- Two main API endpoints:
  - POST /api/v1/generate-recipe  
  - POST /api/v1/suggest-dishes

## 🛠️ Tech Stack

| Layer              | Technology / Library                           |
|--------------------|------------------------------------------------|
| Backend            | FastAPI, Uvicorn                               |
| Frontend           | Streamlit                                      |
| Image Processing   | Pillow                                         |
| Computer Vision    | Ultralytics (YOLO), Transformers               |
| Models             | nateraw/food (food classification) <br> yolo_fruits_and_vegetables_v3.pt (YOLO) |
| LLM                | Llama-3.3-70b-versatile (via Groq)             |
| LLM Integration    | LangChain + Groq                               |
| Environment        | python-dotenv                                  |
| File Upload        | python-multipart                               |
| HTTP Client        | requests                                       |
| Deep Learning      | PyTorch, transformers                          |


## 📁 Project structure

Food-Recipe-Generator/
│
├── 📂 backend/                         # FastAPI backend services
│   ├── 🧠 __pycache__/                 # Python cache files
│   ├── ⚙️ config.json                  # Application configuration settings
│   ├── 🚀 main.py                      # FastAPI main application entry point
│   ├── 📦 models.py                    # Pydantic models / request-response schemas
│   ├── 🤖 pytorch_model.bin            # Saved PyTorch model weights
│   ├── 🛣 routes.py                    # API route definitions (endpoints)
│   └── 🎯 yolo_model.pt                # YOLO model weights (image detection)
│
├── 📂 frontend/                        # Streamlit frontend
│   └── 🖥 frontend.py                  # UI application file
│
├── 📂 uploads/                         # Temporarily stored uploaded images
│
├── 📂 myenv/                           # Virtual environment (ignored in Git)
│
├── 🔐 .env                             # Environment variables (API keys, configs)
├── 📦 requirements.txt                 # Project dependencies
└── ▶️ run_app.py                       # Script to launch the application

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/AdeelJavaid417/Food-Recipe-Generator.git
cd food-recipe-generator
```
### 2. Create virtual environment & install dependencies 
```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
# or on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create .env file
GROQ_API_KEY=your_groq_api_key_here
Optional: PORT=8000

### 4. Run the backend (FastAPI)
uvicorn main:app --reload --port 8000
or use the script if you have one: python run_backend.py

### 5. Run the frontend (Streamlit)
In a new terminal:
Bash
streamlit run app.py
usually opens at http://localhost:8501