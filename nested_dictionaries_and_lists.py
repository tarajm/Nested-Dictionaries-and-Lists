# # ##1 Update Vlaues in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} 
# ]

# # # #Part 1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # x[1][0] 
# # print(x)

# # # #Part 2 Change the last_name of the first student from 'Jordan' to 'Bryant'
# # students[0]['last_name'] = "Bryant"
# # print(students)

# # # #Part 3 In the sports_directory, change 'Messi' to 'Andres'

# # sports_directory["soccer"][0] = "Andres"
# # print(sports_directory)

# # #Part 4 Change the value 20 in z to 30
# z[0]['y'] = 30
# print(z)


#################################

#2 Iterate Through a List of Dictionaries


# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterate_dictionary(list):
#     for i in range(0,len(list)-1):
#         new_lst = ''
#         for key, val in list[i].items():
#             new_lst += f"{key} - {val},"
#         print(new_lst)
        
# iterate_dictionary(students)

# #3 Get Values From a List of Dictionaries

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterate_dictionary2(key_name, list):
#     for i in range(0, len(list)):
#         for key, val in list[i].items():
#             if key == key_name:
#                 print(val)

# print(iterate_dictionary2('first_name', students))
# print(iterate_dictionary2('last_name', students))

# #4 Iterate Through a Dictionary with List Values

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(some_dict):
    for key, val in some_dict.items():
        print(len(val), key)
        for i in val:
            print(i)


print_info(dojo)
# # # output:
# # 7 LOCATIONS
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank
    
# # 8 INSTRUCTORS
# # Michael
# # Amy
# # Eduardo
# # Josh
# # Graham
# # Patrick
# # Minh
# # Devon

