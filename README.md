HRMS Flask App
This project is a basic Human Resource Management System (HRMS) implemented using Flask. It includes functionalities such as employee management, attendance tracking, and basic reporting.

Getting Started
Follow these steps to set up and run the HRMS Flask app on your local machine.

Prerequisites
Make sure you have the following installed:

Python 3.x
Flask
Flask-PyMongo
MongoDB (optional, for database usage)
Installation
Clone the repository to your local machine:
git clone https://github.com/your-username/hrms-flask-app.git
Navigate to the project directory:

bash
cd hrms-flask-app
Install the required Python packages:

bash
pip install -r requirements.txt
Configuration
Set up the MongoDB URI in app.py:
python
app.config['MONGO_URI'] = 'mongodb://localhost:27017/hrms'
Running the App
Start the Flask development server:

bash
python app.py
Access the app in your web browser at http://localhost:5000/.

Project Structure
csharp
hrms-flask-app/
│
├── app.py              # Flask application file
├── templates/          # HTML templates
│   └── home.html       # Home page template
├── static/             # Static files (CSS, JS, etc.)
│   └── style.css       # CSS styles
├── requirements.txt    # Python package requirements
└── README.md           # Project README file
Usage
Navigate to http://localhost:5000/ to access the home page of the HRMS Flask app.
Use the provided API endpoints to add employees, retrieve employee data, and perform attendance tracking.
API Endpoints
/add_employee (POST): Add a new employee.
/employees (GET): Retrieve the list of all employees.
Additional Information
Modify the database URI (MONGO_URI) in app.py to connect to your MongoDB instance.
Customize HTML templates and static files in the templates/ and static/ directories as needed.
