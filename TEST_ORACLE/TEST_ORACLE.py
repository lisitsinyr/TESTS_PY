# Template_main_01.py
#=======================================================================================

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import argparse
import datetime
import getpass
import oracledb

#------------------------------------------
#БИБЛИОТЕКА LU
#------------------------------------------
import LUConst
import LUStrings
import LUSupport
#------------------------------------------

#------------------------------------------
# Разбор аргументов
#------------------------------------------
parser = argparse.ArgumentParser(description='Параметры')
parser.add_argument('-P1', type=str, nargs='?', default='', dest='P1', help='P1')
args = parser.parse_args()
print('-P1 =',args.P1)
#------------------------------------------
#------------------------------------------
P1: str = ''
if args.P1 != '':
    P1 = args.P1
#endif
#------------------------------------------

#-------------------------------------------------------------------------------
# Template (A1: str, A2: str): -> str
#-------------------------------------------------------------------------------
def Template (A1: str, A2: str):
#beginfunction
    pass
#endfunction

#------------------------------------------
# main():
#------------------------------------------
def main():
#beginfunction
    # Password
    #pw = getpass.getpass ("Enter password (ot): ")

    connection = oracledb.connect(user='ot',
                              password='OT',
                              dsn='localhost/orcl')

    print ("Successfully connected to Oracle Database")
    cursor = connection.cursor ()

    # Drop table
    DropTable = """
        begin
            execute immediate 'drop table todoitem';
            exception when others then if sqlcode <> -942 then raise; end if;
        end;"""
    print (DropTable)
    cursor.execute (DropTable)

    # Create table
    CreateTable = """
        create table todoitem (
            id number generated always as identity,
            description varchar2(4000),
            creation_ts timestamp with time zone default current_timestamp,
            done number(1,0),
            primary key (id))"""
    print (CreateTable)
    cursor.execute (CreateTable)

    # Insert some data
    rows = [("Task 1", 0),
        ("Task 2", 0),
        ("Task 3", 1),
        ("Task 4", 0),
        ("Task 5", 1)]
    cursor.executemany ("insert into todoitem (description, done) values(:1, :2)", rows)
    print (cursor.rowcount, "Rows Inserted")

    connection.commit ()

    # Now query the rows back
    for row in cursor.execute ('select description, done from todoitem'):
        if row [1]:
            print (row [0], "is done")
        else:
            print (row [0], "is NOT done")
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule















