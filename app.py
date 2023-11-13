from flask import Flask, jsonify, request
from flask import render_template
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

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
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template("jobpage.html", job = job)

@app.route("/job/<id>/apply")
def apply_to_job(id):
  data = request.args
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', application=data, job=job)
 
  
  


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
