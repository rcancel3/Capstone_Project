import sqlite3, pandas as pd
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
from twilio.rest import Client

class Database:
    def __init__(self, db='Login.db'):
        self.conn = sqlite3.connect(db, check_same_thread=False)
    
    def query(self, sql, params=()):
        return pd.read_sql(sql, self.conn, params=params)
    def check_if_user_exists(self, username, password):
        if self.query("SELECT * FROM login WHERE username = ?", params=(username,)).empty:
            return False
        else:
            # get user_id if password is correct
            user_id = self.query("SELECT * FROM login WHERE username =?", params=(username,))['user_id'].values[0]
            if not check_password_hash(self.query("SELECT * FROM login WHERE username = ?", params=(username,))['password'].values[0], password):
                user_id = None
                return False
            else:
                return user_id
                
    def insert_message(self, user_id, message, time_stamp):
        self.conn.execute("INSERT INTO messages (user_id, message, time_stamp) VALUES (?, ?, ?)", (user_id, message, time_stamp))
        self.conn.commit()
                
                
class MessageClient:
    def __init__(self):
        load_dotenv('.env')
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.send_to_number = os.environ['SEND_TO_NUMBER']
        self.send_from_number = os.environ['SEND_FROM_NUMBER']
        self.client = Client(account_sid, auth_token)
        
    def send(self, body):
        message = self.client.messages.create(
                              body=body,
                              from_=self.send_from_number,
                              to=self.send_to_number
                          )
        return message.sid