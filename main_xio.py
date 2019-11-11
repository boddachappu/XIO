
from flask import Flask, render_template, request
import datetime
import pyodbc
import getpass
import webbrowser
import time

from XIO import *
import subprocess

app = Flask(__name__)


start = time.time()
print(datetime.datetime.now())


def urlopen():
    print('inside urlopen')
    #subprocess.Popen(r'"C:\Program Files\Internet Explorer\IEXPLORE.EXE" http://127.0.0.1:2194/')
    webbrowser.open("http://127.1.1.1:2194/")

@app.route('/')
def homepage():
    return render_template("login.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        global user
        user = request.form['username'].strip()
        global password
        password = request.form['password'].strip()
        global host
        host = request.form['Hostname'].strip()
        global port
        port = request.form['Port Number'].strip()
        global arrayserialnumber
        arrayserialnumber = request.form['Array Serial Number'].strip()
        global Service_Request
        Service_Request = request.form['Service_Request'].strip()
        global Issue_Type
        Issue_Type = request.form['Issue Type'].strip()

        obj = GetServerConnection()
        res = obj.getcon(host, port, arrayserialnumber, user, password)

        if res == 'success':
            return render_template("login2_login.html",)
        else:
            return render_template("login.html", message=res)


@app.route('/login2', methods=['POST', 'GET'])
def sec_login():
    if request.method == 'POST':
        #try:
        global user2
        user2 = request.form['username'].strip()
        global password2
        password2 = request.form['password'].strip()
        obj2 = GetServerConnection()
        res, res_html = obj2.runcommands(arrayserialnumber, host, port, user, password, user2, password2)
        op_file = "C:\\Users\\Public\\Check121\\OUTPUT_XIO"+datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".html"
        file = open(op_file, 'w')
        file.write(res_html)
        file.close()
        #subprocess.Popen(r'"C:\Program Files\Internet Explorer\IEXPLORE.EXE" ' + op_file)
        webbrowser.open(op_file)
        stop_file = time.time()
        print('Time taken to copy file and generate the output html file is ', stop_file-start)
        #except:
            #location1 = 'C\\Users\\Public'
            #print('Unable to start FTP as Check121 folder is missing,Please create a folder name Check121 in ',location1)

        if res == 'Failure':
            return render_template("login2_login.html", message='The second login is not valid')
        else:
            try:
                ADID = getpass.getuser()
                x = datetime.datetime.today().strftime('%Y-%m-%d')
                y = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                Manual_Effort = 3000.00
                stop = time.time()
                Bot_Time_Taken = (stop - start)
                if Manual_Effort < Bot_Time_Taken:
                    Manual_Effort = Bot_Time_Taken + 300
                    print('As it was smaller than BOT TIME taken so new Manual efforts value = ', Manual_Effort)
                Effort_Saving = (Manual_Effort - Bot_Time_Taken)
                print('Efforts saving = ', Effort_Saving)
                print(datetime.datetime.now())
                print('Time taken to finish is', Bot_Time_Taken)
                print('We inserting the data into Database')
                conn = pyodbc.connect(DRIVER='{SQL Server}', SERVER='10.26.119.214',
                                      DATABASE='XIO_LOG_DOWNLOADER',
                                      UID='sa', PWD='wipro@123')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO dbo.XIO_LOG_DOWNLOADER (ADID,SR_No,Array_Serial_Number,Bot_Used_Date,Manual_Efforts_Required,Bot_Time_Taken,Efforts_Saving,Team_Name,Issue_Type,Usage_Create_Date) VALUES (?,?,?,?,?,?,?,'XIO',?,?)",
                    (ADID, Service_Request, arrayserialnumber, x, Manual_Effort, Bot_Time_Taken, Effort_Saving,Issue_Type, y))
                conn.commit()
                cursor.close()
            except:
                stop = time.time()
                print('Time taken to finish is', stop-start)
                print('The database will not be connected if you logged into the VDI')
            return render_template("Output.html", message=res)


stop = time.time()
print('Time taken is', stop-start)
print(datetime.datetime.now())


if __name__ == '__main__':
    urlopen()
    #app.run(debug=True, host='127.1.1.1', port='2194', use_reloader=False)
    app.run(debug=True, host='127.1.1.1', port='2194')