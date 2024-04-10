"""TEST_LUFile.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     TEST_LUFile.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import datetime

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import LUFile
import LUos
import LUErrors
from LUDoc import *

def TEST_LUFile ():
    """TEST_LUFile"""
#beginfunction
    PrintInfoObject('---------TEST_LUFile----------')
    PrintInfoObject(TEST_LUFile)
    PrintInfoObject(LUFile)
#endfunction

def TEST_DirectoryExists ():
    """TEST_DirectoryExists"""
    LPath1 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU'
    LPath2 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_L'
    LPath3 = 'D:\\WORK'
#beginfunction
    PrintInfoObject('---------TEST_DirectoryExists----------')
    PrintInfoObject(TEST_DirectoryExists)

    b = LUFile.DirectoryExists (LPath1)
    s = f'Директория: {LPath1} {b}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    b = LUFile.DirectoryExists (LPath2)
    s = f'Директория: {LPath2} {b}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    b = LUFile.DirectoryExists (LPath3)
    s = f'Директория: {LPath3} {b}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_ForceDirectories ():
    """TEST_ForceDirectories"""
    LPath1 = "D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU"
#beginfunction
    PrintInfoObject('---------TEST_ForceDirectories----------')
    PrintInfoObject(TEST_ForceDirectories)

    LPath0 = LPath1 + '/1/1'
    LUFile.ForceDirectories (LPath0)
    b = LUFile.DirectoryExists (LPath0)
    s = f'Директория: {LPath0} {b}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_GetFileDateTime ():
    """TEST_GetFileDateTime"""
    #LFileName = "D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\TEST_LU.py"
    LFileName = "TEST_LU.py"
#beginfunction
    PrintInfoObject('---------TEST_GetFileDateTime----------')
    PrintInfoObject(TEST_GetFileDateTime)

    b = LUFile.FileExists (LFileName)
    s = f'Файл: {LFileName} {b}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LDateTime = LUFile.GetFileDateTime(LFileName)
    s = f'Файл: {LFileName} {LDateTime}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    s = f'Время последней записи: {LDateTime[0]} Время создания: {LDateTime[1]}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_WriteStrToFile ():
    """TEST_WriteStrToFile"""
    LStr = 'Тестовая строка'
    LFileName = "D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\TEST.txt"
#beginfunction
    PrintInfoObject('---------TEST_WriteStrToFile----------')
    PrintInfoObject(TEST_WriteStrToFile)

    LUFile.WriteStrToFile (LStr, LFileName)
#endfunction

def TEST_Extract_Get ():
    """ TEST_Extract_Get """
    LFileName0 = "1\\1\\1.txt"
#beginfunction
    PrintInfoObject('---------TEST_Extract_Get----------')
    PrintInfoObject(TEST_Extract_Get)

    s = f'Файл: {LFileName0}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    s = LUFile.ExpandFileName (LFileName0)
    s = f'Файл: {s}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LFileDir = LUFile.ExtractFileDir (s)
    s = f'FileDir: {LFileDir}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LFileName = LUFile.ExtractFileName (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LFileName = LUFile.ExtractFileNameWithoutExt (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LFileExt = LUFile.ExtractFileExt (s)
    s = f'FileExt: {LFileExt}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LFileDir = LUFile.GetFileDir (s)
    s = f'FileDir: {LFileDir}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LFileName = LUFile.GetFileName (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    LFileExt = LUFile.GetFileExt (s)
    s = f'FileExt: {LFileExt}'

    LFileName = LUFile.GetFileNameWithoutExt (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_GetFileEncoding ():
    """TEST_GetFileEncoding"""
#beginfunction
    PrintInfoObject('---------TEST_GetFileEncoding----------')
    PrintInfoObject(TEST_GetFileEncoding)


    #LFileName = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\TEST_LUsys.py'
    LFileName = 'TEST_LUsys.py'
    LEncoding = LUFile.GetFileEncoding (LFileName)
    if LEncoding == '':
        LEncoding = LUFile.cDefaultEncoding
    LFile = open (LFileName, 'r', encoding = LEncoding)
    for s in LFile:
        LULog.LoggerAPPS_AddLevel (LULog.TEXT, s[:-1])
    LFile.close()
#endfunction

def TEST_IncludeTrailingBackslash ():
    """TEST_IncludeTrailingBackslash"""
#beginfunction
    PrintInfoObject('---------TEST_IncludeTrailingBackslash----------')
    PrintInfoObject(TEST_IncludeTrailingBackslash)

    LPath1 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\'
    LPath2 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU'
    LPath11 = LUFile.IncludeTrailingBackslash(LPath1)
    LPath21 = LUFile.IncludeTrailingBackslash(LPath2)
    s = f'LPath11: {LPath11}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    s = f'LPath21: {LPath21}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_GetDirNameYYMMDD ():
    """TEST_GetDirNameYYMMDD"""
#beginfunction
    PrintInfoObject('---------TEST_GetDirNameYYMMDD----------')
    PrintInfoObject(TEST_GetDirNameYYMMDD)

    LPath1 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\'
    LPath2 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU'
    LNow: datetime = datetime.datetime.now()
    LDirNameYYMMDD1: str = LUFile.GetDirNameYYMMDD(LPath1, LNow)
    LDirNameYYMMDD2: str = LUFile.GetDirNameYYMMDD(LPath2, LNow)
    s = f'LDirNameYYMMDD1: {LDirNameYYMMDD1}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    s = f'LDirNameYYMMDD2: {LDirNameYYMMDD2}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_GetDirNameYYMM ():
    """TEST_GetDirNameYYMM"""
#beginfunction
    PrintInfoObject('---------TEST_GetDirNameYYMM----------')
    PrintInfoObject(TEST_GetDirNameYYMM)

    LPath1 = r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\TEST_LU\\'
    LPath2 = r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\TEST_LU'
    LNow: datetime = datetime.datetime.now()
    LDirNameYYMM1: str = LUFile.GetDirNameYYMM(LPath1, LNow)
    LDirNameYYMM2: str = LUFile.GetDirNameYYMM(LPath2, LNow)
    s = f'LDirNameYYMMDD1: {LDirNameYYMM1}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    s  = f'LDirNameYYMMDD2: {LDirNameYYMM2}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_GetTempDir ():
    """TEST_GetTempDir"""
#beginfunction
    PrintInfoObject('---------TEST_GetTempDir----------')
    PrintInfoObject(TEST_GetTempDir)

    LTempDir: str = LUFile.GetTempDir()
    s = f'LTempDir: {LTempDir}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_SearchFile ():
    """TEST_SearchFile"""
#beginfunction
    PrintInfoObject('---------TEST_SearchFile----------')
    PrintInfoObject(TEST_SearchFile)

    LFileName = 'TEST_LUFile.py'
    LFullFileName = LUFile.SearchFile(LFileName,'.py')
    s = f'FullFileName: {LFullFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_SearchINIFile ():
    """TEST_SearchINIFile"""
#beginfunction
    PrintInfoObject('---------TEST_SearchINIFile----------')
    PrintInfoObject(TEST_SearchINIFile)

    LFileName = 'TEST_LU.ini'
    LFullFileName = LUFile.SearchFile(LFileName,'.ini')
    s = f'FullFileName: {LFullFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_SearchEXEFile ():
    """TEST_SearchINIFile"""
#beginfunction
    PrintInfoObject('---------TEST_SearchEXEFile----------')
    PrintInfoObject(TEST_SearchEXEFile)

    LFileName = 'python.exe'
    LFullFileName = LUFile.SearchFile(LFileName,'.exe')
    s = f'FullFileName: {LFullFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

def TEST_FileSearch ():
    """TEST_FileSearch"""
#beginfunction
    PrintInfoObject('---------TEST_FileSearch----------')
    PrintInfoObject(TEST_FileSearch)

    LFileName = 'python.exe'
    LFileName = 'notepad.exe'
    LFileName = 'TEST_LU.ini'
    LWinDir = LUos.GetEnvVar ('WinDir')
    LPath = LUos.GetCurrentDir() + ';' + LWinDir
    LFullFileName = LUFile.FileSearch (LFileName, LPath)
    s = f'FullFileName: {LFullFileName}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging ('LOG', 'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')

    TEST_DirectoryExists ()
    TEST_ForceDirectories ()
    TEST_GetFileDateTime ()

    try:
        TEST_WriteStrToFile ()
    except LUErrors.LUFileError_FileERROR as ERROR:
        ERROR.Message = 'Тестовое сообщение'
        s = f'!!!! {ERROR}'
        LULog.LoggerAPPS_AddError(s)
    else:
        ...
    #endtry

    TEST_Extract_Get ()
    TEST_GetFileEncoding ()
    TEST_IncludeTrailingBackslash ()
    TEST_GetDirNameYYMMDD ()
    TEST_GetDirNameYYMM ()
    TEST_GetTempDir ()
    TEST_SearchFile ()
    TEST_SearchINIFile ()
    TEST_SearchEXEFile ()
    TEST_FileSearch ()
    ...
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule