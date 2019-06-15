"""
  User: Liujianhan
  Time: 14:56
 """
__author__ = 'liujianhan'


udacity = ['peter', 'andy', 'sarah', 'gundega', 'job', 'sean']
udacity_upper = [x.upper() for x in udacity]
udacity_capital = [x.capitalize() for x in udacity]
# print(udacity_upper)
# print(udacity_capital)

ta_data = [('Peter', 'USA', 'CS262'),
           ('Andy', 'USA', 'CS212'),
           ('Sarah', 'England', 'CS101'),
           ('Gundega', 'Latvia', 'CS373'),
           ('Job', 'USA', 'CS387'),
           ('Sean', 'USA', 'CS253')]

ta_facts = [name + ' lives in ' + country + ' and is the TA for ' + course + '.' for name, country,
            course in ta_data]

remote_ta_facts = [name + ' lives in ' + country + ' and is the TA for ' + course + '.' for name, country,
            course in ta_data if country != 'USA']

ta_300 = [name + ' is the TA for ' + course for name, _, course in ta_data if course.find('CS3') != -1]

for row in ta_300:
    print(row)
