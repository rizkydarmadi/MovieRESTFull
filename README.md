## Requirement

- python 3.11
- docker compose 3

## How to install(Linux os)

- start docker compose `sudo docker compose up -d`
- create virtualenv `python -m venv env`
- execute in `source env/bin/activate`
- install all dependecies `pip install -r requirements.txt`
- run the server `uvicorn main:app --reload`
