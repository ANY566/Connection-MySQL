Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import mysql.conector
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import mysql.conector
ModuleNotFoundError: No module named 'mysql.conector'
>>> import msyql.connector
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import msyql.connector
ModuleNotFoundError: No module named 'msyql'
>>> import mysql.connector
>>> connector = mysql.connector.connect(host="localhost",user="root",passwd="")
>>> 
>>> cursor = connection.cursor()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cursor = connection.cursor()
NameError: name 'connection' is not defined
>>> curso = connection.cursor()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    curso = connection.cursor()
NameError: name 'connection' is not defined
>>> cursor.execute("show detabases")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    cursor.execute("show detabases")
NameError: name 'cursor' is not defined
>>> for base in cursor:
	print(base)
    connection.close()
    
SyntaxError: unindent does not match any outer indentation level
>>> 
