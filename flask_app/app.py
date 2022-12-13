from flask import Flask, flash, redirect, request, session, url_for, render_template, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from flask_session import Session     
from flask_socketio import SocketIO, emit
import pandas as pd
from WebSupport import Database, MessageClient
from datetime import datetime
import json


# create flask app 
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'ASDSIsoaidj20938sdaiu!@#ASD>,'
login_manager = LoginManager(app)
sess = Session(app)

socketio = SocketIO(app)

db = Database()
message_client = MessageClient()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
    
@app.route("/logout")
def logout_user():
    session['user_id'] = None
    session['username'] = None
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        user_id = db.check_if_user_exists(username, password)
        
        if user_id:
            session['user_id'] = user_id
            session['username'] = username
            return redirect(url_for('review_page'))
        else:
            return 'You are not logged in'
    
    else:
        
        return render_template('login_form.html')
    

@app.route('/', methods=["GET", "POST"])
def review_page():
    if session.get('user_id'):                       
        return render_template('review_page.html')
    else:
        return redirect(url_for('login'))



@socketio.on('is_this_food_related')
def is_this_food_related(data):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_id = session.get('user_id')
    user_name = session.get('username')
    raw_text = data['text']
    
    word_list_of_intrest = ['sick', 'vomit', 'poison']
    
    if any(word.lower() in raw_text for word in word_list_of_intrest):

        db.insert_message(user_id=user_id, message=raw_text, time_stamp=now)
        
        sms_message = 'A customer with name of %s at %s had concerning view about the food and said the following:\n\n%s' % (user_name, now, raw_text)
        
        message_client.send(sms_message)

        emit('is_this_food_related' , {'is_food_related':True})
    else:
        emit('is_this_food_related' , {'is_food_related':False})
        
        
        # socketio.sleep(0.1)




# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)