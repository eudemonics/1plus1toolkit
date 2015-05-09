#!/usr/bin/env python

import os, sys

if os.name == 'nt' or sys.platform == 'win32':
   os.system('sdk.bat')

else:
   os.system('sdk.sh')

sys.exit()
