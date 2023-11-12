from sqlalchemy import create_engine, text
import os

def load_jobs_from_db(engine):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs

# Retrieve the DB connection string from environment variables
db_connection_string = os.environ.get('DB_CONNECTION_STRING')

if db_connection_string:
    # Create the engine
    engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})
else:
    print("DB_CONNECTION_STRING environment variable is not set.")
    # Handle this error appropriately in your code


