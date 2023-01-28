'''
P.15 e.9

num = input("insert 2 fuigures num: ")
if int(num) < 100 and int(num) > 9:
 print(num[::-1])
else: print("only 2 figures num")
'''
'''
P.15 e.10

num = float(input("insert number: "))
int_num = int(num)
if num % 2 != 0:
 if (int_num + 1) % 2 == 0:
  print(int_num+1)
 else: print(int_num+2)
else: print(int_num)
'''
'''
P.18 e.1

num = int(input("insert num: "))
if num < 1:
    if num == 0:
        print("zero")
    else: print("negative")
else: print("positive")
'''
'''
P.18 e.2

a = int(input("first num: "))
b = int(input("second num: "))
c = int(input("third num: "))
if b>a:
   if c>b:
    print("increasing...")
'''
'''
P.18 e.3

a = int(input("first num: "))
b = int(input("second num: "))
c = int(input("third num: "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
if a==b:
    if a>c or a==c:
       print(a)
if a==c:
    if a>b:
       print(a)
if b==c:
    if b>a:
        print(b)
'''
'''
P.18 e.4

num = int(input("insert num: "))
if num >0 and num<10000:
    print(len(str(num)))
'''
'''
P.20 e.1

a = int(input("first num: "))
b = int(input("second num: "))
c = int(input("third num: "))
if a<b and a<c:
    if b<c:
        print(a,b,c)
    else: print(a,c,b)
if b<a and b<c:
    if a<c:
        print(b,a,c)
    else: print(b,c,a)
if c<a and c<b:
    if a < b:
        print(c,a,b)
    else:
        print(c,b,a)
'''
'''
P.20 e.2

grade = int(input("whats's your grade? "))
if grade > 54:
    if grade > 64:
        if grade > 74:
            if grade > 84:
                if grade > 94:
                    print("Excellent")
                else: print("very good")
            else: print("good")
        else: print("almost good")
    else: print("enough")
else: print("not enough")
'''
'''
P.20 e.4

year = int(input("insert year: "))
if (year % 4 == 0 and year % 100 > 0) or (year % 4 == 0 and year % 400 == 0):
 print(year , "was a meuberet year")
else: print(year , "was a regular year")
'''
'''
P.20 e.5

month = int(input("insert month: "))
year = int(input("insert year: "))
if month == 2:
 if (year % 4 == 0 and year % 100 > 0) or (year % 4 == 0 and year % 400 == 0):
  print("29 days")
 else: print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
 print("30 days")
else: print("31 days")
'''
sits = input("insert sits layout: ")
sits_split = sits.split(" ")
if len(sits_split) > 1:
    if len(sits_split) > 2:
        window = sits_split[0][0] ,sits_split[2][-1]
        aisle = sits_split[0][-1] ,sits_split[1][0] ,sits_split[1][-1] ,sits_split[2][0]

MATOSIM: 1
seats_layout = input("insert sits layout: ")
seats_split = seats_layout.split(" ")
if len(seats_split) > 1:
    if len(seats_split) > 2:
      print(len(seats_split[0]) , len(seats_split[1]) , len(seats_split[2]))
    else: print(len(seats_split[0]) , len(seats_split[1]))
else: print(len(seats_split[0]))

