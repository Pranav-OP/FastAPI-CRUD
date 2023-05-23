# FastAPI-CRUD
Performed CRUD operations Python's FastAPI library using MySQL for database and SQLAlchemy for database connectivity. <br />
Reference Article : https://medium.com/@dennisivy/my-first-crud-app-with-fast-api-74ac190d2dcc <br />
livestreamed video : https://www.youtube.com/watch?v=FOZNYBu8u18 <br />

## Virtual Environment Setup
In order to run the app, it is recommended you first create and activate a virtual environment:
```bash
python -m venv crud
# python3 -m venv crud

# To Activate Virtual Environment
# For Windows OS
crud\Scripts\activate

# For Unix-based OS
source crud/bin/activate
```
## Installing Libraries 

Once the virtual environment is activated, <br />
To install all necessary libraries, simply run <br />
```bash
pip install -r requirements.txt
```

## Run the app
There are multiple options available to run the app. <br />
The most common way is by running the command
```bash
uvicorn main:app --reload
```
where main.py is the main driver file <br />
<br />
If you would like to choose a specific port (if 8000 is already occupied by another program), then you can run
```bash
uvicorn main:app --reload --port <PORT>
```
where the `<PORT>` is a number of your choosing. <br />

For the rest of the options when running a uvicorn app, visit https://www.uvicorn.org/#command-line-options.
