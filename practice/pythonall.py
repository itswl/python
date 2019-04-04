from os import path
from os import listdir
import os

import sys


path=os.getcwd()+r'\FI7'
print(path)
for root,dirs,files in os.walk(path):
	for f in files:
		if os.path.splitext(f)[1]== '.py':
			os.chdir(root)
			os.system(f)
