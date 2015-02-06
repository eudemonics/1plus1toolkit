#!/usr/bin/env python
### HALF-ASSED ONE + ONE TOOLKIT
##### VERSION: 1.3.3.7 BETA
##### RELEASE DATE: FEBRUARY 06, 2015
##### AUTHOR: vvn [eudemonics on xda-developers]
##### DESCRIPTION: a spontaneously created but hopefully comprehensive Android toolkit,
##### built originally for the OnePlus One but can be used with most Android devices
##### (DO NOT FLASH INCLUDED ONEPLUS ONE DEVICE FILES ON OTHER DEVICES!), that will or 
##### will not be irregularly maintained at the developer's whim.
##### REQUIREMENTS: Python 2.7, Android SDK tools, USB drivers, pyadb.py library, opointro.py
##### also required, obviously, is a computer that runs an OS that supports python 2.7.
##### HOLY SHIT GITHUB IS FINALLY WORKING!
##### INSTALL INSTRUCTIONS USING GIT:
##### enter command into terminal:
##### git clone https://github.com/eudemonics/1plus1toolkit.git 1plus1toolkit
##### to run after using git clone (without $ sign):
#####   $ cd 1plus1toolkit
#####   $ python opotoolkit.py
##### 
##### VIEW IN BROWSER:
##### https://github.com/eudemonics/1plus1toolkit
#####
##### UPDATE VIA GIT:
##### cd 1plus1toolkit
##### git pull https://github.com/eudemonics/1plus1toolkit.git
##################################################
##################################################
##### USER LICENSE AGREEMENT & DISCLAIMER
##### copyright (C) 2014  vvn <vvn @ notworth.it>
##### 
##### This program is FREE software: you can use it, redistribute it and/or modify
##### it as you wish. Copying and distribution of this file, with or without modification,
##### are permitted in any medium without royalty provided the copyright
##### notice and this notice are preserved. This program is offered AS-IS,
##### WITHOUT ANY WARRANTY; without even the implied warranty of
##### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##### GNU General Public License for more details.
##### 
##### For more information, please refer to the "LICENSE AND NOTICE" file that should
##### accompany all official download releases of this program. 
##################################################
##################################################
##### don't ask about the arbitrary versioning. i am totally making this shit up.
##### getting credited for my work is nice. so are donations.
##### BTC: 1M511j1CHR8x7RYgakNdw1iF3ike2KehXh
##### https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=26PWMPCNKN28L
##### but to really show your appreciation, you should buy my EP instead!
##### you can stream and purchase it at: dreamcorp.bandcamp.com
##### (you might even enjoy listening to it)
##### questions, comments, feedback, bugs, complaints, death threats, marriage proposals?
##### contact me at:
##### vvn (at) notworth (dot) it
##### latest version will always be available HERE:
##### https://github.com/eudemonics/1plus1toolkit

import subprocess, sys, re, os, os.path, hashlib, time, datetime, urllib
from opointro import *
from pyadb import *
global usecolor
if os.name == 'nt' or sys.platform == 'win32':
   try:
      import colorama
      colorama.init()
      s = opointro()
      s.colorlogo()
      startmenu = s.colormenu
      usecolor = 'color'
   except:
      try:
         import tendo.ansiterm
         s = opointro()
         s.colorlogo()
         startmenu = s.colormenu
         usecolor = 'color'
      except:
         s = opointro()
         s.cleanlogo()
         startmenu = s.cleanmenu
         usecolor = 'clean'
         pass
else:
   s = opointro()
   s.colorlogo()
   startmenu = s.colormenu
   usecolor = 'color'

def mainmenu():
   print(startmenu)

