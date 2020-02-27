#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import hashlib
import datetime
import re


# regular expression for cpu_id result = re.match(r'([a-f]|[A-F]|[0-9]){6}$', a)
# for number licenses result3 = re.match(r'([0][0-9][0-9][0-9]|[1][0]([0-1][0-9]|[2][0-4]))$', d)


now = datetime.datetime.now()

# Generation control hash sum for name "*.lic" file
def HexToByte(hexStr):
    bytes = []
    hexStr = ''.join(hexStr.split(" "))
    for i in range(0, len(hexStr), 4):
        bytes.append(int(hexStr[i:i + 6], 16))
    return bytes


# This is function emulator generation licenses.
def genlic(cpu_id, license_id):
    # -*- coding: utf-8 -*-
    # Upper letters.
    cpu_id = cpu_id.upper()
    license_id = license_id.upper()
    control_hash_sum = HexToByte(cpu_id)
    #print(control_hash_sum[0])
    my_file = open(cpu_id + '_' + str(now.year) + '_' + str(now.month) + '_' + str(now.day) + '_' + str(now.hour) + str(now.minute) + '_' + license_id + '_' + str(control_hash_sum[0]) + '.lic', 'w', encoding='utf-8')
    text_for_file = sys.argv[1] + sys.argv[2]
    # This is do secret license key
    info = "----------- This is not real key. It's emulator generator license key on Python ----------- \n"
    lic = hashlib.md5((cpu_id + license_id).encode('utf-8')).hexdigest()
    lic = (hashlib.sha512(lic.encode('utf-8')).hexdigest())
    info2 = "\n----------- You should use compiled language program for generation licenses!!! ----------- \n The EMULTOR licenses developed joker@tjo.biz for develope plugin on PHP on eCommerce store \n" + now.strftime("%d-%m-%Y %H:%M")
    my_file.write(info + lic + info2)
    # Close file
    my_file.close()
    return cpu_id + license_id


#This for check standard format
licenseid = False
cpuid = re.match(r'([a-f]|[A-F]|[0-9]){6}$', sys.argv[1])
licenseid = re.match(r'([0][0-9][0-9][0-9]|[1][0]([0-1][0-9]|[2][0-4]))$', sys.argv[2])
if cpuid is None:
    cpuid = False
if licenseid is None:
    licenseid = False


if __name__ == "__main__":
    if len(sys.argv) == 3:
        if(cpuid == False and bool(licenseid.string) == True):
            raise SystemExit(2)
        elif(bool(cpuid.string) == True and licenseid == False):
            raise SystemExit(3)
        elif (bool(cpuid.string) and bool(licenseid.string)):
            print(genlic(sys.argv[1], sys.argv[2]))
            raise SystemExit(0)
        else:
            raise SystemExit(4)
    else:
        print("Неверное колличество параметров в командной строке")
        raise SystemExit(1)


raise SystemExit(4)