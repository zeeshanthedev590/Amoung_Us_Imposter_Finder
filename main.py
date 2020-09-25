import random  # importing the Random
# Asking The The Names

name1 = input('Enter The Name Of Player 1 : ')
name2 = input('Enter The Name Of Player 2 : ')
name3 = input('Enter The Name Of Player 3 : ')
name4 = input('Enter The Name Of Player 4 : ')
name5 = input('Enter The Name Of Player 5 : ')
name6 = input('Enter The Name Of Player 6 : ')
name7 = input('Enter The Name Of Player 7 : ')
name8 = input('Enter The Name Of Player 8 : ')
name9 = input('Enter The Name Of Player 9 : ')
name10 = input('Enter The Name Of Player 10 : ')

# Making A List Of Names

names = [name1, name2, name3, name4, name5, name6, name7, name8, name9, name10]

# Finding A Imposter Randomly

imposter = random.choice(names)

# Removing Imposter From The List
names.remove(imposter)
# Create a File For The Crew Members

crew = open('crewmates.txt', 'w+')
crew.write(str(names))
crew.close()

# Making A File For Imposter
imposter_file = open('imposter.txt', 'w+')
imposter_file.write(str(imposter))
imposter_file.close()
