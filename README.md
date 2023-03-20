# Projeto-Itinerario

## Requirements:
* Python 3.9+
* Docker
* Docker compose

## Setup
Create a virtual environment:
```shell
python -m venv .venv
```

activate it:
```shell
source .venv/bin/activate
```

and install dependencies
```shell
pip install -r requirements.txt
```

For help, type:
```shell
make help
```


## Libraries and tools
1. FastAPI + uvicorn as web framework
2. SQLAlchemy as ORM
3. Pydantic for data validation and settings management
4. Alembic for database migration
