"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     PATTERNS_PY
     Python (PROJECTS_PY)
 Module:
     ListDir.py

 =======================================================
"""
#------------------------------------------
#БИБЛИОТЕКИ
#------------------------------------------
import argparse
import datetime

#------------------------------------------
#БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import platform

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
GMask: str = ".*"
GFile: str = ""
GDir: str = ""
GShablon: str = ""
GFormat: int = 0

#------------------------------------------
DirName: str = ""
Shablon: str = ""
Shablon0: str = 'call arjd.bat \"{DirName}\"'
Shablon1: str = "{FullFileDir} {FileName} {FileTime} {FileSize}"
Shablon2: str = "{FileName={FullFileName}|{FullFileDir}|{FileDir}"
#------------------------------------------

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
    LBaseName = os.path.basename (ADir)
    if GShablon == Shablon0:
        message = GShablon.format (DirName = LBaseName)
        print (message)
    #endif
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
def FuncFile (AFileName: str):
    """FuncFile"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, AFile.path)
    Lstat = os.stat (AFileName)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
#endfunction

#------------------------------------------
# 
#------------------------------------------
def main():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    LUDoc.PrintInfoObject('-----main----')
    LUDoc.PrintInfoObject(main)

    global GDir
    global GLog
    global GShablon

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    GFormat = LUParserARG.GetParam ('Format', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'Format = {GFormat}')
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    # Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    # Lparser.add_argument ('Format', type = int, default=1, dest = 'Format', help = 'Номер шаблона')
    # # Lparser.add_argument ('-Format', type = int, nargs = '?', default = 1, dest = 'Format', help = 'Номер шаблона')
    # Largs = Lparser.parse_args ()
    # GFormat = Largs.Format
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'Format = {GFormat}')
    #----------------------------------------------------------------

    match GFormat:
        case 1:
            GFile = 'sfile.ini'
            GShablon = Shablon1
        case 2:
            GFile = 'sfile.ini'
            GShablon = Shablon2
        case _:
            GFile = 'sdir.bat'
            GShablon = Shablon0
    #endmatch
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'GFile = {GFile}')
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'GShablon = {GShablon}')
    
    GDir = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'GDir = {GDir}')

    _Option = 0
    _OutFile = 'DirFiles.txt'
    _OutFile = 'CONSOLE'
    # LUFile.FileDelete (_OutFile)

    LUFileUtils.__ListDir (GDir, '.*', False, '', _OutFile, _Option, FuncDir, FuncFile)
#endfunction

#------------------------------------------
# 
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
