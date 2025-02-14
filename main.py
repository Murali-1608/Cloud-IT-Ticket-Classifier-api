import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# Sample categories (Replace this with your actual ML model predictions)
TICKET_CATEGORIES = {
    "network issue": "High Priority",
    "password reset": "Low Priority",
    "server down": "Critical",
}

# Request model
class TicketRequest(BaseModel):
    description: str

@app.get("/")
def read_root():
    return {"message": "Hello, Railway! Your FastAPI app is running 🚀"}

@app.post("/predict")
def predict_ticket(request: TicketRequest):
    """Predicts the priority of an IT ticket based on the description."""
    description = request.description.lower()

    # Simple rule-based classification (Replace this with an ML model later)
    prediction = TICKET_CATEGORIES.get(description, "Medium Priority")

    return {
        "description": request.description,
        "predicted_priority": prediction,
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Use Railway's assigned PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
