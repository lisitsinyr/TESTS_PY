alter session set "_ORACLE_SCRIPT"=true;

rem ��������� ������� ������������!
rem ���������� SQL*Plus � ������������� SYS ��� SYSTEM
rem CREATE USER LYR IDENTIFIED BY lyr
rem DEFAULT TABLESPACE USERS QUOTA 100M ON USERS
rem TEMPORARY TABLESPACE TEMP QUOTA 10M ON TEMP
rem /

rem ALTER USER LYR quota 10M on USERS;

CREATE USER LYR IDENTIFIED BY lyr
DEFAULT TABLESPACE USERS QUOTA 100M ON USERS
/

rem ���� ������������ ����� ��������� ������ � ��������:

GRANT CREATE SESSION TO LYR
/

rem ��������� ������������ ��������� �������� ������� ��.
rem TABLE, PROCEDURE, TRIGGER, VIEW, SEQUENCE.

GRANT CREATE TABLE TO LYR
/
GRANT CREATE PROCEDURE TO LYR
/
GRANT CREATE TRIGGER TO LYR
/
GRANT CREATE VIEW TO LYR
/
GRANT CREATE SEQUENCE TO LYR
/

rem ��������� �������� (ALTER)

GRANT ALTER ANY TABLE TO LYR
/
GRANT ALTER ANY PROCEDURE TO LYR
/
GRANT ALTER ANY TRIGGER TO LYR
/
GRANT ALTER PROFILE TO LYR
/

rem ����� �� �������� �������� ��

GRANT DELETE ANY TABLE TO LYR  
/
GRANT DROP ANY TABLE TO LYR
/
GRANT DROP ANY PROCEDURE TO LYR
/
GRANT DROP ANY TRIGGER TO LYR
/
GRANT DROP ANY VIEW TO LYR
/
GRANT DROP PROFILE TO LYR
/
