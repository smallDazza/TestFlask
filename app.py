from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Hello, welcome to testing with APIs!!!"

@app.route("/about")
def about():
    return "About page for testing "

@app.route("/contact")
def mycontact():
    return " My contact details will show"


courses = [
    {
        "Code": 101,
        "Name": "Diploma of IT",
        "Duration": "1.5 years"
    },
    {
        "Code": 102,
        "Name": "Diploma of Web Dev",
        "Duration": "1.5 years"
    },
    {
        "Code": 103,
        "Name": "Diploma of CS",
        "Duration": "2 years"
    },
    {
        "Code": 104,
        "Name": "Bachelors of IT",
        "Duration": "3 years"
    },
    {
        "Code": 105,
        "Name": "Bachelors of Web Dev",
        "Duration": "3.5 years"
    },
    {
        "Code": 106,
        "Name": "Bachelors of CS",
        "Duration": "4 years"
    }
]

@app.route("/courses")
def list_courses():
    # this is to filter results returned.Using the ? in the url.
    limit = request.args.get("limit")
    if limit:
        return courses[0:int(limit)]
    return courses

@app.route("/courses/103")
def course_103():
    return courses[2]

@app.route("/courses/200")
def error_route():
    return {"error": "Page does not exist"}, 404

# POST request = add something to db 
@app.route("/courses", methods=["POST"])
def add_course():
    body = request.get_json()
    courses.append(body)
    return courses

# DELETE request = remove course 107
@app.route("/courses/107", methods=["DELETE"])
def delete_course():
    del courses[-1]
    return {"message": "duplicate courses removed"}

# PUT & PATCH 
# PUT updates entire list/dictionary specified (in this case 107 dictionary)
@app.route("/courses/107", methods=["PUT"])
def update_course_107():
    body = request.get_json()
    courses[-1] = body
    return courses[-1]

#PATCH allows updating of only whats specified (in this case course name)
@app.route("/courses/101", methods=["PATCH"])
def update_101_name():
    body = request.get_json()
    courses[0]["Name"] = body.get("Name") or courses[0]["Name"]
    courses[0]["Duration"] = body.get("Duration") or courses[0]["Duration"]
    return courses[0]

# this is needed if wanting to run the app.py file in terminal (will auto run flask)
if __name__ == "__main__":
    app.run(debug=True)



