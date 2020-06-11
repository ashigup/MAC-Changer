from mac import *

if __name__ == "__main__":
    mc=MAC_changer()
    new_mac=str(input("New MAC address : "))
    mac=mc.change_mac('eth0',new_mac)
    