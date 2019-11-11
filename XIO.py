import paramiko
import time
import re



class GetServerConnection():
    commands = []
    channel = ""
    commands.append("show-clusters-info")
    commands.append("show-debug-info")
    commands.append("create-debug-info")

    def get_latest_url(latest):
        #print(latest)
        url = re.findall(r'https://\S+', latest)
        #print(url[0])
        global id_url
        id_url = re.findall(r'\w+.tar.gz', url[0])
        #print(id_url)
        k = id[0].split('_')
        #print(k)
        #print(k[len(k) - 2])
        return id_url

    def comments(self,command):
        op = ""
        b = ""
        while ('>' not in op):
            b = self.channel.recv(60000)
            op = op + b.decode('ascii')
            op1 = b.decode('ascii')
            print(op1)
        i = 0
        l = op.splitlines()
        li = []
        while (i < len(l)):
            # print('1 loop')
            if command in l[i]:
                # print('if')
                i = i + 1
                while (('xmcli' in l[i]) == False):
                    li.append(l[i])
                    i += 1
            i += 1
        return li

    def getcon(self, host, port, arrayserialnumber, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.arrayserialnumber = arrayserialnumber
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh.connect(self.host,self.port,self.user,self.password)
            self.channel = ssh.invoke_shell()
            return 'success'
        except:
            print("couldn't establish the ssh connection")
            return "couldn't establish the ssh connection"

    def runcommands(self,arrayserialnumber, host, port, user, password, user2, password2):
        self.output = ""
        self.output_html = ""
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.user2 = user2
        self.password2 = password2
        self.arrayserialnumber = arrayserialnumber
        transport = paramiko.Transport((self.host, self.port))
        # Auth
        transport.connect(username=self.user, password=self.password)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(self.host, self.port, self.user, self.password)
        self.channel = ssh.invoke_shell()
        self.channel.send(user2+'\n')
        time.sleep(2)
        self.channel.send(password2+'\n')
        time.sleep(2)
        self.output_html +="""<!DOCTYPE html>
<html>
<head>
	<title>XIO Command Outputs</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
	<link rel="stylesheet" href="css/custom.css">
	<script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
</head>
<body>
<h1 align="center" style="background-color:grey">DELL EMC</h1>
<h2 align="center" style="background-color:cyan">XIO LOG COLLECTION</h2>
<h3 align="center" style="background-color:cyan">The Command Outputs</h3>
<div class="container">
    	 <div>"""

        self.output_html += """<table border='2' align='center'>"""
        line = []
        op = ""
        b = ""
        while ('>' not in op):
            b = self.channel.recv(60000)
            op = op + b.decode('ascii')
            i = 0
            l = op.splitlines()
            for lines in l:
                line.append(lines)
            if 'Username:' in line[len(line) - 1]:
                break
        if 'xmcli (tech)>' in line[len(line)-1]:
            self.output += '****************Executing the command show-clusters-info*******************'+'\n'
            self.output_html += """<tr><td align='center'><b>"""
            self.output_html += '****************Executing the command show-clusters-info*******************'
            self.output_html += """</td></tr>"""
            print('****************Executing the command show-clusters-info*******************'+'\n')
            self.channel.send('show-clusters-info')
            self.channel.send('\n')
            time.sleep(2)
            #print(self.comments('show-clusters-info'))
            cluster_info = (self.comments('show-clusters-info'))
            idcollect = ""
            for lines in cluster_info:
                self.output += lines+'\n'
                self.output_html += """<tr><td>"""
                self.output_html += lines
                self.output_html += """</td></tr>"""
                #print(lines)
            self.output += '****************Execution Completed for the command show-clusters-info*******************'+'\n'
            self.output_html += """<tr><td align='center'><b>"""
            self.output_html += '****************Execution Completed for the command show-clusters-info*******************'
            self.output_html += """</td></tr>"""
            print('****************Execution Completed for the command show-clusters-info*******************' + '\n')

            if(len(cluster_info) > 2):
                for lines in cluster_info:
                    if lines.find(self.arrayserialnumber) != -1:
                        idcollect = lines.split(" ")
                        for x in idcollect:
                            if x.isdigit():
                                print("yes set context value is " + x)
                                break
                        self.output += '****************Executing set-context cluster-id=' + x + '*******************'+'\n'
                        self.output_html += """<tr><td align='center'><b>"""
                        self.output_html += '****************Executing set-context cluster-id=' + x + '*******************'
                        self.output_html += """</td></tr>"""
                        print('****************Executing set-context cluster-id=' + x + '*******************' + '\n')
                        self.channel.send('set-context cluster-id=' + x)
                        self.channel.send('\n')
                        time.sleep(2)
                        set_context_info = (self.comments('set-context cluster-id=' + x))
                        for lines_context in set_context_info:
                            self.output += lines_context+'\n'
                            self.output_html += """<tr><td>"""
                            self.output_html += lines_context
                            self.output_html += """</td></tr>"""
                        self.output_html += """<tr><td align='center'><b>"""
                        self.output_html += '****************Execution of set-context cluster-id=' + x + 'Completed*******************'
                        self.output_html += """</td></tr>"""
                        self.output += '****************Execution of set-context cluster-id=' + x + 'Completed*******************'+'\n'
                        print('****************Execution of set-context cluster-id=' + x + 'Completed*******************' + '\n')
            self.output_html += """<tr><td align='center'><b>"""
            self.output_html += '****************Executing the command create-debug-info*******************'
            self.output_html += """</td></tr>"""
            self.output += '****************Executing the command create-debug-info*******************' + '\n'
            print('****************Executing the command create-debug-info*******************' + '\n')
            self.channel.send('create-debug-info')
            self.channel.send('\n')
            time.sleep(3)
            latest_url = (self.comments('create-debug-info'))
            for debug in latest_url:
                if debug.startswith('|') or debug.startswith('-') or debug.startswith('/') or debug.startswith(
                        '\\') or '[2K' in debug:
                    continue
                else:
                    # print(debug)
                    if debug.find("https://") != -1:
                        self.output += debug + '\n'
                        self.output_html += """<tr>"""
                        self.output_html += """<td>""" + debug + """</td>"""
                        self.output_html += """</tr>"""
                        # print("useful string = " + debug)
                        logname = debug.split("https://")
                        # print("Splitted string 2nd part " + logname[1])
                        usestring = logname[1].split("DebugInfo/")
                        # print("logs to download = " + usestring[1])
                    elif 'error' in debug:
                        self.output += debug + '\n'
                        self.output_html += """<tr><td style="background-color:red">""" + debug + """</td></tr>"""
                        self.output_html += """<tr><td>""" + "If error is due to space issue in XMS server refer below KB link else please analyse the error" + """</td></tr>"""
                        self.output_html += """<tr>"""
                        self.output_html += """<td style = "background-color:yellow"><a href=""" + "https://emcservice.my.salesforce.com/console" + """ target=""" + "_blank" + """>""" + "Click here for KB article and for Script" + """</a></td>"""
                        self.output_html += """</tr>"""
                    else:
                        self.output += debug + '\n'
                        self.output_html += """<tr>"""
                        self.output_html += """<td>""" + debug + """</td>"""
                        self.output_html += """</tr>"""
            self.output += '****************Executing Completed for the command create-debug-info*******************' + '\n'
            self.output_html += """<tr><td align='center'><b>"""
            self.output_html += '****************Executing Completed for the command create-debug-info*******************'
            self.output_html += """</td></tr>"""
            self.output_html += """</table>"""
            self.output_html += """</div></div></body></html>"""
            print('****************Executing Completed for the command create-debug-info*******************' + '\n')
            try:
                usestring[1] = usestring[1].strip()
                if len(usestring[1]) != 0:
                    print("No Error Encountered So Starting FTP")
                    #sftp = paramiko.SFTPClient.from_transport(transport)
                    print('FTP Started')
                    # Download
                    sftp_start = time.time()
                    try:
                        filepath = '/var/www/xtremapp/DebugInfo/' + usestring[1]
                        localpath = 'C:\\Users\\Public\\Check121\\' + usestring[1]
                        ftp = ssh.open_sftp()
                        ftp.get(filepath, localpath)
                        print('FTP Completed')
                        sftp_end = time.time()
                        print('FTP Complete in ', sftp_end-sftp_start)
                        return self.output, self.output_html
                    except:
                        location = 'C\\Users\\Public'
                        print('Unable to start FTP as Check121 folder is missing,Please create a folder name Check121 in ',location)
                else:
                    print("Encountered Error While downloading logs")
                    return self.output, self.output_html
            except :
                print('Logs were not created check in the original putty for cross check')
                return self.output, self.output_html
        else:
            print('The second login is not valid')
            return 'Failure', self.output_html
        self.channel.close()
        ssh.close()


if __name__ == '__main__':
    ob = GetServerConnection()