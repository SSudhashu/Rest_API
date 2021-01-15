# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import json

# creating the flask app
app = Flask(__name__)


def Send_Notification(deviceToken, serverToken, TITAL, BODY):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
    }

    body = {
        'notification': {'title': TITAL,
                         'body': BODY

                         },
        'to':
            deviceToken,
        'priority': 'high',

    }

    response=requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())

@ app.route('/')
def first():
    return 'Use --- <h1>default/Your Subject /Your Message'

@ app.route('/default/<tital>/<body>')
def default(tital,body):
    tok1 = 'ed2YwBFnucxz5YLi5IEhZz:APA91bExWlPNqeHWx4AdRqQ-5zF0iuY5RuqMGQkqQoPblLT0YfOrM_DZ61Ktd8m8G1cg6rHh0fIoqGRwaoDcQfhYOg9X0SIUx6B5uXyri0KLflYufoLiuBuCh4wTd1-cfJYAmhpNzj2B'
    tok2 = 'ctku-EJ9REqv5A53b14m7m:APA91bFLBhSNEB4NVIhtSUqrSYDYfrmhcUDRMBQUFz_itTmZiYi0M2MrOAMXhoX7qgPcvWg7BiQbcfObXm-_ilUN7LXzLDPb7iac0T9OsXKPYagZKlqucESDrFO6fISdyb8gmxujen_1'
    tok3 = 'fbnsc5dHXeY42wzVsxYgz-:APA91bHj6K66ZnydZjwuLidz6Z7OZ3OFmitzSQVyDu-EhfIbTkvkD5bdzX_bC7IdpWSCL10L4t_swTGZdTRI8Da2TQYarzjqam_daYasESTvZT3XQiPZPgOl4n7-yJILiCpws5qDj6yY'

    sd = 'AAAAsoUpTB8:APA91bGe8iWhcEIDMgaNhZsq4Zx8-X7lvA48MDAYKfmIr3mFcVPNlxtjqdMIGV2Gh80_SxJ-UI3hG6z4D6BlgNgKdT8Xz4xFr6Ptlb5dbdriuCimDONcGghztMd8eCW_jkjTsdaOFDsl'

    Send_Notification(tok1,sd,tital,body)
    Send_Notification(tok2, sd, tital,body)
    Send_Notification(tok3, sd, tital,body)

# driver function
if __name__ == '__main__':
    app.run(debug=True)
