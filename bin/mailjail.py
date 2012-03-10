#!/usr/bin/python
#/etc/postfix/master.cf
#mailjail unix - n n - - pipe
#  flags=FDRq user=_user_ argv=/home/_user_/mailjail/mailjail.py $sender $recipient
#

import sys,os
import time


DIR=os.path.abspath(os.path.dirname(__file__))+"/mail"

if False == os.path.isdir(DIR):
   os.mkdir(DIR)

def main():
  (sender,receipient)=('from','to')
  if len(sys.argv) > 1:
    sender=sys.argv[1]
    if len(sys.argv)> 2:
       receipient = sys.argv[2]
  filename = sender + "-" + receipient+'-'+time.strftime('%Y%m%dT%H%M%S',time.localtime()) + ".eml"

  if sys.stdin.isatty():
    print "*** NO STDIN ***"
    return

  f=open(DIR+'/'+filename,'w')
  if None != f:
    f.writelines(sys.stdin.readlines())
    f.close()


if __name__ == '__main__':
  main()
