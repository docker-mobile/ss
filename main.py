import sys
import os
def firststep():
  print('Installing Required SOFTWARES.......')
  os.system('sudo apt-get install openssh-client -y')
  os.system('sudo apt-get install openssh-server -y')
  os.system('sudo apt-get install curl -y')
  return 0
  pass
def steptwo():
  print "no more step remaining Printing IP"
  os.system('curl ifconfig.io')
  print 'DONE!!!!'
  pass
