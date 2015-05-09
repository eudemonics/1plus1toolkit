#!/bin/bash

# chmod +x sdk.sh to make the script executable
# run with sh sdk.sh or ./sdk.sh
# *NIX AWARE ONLY - do not try to execute in a MS-DOS command prompt!
# If run in Cygwin, removes *nix files
# If run in Linux or OS X:
#   removes Windows files
#   sets access for files needed
#   removes mac or linux files as needed
#   creates softlinks to the actual files
#   adds current directory to $PATH

# by vvn for the HALF-ASSED ONEPLUS ONE TOOLKIT

platform=`uname -s`
here=`pwd | sed 's/ /\\\ /g'`

if [[ "$platform" =~ "CYGWIN"* ]] ; then
  rm -f adb adb-linux fastboot fastboot-linux
else
  rm -f adb.exe Adb*.dll fastboot.exe
  if [[ "$platform" =~ "Darwin"* ]] ; then
    rm -f adb-linux fastboot-linux
    chmod 755 adb fastboot
    PROF=$HOME/.bash_profile
  else
    rm -f adb fastboot
    chmod 755 adb-linux fastboot-linux
    mv adb-linux adb
    mv fastboot-linux fastboot
    PROF=$HOME/.bash_profile
  fi
  i=`which adb`
  if [[ -z "$i" ]] ; then
    if [[ -e $PROF  ]] ; then
      fgrep "$here" $PROF | sed 's/^.*://' | sed 's/:.*$//' > sdk.tmp
      i=`fgrep -x "$here" sdk.tmp`
      rm -f sdk.tmp
      if [[ ! -z "$i" ]] ; then
        echo "Mini-SDK already in profile, installation complete."
        exit
      fi
    fi
    echo export PATH='$PATH':$here >> $PROF
    echo "Mini-SDK installation complete."
  else
    echo "Mini-SDK already in path, installation complete."
  fi
fi
echo "To run toolkit, enter: python opotoolkit.py"