def main():
   os.system('cls' if os.name == 'nt' else 'clear')
   mainmenu()

   global option
   option = raw_input('Select an option 0-14 --> ')
   
   while not re.search(r'^[0-9]$', option) and not re.search(r'^1[0-4]$', option):
      option = raw_input('Invalid selection. Please select an option 0-14 --> ')
 
   if option:

      obj = pyADB()

      if option == '1': #reboot      
         rboption = raw_input("please enter 1 to reboot into android. enter 2 to reboot to bootloader. enter 3 to reboot to recovery. --> ")
         while not re.search(r'^[123]$', rboption):
            rboption = raw_input("invalid selection. please enter 1 to reboot into android, 2 for bootloader, and 3 for recovery. --> ")
         rbtype = "android"
         if rboption == '1':
            rbtype = "android"
         elif rboption == '2':
            rbtype = "bootloader"
         elif rboption == '3':
            rbtype ="recovery"
         checkdev = obj.get_state()
         listdev = obj.attached_devices()
         fastdev = obj.fastboot_devices()
         if "device" in str(checkdev) and listdev is not None and "fastboot" not in str(fastdev):
            print("rebooting via ADB..\n")
            obj.reboot(rbtype)
            time.sleep(0.9)
            main()
         elif "unknown" in str(checkdev) and "fastboot" in str(fastdev):
            print("rebooting via fastboot..\n")
            if rboption == '3':
               rbtype = "bootloader"
            obj.fastreboot(rbtype)
            time.sleep(0.9)
            main()
         elif "unknown" in str(checkdev) and listdev is not None and "device" in str(fastdev):
            print("rebooting via ADB..\n")
            obj.reboot(rbtype)
            time.sleep(0.9)
            main()
         elif "recovery" in [str(fastdev), str(listdev)] and checkdev is not None:
            print("rebooting via ADB...\n")
            obj.reboot(rbtype)
            time.sleep(0.9)
            main()
         elif "unknown" in str(checkdev) and fastdev is not None and listdev is None:
            print("rebooting via fastboot...\n")
            if rboption == '3':
               rbtype = "bootloader"
            obj.fastreboot(rbtype)
            time.sleep(0.9)
            main()
         elif "unknown" in str(checkdev) and "unauthorized" in str(listdev):
            raw_input("verify that DEVICE IS UNLOCKED and COMPUTER IS AUTHORIZED FOR ADB ACCESS, then press ENTER.")
            print("rebooting via ADB...\n")
            obj.reboot(rbtype)
            time.sleep(0.9)
            main()
         elif "unknown" in str(checkdev) and listdev is not None and fastdev is None:
            raw_input("device appears to be in recovery mode. reboot from recovery menu, then press ENTER.")
            checkstate = obj.get_state()
            if "device" in str(checkstate):
               obj.reboot(rbtype)
            time.sleep(0.9)
            main()
         else:
            print("rebooting via fastboot....\n")
            if rboption == '3':
               rbtype = "bootloader"
            fastreboot = obj.fastreboot(rbtype)
            if not fastreboot:
               print("rebooting via ADB after fastboot... \n")
               obj.reboot(rbtype)
               if "error" in str(fastreboot):
                  print("rebooting via fastboot second time...\n")
                  obj.fastreboot(rbtype)
            time.sleep(0.9)
            main()

      elif option == '2': #wipe
         print("\033[35m***WIPING SOME PARTITIONS WILL ERASE YOUR DATA.***\n please make sure to back up any important data before proceeding!\n\n")
         print('''\033[36mCHOOSE AN OPTION 1-8:\033[32m\n
   [1]\033[37m perform a full system wipe [system, data, and cache partitions]\033[32m
   [2]\033[37m wipe only the system partition\033[32m
   [3]\033[37m wipe only the data partition\033[32m
   [4]\033[37m wipe only the cache partition\033[32m
   [5]\033[37m wipe only the boot partition\033[32m
   [6]\033[37m wipe only the recovery partition\033[32m
   [7]\033[37m flash device to factory images [flash system, boot, and recovery]\033[32m
   [8]\033[37m return to main menu\n\n\033[0m''')
         confirmwipe = raw_input("please enter an option 1-8 --> ")
         while not re.search(r'^[1-8]$', confirmwipe):
            confirmwipe = raw_input('not a valid option. please enter a selection between 1-8 from above choices -->')         
         if confirmwipe == '1':
            obj.wipe('all')
            raw_input("press ENTER to continue.")
            time.sleep(0.9)
            main()
         elif confirmwipe == '2':
            obj.wipe('system')
            raw_input("press ENTER to continue.")
            time.sleep(0.9)
            main()
         elif confirmwipe == '3':
            obj.wipe('data')
            raw_input("press ENTER to continue.")
            time.sleep(0.9)
            main()
         elif confirmwipe == '4':
            obj.wipe('cache')
            raw_input("press ENTER to continue.")
            time.sleep(0.9)
            main()
         elif confirmwipe == '5':
            obj.wipe('boot')
            raw_input("press ENTER to continue.")
            time.sleep(0.9)
            main()
         elif confirmwipe == '6':
            obj.wipe('recovery')
            raw_input("press ENTER to continue.")
            time.sleep(0.9)
            main()
         elif confirmwipe == '7':
            obj.wipe('flashall')
            raw_input("press ENTER to continue.")
            time.sleep(0.9)
            main()
         elif confirmwipe == '8':
            time.sleep(0.9)
            main()
         else:
            print("there was a problem connecting to the device. returning to menu..\n")
            time.sleep(0.9)
            main()
            
                          
      elif option == '3': #boot custom recovery
         recovery = raw_input("enter 1 for TWRP, 2 for ClockworkMod, or 3 for Philz recovery --> ")
         while not re.search(r'^[1-3]$', recovery):
            recovery = raw_input("invalid selection. please choose 1 for TWRP, 2 for CWM, or 3 for Philz --> ")
         def dlrecov(recovfile):
            dlfile = "http://notworth.it/opo/" + recovfile
            dl = urllib.URLopener()
            dl.retrieve(dlfile, recovfile)
            site = urllib.urlopen(dlfile)
            meta = site.info()
            dlsize = meta.getheaders("Content-Length")[0]
            fsize = os.path.getsize(recovfile)
            print("file size: \033[33m")
            print(dlsize)
            print("\n\033[0mbytes downloaded: \033[33m")
            print(fsize)
            print("\033[0m\n")
         obj.reboot("bootloader")
         if recovery == '1':
            recovfile = "twrp.img"
            while not os.path.isfile(recovfile):
               print("file \033[32mtwrp.img \033[0mnot found. attempting download...\n")
               dlrecov(recovfile)
            print("file \033[32mtwrp.img \033[0mfound!\n")
            raw_input("press ENTER to continue booting into TWRP..")
            obj.bootimg("twrp.img")
         elif recovery == '2':
            recovfile = "cwm.img"
            while not os.path.isfile(recovfile):
               print("file \033[32mcwm.img \033[0mnot found. attempting download...\n")
               dlrecov(recovfile)
            print("file \033[32mcwm.img \033[0mfound!\n")
            raw_input("press ENTER to continue booting into ClockworkMod Recovery..")
            obj.bootimg("cwm.img")
         elif recovery == '3':
            recovfile = "philz.img"
            while not os.path.isfile(recovfile):
               print("file \033[32mphilz.img \033[0mnot found. attempting download...\n")
               dlrecov(recovfile)
            print("file \033[32mphilz.img \033[0mfound!\n")
            raw_input("press ENTER to continue booting into Philz Recovery..")
            obj.bootimg("philz.img")
         else:
            print("unable to connect to device.\n")    
            
         raw_input("press ENTER to return to main menu..")
         time.sleep(0.9)
         main()

      elif option == '4': #install or uninstall APK
         whichinstall = raw_input("please enter 1 to install, 2 to uninstall, or 3 to return to main menu. --> ")
         while not re.search(r'^[1-3]$', whichinstall):
            whichinstall = raw_input("invalid selection. please enter 1 to install, 2 to uninstall, or 3 to return to main menu. --> ")
         if not os.path.exists('apps'):
            os.makedirs('apps')
         if whichinstall == '1':
            getapk = raw_input("place the APK file to install in the \"apps\" subdirectory, then type the filename --> ")
            apkfile = os.path.join('apps', getapk)
            while not os.path.isfile(apkfile):
               print("\033[37mfile does not exist. please make sure the APK file is in the \"apps\" subdirectory.\033[0m\n")
               getapk = raw_input("enter valid filename for the APK you want to install -->")
               apkfile = os.path.join('apps', getapk)
            print("installing \033[36m" + getapk + "\033[0m...")
            obj.install(apkfile)
            raw_input("press ENTER to continue...")
            time.sleep(0.9)
            main()
            
         if whichinstall == '2':
            getunapk = raw_input("please enter the complete path for the app you wish to uninstall --> ")
            keepcheck = raw_input("would you like to keep your app data? Y or N --> ")
            while not re.search(r'^[nyNY]$', keepcheck):
               keepcheck = raw_input("invalid selection. please enter Y to keep app data or N to erase --> ")
            keepargs = "erase"
            uninstcmd = "pm uninstall " + getunapk
            if re.match(r'(?i)Y', keepcheck):
               keepargs = "keep"
               uninstcmd = "pm uninstall -k " + getunapk
            print("uninstalling \033[36m" + getunapk + "\033[0m...\n")
            obj.uninstall(getunapk, keepargs)
            obj.shell(uninstcmd)
            raw_input("press ENTER to continue...")
            time.sleep(0.9)
            main()
            
         if whichinstall == '3':
            main()
            
         else:
            print("could not connect to device.\n")
            time.sleep(0.9)
            main()

