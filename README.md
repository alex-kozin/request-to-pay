# request-to-pay

This is the official repository for the project created for CSC207 course at
the University of Toronto.

Here are instructions on how to get started:

1) Download the latest version of Python for your machine from here:
   https://www.python.org/downloads/

2) Open your command prompt (terminal), navigate to your favourite folder for
 storing projects in git-bash or any other tool you are using git with and run:

       git clone https://github.com/Mystery3051/request-to-pay.git

    This will create a project folder named **request-to-pay**.
    
3) Using command line (terminal) navigate inside *request_to_pay* folder.
 Your path should now look like that:
 
        ...\request-to-pay\request_to_pay\
 
4) Download a sample database from here: https://we.tl/t-R5Rytm6kOg 
(link expires at 2019-11-08) and place it inside *request_to_pay* folder. The path to the database should look like that:

        ...\request-to-pay\request_to_pay\db.sqlite3
 
5) While inside this folder, type:
 
    ```pip install -r requirements.txt``` if you are on Windows,
    
    ```pip3 install -r requirements.txt``` if you are on Mac.
    
    This will install all packages required to run the project.

6) While in the same folder, run

    ```python manage.py runserver``` on Windows, or
    
    ```python3 manage.py runserver``` on Mac.
    
    Django comes with a testing server that runs by default on ```localhost:8000```
   
7) You have made all the configuration required!

8) To explore the viewpoints, navigate to:
    - `localhost:8000/api/items` to see the list of items
    - `localhost:8000/api/items/1` to retrieve/update/destroy the item with id 1
    
    You can do the same for `orders` and `invoices`
    
    - The user logic is available for access through
     `localhost:8000/userapi/users`
     
     Note that most of the functions are not implemented for users, because
     there will be plugins that configure authentication and user authorization.
     The API does not provide those endpoints.
    
    You can also send POST requests to most endpoints ending with `/new`
    
    For example, try sending this POST request using [HTTPie](https://httpie.org/)
    (you should have installed it in Step 5):
    
        http -f POST http://127.0.0.1:8000/api/items/new name="Coke Ultra" price=200

The backend is deployed on Heroku: https://stormy-tor-06010.herokuapp.com/
