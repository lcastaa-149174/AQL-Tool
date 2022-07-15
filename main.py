# AQLTOOL 2022
# Created by lcastaa one of the devs @ AQLabs
# This file is the main file that contains the menu logics of the script

import os
import time
import subprocess as sub
from sys import platform

def mainmenu():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Main Menu')
    print('[Navigation: Main Menu > ]')
    print('')
    print('[1] Installs')
    print('')
    main_menu_choice = int(input('->: '))
    if main_menu_choice == 1 :
        install()
    elif main_menu_choice == 2:
        tools()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        mainmenu()


########-------##########------###########
# Created by lcastaa one of the devs @ AQLabs
# Main Menu Elements
def install():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Installer')
    print('[Navigation: Main Menu > Installs ]')
    print('')
    print('[1] Apache2')
    print('[2] Nginx')
    print('[3] Pi-hole')
    print('[4] Pi-VPN')
    print('[5] Homebrige')
    print('[6] Docker')
    print('[7] Raspistats')
    install_menu_choice = int(input('->: '))
    if install_menu_choice == 1 :
        apache2()
    elif install_menu_choice == 2 :
        nginx()
    elif install_menu_choice == 3 :
        pihole()
    elif install_menu_choice == 4 :
        pivpn()
    elif install_menu_choice == 5 :
        homebridge()
    elif install_menu_choice == 6 :
        docker()
    elif install_menu_choice == 7 :
        raspistats()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        install()

########-------##########------###########
# Created by lcastaa one of the devs @ AQLabs
# Install Menu Elements

def apache2():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Apache2 Interface')
    print('[Navigation: Main Menu > Installs > Apache2 Interface ]')
    print('')
    print('[1] Install Apache2')
    print('[2] Edit Index File')
    print('[3] -exit-')
    print('')
    apache2_menu_choice = int(input('->: '))
    if apache2_menu_choice == 1 :
        apache2_inst()
    elif apache2_menu_choice == 2 :
        apache2_edit()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        apache2()
def nginx():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Nginx Interface')
    print('[Navigation: Main Menu > Installs > Nginx Interface ]')
    print('')
    print('[1] Install Nginx')
    print('[2] Edit Index File')
    print('[3] -exit-')
    print('')
    nginx_menu_choice = int(input('->: '))
    if nginx_menu_choice == 1 :
        nginx_inst()
    elif nginx_menu_choice == 2 :
        nginx_edit()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        nginx()
def pihole():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-hole Interface')
    print('[Navigation: Main Menu > Installs > Pi-hole Interface ]')
    print('')
    print('[1] Install Pi-hole')
    print('[2] Add URL Packs')
    print('[3] Pi-hole Service Manager')
    print('[4] -exit-')
    print('')
    pi_hole_menu_choice = int(input('->: '))
    if pi_hole_menu_choice == 1 :
        pihole_inst()
    elif pi_hole_menu_choice == 2 :
        pihole_addurls()
    elif pi_hole_menu_choice == 3 :
        pihole_switch()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        pihole()
def pivpn():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-VPN Interface')
    print('[Navigation: Main Menu > Installs > Pi-VPN Interface ]')
    print('')
    print('[1] Install Pi-hole')
    print('[2] Profile Manager')
    print('[3] Pi-VPN Service Manager')
    print('[4] -exit-')
    print('')
    pivpn_menu_choice = int(input('->: '))
    if pivpn_menu_choice == 1 :
        pivpn_inst()
    elif pvpn_menu_choice == 2 :
        pivpn_add()
    elif pivpn_menu_choice == 3 :
        pivpn_switch()
    elif pivpn_menu_choice == 4 :
        exit()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        pivpn()
def homebridge():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Homebridge Interface')
    print('[Navigation: Main Menu > Installs > Hombridge Interface ]')
    print('')
    print('[1] Install Homebridge')
    print('[2] Homebrige Service Manager')
    print('[3] -exit-')
    print('')
    homebridge_menu_choice = int(input('->: '))
    if homebridge_menu_choice == 1 :
        homebridge_inst()
    elif homebridge_menu_choice == 2 :
        homebridge_switch()
    elif homebridge_menu_choice == 3 :
        exit()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        homebridge()
