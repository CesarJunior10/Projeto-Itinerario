run:
	uvicorn src.main:app --reload

install:
	pip install --upgrade pip
	pip install -r requirements.txt
