
# Django Rest API for User Authentication



## Technologies used
 Django, Django rest framework

* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs



## Installation(server)
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").

  

* #### Dependencies

    1.  Clone the project:
        ```bash
          git clone https://github.com/mayurgulhane/django-assignment.git
        ```

     2.  Go to the project directory:
        ```bash
           $ cd django-assignment
        ```

    4. Create and fire up your virtual environment:
        ```bash
            $ python -m venv virtual_name
            $ cd virtual_name/bin/activate
        ```
    5. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    6. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
       http://127.0.0.1:8000/users/
    ```



## API Reference

#### 1. User Registration

* URL: /users/register/
* Method: POST
* Description: Register a new user with first_name, last_name, email, username, and password.
* Request Body:

```http
  {
  "first_name": "first_name",
  "last_name": "last_name",
  "email": "user@example.com",
  "username": "example_user",
  "password": "your_password"
}
```
* Response:
    * 200 OK: Returns a success message and sends an OTP to the user's email for account verification.
    * 400 Bad Request: Returns error details if registration fails.

#### 2. Account Verification
* URL: /users/verify/
* Method: POST
* Description: Verify user account with OTP sent to email after registration.
* Request Body:
```http
 {
  "email_or_username": "user@example.com",
  "otp": "123456"
}
```
* Response:
    * 200 OK: Returns a success message upon successful account verification.
    * 400 Bad Request: Returns error if OTP is invalid or user does not exist.

#### 3. User Login
* URL: /users/login_view/
* Method: POST
* Description: Authenticate and login a user with OTP.
* Request Body:
```http
 {
  "email_or_username": "user@example.com",
  "otp": "123456"
}
```
* Response:
    * 200 OK: Returns user details along with access and refresh tokens.
    * 401 Unauthorized: Returns error for invalid credentials.

#### 4. Forgot Password
* URL: /users/forgot_password/
* Method: POST
* Description: Reset user password using OTP verification.
* Request Body:
```http
 {
  "email_or_username": "user@example.com",
  "password": "new_password"
}
```
* Response:
    * 200 OK: Returns a success message upon password update.
    * 401 Unauthorized: Returns error if user does not exist or invalid credentials.

#### 5. Reset Password
* URL: /users/reset_password/
* Method: POST
* Description: Reset user password using OTP and old password for verification.
* Request Body:
```http
 {
  "email_or_username": "user@example.com",
  "otp": "123456",
  "old_password": "current_password",
  "new_password": "new_password"
}
```
* Response:
    * 200 OK: Returns a success message upon password update.
    * 401 Unauthorized: Returns error for invalid old password or invalid credentials.


## Usage

1. Register a new user using /users/register/.
2. Verify the account using the OTP sent to the registered email address with /users/verify/.
3. Login using /users/login_view/ with the registered email or username and the OTP.
4. Use /users/forgot_password/ to reset the password in case of a forgotten password.
5. Reset the password using /users/reset_password/ with OTP verification and old/new password details.
