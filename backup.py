#!/usr/bin/python3
"""
title: backup.py,
author: Will Lewis
authors email: 30024194@students.sunitafe.com
version of program: 1
copyright: will lewis 2023
desriction: this program backups files and directories and creates a log of failed or successful backup entries amoung sending an email to an admin when theres an error.
"""

import sys
from backupcfg import jobs,dstDir, logFile, smtp
import shutil
import os
from datetime import datetime
import pathlib
import smtplib
 
def errorProcessing(errorMessage):
    """
    errorProccessing displayes an error to the user, a descption of why the error occured as well as emailing an admin with the same information.
    """
    print("ERROR: " + errorMessage) 
    
    file = open(logFile, "a")
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S") 
    """ this allows for a date and time stamp next to all log entries """
    file.write("FAILURE " + dateTimeStamp + " " + errorMessage + "\n" )
    file.close()
    """
    the code above creates a log of successful or unsuccessful log entries comfirming wether a file or dirctory was able to backup.
    """

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + errorMessage + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")
    """
    the code above connects with the google gamil account connected and sends it an error message whenever the backup errorProcessing is triggered to run.
    """
def main():
    """
    this checks for the job name being searched as well as the directory its being pulled from, if it odes not exists the errorProcessing function will happen.
    """
    try:
        if len(sys.argv) != 2:
            errorProcessing("job name missing")
        else:
            jobname = sys.argv[1]
            if not jobname in jobs:
                errorProcessing("Job not found in Dictionary")
            else:
                source = jobs[jobname] 
                if not os.path.exists(source):
                    errorProcessing("Source Does Not Exist")
                    
                else:
                    srcPath = pathlib.PurePath(source)
                    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                    dstLoc = dstDir + "/" + srcPath.name + "-" + dateTimeStamp
                    if pathlib.Path(source).is_dir():
                        shutil.copytree(source, dstLoc)
                    else:
                        shutil.copy2(source, dstLoc)
                    file = open(logFile, "a")
                    file.write("SUCCESS " + dateTimeStamp + " copyed  " + source + " to " + dstLoc + "\n" )
                    file.close()
                    """
                    the code above submits all the successful entires into the log file along with a date stamp.
                    """
                    
                  
                
    except:
        print("ERROR: Program Failed.")
    
if __name__ == "__main__":
    main()

