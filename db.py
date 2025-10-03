# db.py (simplified)
import sqlite3, json, datetime

DB = "data.db"

def get_conn():
    return sqlite3.connect(DB, check_same_thread=False)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    # run SQL from Data model section above...
    conn.commit()
    conn.close()

def add_attendee(event_id, name, email, job_role, interests, embedding):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
      INSERT INTO attendees (event_id, name, email, job_role, interests, embedding, created_ts)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (event_id, name, email, job_role, json.dumps(interests), json.dumps(embedding), datetime.datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
