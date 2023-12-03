#For creating acronyms using Python, you need to write a python program that generates a short form of a word from a
#given sentence. You can do this by splitting and indexing to get the first word and then combine it.

user_input = str(input("Enter : "))
phrase = user_input.split()
Acronym = " "
for i in phrase:
    Acronym  = Acronym  + str(i[0]).upper()

print(Acronym )