# Event Management System (EMS) Using `REST API`

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Extract the project files.
2. Open the project in your preferred Integrated Development Environment (IDE).
3. Ensure the project structure is visible.
4. Install virtual environment using the following command: `pip install virtualenv`.
5. Create a virtual environment using: `python -m venv venv_folder_name`.
6. Activate the virtual environment. In the command prompt, use: 
   - For Windows: `venv_folder_name\Scripts\activate`
   - For Unix or MacOS: `source venv_folder_name/bin/activate`
7. Install Django using: `pip install django`.
8. Navigate to the project directory: `cd ems_project`.
9. Install the required packages using: `pip install -r requirements.txt`.
10. Start the server by running: `python manage.py runserver`.

If the server fails to run, follow these steps:

11. Just see the file in `ems_app\management\commands\task.py`.
12. Run the custom management command using: `python manage.py task`. This command is used to extract data from the CSV file using pandas.
13. After running the task, start the server again using: `python manage.py runserver`.

14. in localhost see the Filtered data `http://localhost:8000/events/find/?latitude=40.7128&longitude=-74.0060&date=2024-03-22`

## Usage

The project is an assessment for developing a RESTful service that manages and queries event data based on a user's geographical location and a specified date. This service ingests data from a provided CSV dataset and offers an API to find events for users.
