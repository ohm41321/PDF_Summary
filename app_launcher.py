"""
PDF Summarizer - Standalone Application Entry Point
This is the main entry point for the PyInstaller packaged application
"""

import os
import sys
import webbrowser
import threading
import time
from pathlib import Path

# Fix for PyInstaller windowed mode - sys.stdout/stderr can be None
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')

# Add the application directory to the path
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Ensure we're in the correct directory
app_dir = Path(os.path.dirname(os.path.abspath(sys.argv[0])))
os.chdir(app_dir)

# Create necessary directories
for directory in ['uploads', 'data', 'cache']:
    (app_dir / directory).mkdir(exist_ok=True)

# Import and run the FastAPI app
from main import app
import uvicorn

def open_browser():
    """Open the browser after a short delay to allow server to start"""
    time.sleep(2)
    webbrowser.open('http://localhost:8000')

if __name__ == "__main__":
    # Open browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()

    # Start the server
    # Use log_level="warning" to reduce console output in windowed mode
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")
    except KeyboardInterrupt:
        sys.exit(0)
