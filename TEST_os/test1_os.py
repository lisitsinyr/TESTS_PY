import sys
import os
import getpass

print(os.name,'\n') # ответ: nt
#print(sys.path,'\n')

# Password
print('\n')
pw = getpass.getpass('Enter password (ot):')
print('\n')
print('pw=',pw)