def docker():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Docker Interface')
    print('[Navigation: Main Menu > Installs > Docker Interface ]')
    print('')
    print('[1] Install Docker')
    print('[2] Uninstall Docker')
    print('[3] -exit-')
    print('')
    docker_menu_choice = int(input('->: '))
    if docker_menu_choice == 1 :
        docker_inst()
    elif docker_menu_choice == 2 :
        docker_uninst()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        docker()
def raspistats():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Raspistats Interface')
    print('[Navigation: Main Menu > Installs > Raspistats Interface ]')
    print('')
    print('[1] Install AQL Raspistats')
    print('[2] -exit-')
    print('')
    raspistats_menu_choice = int(input('->: '))
    if raspistats_menu_choice == 1 :
        raspistats_inst()
    elif raspistats_menu_choice == 2 :
        exit()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        raspistats()

########-------##########------###########
# Created by lcastaa one of the devs @ AQLabs
# This Part is the functions file that contains the MMEEET of the script


def apache2_inst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Apache2 Interface')
    print('[Navigation: Main Menu > Installs > Apache2 Interface > Installing Apache2]')
    print('')
    print('INSTALLING apache2 please wait...')
    print('')
    time.sleep(2)
    os.system('sudo apt install apache2 -y')
    time.sleep(2)
    print('')
    print('INSTALL COMPLETE...')
    exit()
def apache2_edit():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Apache2 Interface')
    print('[Navigation: Main Menu > Installs > Apache2 Interface > Editing Index]')
    print('')
    print('Where is your Index File?')
    time.sleep(1)
    fileloc = input('Location: ')
    print('')
    print('Opening File...')
    os.system('sudo nano'+' '+fileloc)

def nginx_inst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Nginx Interface')
    print('[Navigation: Main Menu > Installs > Nginx Interface > Installing Nginx ]')
    print('')
    print('INSTALLING Nginx please wait...')
    print('')
    time.sleep(2)
    os.system('sudo apt install nginx -y')
    time.sleep(2)
    print('')
    print('INSTALL COMPLETE...')
    exit()
def nginx_edit():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Nginx Interface')
    print('[Navigation: Main Menu > Installs > Nginx Interface > Editing Index]')
    print('')
    print('Where is your Index File?')
    time.sleep(1)
    fileloc = input('Location: ')
    print('')
    print('Opening File...')
    os.system('sudo nano'+' '+fileloc)

def pihole_inst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-hole Interface')
    print('[Navigation: Main Menu > Installs > Pi-hole Interface > Installing Pi-hole ]')
    print('')
    print('INSTALLING Pi-hole please wait...')
    print('')
    time.sleep(2)
    os.system('sudo curl -sSL https://install.pi-hole.net | sudo bash')
    time.sleep(2)
    print('')
    print('INSTALL COMPLETE...')
    exit()
def pihole_addurls():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-hole Interface')
    print('[Navigation: Main Menu > Installs > Pi-hole Interface > Add AD-lists ]')
    print('')
    print('Please Paste URL')
    adlist = str(input('->: '))
    file = open('/etc/pihole/adlists.list','a')
    file.write(adlist)
    file.close()
    print('')
    print('Write Complete...')
    time.sleep(1)
    print('')
    print('Now Restarting Pi-hole Ad Filter...')
    time.sleep(2)
    os.system('sudo pihole -g')
    exit()
def pihole_switch():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-hole Interface')
    print('[Navigation: Main Menu > Installs > Pi-hole Interface > Managage Pi-hole Service ]')
    print('')
    print('Manage the Pi-hole Service')
    print('[1] Restart')
    print('[2] Start')
    print('[3] Stop')
    switch = int(input('->: '))
    if switch == 1 :
        print('')
        print('RESTARTING the Pi-hole Service...')
        time.sleep(2)
        os.system('sudo service pihole-FTL restart')
        os.system('sudo service pihole-FTL status')

    elif switch == 2 :
        print('')
        print('STARTING the Pi-hole Service...')
        time.sleep(2)
        os.system('sudo service pihole-FTL start')
        os.system('sudo service pihole-FTL status')
    elif switch == 3 :
        print('')
        print('STOPING the Pi-hole Service...')
        time.sleep(2)
        os.system('sudo service pihole-FTL stop')
        os.system('sudo service pihole-FTL status')
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        pihole_switch()

