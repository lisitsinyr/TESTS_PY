"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     DelFiles.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime
import logging
import argparse
import platform

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LUConsole
import LUConst
import LUDateTime
import LUDecotators
import LUDict
import LUErrors
import LUFile
import LUFileUtils
import LULog
import LUObjects
import LUObjectsYT
import LUos
import LUParserARG
import LUParserINI
import LUProc
import LUQThread
import LUQTimer
import LUSheduler
import LUStrDecode
import LUStrUtils
import LUSupport
import LUsys
import LUThread
import LUYouTube
import LUDoc

if platform.system() == 'Windows':
    import LUNetwork
    import LUNumUtils
    import LUTimer
    import LUVersion
    import LUParserREG
#endif

#------------------------------------------
#CONST
#------------------------------------------
GDir = ''
GMask = ''
GDays = 100

#------------------------------------------
# FuncDir ()
#------------------------------------------
def FuncDir (ADir: str):
    """FuncDir"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, ADir.path)
    Lstat = os.stat(ADir)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    ...
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
def FuncFile (AFile: str):
    """FuncFile"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, AFile.path)
    Lstat = os.stat(AFile)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    ...
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    LUDoc.PrintInfoObject('-----main----')
    LUDoc.PrintInfoObject(main)

    global GDir
    global GMask
    global GDays

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    GDir = LUParserARG.GetParam ('PDir', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GMask = LUParserARG.GetParam ('PMask', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    GDays = LUParserARG.GetParam ('GDays', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GDays}')
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    Lparser.add_argument ('PDays', type = int, default=100, help = 'PDays')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    # Lparser.add_argument ('-PDays', type = int, nargs = '?', default = 100, dest = 'PDays', help = 'PDays')
    Largs = Lparser.parse_args ()
    GDir = Largs.PDir
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GMask = Largs.PMask
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    GDays = Largs.PDays
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'Pdays = {GDays}')

    GDir = 'D:\\WORK\\TESTS_PY'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GMask = '.*'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    GDays = 100
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'Pdays = {GDays}')

    _OutFile = 'DelFiles.txt'
    _OutFile = 'CONSOLE'
    # LUFile.FileDelete (_OutFile)

    # LUFileUtils.DelFiles(GDir, GMask, True, _OutFile, 1, GDays)

    LULog.STOPLogging ()
#endfunction

#------------------------------------------
# DelFiles
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
