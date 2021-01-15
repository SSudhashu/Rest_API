
from flask import Flask #jsonify, request,send_file
#from flask_restful import Resource, Api
import requests
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#import csv

# creating the flask app
app = Flask(__name__)

sd = 'AAAAsoUpTB8:APA91bGe8iWhcEIDMgaNhZsq4Zx8-X7lvA48MDAYKfmIr3mFcVPNlxtjqdMIGV2Gh80_SxJ-UI3hG6z4D6BlgNgKdT8Xz4xFr6Ptlb5dbdriuCimDONcGghztMd8eCW_jkjTsdaOFDsl'

def App_Being_Used(sdk_path, save_path):
    try:

        cred = credentials.Certificate(
            sdk_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        emp_ref = db.collection("ActivityB")

    except:
        # print('\n!!! SOME ERROR OCCURRED !!!')
        db = firestore.client()
        emp_ref = db.collection("ActivityB")

    a = emp_ref.stream()
    # print('AAAA : ',a.to_di)
    d = {}

    def Count(name, date):

        if name not in d:
            cou = 1
            dat = {}
            dat[date] = cou
            d[name] = dat
        else:
            # date=a['date']
            # print('DATATATATA : ',date)

            dote = d[name]
            # print(dote)

            if date not in dote:

                dote[date] = 1
                d[name] = dote

            else:
                dote[date] = dote[date] + 1
                d[name] = dote

        # print('NOAME : ',d)

    for key in a:
        name = key.id.split(':')[1]
        # print('DATU :',key.to_dict()['date'])
        Count(name, key.to_dict()['date'])


    return d
    # with open(save_path, 'w+') as f:
    #
    #     Writer = csv.writer(f)
    #     Writer.writerow(['Name', 'Count'])
    #     for key in d.keys():
    #         # print("Entered ",[key, d[key]])
    #         if (len(key) != 0):
    #             Writer.writerow([key, d[key]])
    #
    #     f.close()


    #print('\nData Is Stored Successfully !!! \n')

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
    d='''
        <h1>Try<h1> <h2> "/default / Your Subject / Your Message" <h2><br>
        <h1>Try<h1> <h2> "/1" to get the Use Rate <h2>
    '''
    # d='''
    #     1. Try - /default / Your Subject / Your Message
    #     2. To get the USE RATE Try - /1
    # '''
    return d


@ app.route('/1')
def Usedata():
    fd=r'C:/Users/SUDHANSHU/PycharmProjects/FireBase/rock_you_firebase.json'
    d=App_Being_Used(fd, '/UseData.csv')
    #path = "/Use_Rate.csv"
    return d#send_file(path, as_attachment=True)
    #return  "<h1>DONE!!!<h1>"




@ app.route('/default/<tital>/<body>')
def default(tital,body):
    tok1 = 'ed2YwBFnucxz5YLi5IEhZz:APA91bExWlPNqeHWx4AdRqQ-5zF0iuY5RuqMGQkqQoPblLT0YfOrM_DZ61Ktd8m8G1cg6rHh0fIoqGRwaoDcQfhYOg9X0SIUx6B5uXyri0KLflYufoLiuBuCh4wTd1-cfJYAmhpNzj2B'
    tok2 = 'ctku-EJ9REqv5A53b14m7m:APA91bFLBhSNEB4NVIhtSUqrSYDYfrmhcUDRMBQUFz_itTmZiYi0M2MrOAMXhoX7qgPcvWg7BiQbcfObXm-_ilUN7LXzLDPb7iac0T9OsXKPYagZKlqucESDrFO6fISdyb8gmxujen_1'
    tok3 = 'fbnsc5dHXeY42wzVsxYgz-:APA91bHj6K66ZnydZjwuLidz6Z7OZ3OFmitzSQVyDu-EhfIbTkvkD5bdzX_bC7IdpWSCL10L4t_swTGZdTRI8Da2TQYarzjqam_daYasESTvZT3XQiPZPgOl4n7-yJILiCpws5qDj6yY'

    sd = 'AAAAsoUpTB8:APA91bGe8iWhcEIDMgaNhZsq4Zx8-X7lvA48MDAYKfmIr3mFcVPNlxtjqdMIGV2Gh80_SxJ-UI3hG6z4D6BlgNgKdT8Xz4xFr6Ptlb5dbdriuCimDONcGghztMd8eCW_jkjTsdaOFDsl'

    Send_Notification(tok1,sd,tital,body)
    Send_Notification(tok2, sd, tital,body)
    Send_Notification(tok3, sd, tital,body)
    return '<h1>Message is Send...<h1>'

# driver function
if __name__ == '__main__':
    app.run(debug=True)
