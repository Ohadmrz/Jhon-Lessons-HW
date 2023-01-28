# # Base class / parent class
import datetime

# class Person:
#
#     def __init__(self, first_name: str, last_name: str, address: str,
#                  email: str, bdate: datetime.date):
#         self.__first_name = first_name
#         self.__last_name = last_name
#         self.__address = address
#         self.__email = email
#         self.__birth_date: datetime.date = bdate
#
#         # p1 = Person("Valeria", "Aynbinder", "NETANYA",
#         #             "valeria@gmail.com", datetime.date(year=1987, month=2, day=11))
#
#     def get_full_name(self):
#         return f"{self.__first_name} {self.__last_name}"
#
#     def get_address(self):
#         return self.__address
#
#     def get_email(self):
#         return self.__email
#
#     def get_birth_date(self) -> datetime.date:
#         return self.__birth_date
#
#     def get_age(self):
#         return datetime.date.today().year - self.__birth_date.year
#
#     def __str__(self):
#         return f"{self.get_full_name()}, " \
#                f"lives at {self.get_address()}, " \
#                f"{self.get_age()} years old"
#
#     def __repr__(self):
#         return self.__str__()
#
#     # def __repr__(self):
#     #     return self.get_full_name()
#
# ########################################################################################################
# # Derived / child class
# class Student(Person):
#
#     # remove one param for student
#     # add extra param
#
#     def __init__(self, first_name: str, last_name: str, address: str,
#                  email: str, bdate: datetime.date, course_name: str):
#
#         super().__init__(first_name, last_name, address, email, bdate)
#         self.__course = course_name
#         self.__grades = []
#
#         # s1 = Student("Daniel", "Sh", "Ashdod",
#         #              "daniel@gmail.com", datetime.date(year=2002, month=11, day=5),
#         #              "python full stack")
#
#     def add_grade(self, grade):
#         self.__grades.append(grade)
#
#     def get_avg_grade(self):
#         return sum(self.__grades) / len(self.__grades)
#
#     def __str__(self):
#         return f"Student: {super().__str__()}"
#
#     # tal@gmail.com -> tal@jb.com
#     #["tal", "gmail.com"]
#     def get_student_email(self):
#         return super().get_email().split("@")[0] + "@jb.com"
#
#     # def test(self):
#     #     own_str = self.__str__()
#     #     parent_str = super().__str__()
#     #     return own_str, parent_str
#
#     # if no init - will inherit from the parent
#     #     self.study_year = study_year
#     #     self.grades = []
#
#     # def get_best_grade(self):
#     #     return max(self.grades)
#     #
#     # def __str__(self):
#     #     return f"Student {super().__str__()}, starts studying at {self.study_year}"
# #
# ############################################################################################################
# # # Derived / child class
# class Lecturer(Person):
#
#     # if no init - will inherit from the parent
#     def __init__(self, first_name: str, last_name: str, address: str, email: str,
#                  bdate: datetime.date, salary_per_hour: int):
#         super().__init__(first_name, last_name, address, email, bdate)
#         # self.__salary = salary_per_hour
#         self._salary = salary_per_hour
#
#     def get_salary_per_hour(self):
#         return self._salary
#
#     def get_salary_per_course(self, course_hours):
#         return self._salary * course_hours + 1000
#
#     def __str__(self):
#         return f"Lecturer {super().__str__()}"
#
# ############################################################################################################
# ############################
# class LeadLecturer(Lecturer):
#
#     def __init__(self, first_name: str, last_name: str, address: str, email: str,
#                  bdate: datetime.date, salary_per_hour: int,
#                  conference_salary_addition_percent: int):
#         super().__init__(first_name, last_name, address, email, bdate, salary_per_hour)
#
#         self.__conference_salary_addition_percent = conference_salary_addition_percent
#         self.__conferences = []
#     #
#     # l1 = LeadLecturer("Valeria", "Aynbinder", "NETANYA",
#     #                   "valeria@gmail.com", datetime.date(year=1987, month=2, day=11),
#     #                   10, 15)
#
#     def add_conference(self, conference_name):
#         self.__conferences.append(conference_name)
#
#     def get_conferences_num(self):
#         return len(self.__conferences)
#
#     def get_salary_per_conference(self, conference_hours):
#         return self._salary * \
#                (1+self.__conference_salary_addition_percent/100) * conference_hours
#         # return self._salary * (1+self.__conference_salary_addition_percent/100) * conference_hours
#
#     def get_salary_per_course(self, course_hours, bonus=0):
#         return super().get_salary_per_course(course_hours) * bonus
#
#     def __str__(self):
#         return f"Lead {super().__str__()}"
#
# ########################################################################################################################
#
# import datetime
#
# #from lesson13.person import Person, Student, Lecturer, LeadLecturer
#
# if __name__ == '__main__':
#     p1 = Person("Valeria", "Aynbinder", "NETANYA",
#                 "valeria@gmail.com", datetime.date(year=1987, month=2, day=11))
#     p2 = Person("Daniel", "Sh", "Ashdod",
#                 "daniel@gmail.com", datetime.date(year=2002, month=11, day=5))
#
#     print(p1)
#     print(p2)
#
#
#
#     s1 = Student("Daniel", "Sh", "Ashdod",
#                  "daniel@gmail.com", datetime.date(year=2002, month=11, day=5),
#                  "python full stack")
#     s1.add_grade(100)
#     s1.add_grade(99)
#     print(s1.get_avg_grade())
#
#     print(s1)
#
#     print(s1)
#     persons_list = [p1, s1]
#     print(persons_list)
#
#     s2 = Student("Gal", "Mesilati", "Herzliya", "gal@gmail.com",
#                  datetime.date(year=2000, month=3, day=28), "python full stack")
#     print(s2.get_full_name())
#     l1 = LeadLecturer("Valeria", "Aynbinder", "NETANYA",
#                   "valeria@gmail.com", datetime.date(year=1987, month=2, day=11),
#                       10, 15)
#     print(l1)

