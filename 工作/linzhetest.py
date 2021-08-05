import os
import re

lines = os.popen('blkid').readlines()
matchs = "PARTABEL.*"

for line in lines:
    result = re.search(r'PARTLABEL=\"KOLLA_CEPH_DATA_BS_._B\"\s', line)
    if result:
        print("------------------------------------------------")
        print("-------------It's end with B--------------------")
        if "\sUUID" in line:
            print("error, It's can't mount")
        else:
            print("It's OK")
        print(line)
        print("------------------------------------------------")
    result = re.search(r'PARTLABEL=\"KOLLA_CEPH_DATA_BS_.\"\s', line)
    if result:
        print("------------------------------------------------")
        print("------------It's end with out B-----------------")
        if "\sUUID" not in line:
            print("error, It's not mount")
        else:
            print("It's OK")
        print(line)
        print("------------------------------------------------")
