LICENSE AGREEMENT & DISCLAIMER
    copyright (C) 2014  vvn <vvn@notworth.it>

    This program is FREE software: you can redistribute it and/or modify
    it as you wish. Copying and distribution of this file, with or without modification,
	are permitted in any medium without royalty provided the copyright
	notice and this notice are preserved. This program is offered AS-IS,
	WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    For more information, please refer to the "LICENSE AND NOTICE" file that should
    accompany all official download releases of this program. 

HALF-ASSED ONEPLUS ONE TOOLKIT by vvn

VERSION: 1.3.1 STABLE

RELEASE DATE: SEPTEMBER 8, 2014

GITHUB RELEASE DATE: DECEMBER 30, 2014

YEAH!!!! finally got github working with it! :)
https://github.com/eudemonics/1plus1toolkit.git

THIS VERSION IS PROBABLY BROKEN AS I AM NOT FINISHED EDITING IT.
working versions:
http://notworth.it/opo/opotoolkit.py.txt
http://notworth.it/opo/opointro.py.txt
http://notworth.it/opo/pyadb.py.txt

seriously?! there are formatting rules that totally screw up the way this file is viewed?! GRR.

this is a very half-assed project, as you might assume from the name of it, and i cannot guarantee fast or frequent updates. i will continue updating and adapting the application to support the latest official updates from both OnePlus and CyanogenMod11S, and will make every attempt to enable as much backwards-compatibility as possible. when something is NOT backwards compatible (such as re-unlocking your bootloader on firmware versions newer than XNPH25R), i will include an emphasized warning in the app itself before the command execution.
 
 REQUIREMENTS FOR SCRIPT TO WORK:
 * opotoolkit.py is the main script. that's the one file you REALLY need.
 * my PYADB library, named "pyadb.py", needs to be in the same directory as opotoolkit.py.
 * opointro.py also needs to be in the same directory as "opotoolkit.py" and "pyadb.py".
 * obviously, you'll need python 2.7. ***DO NOT RUN AS PYTHON 3.x!*** 
   - download python 2.7.x here: https://www.python.org/downloads/
 * you need ADB and FASTBOOT from the android SDK. download the SDK here: https://developer.android.com/sdk/
 * IF YOU ARE ON WINDOWS, you need the colorama module in order for the script to be viewed properly. windows doesn't support ANSI codes natively in python so you'll have to install and use the colorama module. once python 2.7 is installed, get pypi:
   - download this script and run it: https://bootstrap.pypa.io/get-pip.py
   - open command prompt as admin in script directory and type: "python get-pip.py"
   - install colorama after pypi is successfully installed: pip install colorama
   - just in case you don't install support for ANSI i spent a considerable amount of time making entirely new menus for you damn windows users (this is what opointro.py is for).
 * finally, you need an OS that supports Python and the android SDK, which I'm afraid narrows it down to:
   - Linux (all flavors) - ***IMPORTANT*** if using the included binaries, RENAME "adb-linux" and "fastboot-linux" to adb and fastboot!!!
   - Mac OSX (exotic jungle cats and beyond)
   - Windows (pretty much all releases, or starting from whichever one could support Python 2.x.)
 i apologize for limiting your options like that.
 
 you can either put the scripts and other files in the same directory as your android SDK,
 or set an environmental path variable for your android SDK directory.
  
##################################################################################
 
 SETTING UP AN ENIVIRONMENTAL PATH VARIABLE (HIGHLY RECOMMENDED):

if you're on windows you can go to my pastebin (pastebin.com/u/eudemonics), find the only powershell script on there, and steal/adapt the code to create your own environment path variable. but it's much easier to configure in system properties - i'm not on windows right now so these may not be exact instructions, but you should be able to right click on "my computer", select "properties", go to the "environment" tab in system settings, and add the environment path there. linux and OSX users just need to add the android SDK directory to their ~/.bash_profile or ~/.bashsrc or wherever environment paths are defined. if you still don't understand environmental path variables or symbolic links, i highly recommend google (or startpage.com, the private version).

if you don't want to go to the trouble of creating the environmental path variables, and you want to use the android SDK on your computer, then just extract all the files from the ZIP into your android SDK directory.

##################################################################################

HOW TO RUN THE TOOLKIT:

plug phone to computer via USB, turn on android debugging.

if you don't have "developer options" in your settings anywhere, you'll have to enable it. go to your general settings to "about phone" and tap on the build info (towards the bottom) 7 TIMES. then open "developer options" in settings and enable android USB debugging.

open command prompt or terminal window to scripts directory. start toolkit by entering:
"python opotoolkit.py"

if everything is installed and in the right places, you should see a menu like the attached screenshot. if for some reason you get a permission denied error, try launching the command prompt or terminal as administrator or superuser.

i'll continue working on it and adding more when i can so keep checking this space. everything's open source; use, share, steal whatever you want from the code. some credit would be nice, though.

