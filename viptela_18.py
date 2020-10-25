#gkopels

from shutil import copyfile
import sys
import os
import time

temp_user_data_file = 'temp_user-data.txt'
user_data_file = 'user-data'
serial_numbers_file = 'viptela_device_list.txt'
otp_numbers_file = 'viptela_device_otp.txt'


def main():
    ad = input('Please enter the number of the first device: ')
    device_id = ad
    device_ip = 4
    # copy user data template file to variable
    with open(temp_user_data_file, 'r') as template_fh:
        data_template=template_fh.read()
    template_fh.close

    # copy user data template file to variable
    serial_numbers = open(serial_numbers_file).read().splitlines()
    otp_numbers = open(otp_numbers_file).read().splitlines()

    # validate two files have same number of lines
    if (len(serial_numbers) != len(otp_numbers)):
        print ("two files have different number of lines")
        exit(1)

    for i in range(ad -1,len(otp_numbers)):
        otp_num = otp_numbers[i]
        serial_num = serial_numbers[i]
        temp_data = data_template.replace('$SN_NUM', serial_num).replace('$SN_OTP', otp_num).replace('$SITE_NUM', str(device_ip))
        # insert temp_data into user_data file
        with open(user_data_file, "w") as user_data_fh:
            user_data_fh.write(temp_data)
        user_data_fh.close

        print os.system('sudo genisoimage -o /root/obs/images/config%d.iso -V cidata -r -J meta-data user-data' % (device_id))
        time.sleep(3)
        device_id += 1
        device_ip += 1
        if (device_id==ad+70):
            print os.system('sudo ls -l /root/obs/images')
            exit(0)



    return

if __name__ == "__main__":
    main()


