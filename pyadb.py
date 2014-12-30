#!/usr/bin/env python
### PYADB (Python 2.7 Library)
##### VERSION: 1.3.3.7
##### RELEASE DATE: OCTOBER 13, 2014
##### AUTHOR: vvn
##### DESCRIPTION: simple library to port ADB and FASTBOOT functions to PYTHON
#####
##### for now it's a required companion to the 'half-assed one plus one toolkit'.
##### this project is vaguely based on some github code i found that had too many errors.
##### i know it isn't anything new. i know it's probably been done better.
##### but i wanted one that worked for me. if it works for you, go ahead and use it too!
##################################################
##################################################
##### USER LICENSE AGREEMENT & DISCLAIMER
##### copyright, copyleft (C) 2014  vvn <vvn@eudemonics.org>
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
##### (you might even enjoy it)
##### questions, comments, feedback, bugs, complaints, death threats, marriage proposals?
##### contact me at:
##### vvn (at) notworth (dot) it
##### latest version will always be available HERE:
##### http://notworth.it/opo/pyadb.py.txt (remove *.txt extension, obviously.)
##### MD5 checksum file will accompany it:
##### http://notworth.it/opo/pyadb.py.txt.md5
##### there be only code after this -->

import os, subprocess, sys, datetime
from subprocess import call, Popen, PIPE

