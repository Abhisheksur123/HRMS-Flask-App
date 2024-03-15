from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from wtforms import Form, StringField, validators

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/hrms'  # MongoDB URI
mongo = PyMongo(app)

# Define Employee Form for Input Validation
class EmployeeForm(Form):
    name = StringField('Name', validators=[validators.InputRequired()])
    designation = StringField('Designation', validators=[validators.InputRequired()])
    department = StringField('Department', validators=[validators.InputRequired()])
    date_of_joining = StringField('Date of Joining', validators=[validators.InputRequired()])

# Routes
@app.route('/')
def home():
    employees = mongo.db.employee.find()
    return render_template('home.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    form = EmployeeForm(request.form)
    if form.validate():
        data = form.data
        new_employee = {
            'name': data['name'],
            'designation': data['designation'],
            'department': data['department'],
            'date_of_joining': data['date_of_joining']
        }
        mongo.db.employee.insert_one(new_employee)
        return jsonify({'message': 'Employee added successfully'}), 201
    else:
        errors = form.errors
        return jsonify({'errors': errors}), 400

@app.route('/employees')
def get_employees():
    employees = list(mongo.db.employee.find())
    return jsonify(employees)

# Error Handling
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found', 'message': 'The requested resource was not found.'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
