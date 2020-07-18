# put your python code here
grades_str = input()
grades_lst = grades_str.split()

a_quan = grades_lst.count('A')
a_percentage = a_quan / len(grades_lst)
print(round(a_percentage, 2))
