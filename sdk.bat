@echo OFF

set OPO_HOME=%CD%
set PATH=%PATH%;%CD%;

del adb
del adb-linux
del fastboot
del fastboot-linux

icacls adb.exe /grant %USERNAME%:F
icacls Adb*.dll /grant %USERNAME%:F
icacls fastboot.exe /grant %USERNAME%:F

echo "Mini-SDK installation complete."
