#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# asked to print the length of the string Belgium
print(len(Belgium))

#created a new variable called 'length' to capture the string length
length = len(Belgium)
#printed a hyphen times the length
print("-" * length)

# use the replace method with the old seperator then comma and the new seperator in speech marks
print(Belgium.replace(',', ':'))

#created a new variable with the output from the replace method called Belgium1
Belgium1 = "Belgium:10445852:Brussels:737966:Europe:1830:Euro:Catholicism:Dutch:French:German"
# created a new variable called parts using the split method on the Belgium string - used colon as the default seperator
parts = Belgium1.split(':')
# created a new variable, converted parts 1 and 3 into integers and added them together
combined_pop = int(parts[1]) + int(parts[3])
# printed the sum
print(combined_pop)
