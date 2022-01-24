#ASSIGNMENT2
#--------------------------------------
#Q1
statement = "Python is a case sensitive language"
#a)
print(len(statement))
#b)
print(statement[::-1])
#c)
print(statement[10:26])
#d)
print(statement.replace("a case sensitive","object oriented"))
#e)
print(statement.find("a"))
#f)
print(statement.replace(" ",""))
#___________________________________________________________________________________
#Q2
NAME='ARSH SHARMA'
SID='21103057'
DEPARTMENT='COMPUTER SCIENCE'
CGPA='9.9'
print(f'''Hey, {NAME} Here!
My SID is {SID}
I am from {DEPARTMENT} department and my CGPA IS {CGPA}''')
#_____________________________________________________________________________________
#Q3
a=56
b=10
#a)
print(a&b)
#b)
print(a|b)
#c)
print(a^b)
#d)
a=a<<2
b=b<<2
#e)
a=a>>2
b=b>>4
#_________________________________________________________________________________________
#Q4
print('Enter three numbers:')
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
if (a>b):
    if(a>c):
     print('The greatest number is a:',a)
    else:
       print('The greatest number is c: ',c)
else:
    if (b>c):
       print('The greatest number is b:',b)
    else:  
      print ('The greatest number is c:',c)
#______________________________________________________________________________________________
#Q5
Statement=str(input('Enter a statement: '))
if 'name' in statement:
 print('YES')
else:
 print('NO')
#python is a case sensitive language, so anything written other than 'name' would be given a no.
#____________________________________________________________________________________________
#Q6
lenght1 = int(input('lenght of first side: '))
lenght2 = int(input('lenght of second side: '))
lenght3 = int(input('lenght of third side: '))
if lenght1+lenght2>lenght3 and lenght2+lenght3>lenght1 and lenght3+lenght1>lenght2:
  print('yes')
else:
 print('no')
