#=======================================================================================
# TEST_LU_sys.py
#=======================================================================================

#------------------------------------------
# БИБЛИОТЕКИ python 
#------------------------------------------
import os
import sys

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
#PYDir = 'D:\\PROJECTS\\!TOOLS\\TOOLS_PY\\PY'
#sys.path.append (PYDir)
#import LU_sys
#------------------------------------------
def main ():
    print('os.name->',os.name) # ответ: nt
    print("os.environ['PYTHONPATH']->", os.environ['PYTHONPATH'])
    print("sys.path->", sys.path)

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