class pyADB(object):

   # adb commands
   def call_adb(self, command):
      response = ''
      command_text = 'adb %s' % command
      # command_text = r'"%s"' % command_text
      command_text = command_text + '; exit 0'
      # output = Popen(command_text, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
      output = subprocess.check_call(command_text, shell=True, stderr=subprocess.STDOUT)
      return output
      # response = output.communicate()
      # return response

   # fastboot commands
   def call_fastboot(self, command):
      response = ''
      command_text = 'fastboot %s' % command
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
      response, errors = output.communicate()
      # response = output.stdout()
      return response
      
   # check for any ADB device
   def adbcallany(self, device_id):
      command = 'devices -s %s' % device_id
      result = self.call_adb(command)
      return result or None
      pass

   # check for any fastboot device
   def fastbootany(self, device_id):
      command = 'devices -s %s' % device_id
      result = self.call_fastboot(command)
      return result or None
      pass

   # return list of attached devices
   def attached_devices(self):
      command_text = "adb devices -l"
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
      response = output.communicate()
      return response or None
   
      # result = self.call_adb(command)
      # devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
      # return [device for device in devices if len(device) > 2]
      # return result

   # fastboot return list of devices
   def fastboot_devices(self):
      command_text = 'fastboot devices'
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
      response = output.communicate()
      return response or None
      # command = "devices -l"
      # result = self.call_adb(command)   
      # return result   

   # get device state
   def get_state(self):
      results = ''
      command_text = 'adb get-state'
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
      response = output.communicate()
      return response or None
      #result = self.call_adb("get-state")
      #return result or None

   # install APK
   def install(self, path_to_app):
      command = "install %s" % path_to_app
      result = self.call_adb(command)
      return result

   # uninstall APK
   def uninstall(self, path_to_app, args):
      command = "uninstall %s" % path_to_app
      if 'keep' in args:
         command = "uninstall -k %s" % path_to_app
      result = self.call_adb(command)
      return result

   # reboot
   def reboot(self, rb_type):
      command = "reboot"
      if 'recovery' in rb_type:
         command += " recovery"
      elif 'bootloader' in rb_type:
         command += " bootloader"
      result = self.call_adb(command)
      return result
      
   # fastboot reboot
   def fastreboot(self, rb_type):
      command = "reboot"
      if 'bootloader' in rb_type:
         command = "reboot-bootloader"
      result = self.call_fastboot(command)
      return result

   # push files
   def push(self, local, remote):
      command = "push -p " + r'"%s"' % local
      command += " " + r'"%s"' % remote
      result = self.call_adb(command)
      return result

   # pull files
   def pull(self, remote, local):
      command = "pull -p " + r'"%s"' % remote
      command += " " + r'"%s"' % local
      result = self.call_adb(command)
      return result

   # sync
   def sync(self, local, directory):
      command = "sync"
      if "none" in local:
         if "none" not in directory:
            command = "sync " + directory
      elif "none" not in local:
         command = "-p " + local + " sync"
         if "none" not in directory:
            command = "-p " + local + " sync " + directory
      else:
         command = "sync"
      result = self.call_adb(command)
      return result
      
   # shell command
   def shell(self, shellcmd):
      command = "shell " + shellcmd
      result = self.call_adb(command)
      return result
      
   # list packages
   def listpkg(self):
      command = "shell pm list packages"
      result = self.call_adb(command)
      return result 
      
   # search packages
   def searchpkg(self, query):
      command = "shell pm list packages | grep %s" % query
      result = self.call_adb(command)
      return result
      
   # find path for package
   def pathpkg(self, package):
      command = "shell pm path %s" % package
      result = self.call_adb(command)
      return result
   
   # pull APK from default package location
   def apkpull(self, pkgname):
      command = "pull /data/app/%s" % pkgname
      result = self.call_adb(command)
      return result
      
   # backup device   
   def backup(self, backupfile, backapk, backobb, backshared, backall, backsys):
      command = "adb backup -f %s" % backupfile
      cmdapk = " -noapk"
      cmdshared = " -noshared"
      cmdall = ""
      cmdsys = " -system"
      if "apk" in backapk:
         cmdapk = " -apk"
      else:
         cmdapk = " -noapk"
      if "obb" in backobb:
         cmdobb = " -obb"
      else:
         cmdobb = ""
      if "shared" in backshared:
         cmdshared = " -shared"
      else:
         cmdshared = " -noshared"
      if "all" in backall:
         cmdall = " -all"
      else:
         cmdall = ""
      if "sys" not in backsys:
         cmdsys = " -nosystem"
      else:
         cmdsys = " -system"
      command = 'adb backup -f ' + backupfile + cmdapk + cmdobb + cmdshared + cmdall + cmdsys
      if "full" in backall:
         command = 'adb backup -apk -shared -all -system -f ' + backupfile
      print(command)
      output = subprocess.check_call(command, shell=True, stdout=PIPE)
      return output
    
   # restore device   
   def restore(self, restorefile):
      command = "restore %s" % restorefile
      result = self.call_adb(command)
      return result
   
   # boot from image file   
   def bootimg(self, boot_file):      
      command = "boot " + boot_file
      result = self.call_fastboot(command)
      return result
   
   # install update ZIP         
   def update(self, update_file):      
      command = "update " + update_file
      result = self.call_fastboot(command)
      return result
   
   # fastboot flash image  
   def flashf(self, type, file):
      command = "flash %s %s" % (type, file)
      result = self.call_fastboot(command)
      return result
   
   # unlock bootloader 
   def unlockboot(self):
      command = "oem unlock"
      result = self.call_fastboot(command)
      return result
      
   # lock bootloader 
   def lockboot(self):
      command = "oem lock"
      result = self.call_fastboot(command)
      return result
   
   # sideload installation
   def sideload(self, file):
      command = "sideload %s" % file
      result = self.call_adb(command)
      return result
      
   # bugreport
   def bugreport(self):
      filename = "bugreport-" + str(datetime.date.today()) + ".txt"
      command = "adb bugreport > " + filename
      output = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
      response = output.communicate()
      print("bug report saved as: " + filename)
      return response
      
   # logcat
   def logcat(self):
      command = "adb logcat"
      output = Popen(command, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
      response = output.communicate()
      return response
      
   # wipe/erase partitions
   def wipe(self, parts):
      command = "-w erase"
      if 'system' in parts:
         command = "erase system"
      elif 'all' in parts:
         command = "flashall"
      elif 'data' in parts:
         command = "erase data"
      elif 'cache' in parts:
         command = "erase cache"
      elif 'boot' in parts:
         command = "erase boot"
      elif 'recovery' in parts:
         command = "erase recovery"
      elif 'flashall' in parts:
         command = "flashall"
      else:
         command = "-w erase system"
      result = self.call_fastboot(command)
      return result
      
   # services list
   def listsvc(self):
      command = "shell su -c service list"
      result = self.call_adb(command)
      return result
      
   # services search
   def searchsvc(self, query):
      command = "shell su -c service list | grep %s" % query
      result self.call_adb(command)
      return result
   
   # usb tether connect - switch = 1 enables usb tether, switch = 0 turns it off   
   def usbtether(self, switch):
      command = "shell su -c service call connectivity 34 i32 " + str(switch)
      result = self.call_adb(command)
      return result
