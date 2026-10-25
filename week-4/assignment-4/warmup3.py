# Create two hardcoded lists of programming languages (some overlap, some unique to each list). 
# Convert each to a set and print:
# The union (all languages from both lists, no duplicates)
# The intersection (languages in both lists)
# The difference (languages only in the first list)
language_1 = ['Python', 'JavaScript', 'Java', 'C++']
language_2 = ['Python', 'JavaScript', 'Ruby', 'Swif']

set_1 = {'Python', 'JavaScript', 'Java', 'C++'}
set_2 = {'Python', 'JavaScript', 'Ruby', 'Swif'}
print (set_1.union(set_2))
print (set_1.difference(set_2))
print (set_1.intersection(set_2))