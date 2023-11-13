'''
Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
'''

# numura ievade
numurs = int(input("Ievadiet skaitli: "))

# paarbaudisana
if numurs % 2 != 0:
    print("Skaitlis ir nepāra.")
else:
    print("Skaitlis ir pāra.")
