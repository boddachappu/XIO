# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:53:15 2018

@author: VI331224
"""
import pandas as pd
import pyodbc
import datetime
import getpass

conn = pyodbc.connect(DRIVER='{SQL Server}', SERVER='10.26.119.214',
                      DATABASE='universal_log_analyzer_usage',
                      UID='sa', PWD='wipro@123')
print(conn)
user = getpass.getuser()
x = datetime.datetime.today().strftime('%Y-%m-%d')
y = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
cursor = conn.cursor()
"""cursor.execute(
    "INSERT INTO Universal_Log_Analyzer_Usage (ADID,SR_NO,Array_Serial_Number,Bot_Used_Date,Manual_Effort_Required,Bot_Time_Taken,Effort_Saving,Team_Name,Issue_Type,Usage_Create_Date) VALUES (?,?,?,?,?,?,?,'Isilon','BMC_CMC',?)",
    (user, self.sr, self.arraySerial, x, Manual_Effort, Bot_Time_Taken, Effort_Saving, y))
conn.commit()"""

data = pd.read_sql_query("select * from Universal_Log_Analyzer_Usage where Team_Name = 'Isilon' and ADID not in ('SU376489','VI331224','MA324568','NA376494','GA394237') order by SLNO asc",conn)
print(data)
cursor.close()
conn.close()