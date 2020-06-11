#Author -- ashigup --aka-- Lucifer07 
#Contact -- githhub.com/ashigup

import subprocess
import re

class MAC_changer:
    def get_mac(self,iface):
      output = subprocess.run(["ifconfig",iface],shell=False,capture_output=True)
      cmd_result=output.stdout.decode('utf-8') 
      pattern=r'ether\s[A-Za-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}'
      regex=re.compile(pattern)
      ans=regex.search(cmd_result)
      c=ans.group().split(" ")[1]
      return c


    def change_mac(self,iface,new_mac):
        print("[+] Your current MAC address is : ",self.get_mac(iface))
        output=subprocess.run(["sudo","ifconfig",iface,"down",],shell=False,capture_output=True)
        print(output.stderr.decode('utf-8'))
        output=subprocess.run(["sudo","ifconfig",iface,"hw","ether",new_mac],shell=False,capture_output=True)
        print(output.stderr.decode('utf-8'))
        output=subprocess.run(["sudo","ifconfig",iface,"up",],shell=False,capture_output=True)
        print(output.stderr.decode('utf-8'))
        print("[+] Your updated MAC address is : ",self.get_mac(iface))
