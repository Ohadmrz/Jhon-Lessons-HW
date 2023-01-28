'''
Q.1

list = [10,20,30,40,50,60,70,80,90,100]
for i, num in enumerate(list):
    if i%2!=0:
        print(num)
'''
'''
Q.2

cities = ['New york','Kyiv','Paris']
countries = ['USA','Ukraine','France']
for i in range(len(cities)-1,-1,-1):
    print(f"{countries[i]}-{cities[i]}")
'''''
'''''
Q.3

names = ['moti','ohad','faloop']
for name in names:
     print(f"Dr. {name}")
'''
''''
Q.4
str/int/float/list
'''
''''
Q.5
second-largest numbers
'''
'''
nums = [54, -1, 45, 987, 5, 2, 65, 7, 12]
max_num = max(nums[0:2])
second_max = min(nums[0:2])
# max_num = nums[0]
# second_max = nums[1]
for num in nums:
    if num < second_max:
        continue
    if second_max < num < max_num:
        second_max = num
    if num > max_num:
        second_max = max_num
        max_num = num
print(second_max)
print(max_num)
'''
'''
Q.6
'''
'''
rows = int(input("insert number of rows: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print('\n', end='')

'''
rows = int(input("insert wave lengh: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print('\n', end='')
for i in range(rows,1,-1):
    for j in range(1, i):
        print(j, end=" ")
    print('\n', end='')



# goods = [['apple', 'pear', 'peach', 'chery' ],
# ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
#     'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry' ]]
# for team in goods:
#     for word in team:
#         a = int(len(word))
#         print(max(a))






