# Auth-JWT-FastAPI

```bash
project_name/
├── app/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── jwt_settings.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   ├── main.py
├── .env
├── requirements.txt
```

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