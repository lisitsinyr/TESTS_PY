#=======================================================================================
# CompoundStatements_04_08.py
#=======================================================================================

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
#import os
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ
#------------------------------------------
#
#------------------------------------------

#------------------------------------------
# ОПРЕДЕЛЕНИЯ
#------------------------------------------
#Test = ""

#------------------------------------------------------------
# 8.1. The if statement
#------------------------------------------------------------
# if_stmt ::=  "if" assignment_expression ":" suite
#              ("elif" assignment_expression ":" suite)*
#              ["else" ":" suite]
#------------------------------------------------------------
def The_if_statement_04_08_01():
#beginfunction
    print ("=========================")
    print ("04_08_01 The if statement")
    print ("=========================")
    a = 1
    b = 2
    c = 1
    d = 2
    if (a == b):
        print (a, b)
    elif (c == d):
        print (c, d)
    elif (c != d):
        print (a, b)
    else:
        print (a, b, c, d)
    #endif
#endfunction
        
#------------------------------------------------------------
# 8.2. The while statement¶
# while_stmt ::=  "while" assignment_expression ":" suite
#                ["else" ":" suite]
#------------------------------------------------------------
def The_while_statement_04_08_02():
#beginfunction
    print ("============================")
    print ("04_08_02 The_while_statement")
    print ("============================")
    i = 1
    while (i < 10):
        print (i)
        i = i + 1
    else:
        ...
        #print ("else:",i)
    #endwhile
#endfunction

#------------------------------------------------------------
# 8.3. The for statement
# for_stmt ::=  "for" target_list "in" starred_list ":" suite
#              ["else" ":" suite]
#------------------------------------------------------------
# range(stop);
# range(start, stop);
# range(start, stop, step).
#------------------------------------------------------------
# break
# continue
#------------------------------------------------------------
#else
#else напрямую связана с оператором break и выполняется лишь тогда,
# когда выход из цикла был произведен НЕ через break
#---------------------------------------------------------------
def The_for_statement_04_08_03():
#beginfunction
    print ("==========================")
    print ("04_08_03 The_for_statement")
    print ("==========================")
    for i in range (1,10+1,1):
    #for i in enumerate(1, start=1):
        print (i)
    else:
        print ("else:",i)
        #SUITE
    #endfor
#endfunction

def TEST_CompoundStatements(ATest):
#beginfunction
    match ATest:
        case '04_08_01':
            The_if_statement_04_08_01()
        case '04_08_02':
            The_while_statement_04_08_02()
        case '04_08_03':
            The_for_statement_04_08_03()
        case _:
            print ("Тест не разработан...")
            ...
    #endmatch
#endfunction

#beginmodule
#endmodule
#------------------------------------------
