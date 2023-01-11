#=======================================================================================
# TEST_LUStrings.py
#=======================================================================================

#------------------------------------------
# БИБЛИОТЕКИ python 
#------------------------------------------
import sys

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
PYDir: str = 'D:\\PROJECTS\\!TOOLS\\TOOLS_PY\\PY'
sys.path.append (PYDir)
print (PYDir)
import LUStrings
#------------------------------------------
#beginmodule

# AddChar (Pad, Input, Length):
print ('-------------------------------')
print ('AddCharLU (Pad, Input, Length):')
String = 'Input'
print ('String='+String)
String = LUStrings.AddChar ('.', String, 20)
print ('String='+String)

# AddCharR (Pad, Input, Length):
print ('-------------------------------')
print ('AddCharR (Pad, Input, Length):')
String = 'Input'
print ('String='+String)
String = LUStrings.AddCharR ('.', String, 20)
print ('String='+String)

# ExtractWord (i, String, Delimiter):
print ('-------------------------------')
print ('ExtractWord (i, String, Delimiter):')
String = 'один,два,три'
print ('String='+String)
String = LUStrings.ExtractWord (2, String, ',')
String = String.strip (' ')
print ('String='+String)

# WordCount (String, Delimiter):
print ('-------------------------------')
print ('WordCount (String, Delimiter):')
String = 'один,два,три'
print ('String='+String)
Num = LUStrings.WordCount (String, ',')
print ('Num=', Num)

# ExistWord (String, Delimiter, Word):
print ('-------------------------------')
print ('ExistWord (String, Delimiter, Word):')
String = 'один,два,три'
print ('String='+String)
Bool = LUStrings.ExistWord (String, ',', 'два')
print ('Bool=',Bool)
print ('-------------------------------')

#endmodule
