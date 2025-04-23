txt = """One of the most effective ways to reduce the friction
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a
method for making cues more
obvious but you can also optimize your environment to make
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your
daily
routine
Habits are easier to build when they fit into the flow of your
life
You are more likely to go to the gym if it is on your way to
work
because stopping does not add much friction to your lifestyle
"""
letter_counter_dict = {}
alphabet = txt.lower().strip().replace("\n", "").replace(" ", "")
for letter in alphabet:
    if letter not in letter_counter_dict:
        letter_counter_dict[letter] = 1
    else:
        letter_counter_dict[letter] += 1 

for letter, count in letter_counter_dict.items():
    print(f"{letter.title()}: {count}")
# make the string lower case and remove the new line and spaces
# create an empty dictionary to store the letters
# loop through the string
# check if the letter is not in the dictionary
# if the letter is not in the dictionary add it and set thevalue to 1
# if the letter is in the dictionary add 1 to the value
# print the dictionary
print("$!#$&*" * 10)
letter_counter_dict = {}
for letter in alphabet:
   
       letter_counter_dict[letter] = letter_counter_dict.get(letter, 0) + 1

for letter, count in letter_counter_dict.items():
    print(f"{letter.title()}: {count}")
