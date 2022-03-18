import math

with open('.//2019_Oscars.csv', 'r', encoding='utf-8-sig') as file:
    data = file.read().splitlines()
    del data[0]

# what needs to be done?
# 1. Adding id to each line
# 2. Find out how much times a Movie was a nomenee in 2019
# 3. Final dataset may be:
# [0,Vice,3,'ACTOR IN A SUPPORTING ROLE, ACTOR IN A LEADING ROLE']
# Explanation:
# id, movie, number of nominations, possible awards

# finalDataSet = []
for movie in data:
    oscarNominee = movie.split(',')
    print(oscarNominee)
    break
