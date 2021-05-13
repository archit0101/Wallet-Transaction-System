# E-Wallet
## Installation of packages(Django is used for making REST API calls)
### 1) psycopg2 (pip install psycopg2): Connector for connecting our web application to Postgre DB.
### 2) Django (pip install Django)
### 3) Postgresql database for maintaining the account balances and the transaction logs which is hosted on heroku.
### 4) Navigate into the project Folder under name Archit and Run the application using (python manage.py runserver)


## The implemented functions include:
### 1) `Signup` and `Login`
       As soon as we hit the server, we see the page for `Sign-In` or `Register`. If already account exists then user can Login directly else the page will ask to signup first.
       After successfull Register, an account will be created for the user with default $100 balance.
  ![Screenshot from 2021-05-12 19-18-11](https://github.com/archit0101/E-Wallet/blob/main/screenshots/Login.png)
   
   ![Screenshot from 2021-05-12 19-18-11](https://github.com/archit0101/E-Wallet/blob/main/screenshots/Register.png)

### 2) `Credit` and `Debit`  and `minimum balance`
       `Debit`: You need to give the username and the amount that needs to be sent money to. The username should Exist else will shoot an error of `username not found`. Also in case your balance would fall below minimum balance($100) then the Debit operation will not occur and will give u a `warning to maintain minimum balance`.
       `Credit`: You need to Give the amount to be Credited.
       
  ![Screenshot from 2021-05-12 19-19-01](https://github.com/archit0101/E-Wallet/blob/main/screenshots/wallet.png)

   
### 3) `Transaction Log`
       A transaction log will be maintained for each user that is stored as one big table in database and will tell uss the type of transaction `Credit/Debit` and the `Amount` credited or debited
       
     
  ![Screenshot from 2021-05-12 19-20-08](https://github.com/archit0101/E-Wallet/blob/main/screenshots/wallet.png)
  
## Assumptions
### 1) Database Connectivity
       The Application code consist of the credentials of heroku database that may change over time automatically which may need to be updated in the application code.

## STEPS TO RUN:
### 1) Install all the necessary requirements using `requirements.txt` (`pip install -r requirements.txt`).
### 2) Locate into the project folder in which file `manage.py` is present.
### 3) Run the Application using command (`python manage.py runserver`)
### 4) Visit the URL on which server is running(`http://127.0.0.1:8000/`)

## Major Cases Hanadled:
### Uploaded the video `Demo.py` explaining all the major cases handled and also find the link for the uploaded video:
https://iiitaphyd-my.sharepoint.com/:v:/g/personal/archit_g_students_iiit_ac_in/EQEyw5Z-FnZGpAUrK7-viGYB1qH5MMyQPo1CjoaB06kZ5g?e=cURDtp



