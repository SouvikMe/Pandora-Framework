#!/usr/bin/env python
import os
import time


print '\33[92;1mInstalling the Pandora\'s Framework\33[00m'
time.sleep(3)
di = os.getcwd()

os.system('chmod +x ' + di + '/pandora/pandogen.py')
os.system('chmod +x ' + di + '/pandora/pandora.py')
os.system('ln -s ~/Pandora-Framework/pandora/pandora.py Pandora')
os.system('ln -s ~/Pandora-Framework/pandora/pandogen.py Pandogen')

print '\33[92;1mInstalling neccessary packages\33[00m'
os.system('pkg update')
os.system('pkg upgrade')
os.system('pkg install python2')
print '\33[93;1mInstaling requirements\33[00m'
time.sleep(2)
os.system('pip install -r requirements.txt')
print 'Installation of packages:\33[92;1m  done\33[00m'
print 'Successfully installed\33[91;1m Pandora\33[00m'
print 'Finishing up...... '
time.sleep(3)
print 'run program as \33[94;1m./Pandora\33[00m'

