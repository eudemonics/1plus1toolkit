#!/usr/bin/env python
### PYADB (Python 2.7 Library)
##### VERSION: 1.3.666 BETA
##### RELEASE DATE: AUGUST 22, 2015
##### AUTHOR: vvn <lost [at] nobody [dot] ninja>
##### DESCRIPTION: simple library to port ADB and FASTBOOT functions to PYTHON
#####
##### for now it's a required companion to the 'half-assed one plus one toolkit'.
##### this project is vaguely based on some github code i found that had too many errors.
##### i know it isn't anything new. i know it's probably been done better.
##### but i wanted one that worked for me. if it works for you, go ahead and use it too!
##################################################
##################################################
##### USER LICENSE AGREEMENT & DISCLAIMER
##### copyright, copyleft (C) 2014-2015  vvn <lost [at] nobody [dot] ninja>
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
##### lost [at] nobody [dot] ninja
##### latest version will always be available HERE:
##### https://github.com/eudemonics/opotoolkit
##### there be only code after this -->

import os, subprocess, sys, datetime, shlex
from subprocess import call, Popen, PIPE, STDOUT

class pyADB(object):

   # adb commands
   
   def call_adb(self, command):
      response = ''
      rawcmd = r'%s' % command
      command_text = 'adb %r' % rawcmd
      command_text = r'"%s"' % command_text
      command_text = command_text + '; exit 0'
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      output = subprocess.check_call(command_text, shell=True, stderr=subprocess.STDOUT)
      return output
      response = output.communicate()[0]
      return response

   # fastboot commands
   def call_fastboot(self, command):
      response = ''
      command_text = 'fastboot %s' % command
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response, errors = output.communicate()[0]
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
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response = output.communicate()[0]
      return response or None
   
      result = self.call_adb(command_text)
      devices = result.partition('\n')[2].replace('\n', '').split('\tdevice')
      return [device for device in devices if len(device) > 2]
      return result

   # fastboot return list of devices
   def fastboot_devices(self):
      command_text = 'fastboot devices'
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response, errors = output.communicate()[0]
      return response
      # command = "devices -l"
      # result = self.call_adb(command)   
      # return result   

   # get device state
   def get_state(self):
      results = ''
      command_text = 'adb get-state'
      output = Popen(command_text, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response = output.communicate()[0]
      return response or None
      #result = self.call_adb("get-state")
      #return result or None

   # install APK
   def install(self, path_to_app):
      command = "install %s" % path_to_app
      result = self.call_adb(command)
      return result

   # uninstall APK
   def uninstall(self, path_to_app, *args):
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
   
   # root shell command
   def rootshell(self, shellcmd):
      command = "shell su && " + shellcmd
      result = self.call_adb(command)
      return result
         
   # list packages
   def listpkg(self):
      cmd = 'adb shell pm list packages -f | sed -ne "s/package://p"'
      output = Popen(cmd, stdin = PIPE, stdout = PIPE, stderr = PIPE) % cmd1
      response = output.communicate()[0]
      return response
      
   # search packages
   def searchpkg(self, query):
      cmd1 = 'adb shell pm list packages -f | grep %s | sed -ne "s/package://p"' % query
      output = Popen(cmd1, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response = output.communicate()[0]
      response = filter(None, response)
      return response or None
      
   # find path for package
   def pathpkg(self, package):
      cmd = 'adb shell pm list packages -f %s | sed -ne "s/package://p"' % package
      output = Popen(cmd, shell=True, stdin = PIPE, stdout = PIPE, stderr = STDOUT)
      resp = output.communicate()[0]
      response = resp.split('=')[0]
      return response
   
   def pullapk(self, pkgname):
      cmd = "adb shell pm list packages -f %s" % pkgname
      com1 = Popen(cmd, shell=True, stdin = PIPE, stdout = PIPE, stderr = STDOUT)
      path = com1.communicate()[0]
      pathresult = path.split('=')[0]
      pathresult = pathresult.strip('package:')
      pkgpath = str(pathresult)
      command = "adb pull -p %s" % pkgpath
      output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response = output.communicate()[0]
      return response
   
   # pull APK from package location on device
   def apkpull(self, pkgname):
      com1 = "adb shell pm list packages -f %s | sed -ne 's/package://;s/=.*$//p'"
      packages = []
      output = Popen(com1, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      for o in output:
         pkg1 = o.rsplit("=")[0]
         pkg = pkg1.split(":")[1]
         packages.append(pkg)
      response = []
      for package in packages:
         command = "adb pull -p " + r'"%s"' % package
         output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
         response.append(output.communicate()[0])
      return response
      
   def defaultapkpull(self, package):
      command = "adb pull -p %s" % package
      output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response = output.communicate()[0]
      return response
   
   def getfeatures(self):
      command = "shell pm list features"
      result = self.call_adb(command)
      return result
      
   def getallpermissions(self):
      command = "shell pm list permissions -g -f"
      result = self.call_adb(command)
      return result
   
   def getpermissions(self, package):
      command = "adb shell pm list permissions -g -f | grep -A 4 %s" % package
      output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response = output.communicate()
      return response
   
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
      output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response = output.communicate()
      print("bug report saved as: " + filename)
      return response
      
   # logcat
   def logcat(self):
      command = "adb logcat"
      output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
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
      command = "shell service list"
      result = self.call_adb(command)
      return result
      
   # services search
   def searchsvc(self, query):
      command = "shell service list | grep %s" % query
      result = self.call_adb(command)
      return result
      
   # get usb modes from getprop
   def usbpropcheck(self):
      command = "shell getprop sys.usb.state"
      result = self.call_adb(command)
      return result
   
   # get DNS servers from getprop
   def getdns(self):
      command = "adb shell getprop net.dns1 && adb shell getprop net.dns2"
      output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response, errors = output.communicate()
      return response or None
      
   # set DNS servers using setprop
   def setdns(self, dns1, *args):
      command = "adb shell su -c setprop net.dns1 %s" % dns1
      if args:
         i = 2
         lim = len(args) + 2
         for arg in args:
            while i < lim:
               command = command + " && adb shell su -c setprop net.dns" + str(i) + " %s" % arg
               i += 1
            if i >= lim:
               break
      output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
      response, errors = output.communicate()
      return response
   
   # usb tether connect - switch = 1 enables usb tether, switch = 0 turns it off   
   def usbtether(self, switch):
      command = "shell su -c service call connectivity 34 i32 " + str(switch)
      result = self.call_adb(command)
      return result
      
   # enable wifi debugging - requires root - not tested!
   def wifidebug(self, switch): # switch 1 enables wifi debugging, 0 or 2 disables
      cmd = "adb shell su -c ifconfig wlan0 | sed -ne 's/^.*ip //;s/ mask.*$//p'"
      ipaddr = os.system(cmd)
      commands = []
      wifioff = "sed -i 's/5555/-1/g' wifidebug.sh"
      wifion = "sed -i 's/-1/5555/g' wifidebug.sh"
      if switch == '1':
         commands = "adb shell su -c mount -o rw,remount /data","adb push wifidebug.sh /data/data","adb shell su -c chmod 0775 /data/data/wifidebug.sh","adb shell su -c sh /data/data/wifidebug.sh","adb kill-server","adb start-server","adb connect " + r'"%s"' % ipaddr
      else:
         commands = wifioff,"adb shell su -c mount -o rw,remount /data","adb push wifidebug.sh /data","adb shell su -c chmod 0775 /data/wifidebug.sh","adb shell su -c sh /data/wifidebug.sh","adb disconnect localhost",wifion
      response = []
      for command in commands:
         output = Popen(command, shell=True, stdout=PIPE, stderr=STDOUT, stdin=PIPE)
         result = output.communicate()
         response.append(result)
      return response

   def launchdrozer(self):
      cmd = "adb install drozer.apk"
      os.system(cmd)
      command = "adb shell am broadcast -n com.mwr.dz/.receivers.Receiver -c com.mwr.dz.START_EMBEDDED"
      command2 = "adb shell su am startservice -n com.mwr.dz/.services.ServerService -c com.mwr.dz.START_EMBEDDED"
      command3 = "adb shell am start -n com.mwr.dz/.activities.MainActivity && adb shell input tap 1240 720"
      
