from fastapi import FastAPI, Query
import subprocess
import requests

app = FastAPI()

@app.get("/email1")
async def read_root(q: str = Query(..., description="Email address to check")):
    return {"result": run_holehe(q)}

@app.get("/phone1")
async def a(q: str = Query(..., description="Email address to check")):
    return {"result": "a"}

def run_phoneinfoga():
    try:
        r = requests.get("http://localhost:5000/api/v2/scanners", headers = {"content-type": "application/json"})
    except Exception as e:
        return {"error": str(e)}

def run_holehe(email):
    try:
        # Run the Holehe command with the correct flags
        result = subprocess.run(['holehe', email, '--only-used', '--no-color'], capture_output=True, text=True)
        
        if result.stdout:
            # Split the output by lines
            lines = result.stdout.splitlines()
            
            # Filter out lines that contain "Twitter:" or "1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ"
            filtered_lines = [
                line for line in lines 
                if "Twitter:" not in line and "1FHDM49QfZX6pJmhjLE5tB2K6CaTLMZpXZ" not in line and "megadose"
            ]
            
            # Join the filtered lines back into a single string
            cleaned_output = "\n".join(filtered_lines)
            return cleaned_output
        
        else:
            return {"error": result.stderr}
    
    except Exception as e:
        return {"error": str(e)}
    
    

