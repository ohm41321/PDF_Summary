"""
LM Studio Configuration Helper
Helps detect and configure LM Studio settings
"""
import requests
import json
import os

def check_lmstudio_status(url="http://localhost:1234"):
    """Check if LM Studio is running and get available models"""
    try:
        response = requests.get(f"{url}/v1/models", timeout=5)
        if response.status_code == 200:
            data = response.json()
            models = data.get("data", [])
            return {
                "status": "running",
                "url": url,
                "models": [m.get("id", "unknown") for m in models],
                "model_count": len(models)
            }
        else:
            return {"status": "error", "code": response.status_code}
    except requests.exceptions.ConnectionError:
        return {"status": "not_running"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def generate_env_template(models=None):
    """Generate .env file template with detected models"""
    env_content = """# LM Studio Configuration
# Change these values to match your LM Studio setup

# LM Studio server URL (default: http://localhost:1234)
LM_STUDIO_URL=http://localhost:1234

"""
    if models and len(models) > 0:
        env_content += f"# Detected models: {', '.join(models[:5])}\n"
        if len(models) > 0:
            env_content += f"LLM_MODEL={models[0]}\n"
    else:
        env_content += "# LLM Model (change to match your loaded model)\n"
        env_content += "LLM_MODEL=qwen2.5-7b-instruct\n"
    
    env_content += "\n# Embedding Model\n"
    env_content += "EMBEDDING_MODEL=bge-m3\n"
    
    return env_content

if __name__ == "__main__":
    print("Checking LM Studio status...")
    status = check_lmstudio_status()
    
    if status["status"] == "running":
        print(f"✓ LM Studio is running at {status['url']}")
        print(f"✓ Found {status['model_count']} model(s):")
        for model in status["models"]:
            print(f"  - {model}")
        
        env_content = generate_env_template(status["models"])
    else:
        print("✗ LM Studio is not running or not reachable")
        print("Please:")
        print("  1. Open LM Studio")
        print("  2. Load a model")
        print("  3. Click 'Start Server'")
        print("  4. Run this script again")
        
        env_content = generate_env_template()
    
    # Save .env file
    with open(".env.example", "w", encoding="utf-8") as f:
        f.write(env_content)
    
    print(f"\nGenerated .env.example with recommended settings")
