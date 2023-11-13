from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ.get('DB_CONNECTION_STRING')
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    query = text("SELECT * FROM jobs WHERE id = :val")
    result = conn.execute(query, {'val': id}) 
    #gave error here before, fixed
    
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return (rows[0]._asdict())






#load_jobs_from_db()



def add_application_to_db(job_id, data):
  with engine.connect() as conn:
            query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
            conn.execute(query, {
                'job_id': job_id,
                'full_name': data['full_name'],
                'email': data['email'],
                'linkedin_url': data['linkedin_url'],
                'education': data['education'],
                'work_experience': data['work_experience'],
                'resume_url': data['resume_url']
            })



    


#with engine.connect() as conn:
#  result = conn.execute(text("select * from jobs"))

#  result_dicts = []
#  for row in result.all():
#    result_dicts.append(row._asdict())

#  print(result_dicts)
  
  
  #print("Type:", type(result_all))
  #print("result.all():", result_all)
  #print("type of result:", type(result))
  #first_result = result_all[0]
  #print("type of first result:", type(first_result))
  #print(first_result)
  #first_result_dict = first_result._asdict()
  #print("type(first_result_dict):", type(first_result_dict))
  #print(first_result_dict)