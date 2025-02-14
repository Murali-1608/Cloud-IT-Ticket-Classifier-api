# Cloud-IT-Ticket-Classifier-api

This FastAPI project classifies IT support tickets based on priority.

##  Features:
- Uses **Machine Learning (DistilBERT)** for classification
- Provides **priority prediction**
- Free deployment on **Railway.app**

##  API Endpoints:
- `GET /` → Home
- `POST /predict` → Predicts ticket priority

##  How to Run Locally:
```sh
uvicorn main:app --host 0.0.0.0 --port 8080
