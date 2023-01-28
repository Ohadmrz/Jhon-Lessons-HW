#
# l = [['Paris', 'London', 'New York'], [45, True, 5.5, 'hello'], -3,[5, ['#', '$', '%', '^', [10, 20, 30, 40]]],
# [['a'], ['b'], 'c', [['d']]]]
# print(l[2])
# print(l[1][2])
# print(l[0][::-1])
# print(l[1:3])
# print(l[3][1][3])
# print(l[4][0][0])
# print(l[4][1])
# print(l[4][3][0][0])
# print(l[3][1][4][1:4:2])
# print(l[3][1][-2::-3])

# #
# # def yalla(the_dic:dict) -> list:
# #     my_dic = {}
# #     for subject, grade_list in (the_dic).items():
# #         my_dic[subject] = {}
# #     return my_dic
# #
# # the_dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# # result = yalla(the_dic)
# # print(result)
# # #the_dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# #
# #
# # for i in range(0,len(the_dic[key])):
# #     my_dic[key] =
#
#
# #
# #
# #
# #
# # the_dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# #
# # my_list = []
# # my_dic = {}
# # for subject, grades_list in the_dic.items():
# #     for grade in grades_list:
# #         #print(grade)
# #         my_dic[subject] = grade
# #
# #         #print(my_dic)
# #         my_list.append(my_dic)
# #         my_dic.pop(subject[])
# #     print(my_list)
# #
# # #print(my_list)
# #
# #
# #
# # #
# # #
# # # the_dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# # #
# # # my_list = []
# # # my_dic = {}
# # # for subject, grades_list in the_dic.items():
# # #     for grade in grades_list:
# # #         #print(grade)
# # #         my_dic[subject] = grade
# # #         #print(my_dic)
# # #     my_list.append(my_dic)
# # #     print(my_list)
# # #
# # # #print(my_list)
# # #
# # #
# #
# # the_dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# #
# # my_list = []
# # my_dic = {}
# # for subject, grades_list in the_dic.items():
# #     for grade in grades_list:
# #         #print(grade)
# #         my_dic[subject] = grade
# #         #print(my_dic)
# #         my_list.append(my_dic)
# #     print(my_list)
# #
# # #print(my_list)
# # #
# #
# #
# # the_dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# #
# # my_list = []
# # my_dic = {}
# # a = 0
# # for left,right in the_dic.items():
# #     for l in right:
# #         while a< len(right):print(my_list)
# # print(my_dic)
# #
# #
# # #
# # #
# # #
# #
#
#
# the_dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#
# my_list = []
# my_dic = {}
# my_dicc = {}
# a=0
# while a<5:
#     for subject, grades_list in the_dic.items():
#         for index,grade in enumerate(grades_list):
#             print(subject)
#             print(grades_list)
#             if subject in my_dic:
#                 my_dic.pop(subject)
#                 my_dic[subject] = grade
#                 my_list.append(my_dic)
#             else:
#                 my_dic[subject] = grade
#                 my_list.append(my_dic)
#     break
#         #   my_dic[subject]=grades_list[index]
#          #   my_list.append(my_dic) break
# #print(subject)
# #print(grades_list)
# print(my_dic)
# print(my_list)
#         #print(f'{subject}:{grade}')
#         # a=0
#         # while a< 5:
#         #
#         #  if subject not in my_dic:
#         #     my_dic[subject] = grades_list[a]
#         #     my_list.append(my_dic)
#         #     a+=1
#         #  else: print(f'{my_dic}\n{my_list}')
#         #  a+=1
#         #    # my_dic[subject].append(grade)
#         #print(grade)
#         #my_dic[subject]= grade
#         #print(my_dic)
#        # my_list.append(my_dic)
# #print(my_list)
#
#
# #print(my_list)
#
import pickle


student = {
    'name': 'David',
    'city': 'Tel Aviv',
    'grades': {'math':[98, 87, 90],
               'english': [85]
               }
}
with open('test.pckl', 'wb') as fh:
    pickle.dump(student, fh)


with open('test.pckl', 'rb') as fh:
    my_data = pickle.load(fh)

print(my_data)


class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades


s = Student('a', 'b', [90])
print(s.__dict__)