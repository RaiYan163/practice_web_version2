from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ.get('DB_CONNECTION_STRING')
if db_connection_string:
    engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})
else:
    print("DB_CONNECTION_STRING environment variable is not set.")
    # Handle this error appropriately in your code



def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    return jobs




#load_jobs_from_db()

    


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