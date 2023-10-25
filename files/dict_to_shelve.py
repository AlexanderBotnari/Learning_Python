import shelve

# university = {
#     'schedules': {
#         'monday_schedule': ['Python', 'Kotlin', 'Math', 'ML'],
#         'tuesday_schedule': ['Java', 'BD', 'WEB'],
#         'wednesday_schedule': ['OOP', 'Math', 'Android', 'Design'],
#         'thursday_schedule': ['English', 'Python', 'Blockchain'],
#         'friday_schedule': ['XML', 'Swift', 'C++']
#     },
#
#     'tutors': {
#         'Math': ['John Snow', 'Mat Daemon'],
#         'Python': ['Youra Alah', 'Will Turner']
#     }
# }

university = shelve.open('university_file')
university['schedules'] = {
    'monday_schedule': ['Python', 'Kotlin', 'Math', 'ML'],
    'tuesday_schedule': ['Java', 'BD', 'WEB'],
    'wednesday_schedule': ['OOP', 'Math', 'Android', 'Design'],
    'thursday_schedule': ['English', 'Python', 'Blockchain'],
    'friday_schedule': ['XML', 'Swift', 'C++']
}

university['tutors'] = {
    'Math': ['John Snow', 'Mat Daemon'],
    'Python': ['Youra Alah', 'Will Turner']
}

print(university['tutors'])
university.close()
