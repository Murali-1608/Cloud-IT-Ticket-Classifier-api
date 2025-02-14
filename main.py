import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Railway!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Railway uses PORT env variable
    uvicorn.run(app, host="0.0.0.0", port=port)