def pivpn_inst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-VPN Interface')
    print('[Navigation: Main Menu > Installs > Pi-VPN Interface > Installing Pi-VPN ]')
    print('')
    print('INSTALLING Pi-VPN please wait...')
    print('')
    time.sleep(2)
    os.system('sudo curl -L https://install.pivpn.io | sudo bash')
    time.sleep(2)
    print('')
    print('INSTALL COMPLETE...')
    exit()
def pivpn_add():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-VPN Interface')
    print('[Navigation: Main Menu > Installs > Pi-VPN Interface > Profile Manager ]')
    print('')
    print('[1] Add New Profile')
    profile_man = int(input('->: '))
    if profile_man == 1 :
        print('')
        os.system('pivpn add')
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        pivpn_add()
def pivpn_switch():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Pi-VPN Interface')
    print('[Navigation: Main Menu > Installs > Pi-VPN Interface > Managage Pi-VPN Service ]')
    print('')
    print('Manage the Pi-VPN Service')
    print('[1] Restart')
    print('[2] Start')
    print('[3] Stop')
    switch = int(input('->: '))
    if switch == 1 :
        print('')
        print('RESTARTING the Pi-VPN Service...')
        time.sleep(2)
        os.system('sudo service openvpn restart')
        os.system('sudo service openvpn status')

    elif switch == 2 :
        print('')
        print('STARTING the Pi-VPN Service...')
        time.sleep(2)
        os.system('sudo service openvpn start')
        os.system('sudo service openvpn status')
    elif switch == 3 :
        print('')
        print('STOPING the Pi-VPN Service...')
        time.sleep(2)
        os.system('sudo service openvpn stop')
        os.system('sudo service openvpn status')
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        pihole_switch()

def homebridge_inst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Homebridge Interface')
    print('[Navigation: Main Menu > Installs > Homebridge Interface > Installing Homebridge ]')
    print('')
    print('ADDING Homebridge GPG keys please wait...')
    print('')
    time.sleep(1)
    os.system('sudo curl -sSfL https://repo.homebridge.io/KEY.gpg | sudo gpg --dearmor | sudo tee /usr/share/keyrings/homebridge.gpg  > /dev/null && echo "deb [signed-by=/usr/share/keyrings/homebridge.gpg] https://repo.homebridge.io stable main" | sudo tee /etc/apt/sources.list.d/homebridge.list > /dev/null')
    time.sleep(2)
    print('')
    print('UPDATING System...')
    print('')
    time.sleep(1)
    os.system('sudo apt-get update')
    time.sleep(2)
    print('')
    print('INSTALLING Homebridge...')
    print('')
    time.sleep(1)
    os.system('sudo apt-get install homebridge -y')
    time.sleep(2)
    print('')
    print('Install COMPLETE...')
    print('')
    exit()
def homebridge_switch():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Homebrige Interface')
    print('[Navigation: Main Menu > Installs > Hombridge Interface > Managage Hombridge Service ]')
    print('')
    print('Manage the Hombridge Service')
    print('[1] Restart')
    print('[2] Start')
    print('[3] Stop')
    switch = int(input('->: '))
    if switch == 1 :
        print('')
        print('RESTARTING the Hombridge Service...')
        time.sleep(2)
        os.system('sudo service homebridge restart')
        os.system('sudo service homebridge status')
        exit()
    elif switch == 2 :
        print('')
        print('STARTING the Hombridge Service...')
        time.sleep(2)
        os.system('sudo service homebridge start')
        os.system('sudo service homebridge status')
        exit()
    elif switch == 3 :
        print('')
        print('STOPING the Hombridge Service...')
        time.sleep(2)
        os.system('sudo service homebridge stop')
        os.system('sudo service homebridge status')
        exit()
    else:
        print('Invalid Option...')
        print('Choose Again...')
        time.sleep(2)
        homebridge_switch()

