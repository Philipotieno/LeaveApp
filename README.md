Leave Management
-----

### Introduction

Leave management app to create, list and update leave.


### Getting Started

To start and run the local development server,

1. Clone this repo:
    ```
    $ git clone https://github.com/Philipotieno/LeaveApp.git
    ```

2. Initialize and activate a virtualenv:
    ```
    $ python -m venv venv
    ```
3. Install the dependencies:
    ```
    $ pip install -r requirements.txt
    ```

4. Make migrations:
    ```
    $ python manage.py makemigrationsmigrate
    $ python manage.py migrate
    ```

5. Run the development server:
    ```
    $ python manage.py runsever
    ```

6. Navigate to index page [http://localhost:8000](http://localhost:8000)


### Formatting and Style
    ```
        $ pre-commit install
        $ pre-commit run --all-files
    ```