you can use the pyadb.py library to incorporate adb/fastboot commands into your own python projects. i'll be adding more features to that, but for now most of the common features are covered.
 
 USE AT YOUR OWN RISK. i am not responsible for any damage to your device.
 
 i have tested every function except the unlock bootloader and sync functions.
 everything works except the uninstall APK function, but i think i just don't quite understand the adb command.
 
 to report bugs, ask questions, offer suggestions, explain the adb uninstall and sync functions(?!), bitch at me, propose marriage, or send anonymous death threats, email me: vvn (at) notworth (dot) it
 
 feel free to share, modify, whatever.
 some credit would be nice. donations are super nice. but buying & sharing my EP would be the most awesome way to show your appreciation. really, it would mean the world to me.
 
 you can stream and buy the EP at: http://dreamcorp.bandcamp.com or any major online music retailer (itunes, google play, amazon, spotify, cdbaby, etc.) - just search for "the dream corporation" and album title "last night on earth"
 follow on facebook: http://www.facebook.com/dreamcorporation
 and of course, more music on soundcloud: http://www.soundcloud.com/dreamcorp
  
##################################################################################

CHANGES IN v1.3.1:

oh dear god i don't even know where to start. will edit later.
THIS VERSION IS PROBABLY BROKEN IF YOU ARE DOWNLOADING FROM GITHUB - BEWARE!

##################################################################################
 
 CHANGES IN v1.3B:
 
 updated README. added linux binaries to zip package. updated PYADB.PY library for increased flexibility. also authored and attached a license agreement and disclaimer document. fixed function to copy files between device and computer - it works now, even added progress status. sync works too! 
 
 did i mention i hate windows? added support for ANSI colors - well, provided windows users install the colorama module. (pip install colorama) there's actually more, but i'm too lazy to provide comprehensive details.
 
##################################################################################
 
 CHANGES IN v1.2B:
 
 new SuperSU binary - we are now on v2.02! many thanks to chainfire for the development and maintenance of SuperSU. also added a 3rd rooting option using the "Superuser" zip - this is an older file that may work on older devices. or not. hey look, options!
 
 also added some more flashing options and made the sideload/install from device/fastboot options a bit more flexible instead of always following the same path.
 
 probably not even noticeable to most people, but for some reason TWRP hasn't been behaving all the time, especially with installing the SuperSU binaries for rooting. so instead of TWRP or stock recovery being the only options, i added ClockworkMod and Philz as options to whatever functions (flash and sideload) that use a custom recovery and were previously only able to use TWRP. i've tested rooting with the towelroot method on my samsung galaxy note 3 and it works perfectly, doesn't even trigger the knox 0x1 bit (as long as firmware is NE6 or earlier) and no reboot required. towelroot will not work for the oneplus one though - i tested the latest superSU (2.02) update on the OPO's latest update (33R) and it flashes successfully through Philz Recovery.
 
 developing and running the script primarily on a Macbook Pro OSX 10.8 with Python 2.7.x, though sometimes i work on it in a Linux Debian environment. i have no clue how this script will run in Python 3, i could try it and find out, but i just don't care.
 
 also new - check out the sweet ASCII art i added (even in oneplus' signature colors)! since it's the first thing you see when you run the script, you probably can't miss it. added because, obviously, it's an absolute REQUIREMENT that every terminal application (at least, the ones that matter) include some uber leet ASCII. like, the functionality doesn't even matter. handling exceptions doesn't matter (i don't do much of that here, by the way). all that matters is whether or not you have ASCII art, and how uberleet it is. otherwise, nobody will give a shit about you or your app. (at least, that's what i was told. mommy????)
 
 i tested the crap out of this with my oneplus one 64GB with the hallucinatory display (my oneplus one's display has issues with abusing psychedelics, apparently), since i'm getting a brand new warranty replacement soon. yay! i am pleased to report that none of the functions i have extensively tested in this program have caused my phone to brick or do anything where it wasn't able to boot into the system. (though if you DON'T follow instructions, you CAN brick your device. so stop being such a rebel.) i accidentally upgraded to the latest OTA (33R) and was unable to root or even boot into the TWRP image (my bootloader is unlocked but still on stock recovery), then reverted back by flashing the 30O images, then realized the problem wasn't the update but TWRP. also tested the 33R OTA update - i can confirm that's working.
 
 in a future release there will be more functionality for other phones. i plan to add a script for deodexing, and maybe if i am not too tired i'll create a stock ROM with root already injected into it.
 
 my github repository is still being a jerk and won't let me commit anything. sorry. keep checking my pastebin until then to get the latest updates:
 
 http://pastebin.com/u/eudemonics
 
 there might be some errors. i don't know. i thought i fixed the ones i came across. i really need sleep.
 
##################################################################################
 
 CHANGES IN v1.1:
 
   - most files in script can be downloaded directly from script by demand to proper location, making it an easier install and a more seamless user experience
   - added support and files for latest updates: XNPH33R released 8/22/2014, and XNPH30O updates #1 and #2
   - can now flash entire factory stock ROMs - full XNPH30O and XNPH25R stock images - or flash your own custom ROM
   - updated PYADB library to return STDOUT response instead of just a '0' success or error if not 0.
   - reboot functions should behave a bit more sanely now that the piped STDOUT response can be used as qualifiers
   - added more details and instructions in certain procedures, especially those having to do with booting into recovery.
   - several root options available now: superSU is recommended for OnePlus One. TowelRoot is recommended for Android firmware releases earlier than June 2014. I also included a "superuser" zip file which is also supposed to be for rooting, but unless you are well acquainted with what it does, which devices it supports, and what to do with it, I would advise you not to try flashing it.
   -i shuffled a lot of items around, it's very likely that there may be some syntax errors floating around. Please report any errors you come across to me at vvn (at) eudemonics (dot) org. thanks!!
   
##################################################################################
   
for the most up-to-date version of the toolkit, check my pastebin:

http://pastebin.com/u/eudemonics

##################################################################################
