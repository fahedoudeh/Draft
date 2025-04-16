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
