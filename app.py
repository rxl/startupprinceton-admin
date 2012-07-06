from flask import Flask, request, render_template
import urlparse, urllib
import time
import datetime
import os
from flask import send_from_directory
from flaskext.mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config.update(
    DEBUG = True,
    #Email settings
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587, # 465 or 587
    MAIL_USE_TLS = True,
    MAIL_USERNAME = 'info@princetoneclub.com',
    MAIL_PASSWORD = 'Tigerlaunch#1'
)

mail = Mail(app)

@app.route('/')
def index():
    return '''
        <h1>The Princeton Entrepreneurship Club</h1>
        <h2>Internal Tools</h2>
        <p><a href="/add_event">Add Event</a></p>
        <p><a href="http://www.princetoneclub.com">Website</a></p>
    '''

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

# to do:
# convert incoming dates to date formats
# allow script to send email containing url
# have error checking in the form

@app.route('/add_event', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
        
        timedelta = datetime.timedelta(hours=0)
        starts = request.form['starts']
        if starts.endswith('AM'):
            starts = starts.rstrip('AM')
            timedelta = datetime.timedelta(hours=5)
        elif starts.endswith('PM'):
            starts = starts.rstrip('PM')
            timedelta = datetime.timedelta(hours=17)
        t_stripped = time.strptime(starts, '%m-%d-%Y %H:%M')
        d = datetime.datetime(t_stripped.tm_year, t_stripped.tm_mon, t_stripped.tm_mday, t_stripped.tm_hour, t_stripped.tm_min)
        d_shifted = d + timedelta
        starts_formatted = d_shifted.strftime("%Y%m%dT%H%M00Z")
        
        ends = request.form['ends']
        if ends.endswith('AM'):
            ends = ends.rstrip('AM')
            timedelta = datetime.timedelta(hours=5)
        elif ends.endswith('PM'):
            ends = ends.rstrip('PM')
            timedelta = datetime.timedelta(hours=17)
        t_stripped = time.strptime(ends, '%m-%d-%Y %H:%M')
        d = datetime.datetime(t_stripped.tm_year, t_stripped.tm_mon, t_stripped.tm_mday, t_stripped.tm_hour, t_stripped.tm_min)
        d_shifted = d + timedelta
        ends_formatted = d_shifted.strftime("%Y%m%dT%H%M00Z")
        
        date1 = starts_formatted #'20120301T240000Z'
        date2 = ends_formatted #'20120303T270000Z'
        text = request.form['headline']
        if (request.form['website'].strip() != ""):
            text += ' (' + request.form['website'] + ')'
        
        params = {
            'action' : 'TEMPLATE',
            'text' : text,
            'dates' : date1 + '/' + date2,
            'location' : request.form['location'],
            'details' : request.form['details'],
            'prop' : 'name:eclubform'
        }
        
        #add_gcal_url = 'http://www.google.com/calendar/event?action=TEMPLATE' + '&text=' + headline + '&dates=' + date_time + '&location=' + location + '&details=' + announcement + '&prop=name:eclubform'
        #params = { 'name' : 'ryan', 'age' : 21 }
        utf_params = {}
        for k, v in params.iteritems():
            utf_params[k] = unicode(v).encode('utf-8')
        query = urllib.urlencode(utf_params)
        parts = ['http', 'www.google.com', '/calendar/event', '', query, '']
        add_to_gcal_url = urlparse.urlunparse(parts)
        
        messageText = '<h2>url</h2><p>' + add_to_gcal_url + '</p><h2>name</h2><p>' + name + '</p><h2>email</h2><p>' + email + '</p>'
        
        # send mail
        msg = Message("New Event Submission", sender="info@princetoneclub.com", recipients=["me@ryanshea.org"])
        msg.html = messageText
        #print msg
        mail.send(msg)
        
        return messageText;
    else:
        return render_template('add_event.html')

if __name__ == '__main__':
	app.run()