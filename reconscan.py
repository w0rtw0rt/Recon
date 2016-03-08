#!/usr/bin/env python
'''
 Author: Gerben (0x90) -- @N0_Operation & Bas -- B0x41S & Sander -- DTCTD.
 This tool is an automation script for the reconphase during a pentest, it was inspired by a few github repos.
'''

import os
from Modules import recon

os.system('cls' if os.name == 'nt' else 'clear')

print '\033[1;30m ########:: ########:: ######::: #######:: ##::: ##:::::\033[1;m'
print '\033[1;30m ##.... ##: ##.....:: ##... ##: ##.... ##: ###:: ##:::::\033[1;m'
print '\033[1;30m ##:::: ##: ##::::::: ##:::..:: ##:::: ##: ####: ##:::::\033[1;m'
print '\033[1;30m ########:: ######::: ##::::::: ##:::: ##: ## ## ##:::::\033[1;m'
print '\033[1;30m ##.. ##::: ##...:::: ##::::::: ##:::: ##: ##. ####:::::\033[1;m'
print '\033[1;30m ##::. ##:: ##::::::: ##::: ##: ##:::: ##: ##:. ###:::::\033[1;m'
print '\033[1;30m ##:::. ##: ########:. ######::. #######:: ##::. ##:::::\033[1;m'
print '\033[1;30m..:::::..::........:::......::::.......:::..::::..::0x90\033[1;m'

try:
    if __name__ == '__main__':
        try:
            recon.checkpath("./results/")
            recon.checkpreq()
        except:
            pass

        try:
            # See if there is a target list in the file ips
            with open("./ips") as f:
                print('\033[1;32m[*]  Found IP list, using as input\033[1;m')
                ips = f.readlines()
                for ip in ips:
                    recon.scanner(ip.strip('\n\r'), 'TCP')
                    recon.scanner(ip.strip('\n\r'), 'UDP')
        except:
            ips = recon.getIp()

            for ip in (str(ips)).split():
                recon.scanner(ip, 'TCP')
                recon.scanner(ip, 'UDP')

except:
    print '\033[1;31m[*]  Recon is ending: Killing all Processes!\033[1;m'
    PROCNAME = ("python", "nmap", "dirb", "hydra")
    for proc in psutil.process_iter():
        if proc.name() in PROCNAME:
            proc.kill()
    exit()


