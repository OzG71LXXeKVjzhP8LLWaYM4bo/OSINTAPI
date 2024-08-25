from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
async def read_root():
    email_to_check = "test@gmail.com"
    return {"Hello": run_holehe(email_to_check)}

def run_holehe(email):
    try:
        # Run the Holehe command as a subprocess
        result = subprocess.run(['holehe', email], capture_output=True, text=True)
        
        # Print the output from Holehe
        return result.stdout
        
        # Check if there were any errors
        if result.stderr:
            print("Errors:", result.stderr)
    
    except Exception as e:
        print(f"An error occurred: {e}")