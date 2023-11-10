from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Khulna, Bangladesh',
    'Salary': 'Tk. 1,00,000'
}, {
    'id': 2,
    'title': 'Software Engineer',
    'Location': 'Dhaka, Bangladesh',
    'Salary': 'Tk. 2,00,000'
}, {
    'id': 3,
    'title': 'Cloud specialist',
    'Location': 'Khulna, Bangladesh',
    'Salary': 'Tk. 2,00,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, person_name="Raiyan")

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
