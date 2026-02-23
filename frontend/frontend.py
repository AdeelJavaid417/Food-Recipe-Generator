import streamlit as st
import requests
from PIL import Image

st.title("🍕 Food Detector & Recipe Generator")

tab1, tab2 = st.tabs(["Single Food", "Multi-Food Plate (YOLO Model)"])

with tab1:
    file = st.file_uploader("Upload a food photo", type=["jpg", "png", "jpeg"])
    if file:
        image = Image.open(file)
        st.image(image, caption="Your Food Image", width="stretch")
        
        if st.button("Detect & Get Recipe"):
            with st.spinner("Detecting food and generating recipe..."):
                # ← FIXED LINE
                files = {"file": (file.name, file.getvalue(), file.type)}
                response = requests.post("http://localhost:8000/detect", files=files)
                
                # Add safety check
                if response.status_code != 200:
                    st.error(f"Backend error: {response.status_code}")
                    st.write(response.text)
                else:
                    data = response.json()
                    st.success(f"**Detected: {data['detected_food']}** ({data['confidence']})")
                    st.markdown("### 🍴 Recipe")
                    st.write(data["recipe"])

with tab2:
    st.markdown("### Upload a plate with multiple fruits/vegetables")
    file = st.file_uploader("Upload plate photo", type=["jpg", "png", "jpeg"], key="multi")
    if file:
        image = Image.open(file)
        st.image(image, caption="Your Plate", width="stretch")
        
        if st.button("Detect Ingredients & Generate Recipe"):
            with st.spinner("Detecting with your YOLO model..."):
                
                files = {"file": (file.name, file.getvalue(), file.type)}
                response = requests.post("http://localhost:8000/multi_detect", files=files)
                
              
                if response.status_code != 200:
                    st.error(f"Backend error: {response.status_code}")
                    st.write(response.text)
                else:
                    data = response.json()
                    
                    if "message" in data:
                        st.warning(data["message"])
                    else:
                        st.success(f"**Detected: {', '.join(data['detected_ingredients'])}**")
                        st.markdown("### 🍲 Recipe Using Your Ingredients")
                        st.write(data["dishes"])

st.caption("Powered by Hugging Face Food101 Model + Groq LLM + Your Trained YOLO")