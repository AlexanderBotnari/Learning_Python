import shelve

monday_schedule = ['Python', 'Kotlin', 'Math', 'ML']
tuesday_schedule = ['Java', 'BD', 'WEB']
wednesday_schedule = ['OOP', 'Math', 'Android', 'Design']
thursday_schedule = ['English', 'Python', 'Blockchain']
friday_schedule = ['XML', 'Swift', 'C++']

with shelve.open('schedule_file', writeback=True) as file:
    # file['monday_schedule'] = monday_schedule
    # file['tuesday_schedule'] = tuesday_schedule
    # file['wednesday_schedule'] = wednesday_schedule
    # file['thursday_schedule'] = thursday_schedule
    # file['friday_schedule'] = friday_schedule

    # temp_schedule = file['tuesday_schedule']
    file['friday_schedule'].append('WEB')
    # file['tuesday_schedule'] = temp_schedule

    for key, schedule in file.items():
        print(key, schedule)
