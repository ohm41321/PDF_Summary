"""
PDF Summarizer - Standalone Application Entry Point
"""

import os
import sys
import traceback
import webbrowser
import threading
import time
from pathlib import Path

# Fix for PyInstaller windowed mode
if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')

def resource_path(relative_path):
    """Get absolute path to resource"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Add the application directory to the path
app_dir = Path(os.path.dirname(os.path.abspath(sys.argv[0])))
os.chdir(app_dir)

# Create necessary directories
for directory in ['uploads', 'data', 'cache']:
    (app_dir / directory).mkdir(exist_ok=True)

def show_error_and_wait(title, message):
    """Show error message and wait for user to see it"""
    print("=" * 60)
    print(f"ERROR: {title}")
    print("=" * 60)
    print()
    print(message)
    print()
    print("=" * 60)
    print("Press ENTER to exit...")
    try:
        input()
    except:
        time.sleep(10)

def main():
    """Main application entry point"""
    try:
        # Check if index.html exists
        html_path = resource_path("index.html")
        if not os.path.exists(html_path):
            show_error_and_wait(
                "Missing index.html",
                f"Cannot find index.html!\n\n"
                f"Expected at: {html_path}\n"
                f"Current directory: {os.getcwd()}\n\n"
                f"Files in current directory:\n"
                + "\n".join(os.listdir("."))
            )
            sys.exit(1)

        print("Loading application...")
        
        # Import and run the FastAPI app
        from main import app
        import uvicorn

        def open_browser():
            """Open the browser after a short delay"""
            time.sleep(2)
            webbrowser.open('http://localhost:8000')

        # Open browser in a separate thread
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()

        # Start the server
        print("Starting server on http://localhost:8000")
        print("Press Ctrl+C to stop")
        print()
        
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")
        
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)
    except Exception as e:
        error_msg = traceback.format_exc()
        show_error_and_wait(
            "Application Error",
            f"Error: {str(e)}\n\n"
            f"Full traceback:\n{error_msg}"
        )
        sys.exit(1)

if __name__ == "__main__":
    main()