############################################################
############################################################
# OPTION 5: COPY/SYNC FILES BETWEEN DEVICE & COMPUTER #
############################################################
############################################################

      elif option == '5': #copy and/or sync between computer and device
         copytype = raw_input("to push file from computer to device, enter T. to pull file from device to computer, enter F. to sync, enter S --> ")
         matchT = re.search(r'(?i)T', copytype)
         matchF = re.search(r'(?i)F', copytype)
         matchS = re.search(r'(?i)S', copytype)
         while not re.search(r'^[FfSsTt]$', copytype):
            copytype = raw_input("invalid option. please enter T to push file, F to pull file, or S to sync --> ")
            
         if matchT:
            getpushfile = raw_input("please enter the file or directory you wish to copy as the RELATIVE path from the script location --> ")
            while not os.path.exists(getpushfile):
               getpushfile = raw_input("file does not exist. please enter valid path --> ")
            getpushremote = raw_input("please enter destination path for copied file(s) on the device --> ")
            obj.push(getpushfile, getpushremote)
            raw_input("file transfer complete. press ENTER to continue...")
            
         elif matchF:
            getpullfile = raw_input("please enter path for the file or directory on your device to copy --> ")
            getpulllocal = raw_input("please enter the copy destination folder as a RELATIVE path from the script location --> ")
            if not os.path.exists(getpulllocal):
               print("copy destination \033[35m" + getpulllocal + " \033[0mdoes not exist! creating new directory...")
               os.makedirs(getpulllocal)
            obj.pull(getpullfile, getpulllocal)
            print("\033[32mtransferred file(s) in destination directory:\n")
            for fn in next(os.walk(getpulllocal))[2]:
               fullpath = os.path.join(getpulllocal, fn)
               if os.path.getmtime(fullpath) >= os.path.getctime(getpulllocal):
                  print(fullpath)
            print("\033[0m\n")
            raw_input("file transfer complete. press ENTER to continue...")
            
         elif matchS:
            syncargs = raw_input("enter 1 to set sync directory, or 2 to sync the default system and data directories. --> ")
            while not re.search(r'^[12]$', syncargs):
               syncargs = raw_input("invalid selection. please enter 1 to set sync directory, or 2 to use default. --> ")
            if syncargs == '1':
               syncdir = raw_input("please enter sync directory --> ")
               localargs = raw_input("enter 1 to set local sync directory, or 2 to use default ANDROID_PRODUCT_OUT --> ")
               while not re.search(r'^[12]$',localargs):
                  localargs = raw_input("invalid selection. enter 1 to set local sync directory or 2 to use default ANDROID_PRODUCT_OUT --> ")
               if localargs == '1':
                  localdir = raw_input("please enter relative path for local directory to sync device --> ")
                  while not os.path.exists(localdir):
                     print("the path you entered does not exist. would you like to create " + localdir + " as a new directory?\n")
                     crlocaldir = raw_input("enter 1 to create new directory or 2 to enter another location. --> ")
                     while not re.search(r'^[12]$', crlocaldir):
                        crlocaldir = raw_input("invalid selection. please enter 1 to create directory, or 2 to enter another location. --> ")
                     if crlocaldir == '1':
                        os.makedirs(localdir, 0755)
                     else:
                        localdir = raw_input("please enter relative path for local directory to sync device with --> ")
                  localsyncdir = os.path.join(localdir, syncdir)
                  while not os.path.exists(localsyncdir):
                     os.makedirs(localsyncdir, 0755)
                     print(localsyncdir + " created\n")
               else:
                  localdir = "none"
               obj.sync(localdir, syncdir)
               if "none" not in localdir:
                  print("\033[32mfile(s) in sync directory:\n")
                  for fn in next(os.walk(localdir))[2]:
                     fullpath = os.path.join(localdir, fn)
                     if os.path.getmtime(fullpath) >= os.path.getctime(localdir):
                        print(fullpath)
                  print("\033[0m\n")
               raw_input("press ENTER to continue...")
            elif syncargs == '2':
               # obj.sync()
               localargs = raw_input("enter 1 to set local sync directory, or 2 to use default ANDROID_PRODUCT_OUT --> ")
               while not re.search(r'^[12]$',localargs):
                  localargs = raw_input("invalid selection. enter 1 to set local sync directory or 2 to use default ANDROID_PRODUCT_OUT --> ")
               if localargs == '1':
                  localdir = raw_input("please enter relative path for local directory to sync device --> ")
                  while not os.path.exists(localdir):
                     print("the path you entered does not exist. would you like to create " + localdir + " as a new directory?\n")
                     crlocaldir = raw_input("enter 1 to create new directory or 2 to enter another location. --> ")
                     while not re.search(r'^[12]$', crlocaldir):
                        crlocaldir = raw_input("invalid selection. please enter 1 to create directory, or 2 to enter another location. --> ")
                     if crlocaldir == '1':
                        os.makedirs(localdir, 0755)
                     else:
                        localdir = raw_input("please enter relative path for local directory to sync device with --> ")
               else:
                  localdir = "none"
               obj.sync(localdir, "none")
               raw_input("press ENTER to continue...")
            else:
               print("could not connect to device.\n") 
         
         else:
            print("could not connect to device.\n") 
            
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 6 - BACKUP OR RESTORE #
############################################################
############################################################

      elif option == '6': #backup
         whichbackup = raw_input("to backup, enter 1. to restore, enter 2 --> ")
         while not re.search(r'^[12]$', whichbackup):
            whichbackup = raw_input("invalid selection. please enter 1 to backup or 2 to restore. --> ")
         if whichbackup == '1':
            fullbackup = raw_input("would you like to do a full backup, including system apps and sdcard contents? enter Y or N --> ")
            while not re.search(r'^[yYnN]$', fullbackup):
               fullbackup = raw_input("invalid selection. please enter Y for full backup or N for other options --> ")
            if fullbackup.lower() == 'y':
               backapk = "apk"
               backobb = "obb"
               backshared = "shared"
               backall = "full"
               backsys = "sys"
            else:
               checkapk = raw_input("enter 1 to include APK files, or 2 to exclude --> ")
               while not re.search(r'^[12]$', checkapk):
                  checkapk = raw_input("invalid selection. enter 1 to include APK files, or 2 to exclude --> ")
               if checkapk == '1':
                  backapk = "apk"
                  checkobb = raw_input("enter 1 to include APK expansion files, or 2 to exclude --> ")
                  while not re.search(r'^[12]$', checkobb):
                     checkobb = raw_input("invalid selection. enter 1 to include APK expansion files, or 2 to exclude --> ")
                  if checkobb == '1':
                     backobb = "obb"
                  else:
                     backobb = "no"
               else:
                  backapk = "no"
               checkshared = raw_input("enter 1 to backup sdcard [userdata] contents, or 2 to exclude --> ")
               while not re.search(r'^[12]$', checkshared):
                  checkshared = raw_input("invalid selection. enter 1 to backup sdcard contents, or 2 to exclude --> ")
               if checkshared == '1':
                  backshared = "shared"
                  checkall = raw_input("enter 1 to backup all installed applications, or 2 to exclude --> ")
                  while not re.search(r'^[12]$', checkall):
                     checkall = raw_input("invalid selection. enter 1 to backup all installed applications, or 2 to exclude --> ")
                  if checkall == '1':
                     backall = "all"
                  else:
                     backall = "no"
               else:
                  backshared = "no"
                  backall = "all"
               checksys = raw_input("enter 1 to backup system apps, or 2 to exclude --> ")
               while not re.search(r'^[12]$',checksys):
                  checksys = raw_input("invalid selection. enter 1 to backup system apps, or 2 to exclude --> ")
               if checksys == '1':
                  backsys = "sys"
               else:
                  backsys = "no"
            backupfile = 'backup-' + str(datetime.date.today()) + '.ab'
            raw_input("to continue with backup, press ENTER. then check device and follow prompts to continue. the backup process may take awhile.")
            obj.backup(backupfile, backapk, backobb, backshared, backall, backsys)
            raw_input("backup complete! backup file saved as: \033[35m" + backupfile + "\033[0m. press ENTER to return to main menu.")
         elif whichbackup == '2':
            restorefile = raw_input("please enter path to backup file on your computer [ex. \'backup-yyyy-mm-dd.ab\'] --> ")
            while not os.path.isfile(restorefile):
               restorefile = raw_input("file does not exist. please enter valid path --> ")
            obj.restore(restorefile)
            raw_input("restore complete! press ENTER to reboot and continue..")
            obj.reboot("android")
         else:
            print("unable to connect to device. returning to main menu..")
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 7 - ROOT DEVICE #
############################################################
############################################################

      elif option == '7': #root
      
         def twrpdl(): # DOWNLOAD TWRP CUSTOM RECOVERY
            TWRPurl = "http://notworth.it/opo/twrp.img"
            TWRPmd5 = "77ba4381b13a03cc6dcff90f95e59a24"
            dl = urllib.URLopener()
            dl.retrieve(TWRPurl, "twrp.img")
            site = urllib.urlopen(TWRPurl)
            meta = site.info()
            dlsize = meta.getheaders("Content-Length")[0]
            fsize = os.path.getsize("twrp.img")
            if usecolor == 'color':
               print("file size: \033[33m")
               print(dlsize)
               print("\n\033[0mbytes downloaded: \033[33m")
               print(fsize)
               print("\033[0m\n")
               print("\033[34mchecking md5 signature...\033[0m\n")
            else:
               print("file size: ")
               print(dlsize)
               print("bytes downloaded: ")
               print(fsize)
               print("checking md5 signature...")
            md5_read = ''
            integrity = ''
            with open("twrp.img", "r+b") as sf:
               sfdata = sf.read()
               md5_read = hashlib.md5(sfdata).hexdigest()
            if TWRPmd5 == md5_read:
               print("MD5 verified!")
               integrity = 'passed'
            else:
               print("MD5 file integrity check failed!")
               integrity = 'failed'
            if integrity == 'failed':
               if dlsize != fsize:
                  with open("twrp.img", "r+b") as f:
                     # read contents of downloaded file
                     fdata = f.read()
                     f.write(site.read())
                     f.flush()
                     os.fsync(f.fileno())
                     f.close()
         
         def recovdl(recovimg): # DOWNLOAD IMAGE FROM SITE
            recovurl = "http://notworth.it/opo/" + recovimg
            if recovimg == 'philz.img':
               recovmd5 = "b2f8fb888e1377f00187ad0bd35a6584"
            elif recovimg == 'cwm.img':
               recovmd5 = "b60bd10f3f7cc254a4354cdc9c69b3bd"
            else: # twrp.img MD5
               recovmd5 = "77ba4381b13a03cc6dcff90f95e59a24"
            dl = urllib.URLopener()
            dl.retrieve(recovurl, recovimg)
            site = urllib.urlopen(recovurl)
            meta = site.info()
            dlsize = meta.getheaders("Content-Length")[0]
            fsize = os.path.getsize(recovimg)
            if usecolor == 'color':
               print("file size: \033[33m")
               print(dlsize)
               print("\n\033[0mbytes downloaded: \033[33m")
               print(fsize)
               print("\033[0m\n")
               print("\033[34mchecking md5 signature...\033[0m\n")
            else:
               print("file size: ")
               print(dlsize)
               print("bytes downloaded: ")
               print(fsize)
               print("checking md5 signature...")
            md5_read = ''
            integrity = ''
            with open(recovimg, "r+b") as sf:
               sfdata = sf.read()
               md5_read = hashlib.md5(sfdata).hexdigest()
            if recovmd5 == md5_read:
               print("MD5 verified!")
               integrity = 'passed'
            else:
               print("MD5 file integrity check failed!")
               integrity = 'failed'
            if integrity == 'failed':
               if dlsize != fsize:
                  with open(recovimg, "r+b") as f:
                     # read contents of downloaded recovery file
                     fdata = f.read()
                     f.write(site.read())
                     f.flush()
                     os.fsync(f.fileno())
                     f.close()
         
         def chooserec(): # CHOOSE WHICH CUSTOM RECOVERY TO BOOT INTO ONCE
            recovimg = "twrp.img"
            pickrecov = raw_input("press 1 to flash superSU in TWRP Recovery, 2 to use Philz Recovery, or 3 to use CWM. --> ")
            while not re.search(r'^[123]$', pickrecov):
               pickrecov = raw_input("invalid selection. press 1 to flash superSU in TWRP Recovery, 2 for Philz, or 3 for CWM. --> ")
            if pickrecov == '1': # SUPERSU TWRP
               recovimg = "twrp.img"
            elif pickrecov == '2': # SUPERSU PHILZ
               recovimg = "philz.img"
            elif pickrecov == '3': # SUPERSU CWM
               recovimg = "cwm.img"
            else:
               print("unable to connect to device. returning to main menu..\n")
            return recovimg
            
         superSU = 'UPDATE-SuperSU-v2.45.zip'
         def sudl(): # DOWNLOAD SUPERSU ZIP
            URLsuperSU = "http://download.chainfire.eu/695/SuperSU/UPDATE-SuperSU-v2.45.zip?retrieve_file=1"
            MD5superSU = "9dbd5253b8f10a8064273dbec3bc78c8"
            
            dl = urllib.URLopener()
            dl.retrieve(URLsuperSU, superSU)
           
            site = urllib.urlopen(URLsuperSU)
            meta = site.info()
            dlsize = meta.getheaders("Content-Length")[0]
            fsize = os.path.getsize(superSU)
            if usecolor == "color":
               print("file size: \033[33m")
               print(dlsize)
               print("\n\033[0mbytes downloaded: \033[33m")
               print(fsize)
               print("\033[0m\n")
               print("\033[34mchecking md5 signature...\033[0m\n")
            else:
               print("file size: ")
               print(dlsize)
               print("bytes downloaded: ")
               print(fsize)
               print("checking md5 signature...")
            md5_read = ''
            integrity = ''
            with open(superSU, "r+b") as sf:
               sfdata = sf.read()
               md5_read = hashlib.md5(sfdata).hexdigest()
            if MD5superSU == md5_read:
               print("MD5 verified!")
               integrity = 'passed'
            else:
               print("MD5 file integrity check failed!")
               integrity = 'failed'
            if integrity == 'failed':
               if dlsize != fsize:
                  with open(superSU, "r+b") as f:
                     # read contents of downloaded SuperSU file
                     fdata = f.read()
                     f.write(site.read())
                     f.flush()
                     os.fsync(f.fileno())
                     f.close()
            
         def suroot(recovimg):
            while not os.path.isfile(superSU):
               if usecolor == 'color':
                  print("file \033[32m" + superSU + " \033[0mnot found.\n \033[40m\033[34;1mattempting download...\033[0m\n")
               else:
                  print("file " + superSU + " not found. \n attempting download... \n")
               sudl()
            if usecolor == 'color':   
               print("file \033[32m" + superSU + " \033[0mfound!\n")
            else:
               print("file " + superSU + " found!\n")
            while not os.path.isfile(recovimg):
               if usecolor == 'color':
                  print("file \033[32m" + recovimg + " \033[0mnot found. attempting download...\n")
               else:
                  print("file " + recovimg + " not found. attempting download...\n")
               recovdl(recovimg)
            if usecolor == 'color':
               print("file \033[32m" + recovimg + " \033[0mfound!\n")
            else:
               print("file " + recovimg + " found!\n")
            raw_input("press ENTER to copy file to device, then reboot into bootloader.")
            remotesuperSU = '/sdcard/UPDATE-SuperSU-v2.45.zip'
            obj.push(superSU, remotesuperSU)
            obj.reboot("bootloader")
            raw_input("press ENTER to boot into custom recovery.")
            obj.bootimg(recovimg)
            print("check that device is connected and booted into custom recovery. on device, choose the ADB SIDELOAD option [sometimes under ADVANCED].\n")
            raw_input("press ENTER to continue with flashing superSU file via ADB sideload.")
            obj.sideload(superSU)
            sidefail = raw_input("if install failed, press 1 to attempt install from device. else, reboot into system from device recovery menu and press ENTER. --> ")
            if sidefail == '1':
               print("on device recovery menu, choose INSTALL, then select file \033[36m" + superSU + "\033[0m from the \033[36m/SDCARD\033[0m root directory.\n")
               raw_input("swipe to install - this may take a moment. if install is successful, select REBOOT from recovery menu. press ENTER to continue.")
            obj.reboot("android")
         
         superusr = 'Superuser-3.1.3-arm-signed.zip'
         def susrdl():  # DOWNLOAD SUPERUSER ZIP
            URLsuperusr = "http://notworth.it/opo/Superuser-3.1.3-arm-signed.zip"
            MD5superusr = "b3c89f46f014c9df7d23b94d37386b8a"
            dl = urllib.URLopener()
            dl.retrieve(URLsuperusr, superusr)
            site = urllib.urlopen(URLsuperusr)
            meta = site.info()
            dlsize = meta.getheaders("Content-Length")[0]
            if usecolor == "color":
               print("file size: \033[33m")
               print(dlsize)
               print("\n\033[0mbytes downloaded: \033[33m")
               print(fsize)
               print("\033[0m\n")
               print("\033[34mchecking md5 signature...\033[0m\n")
            else:
               print("file size: ")
               print(dlsize)
               print("bytes downloaded: ")
               print(fsize)
               print("checking md5 signature...")
            md5_read = ''
            integrity = ''
            with open(superusr, "r+b") as sf:
               sfdata = sf.read()
               md5_read = hashlib.md5(sfdata).hexdigest()
            if MD5superusr == md5_read:
               print("MD5 verified!")
               integrity = 'passed'
            else:
               print("MD5 file integrity check failed!")
               integrity = 'failed'
            if integrity == 'failed':
               if dlsize != fsize:
                  with open(superusr, "r+b") as f:
                     # read contents of downloaded Superuser file
                     fdata = f.read()
                     f.write(site.read())
                     f.flush()
                     os.fsync(f.fileno())
                     f.close()
            
         def susrroot(recovimg): # FLASH SUPERUSER ZIP IN CUSTOM RECOVERY
            while not os.path.isfile(superusr):
               if usecolor == 'color':
                  print("file \033[32m" + superusr + " \033[0mnot found. attempting download...\n")
               else:
                  print("file " + superusr + " not found. attempting download... \n")
               susrdl()
            if usecolor == 'color':
               print("file \033[32m" + superusr + " \033[0mfound!\n")
            else:
               print("file " + superusr + " found!\n")
            while not os.path.isfile(recovimg):
               if usecolor == 'color':
                  print("file \033[32m" + recovimg + " \033[0mnot found. attempting download...\n")
               else:
                  print("file " + recovimg + " not found. attempting download...")
               recovdl(recovimg)
            if usecolor == 'color':
               print("file \033[32m" + recovimg + " \033[0mfound!\n")
            else:
               print("file " + recovimg + " found!")
            raw_input("press ENTER to copy file to device and reboot into bootloader.")
            remotesuperusr = '/sdcard/Superuser-3.1.3-arm-signed.zip'
            obj.push(superusr, remotesuperusr)
            obj.reboot("bootloader")
            raw_input("press ENTER to boot into custom recovery.")
            obj.bootimg(recovimg)
            if usecolor == 'color':
               print("on device, choose INSTALL from recovery menu, then select file \033[36m" + superusr + "\033[0m in the \033[36m/sdcard\033[0m directory.\n")
            else:
               print("on device, choose INSTALL from recovery menu, then select file " + superusr + " in the /sdcard directory.\n")
            raw_input("if install is successful, select REBOOT from recovery menu on device. press ENTER to continue.")
         
         trfile = 'apps/tr.apk'
         def trdl(): # DOWNLOAD TOWELROOT APK
            dl = urllib.URLopener()
            URLtr = "https://towelroot.com/tr.apk"
            MD5tr = "e287e785d0e3e043fb0cfbfe69309d8e"
            dl.retrieve(URLtr, trfile)
            site = urllib.urlopen(URLtr)
            meta = site.info()
            dlsize = meta.getheaders("Content-Length")[0]
            fsize = os.path.getsize(trfile)
            if usecolor == "color":
               print("file size: \033[33m")
               print(dlsize)
               print("\n\033[0mbytes downloaded: \033[33m")
               print(fsize)
               print("\033[0m\n")
               print("\033[34mchecking md5 signature...\033[0m\n")
            else:
               print("file size: ")
               print(dlsize)
               print("bytes downloaded: ")
               print(fsize)
               print("checking md5 signature...")
            md5_read = ''
            integrity = ''
            with open(trfile, "r+b") as sf:
               sfdata = sf.read()
               md5_read = hashlib.md5(sfdata).hexdigest()
            if MD5tr == md5_read:
               print("MD5 verified!")
               integrity = 'passed'
            else:
               print("MD5 file integrity check failed!")
               integrity = 'failed'
            if integrity == 'failed':
               if dlsize != fsize:
                  with open(trfile, "r+b") as f:
                     # read contents of downloaded TowelRoot file
                     fdata = f.read()
                     f.write(site.read())
                     f.flush()
                     os.fsync(f.fileno())
                     f.close()
            
         def towroot(): # INSTALL TOWELROOT APK
            if not os.path.exists('apps'):
               os.makedirs('apps', 0755)
            while not os.path.isfile(trfile):
               print("file \033[32m" + trfile + " \033[0mnot found. attempting download...\n")
               trdl()
            print("file \033[32m" + trfile + " \033[0mfound!\n")
            raw_input("press ENTER to install..")
            obj.install(trfile)
            obj.shell('am start -n com.geohot.towelroot/com.geohot.towelroot.TowelRoot')
            print("if APK installed successfully, it should automatically launch on your device.")
            raw_input("tap on MAKE IT RAIN. the results should appear shortly. follow instructions on device, then press ENTER to continue..")
            
         print("\033[36mif the firmware release date for your device is before june 2014, there is a chance the towelroot exploit may work.")
         print("\033[35mhowever, superSU is a safer and more widely confirmed root method for the ONEPLUS ONE. ATTEMPT AT YOUR OWN RISK!\033[0m\n")
         rootcheck = raw_input("which root method would you like to try? enter 1 for superSU [recommended for oneplus one], 2 for towelroot, 3 for Superuser, or 4 to install custom ZIP file. --> ")
         while not re.search(r'^[1-4]$', rootcheck):
            rootcheck = raw_input("invalid selection. enter 1 to install superSU package, 2 to install towelroot exploit, 3 to install Superuser, or 4 to install custom ZIP file. --> ")
               
         if rootcheck == '1': # SUPERSU
            bootcustom = raw_input("press 1 to install superSU in custom recovery, 2 to install in your installed recovery, or 3 to install in fastboot [lower success rate]. --> ")
            while not re.search(r'^[1-3]$', bootcustom):
               bootcustom = raw_input("invalid choice. please enter 1 to load custom recovery, 2 to use installed recovery, or 3 for fastboot. --> ")
            if bootcustom == '1': # SUPERSU TWRP
               recovimg = chooserec()
               suroot(recovimg) # SUPERSU CUSTOM RECOVERY
               time.sleep(0.9)
               main()
            elif bootcustom == '2': # INSTALLED RECOVERY
               while not os.path.isfile(superSU):
                  if usecolor == 'color':
                     print("file \033[32m" + superSU + " \033[0mnot found. attempting download...\n")
                  else:
                     print("file " + superSU + " not found. attempting download...")
                  sudl()
               if usecolor == 'color':
                  print("file \033[32m" + superSU + " \033[0mfound!\n")
               else:
                  print("file " + superSU + " found!\n")
               raw_input("press ENTER to copy file to device, then reboot into recovery.")
               remotesuperSU = '/sdcard/UPDATE-SuperSU-v2.45.zip'
               obj.push(superSU, remotesuperSU)
               raw_input("file copied to device. press ENTER to continue to recovery..")
               obj.reboot("recovery")
               raw_input("in recovery menu on device, please select APPLY UPDATE, then APPLY FROM ADB. press ENTER when ready.")
               obj.sideload("UPDATE-SuperSU-v2.45.zip")
               superfail = raw_input("choose REBOOT SYSTEM from device menu. if update successful, press ENTER. else, press 1 to install superSU from TWRP, or 2 to install superSU from Philz --> " )
               ogj.reboot("android")
               if superfail == '1': # SUPERSU TWRP
                  suroot("twrp.img")
               elif superfail == '2': # SUPERSU PHILZ
                  suroot("philz.img")
               else:
                  obj.get_state()
               time.sleep(0.9)
               main()
               
            elif bootcustom == '3': # SUPERSU FASTBOOT
               updatewhich = raw_input("to try installing superSU in fastboot, press 1. else, enter name of ZIP file to install --> ")
               if updatewhich == '1': # SUPERSU FASTBOOT
                  while not os.path.isfile(superSU):
                     if usecolor == 'color':
                        print("file \033[32m" + superSU + " \033[0mnot found. attempting download...\n\n")
                     else:
                        print("file " + superSU + " not found. attempting download...\n\n")
                     sudl()
                  raw_input("press ENTER to reboot into bootloader.")
                  obj.reboot("bootloader")
                  if usecolor == 'color':
                     print("\033[35mattempting to install superSU via fastboot...\n\033[0m")
                  else:
                     print("attempting to install superSU via fastboot...\n")
                  obj.update(superSU)
                  failsu = raw_input("if installation failed, press 1 to try sideload method. otherwise, press ENTER to continue...")
                  if failsu == '1': # SUPERSU SIDELOAD
                     obj.fastreboot("android")
                     time.sleep(0.9)
                     print("\033[32mmake sure your computer is authorized to access your device over ADB.\033[0m\n")
                     raw_input("press ENTER to continue rebooting to recovery..")
                     obj.reboot("recovery")
                     raw_input("in recovery menu on device, please select APPLY UPDATE, then APPLY FROM ADB. press ENTER when ready.")
                     obj.sideload("UPDATE-SuperSU-v2.45.zip")
                     superfail = raw_input("choose REBOOT SYSTEM from device menu. if update successful, press ENTER. else, press 1 to install superSU from TWRP, or 2 to install superSU from Philz --> " )
                     ogj.reboot("android")
                     if superfail == '1': # SUPERSU TWRP
                        suroot("twrp.img")
                     elif superfail == '2': # SUPERSU PHILZ
                        suroot("philz.img")
                     else:
                        obj.get_state()
                  time.sleep(0.9)
                  main()
               else:
                  print("attempting to install " + updatewhich + "...\n\n")
                  while not os.path.isfile(updatewhich):
                     updatewhich = raw_input("invalid file path. please enter correct path of ZIP file to install --> ")
                  obj.update(updatewhich) # CUSTOM FASTBOOT UPDATE
                  failupd = raw_input("if installation failed, press 1 to try sideload method. otherwise, press ENTER to continue...")
                  if failupd == '1':
                     obj.fastreboot("android")
                     time.sleep(0.9)
                     print("\033[32mmake sure your computer is authorized to access your device over ADB.\033[0m\n")
                     raw_input("press ENTER to continue..")
                     obj.reboot("recovery")
                     raw_input("in recovery menu on device, please select APPLY UPDATE, then APPLY FROM ADB. press ENTER when ready.")
                     obj.sideload(updatewhich) # CUSTOM SIDELOAD
                     raw_input("please follow reboot prompts on device recovery menu, then press ENTER to continue...")
                  else:
                     obj.fastreboot("android")
                  time.sleep(0.9)
                  main()
            else:
               print("failed to connect to device. returning to main menu.. \n\n")
               

         elif rootcheck == '2': # TOWELROOT
            towroot()
            trysuroot = raw_input("if towelroot failed, press 1 to launch superSU method. otherwise, press ENTER to return to main menu. --> ")
            if trysuroot == '1': # SUPERSU
               recovimg = chooserec()
               suroot(recovimg) # SUPERSU CUSTOM RECOVERY
               time.sleep(0.9)
               main()
            else:
               time.sleep(0.9)
               main()
         
         elif rootcheck == '3': # SUPERUSER or CUSTOM ZIP FILE
            bootcustom = raw_input("press 1 to install Superuser in TWRP recovery, 2 to install in Philz recovery, or 3 to install in fastboot [lowest success rate]. --> ")
            while not re.search(r'^[123]$', bootcustom):
               bootcustom = raw_input("invalid choice. please enter 1 to load TWRP, 2 for Philz, or 3 for fastboot. --> ")
            if bootcustom == '1':
               susrroot("twrp.img")
            elif bootcustom == '2':
               susrroot("philz.img")
            elif bootcustom == '3':
               while not os.path.isfile(superusr):
                  print("file \033[32m" + superusr + " \033[0mnot found. attempting download...\n\n")
                  sudl()
               raw_input("press ENTER to reboot into bootloader.")
               obj.reboot("bootloader")
               print("\033[35mattempting to install Superuser via fastboot...\n\033[0m")
               obj.update(superusr)
               failsu = raw_input("if installation failed, press 1 to try sideload method. otherwise, press ENTER to continue...")
               if failsu == '1':
                  obj.fastreboot("android")
                  time.sleep(0.9)
                  print("\033[32mmake sure your computer is authorized to access your device over ADB.\033[0m\n")
                  raw_input("press ENTER to continue..")
                  obj.reboot("recovery")
                  raw_input("in recovery menu on device, please select APPLY UPDATE, then APPLY FROM ADB. press ENTER when ready.")
                  obj.sideload(superusr)
                  superfail = raw_input("choose REBOOT SYSTEM from device menu. if update successful, press ENTER. else, press 1 to install Superuser via TWRP or 2 to install Superuser via Philz. --> " )
                  if superfail == '1':
                     susrroot("twrp.img")
                  elif superfail == '2':
                     susrroot("philz.img")
                  else:
                     obj.get_state()
               time.sleep(0.9)
               main()
                  
            elif rootcheck == '4':
               updatefile = raw_input("please enter path of ZIP file to install --> ")
               while not os.path.isfile(updatefile):
                  updatefile = raw_input("invalid file path. please enter correct path of ZIP file to install --> ")
               raw_input("press ENTER to reboot into bootloader.")
               obj.reboot("bootloader")
               print("attempting to install " + updatefile + "...\n")
               obj.update(updatefile)
               raw_input("press ENTER to continue...")
               obj.fastreboot("android")
               time.sleep(0.9)
               main()
            
            else:
               print("failed to connect to device. returning to main menu.. \n\n")
               
         else:
            print("failed to connect to device. returning to main menu.. \n\n")
                  
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 8 - FLASH STOCK IMAGES/PARTITIONS #
############################################################
############################################################
         
      elif option == '8': #flash stock images/partitions
      
         def dlimg(imgfile):
            dlfile = "http://notworth.it/opo/" + imgfile
            dl = urllib.URLopener()
            dl.retrieve(dlfile, imgfile)
            site = urllib.urlopen(dlfile)
            meta = site.info()
            dlsize = meta.getheaders("Content-Length")[0]
            fsize = os.path.getsize(imgfile)
            print("file size: \033[33m")
            print(dlsize)
            print("\n\033[0mbytes downloaded: \033[33m")
            print(fsize)
            print("\033[0m\n")
      
         def flashmenu():
            if usecolor == 'color':
               menuflash = colorflashmenu
            else:
               menuflash = cleanflashmenu
            print(menuflash)
            flashsel = raw_input("select an option from 1 through 9 from menu --> ")
            while not re.search(r'^[1-9]$', flashsel):
               flashsel = raw_input("invalid selection. please choose an option between 1 and 9 --> ")
            if usecolor == 'color':
               print(colorversionmenu)
            else:
               print(cleanversionmenu)
                  
            verssel = raw_input("choose target version 1-5 from menu, or 6 to exit --> ")
            while not re.search(r'^[1-6]$', verssel):
               verssel = raw_input("invalid selection. please choose an option between 1-6 --> ")
            #vers = ''
   
            if verssel == '1':
               vers = 'XNPH25R'
   
            elif verssel == '2':
               vers = 'XNPH30O'
   
            elif verssel == '3':
               vers = 'XNPH33R'
      
            elif verssel == '4':
               vers = 'XNPH38R'
      
            elif verssel == '5':
               vers = 'XNPH44S'
   
            elif verssel == '6':
               print("returning to main menu..")
               time.sleep(0.9)
               main()
   
            else:
               print("an error has occurred. returning to main menu..")
               time.sleep(0.9)
               main()
            
            if re.search(r'^[1-7]$', flashsel):
               print("\n\033[34mrebooting into bootloader...\033[0m\n")
               obj.reboot("bootloader")
            
            if flashsel == '1':
               imgfile = vers + "/boot.img"
               while not os.path.isfile(imgfile):
                  if not os.path.exists(vers):
                     os.makedirs(vers, 0755)
                  print("downloading %s...") % imgfile
                  dlimg(imgfile)
               raw_input("press ENTER to proceed with flashing boot image..")
               obj.flashf("boot", imgfile)
               raw_input("press ENTER key to continue...")
               flashmenu()
               
            elif flashsel == '2':
               whichsize = raw_input("IMPORTANT!! choose correct storage capacity: enter 1 for 16gb device, or 2 for 64gb device. --> ")
               while not re.search(r'^[12]$', whichsize):
                  whichsize = raw_input("invalid selection. enter 1 for 16gb device, or 2 for 64gb device. --> ")
               if whichsize == '1':
                  imgfile = vers + "/userdata.img"
               elif whichsize == '2':
                  imgfile = vers + "/userdata_64G.img"
               else:
                  print("ERROR: an unknown error has occurred.")
               while not os.path.isfile(imgfile):
                  if not os.path.exists(vers):
                     os.makedirs(vers, 0755)
                  print("downloading %s") % imgfile
                  dlimg(imgfile)
               raw_input("press ENTER to proceed with flashing data.")
               obj.flashf("data", imgfile)
               raw_input("press ENTER key to return to flash menu...")
               flashmenu()
               
            elif flashsel == '3':
               imgfile = vers + "/system.img"
               while not os.path.isfile(imgfile):
                  if not os.path.exists(vers):
                     os.makedirs(vers, 0755)
                  print("downloading %s...") % imgfile
                  dlimg(imgfile)
               raw_input("press ENTER to proceed with flashing system.")
               obj.flashf("system", imgfile)
               raw_input("press ENTER key to continue...")
               flashmenu()
               
            elif flashsel == '4':
               imgfile = vers + "/recovery.img"
               while not os.path.isfile(imgfile):
                  if not os.path.exists(vers):
                     os.makedirs(vers, 0755)
                  print("downloading %s...") % imgfile
                  dlimg(imgfile)
               raw_input("press ENTER to proceed with flashing recovery.")
               obj.flashf("recovery", imgfile)
               raw_input("press ENTER key to continue...")
               flashmenu()
               
            elif flashsel == '5':
               imgfile = vers + "/cache.img"
               while not os.path.isfile(imgfile):
                  if not os.path.exists(vers):
                     os.makedirs(vers, 0755)
                  print("downloading %s...") % imgfile
                  dlimg(imgfile)
               raw_input("press ENTER to proceed with flashing cache.")
               obj.flashf("cache", imgfile)
               raw_input("press ENTER key to continue...")
               flashmenu()
               
            elif flashsel == '6':
               if not os.path.exists(vers):
                  os.makedirs(vers, 0755)
               imgfile = vers + "/flash-radio.sh"
               while not os.path.isfile(imgfile):
                  print("downloading %s...") % imgfile
                  dlimg(imgfile)
                  os.chmod(imgfile, 0755)
               while not os.path.isfile(vers + "/boot.img"):
                  print("downloading %s/boot.img..") % vers
                  dlimg("%s/boot.img") % vers
               while not os.path.isfile(vers + "/emmc_appsboot.mbn"):
                  print("downloading %s/emmc_appsboot.mbn..") % vers
                  dlimg("%s/emmc_appsboot.mbn") % vers
               while not os.path.isfile(vers + "/NON-HLOS.bin"):
                  print("downloading %s/NON-HLOS.bin..") % vers
                  dlimg("%s/NON-HLOS.bin") % vers
               while not os.path.isfile(vers + "/rpm.mbn"):
                  print("downloading %s/rpm.mbn..") % vers
                  dlimg("%s/rpm.mbn") % vers
               while not os.path.isfile(vers + "/sbl1.mbn"):
                  print("downloading %s/sbl1.mbn..") % vers
                  dlimg("%s/sbl1.mbn") % vers
               while not os.path.isfile(vers + "/sdi.mbn"):
                  print("downloading %s/sdi.mbn..") % vers
                  dlimg("%s/sdi.mbn") % vers
               while not os.path.isfile(vers + "/tz.mbn"):
                  print("downloading %s/tz.mbn..") % vers
                  dlimg("%s/tz.mbn") % vers
               while not os.path.isfile(vers + "/logo.bin"):
                  print("downloading %s/logo.bin..") % vers
                  dlimg("%s/logo.bin") % vers
               subprocess.call(['./flash-radio.sh'], cwd='%s', shell=True) % vers
               raw_input("press ENTER key to continue...")
               flashmenu()
               
            elif flashsel == '7':
               if not os.path.exists(vers):
                  os.makedirs(vers, 0755)
               while not os.path.isfile(vers + "/boot.img"):
                  print("downloading %s/boot.img..") % vers
                  dlimg("%s/boot.img") % vers
               while not os.path.isfile(vers + "/emmc_appsboot.mbn"):
                  print("downloading %s/emmc_appsboot.mbn..") % vers
                  dlimg("%s/emmc_appsboot.mbn") % vers
               while not os.path.isfile(vers + "/NON-HLOS.bin"):
                  print("downloading %s/NON-HLOS.bin..") % vers
                  dlimg("%s/NON-HLOS.bin") % vers
               while not os.path.isfile(vers + "/rpm.mbn"):
                  print("downloading %s/rpm.mbn..") % vers
                  dlimg("%s/rpm.mbn") % vers
               while not os.path.isfile(vers + "/sbl1.mbn"):
                  print("downloading %s/sbl1.mbn..") % vers
                  dlimg("%s/sbl1.mbn") % vers
               while not os.path.isfile(vers + "/flash-extras.sh"):
                  print("downloading %s/flash-extras.sh..") % vers
                  dlimg("%s/flash-extras.sh") % vers
                  os.chmod(vers + "/flash-extras.sh", 0755)
               raw_input("press ENTER to proceed with running flash-extras.sh script.")
               subprocess.call(['./flash-extras.sh'], cwd='%s', shell=True) % vers
               raw_input("press ENTER key to continue...")
               obj.fastreboot("android")
               flashmenu()
               
            elif flashsel == '8':
               romsel = raw_input("enter 1 to flash stock ROM for %s, 2 to flash custom ROM, or 3 to return to main menu. --> ") % vers
               while not re.search(r'^[1-3]$', romsel):
                  romsel = raw_input("invalid selection. enter an option 1-3. --> ")
               if romsel == '1':
                  imgfile = vers + "/%s-bacon-signed-fastboot.zip" % vers
                  if not os.path.exists(vers):
                     os.makedirs(vers, 0755)
                  while not os.path.isfile(imgfile):
                     print("file \033[32m" + imgfile + " \033[0mnot found. attempting download...\n")
                     dlimg(imgfile)
                  print("file \033[32m" + imgfile + " \033[0mfound!\n")
                  raw_input("press ENTER to reboot into bootloader..")
                  obj.reboot("bootloader")
                  obj.update(imgfile)
                  failupd = raw_input("if update failed, press 1. otherwise, press ENTER key to continue. --> ")
                  if failupd == '1':
                     obj.fastreboot("android")
                     raw_input("check that device is unlocked and computer is authorized for ADB access. press ENTER to continue..")
                     imgfileonly = imgfile[8:]
                     rimgfile = "/sdcard/" + imgfileonly
                     obj.push(imgfile, rimgfile)
                     raw_input("press ENTER to reboot into recovery.")
                     obj.reboot("recovery")
                     print("choose APPLY UPDATE from recovery menu and select APPLY FROM ADB.\n")
                     raw_input("press ENTER to install from stock image now.")
                     obj.sideload(imgfile)
                     failside = raw_input("if update failed, press 1 to update from device storage. else, push POWER button on device to reboot, then press ENTER to continue. --> ")
                     if failside == '1':
                        print("choose APPLY UPDATE from recovery menu, then select CHOOSE FROM INTERNAL STORAGE.\n")
                        print("select file \033[32m" + imgfileonly + " \033[0mfrom root of SDCARD directory and install.\n")
                        print("\033[35mif update fails again, return to main menu and choose option 3 to reboot into custom recovery.\033[0m\n\n")
                        menusel = raw_input("enter 1 to return to flash menu, or 2 to return to main menu. --> ")
                        while not re.search(r'^[12]$',menusel):
                           menusel = raw_input("invalid selection. press 1 for flash menu, or 2 to return to main menu. --> ")
                        if menusel == '1':
                           time.sleep(0.9)
                           flashmenu()
                        elif menusel == '2':
                           time.sleep(0.9)
                           main()
                        else:
                           print("error connecting to device. returning to main menu...\n")
                           time.sleep(0.9)
                           main()
                     else:
                        print("\033[32mreturning to flash menu..\033[0m\n\n")
                        time.sleep(0.9)
                        flashmenu()
                  else:
                     print("\033[32mreturning to flash menu..\033[0m\n\n")
                     time.sleep(0.9)
                     flashmenu()
               elif romsel == '2':
                  print("\033[31mmake sure device is unlocked and PC is authenticated for ADB access.\033[0m\n")
                  romname = raw_input("place ROM file into same directory as the script home, then enter filename --> ")
                  while not os.path.isfile(romname):
                     romname = raw_input("invalid filename. make sure ROM ZIP file to flash is in correct location, then enter filename --> ")
                  rimgfile = "/sdcard/" + romname
                  print("\033[32mpushing update file to device..\033[0m\n")
                  obj.push(romname, rimgfile)
                  raw_input("press ENTER to reboot to bootloader.")
                  obj.reboot("bootloader")
                  while not os.path.isfile("twrp.img"):
                     print("file \033[32mtwrp.img \033[0mnot found. attempting download...\n")
                     dlimg("twrp.img")
                  print("file \033[32mtwrp.img \033[0mfound!\n")
                  raw_input("press ENTER to continue booting into TWRP recovery.")
                  obj.bootimg("twrp.img")
                  print("on device, choose ADVANCED from TWRP menu, then select INSTALL ZIP and to APPLY VIA ADB SIDELOAD.\n")
                  raw_input("press ENTER to install the zip file you specified.")
                  obj.sideload(imgfile)
                  failside = raw_input("if update failed, enter 1 to try installing from device storage. otherwise, push select REBOOT from device recovery menu, reboot into system, and press ENTER to continue. --> ")
                  if failside == '1':
                     print("select INSTALL on device TWRP menu, then find your file \033[32m" + romname + " \033[0min device SDCARD root and swipe to install file.\n")
                     menusel = raw_input("when flash complete, select REBOOT into SYSTEM from recovery options on device. then enter 1 to return to flash menu, or 2 for main menu.")
                     while not re.search(r'^[12]$',menusel):
                        menusel = raw_input("invalid selection. enter 1 for flash menu, or 2 to return to main menu.")
                     if menusel == '1':
                        time.sleep(0.9)
                        flashmenu()
                     elif menusel == '2':
                        time.sleep(0.9)
                        main()
                     else:
                        print("an unknown error has occurred. returning to main menu...\n")
                        time.sleep(0.9)
                        main()
                        
               elif romsel == '3':
                  print("returning to main menu..")
                  time.sleep(0.9)
                  main()
                  
            elif flashsel == '0':
               checkreboot = raw_input("press 1 to reboot device into system, or ENTER to continue.. --> ")
               if checkreboot == '1':
                  obj.fastreboot("android")
               time.sleep(0.9)
               main()
               
            else:
               print("unable to connect to device. returning to flash menu..")
               time.sleep(0.9)
               flashmenu()
         
         flashmenu()
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 9 - UNLOCK BOOTLOADER #
############################################################
############################################################

      elif option == '9': # unlock bootloader
      
         def recovflash():
            flashcont = raw_input("select 1 to continue flashing recovery. select 2 to flash a stock or custom image. select 3 to return to flash menu. --> ")
            while not re.search(r'^[123]$', flashcont):
               flashcont = raw_input("invalid selection. select 1 to continue flashing recovery. select 2 to flash a stock partition image. select 3 to return to flash menu. --> ")
            if flashcont == '1':
               recovchoice = raw_input("enter 1 for TWRP, 2 for ClockworkMod, or 3 for Philz recovery --> ")
               while not re.search(r'^[1-3]$', recovchoice):
                  recovchoice = raw_input("invalid selection. please choose 1 for TWRP, 2 for CWM, or 3 for Philz --> ")
               obj.reboot("bootloader")
               if recovchoice == '1':
                  recovfile = "twrp.img"
                  while not os.path.isfile(recovfile):
                     print("file \033[32mtwrp.img \033[0mnot found. attempting download...\n")
                     dlrecov(recovfile)
                  print("file \033[32mtwrp.img \033[0mfound!\n")
                  raw_input("press ENTER to flash twrp.img over current recovery.")
                  obj.flashf("recovery","twrp.img")
               elif recovchoice == '2':
                  recovfile = "cwm.img"
                  while not os.path.isfile(recovfile):
                     print("file \033[32mcwm.img \033[0mnot found. attempting download...\n")
                     dlrecov(recovfile)
                  print("file \033[32mcwm.img \033[0mfound!\n")
                  raw_input("press ENTER to flash cwm.img over current recovery.")
                  obj.flashf("recovery","cwm.img")
               elif recovchoice == '3':
                  recovfile = "philz.img"
                  while not os.path.isfile(recovfile):
                     print("file \033[32mphilz.img \033[0mnot found. attempting download...\n")
                     dlrecov(recovfile)
                  print("file \033[32mphilz.img \033[0mfound!\n")
                  raw_input("press ENTER to flash philz.img over current recovery.")
                  obj.flashf("recovery","philz.img")
               else:
                  print("unable to connect to device.\n")
                  
            elif flashcont == '2':
               flashmenu()   
                                
            elif flashcont == '3':
               main()
               
            else:
               print("unable to connect to device.\n")
            
            time.sleep(0.9)
            
         bootcolormenu = '''
         \033[33m***UNLOCKING YOUR BOOTLOADER WILL WIPE YOUR DEVICE!!!***\033[0m
         \033[37mIF YOUR DEVICE HOLDS IMPORTANT DATA, BACK UP DEVICE BEFORE YOU CONTINUE!\033[0m
         '''
         bootcleanmenu = '''
         ***UNLOCKING YOUR BOOTLOADER WILL WIPE YOUR DEVICE!!!***
         IF YOUR DEVICE HOLDS IMPORTANT DATA, BACK UP DEVICE BEFORE YOU CONTINUE!'''
         
         if usecolor == 'color':
            print(bootcolormenu)
         else:
            print(bootcleanmenu)
            
         bunlock = raw_input("enter 1 to continue unlocking bootloader. enter 2 to skip to flashing custom recovery or images. enter 3 to re-lock bootloader. or enter 4 to return to previous menu. --> ")
         while not re.search(r'^[1-4]$', bunlock):
            bunlock = raw_input("invalid selection. enter 1 to unlock bootloader and wipe device. enter 2 to skip to flashing custom recovery or images. enter 3 to re-lock bootloader. or enter 4 to return to previous menu. --> ")
         
         if bunlock == '1':
            obj.reboot("bootloader")
            obj.unlockboot()
            print("your device should reboot after successfully unlocking the bootloader.\n")
            raw_input("press ENTER to continue...")
            recovflash()
            
         elif bunlock == '2':
            recovflash()
                    
         elif bunlock == '3':
            print("\033[33mREMINDER: to unlock your device again, you MUST downgrade to firmware release XNPH25R or earlier!\033[0m\n")
            btlockconfirm = raw_input("press ENTER to continue, or 1 to exit to the previous menu --> ")
            if btlockconfirm == '1':
               flashmenu()
            else:
               obj.reboot("bootloader")
               obj.lockboot()
               raw_input("press ENTER to reboot your device")
               obj.fastreboot("android")
         
         elif bunlock == '4':
            print("returning to previous menu menu..")
            time.sleep(0.9)
            flashmenu()
                  
         else:
            print("an unknown error has occurred. returning to main menu..")
            time.sleep(0.9)
            flashmenu()
               
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 10 - RUN SHELL COMMAND #
############################################################
############################################################

      elif option == '10': #run shell command
         shellcmd = raw_input("enter shell command --> ")
         while shellcmd:
            obj.shell(shellcmd)
            shellcmd = raw_input("enter another shell command, or press ENTER to return to main menu --> ")
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 11 - GET BUGREPORT #
############################################################
############################################################

      elif option is '11': #get bugreport
         raw_input("please allow several minutes for process to complete. press ENTER to start generating bug report.")
         obj.bugreport()
         raw_input("press ENTER to return to main menu.")
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 12 - LIST INSTALLED PACKAGES #
############################################################
############################################################

      elif option == '12': # list packages
         print("LISTING INSTALLED PACKAGES...")
         obj.listpkg()
         raw_input("press ENTER to return to main menu.")
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 13 - LIST SERVICES #
############################################################
############################################################

      elif option == '13': # list services
         print("LISTING RUNNING SERVICES...")
         obj.listsvc()
         raw_input("press ENTER to return to main menu.")
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 14 - GET LOGCAT #
############################################################
############################################################
                  
      elif option == '14': #get logcat
         print("logcat will open in a new window. close logcat window to return to menu.")
         if os.name == 'nt':
            process = subprocess.Popen('start /wait adb logcat', shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE)
         else:
            process = subprocess.Popen(['xterm', '-e', 'adb', 'logcat', 'sleep 4'], stdout=subprocess.PIPE)
         line = process.stdout.readline()
         while line:
            print line
            line = process.stdout.readline()
         time.sleep(0.9)
         main()

############################################################
############################################################
# OPTION 0 - QUIT #
############################################################
############################################################

      elif option == '0': #quit
         print("thanks for using the HALF-ASSED ONEPLUS ONE TOOLKIT! bye!")
         sys.exit()
                  
      else:
         print '\n\033[32man unhandled exception occurred. returning to main menu..\033[0m\n'
         time.sleep(0.9)
         main()

main()
sys.exit()
