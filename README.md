# Auth-JWT-FastAPI

## Create a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate 
# On Windows: .\venv\Scripts\activate
```

## Install FastAPI, Uvicorn (ASGI server), and other required packages:
```bash
python -m pip install -r requirements.txt
python -m pip install --upgrade pip
```

## Start the server:
```bash
uvicorn app.main:app --reload
```