#!/usr/bin/python3

jobs = {"job1" : "work/file1.txt",
        "job2" : "/home/ec2-user/environment/ictprg302/work/Dir1",
        "job3" : "work/missing.txt"}
        
dstDir = "/home/ec2-user/environment/ictprg302/backups"

logFile = "/home/ec2-user/environment/ictprg302/backup.log"

smtp = {"sender": "wlewis@sunitafe.edu.au",
        "recipient": "will.lewis456@gmail.com",
        "server": "smtp.gmail.com",
        "port": 587,
        "user": "will.lewis456@gmail.com", # need to specify a gmail email address with an app password setup
        "password": "ptxdnxyetrblvplh"}   # need a gmail app password