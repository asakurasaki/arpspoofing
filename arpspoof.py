import os
import time
from datetime import datetime


def arp_table_extraction():
    arp_table=os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()

    addresses = {}

    for line in arp_table_lines:
        if "dynamic" in line:
            ip, mac, _type = line.split()
            addresses[ip] = mac

    identify_duplication(addresses)

def identify_duplication(addresses):
    temp_mac_list = []
    print("scanning")
    time.sleep(3)
    for mac in addresses.values():
        if mac in temp_mac_list:
            print("FOUND!")
            create_log("Arp Spoofed! \nThe address is: "+ mac)
            break
        temp_mac_list.append(mac)
def create_log(message):
    print("Generating logs....")
    time.sleep(3)
    date = datetime.now()
    with open("log.txt", "a") as log:
        log.write(message + "\nDate: {} \n\n".format(date))

    print("The event is logged in log.txt")

if __name__ == "__main__":
    arp_table_extraction()