def docker_inst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Docker Interface')
    print('[Navigation: Main Menu > Installs > Docker Interface > Installing Docker ]')
    print('')
    print('UPDATING System...')
    print('')
    time.sleep(1)
    os.system('sudo apt-get update && sudo apt-get upgrade -y')
    time.sleep(2)
    print('')
    print('INSTALLING Docker...')
    print('')
    time.sleep(1)
    os.system('sudo curl -sSL https://get.docker.com | sudo sh')
    time.sleep(2)
    whoami = sub.getoutput('whoami')
    print('')
    print('ADDING'+' '+whoami+' '+'to Docker group')
    print('')
    time.sleep(1)
    os.system('sudo usermod -aG docker '+whoami)
    time.sleep(2)
    print('')
    print('ADDING'+' '+whoami+' '+'to Docker permissions...')
    print('')
    time.sleep(1)
    os.system('sudo usermod -aG docker '+whoami)
    time.sleep(2)
    print('')
    print('INSTALLING Libffi-Dev Libssl-Dev Libraries...')
    print('')
    time.sleep(1)
    os.system('sudo apt-get install libffi-dev libssl-dev -y')
    time.sleep(2)
    print('')
    print('INSTALLING Python3-dev...')
    print('')
    time.sleep(1)
    os.system('sudo apt install python3-dev -y')
    time.sleep(2)
    print('')
    print('INSTALLING Python3 Python3-Pip')
    print('')
    time.sleep(1)
    os.system('sudo apt-get install python3 python3-pip -y')
    time.sleep(2)
    print('')
    print('INSTALLING Docker-Compose...')
    print('')
    time.sleep(1)
    os.system('sudo pip3 install docker-compose')
    time.sleep(2)
    print('')
    print('STARTING Docker Engine')
    print('')
    time.sleep(1)
    os.system('sudo systemctl enable docker')
    time.sleep(2)
    exit()
def docker_uninst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Docker Interface')
    print('[Navigation: Main Menu > Installs > Docker Interface > Uninstalling Docker ]')
    print('')
    print('PURGING Docker please wait...')
    print('')
    time.sleep(2)
    os.system('sudo apt-get purge -y docker-ce docker-ce-cli')
    os.system('sudo apt-get autoremove -y --purge docker-ce docker-ce-cli')
    os.system('sudo rm -rf /var/lib/docker')
    os.system('sudo rm -r /etc/apparmor.d/docker')
    os.system('sudo groupdel docker')
    os.system('sudo rm -rf /var/run/docker.sock')
    os.system('sudo ifconfig docker0 down')
    os.system('sudo brctl delbr docker0')
    time.sleep(2)
    print('')
    print('UN-INSTALL COMPLETE...')

def raspistats_inst():
    if platform == "win32" :
        os.system('cls')
    elif platform == "linux" or "linux2":
        os.system('clear')
    print('AQLabs Raspistats Interface')
    print('[Navigation: Main Menu > Installs > Raspistats Installer ]')
    print('')
    print('UPDATING System...')
    print('')
    time.sleep(1)
    os.system('')
    time.sleep(2)
    print('')
    print('...')
    print('')
    time.sleep(1)
    os.system('sudo apt-get update && sudo apt-get full-upgrade -y')
    time.sleep(2)
    print('')
    print('INSTALLING Python3-Pip...')
    print('')
    time.sleep(1)
    os.system('sudo apt-get install python3-pip -y')
    time.sleep(2)
    print('')
    print('UPGRADING SetUpTools...')
    print('')
    time.sleep(1)
    os.system('sudo pip3 install --upgrade setuptools')
    time.sleep(2)
    print('')
    print('INSTALLING Adafruit-Python-Shell...')
    print('')
    time.sleep(1)
    os.system('sudo pip3 install --upgrade adafruit-python-shell')
    time.sleep(2)
    print('')
    print('DOWNLOADING Raspi-Blinka')
    print('')
    time.sleep(1)
    os.system('sudo wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py')
    time.sleep(2)
    print('')
    print('INSTALLING Adafruit-Circuitpython-Ssd1306...')
    print('')
    time.sleep(1)
    os.system('pip3 install adafruit-circuitpython-ssd1306')
    time.sleep(2)
    print('')
    print('INSTALLING Python3-pil...')
    print('')
    time.sleep(1)
    os.system('sudo apt-get install python3-pil -y')
    time.sleep(2)
    print('')
    print('INSTALLING Git...')
    print('')
    time.sleep(1)
    os.system('sudo apt install git -y')
    time.sleep(2)
    print('')
    print('CLONING Repository...')
    print('')
    time.sleep(1)
    os.system('git clone https://github.com/mklements/OLED_Stats.git')
    time.sleep(2)
    print('')
    print('EXECUTING Raspi-Blinka...')
    print('')
    time.sleep(1)
    os.system('sudo python3 raspi-blinka.py')

mainmenu()