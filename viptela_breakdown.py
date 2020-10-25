#gkopels@cisco.com
#Delete vedge image

import time
import os
device_name = input('Please enter the first device ID number to remove: ')
n = input('How many devices do you want to remove? ')
count = 0

while (count < n):
    print os.system('sudo rm -r /root/obs/images/vedge-%d.qcow2' % (device_name))
    time.sleep(3)
    print os.system('sudo rm -r /root/obs/images/config%d.iso' % (device_name))
    time.sleep(3)
    print os.system('sudo virsh destroy vedge-B%d' %(device_name))
    time.sleep(3)
    print os.system('sudo virsh undefine vedge-B%d\n' % (device_name))
    time.sleep(5)
    count = count + 1
    device_name = device_name + 1

print os.system('sudo ls -alt /root/obs/images/')
