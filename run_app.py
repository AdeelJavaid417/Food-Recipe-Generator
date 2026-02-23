import subprocess
import threading
import time
import webbrowser
import os

# Path to your backend and frontend folders
BACKEND_DIR = "backend"
FRONTEND_DIR = "frontend"
BACKEND_PORT = 8000
FRONTEND_PORT = 8501

def start_backend():
    """Start FastAPI backend with uvicorn in a separate process"""
    print("Starting FastAPI backend...")
    subprocess.run([
        "uvicorn", "main:app",
        "--host", "127.0.0.1",
        "--port", str(BACKEND_PORT),
        "--reload"
    ], cwd=BACKEND_DIR)

def start_frontend():
    """Wait a bit for backend, then start Streamlit"""
    print("Waiting for backend to start...")
    time.sleep(5)  # Give backend time to boot
    
    print("Starting Streamlit frontend...")
    subprocess.run([
        "streamlit", "run", "frontend.py",
        "--server.port", str(FRONTEND_PORT),
        "--server.address", "127.0.0.1"
    ], cwd=FRONTEND_DIR)

if __name__ == "__main__":
    # Start backend in background thread
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()
    
    # Start frontend in main thread
    start_frontend()
    
    # Optional: Auto-open browser
    time.sleep(8)
    webbrowser.open(f"http://localhost:{FRONTEND_PORT}")