########################################################################################################################

class Person:
    def __init__(self, id_nu: str, first_na: str, last_na: str, address_x: str, birth_y: int):
        self.id = id_nu
        self.first_name = first_na
        self.last_name = last_na
        self.address_ = address_x
        self.phone_number = []
        self.birth_year = birth_y
        self.today_year = 2022

        def __str__(self):
         return f"{self.id_nu: str}{self.first_na: str}{self.last_na: str}{self.address_x}{self.phone_nu: str}{self.birth_y: int}"


    def get_age(self):
        return f"{self.first_name}'s age is: {self.today_year-self.birth_year}"

    def add_phone(self,cc):
        self.phone_number.append(cc)

    def remove_phone(self,kak):
        self.phone_number.remove(kak)

ohad = Person('308453422','ohad','meroz','gurit kadman 2,tel-aviv' ,1992)
print(ohad.phone_number)
ret_val = ohad.get_age()
print(ret_val)
ttt= '88448'
ret_val = ohad.add_phone('jkhjh')
print(ret_val)
print(ohad.phone_number)
ret_val = ohad.add_phone(ttt)
print(ohad.phone_number)
# ret_val = ohad.remove_phone(ttt)
# print(ohad.phone_number)

########################################################################################################################

nums = [7, 8, 43, 5, 2, 7, 2, 6]
print(nums[2:5])
print(nums[2:])
print(nums[:5])
print(nums[:5:2])
print(nums[3])
print(nums[3:4])

word = "banana and apple"
print(word[::-1])


a = 5
b = 6
if a != b:
    print('bla')
if a is not b:
    print('bla')

s = "dfsdf"
if s is None:
    pass
#
# ['banana','apple','pear']
# a 2
# p 2
# e 1

a = 5
b = 5
print(a is b)
c = input("insert num1:")
d = input("insert num2:")
print(c is d)


d= {'Science': [88, 89, 62, 95],
'Language': [77, 78, 84, 80]}

#[{'Science': 88, 'Language': 77},
# {'Science': 89, 'Language': 78},
# {'Science': 62, 'Language': 84},
# {'Science': 95, 'Language': 80}]

def dict2list(orig_dict) -> list:
    ret_list = []
    for prof, grades_list in orig_dict.items():
        for i, grade in enumerate(grades_list):
            if len(ret_list) < i+1:
                ret_list.append({})
            ret_list[i][prof] = grade
    return ret_list

print(dict2list(d))

# []
# [{}] -> [{'science': 92}]
# [{'science': 92}, {'science': 90},
#  {'science': 99}, {'science': 99}]
# [{'science': 92, 'lang':70}, {'science': 90, 'lang': 70},
#  {'science': 99, 'lang':70}, {'science': 99, 'lang':70}]