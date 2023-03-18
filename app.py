from flask import Flask, jsonify, request

app = Flask(__name__)


# example course data
courses = [
    {'id': 1, 'name': 'Intro to Programming', 'instructor': 'John Smith', 'email': 'johnsmith@school.edu'},
    {'id': 2, 'name': 'Web Development', 'instructor': 'Jane Doe', 'email': 'janedoe@school.edu'},
    {'id': 3, 'name': 'Database Design', 'instructor': 'John Smith', 'email': 'johnsmith@school.edu'},
    {'id': 4, 'name': 'Mobile App Development', 'instructor': 'Mark Johnson', 'email': 'markjohnson@school.edu'},
]

V1_API = '/v1/api'

@app.route(V1_API + '/courses', methods=['GET'])
def get_courses():
    instructor_name = request.args.get('instructor_name')
    instructor_email = request.args.get('instructor_email')
    matching_courses = []
    for course in courses:
        if course['instructor'] == instructor_name or course['email'] == instructor_email:
            matching_courses.append({'id': course['id'], 'name': course['name']})
    return jsonify(matching_courses)

@app.route("/")
def hello_world():
    return "<p>Hello, World! 2023 VT capstone</p>"


if __name__ == '__main__':
    app.run(debug=True)