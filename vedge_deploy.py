#gkopels@cisco.com
#Creates vEdge 18.1 using the following image: vedge-18.1.qcow2
import time
import os
device_name = input('Please enter the first device ID number: ')
n = input('How many devices do you want to create? ')
count = 1

while (count < n):
    print os.system('sudo cp /root/obs/images/viptela-edge-18.3.qcow2 /root/obs/images/vedge-%d.qcow2' % (device_name))
    time.sleep(10)
    print os.system('sudo virt-install  --connect=qemu:///system \
    --name=vedge-B%d \
    --os-type=linux \
    --os-variant ubuntu14.04 \
    --arch=x86_64 \
    --hvm \
    --cpu host \
    --ram=2048 \
    --vcpus=2 \
    --import \
    --disk path=/root/obs/images/vedge-%d.qcow2,bus=ide,size=5,format=qcow2 \
    --network bridge=br149,model=virtio \
    --network bridge=br150,model=virtio \
    --network bridge=br205,model=virtio \
    --network bridge=br502,model=virtio \
    --accelerate --graphics vnc,password=cisco,listen=0.0.0.0 --noautoconsole -v \
    --disk path=/root/obs/images/config%d.iso,device=cdrom,bus=ide\n' %(device_name,device_name,device_name))
    #--noreboot\n' %(device_name,device_name,device_name))
    time.sleep(10)
    print os.system('sudo virsh --connect qemu:///system start vedge-B%d\n' % (device_name))
    time.sleep(10)
    count = count + 1
    device_name = device_name + 1

print os.system('virsh list --all')



