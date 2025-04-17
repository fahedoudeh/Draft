txt = """Er is er één jarig, hoera, hoera,
Dat kun je wel zien: dat is hij/zij.
Dat vinden wij allen zo prettig ja, ja,
En daarom zingen wij blij.

Hij/zij leve lang hoera, hoera.
Hij/zij leve lang hoera, hoera.
Hij/zij leve lang hoera, hoera.
Hij/zij leve lang hoera, hoera.

Lang zal hij/ze leven
Lang zal hij/ze leven
Lang zal hij/ze leven in de Gloria
In de Gloria
In de Gloria

Hieperdepiep – hoera
Hieperdepiep – hoera
Hieperdepiep – hoera"""

# count how many A's in the variable txt
count = txt.count('a')
print(count)

counter = 0
for letter in txt:
    if letter == "a":
        counter += 1
print(counter)

# ------------------------

letter_counter_dict = {}

for letter in txt:
    if letter in letter_counter_dict:
        letter_counter_dict[letter] += 1
    else:
        letter_counter_dict[letter] = 1

print(letter_counter_dict)            

txt = """welcome """ 


cont_dict = {}
for letter in txt:
    if letter in cont_dict:
        cont_dict[letter] += 1
    else:
        cont_dict[letter] = 1

print(cont_dict)

# create an empty dictionary to store the letters
cont_dict = {}
for letter in txt:
# get the value of the letter from the dictionary
# if the letter is not in the dictionary set the value to 0
    cont_dict[letter] = cont_dict.get(letter, 0)
    print(cont_dict)
    # add 1 to the value of the letter
    cont_dict[letter] += 1
    print(cont_dict)
print(cont_dict)



# create an empty dictionary to store the letters
cont_dict ={}
# get the value of the letter from the dictionary
for letter in txt:
    # if the letter is not in the dictionary set the value to 0
    cont_dict[letter] = cont_dict.setdefault(letter, 0)
    print(cont_dict)
# add 1 to the value of the letter
    cont_dict[letter] += 1
    print(cont_dict)
cont_dict.update(hani = 44)    
print(cont_dict)


