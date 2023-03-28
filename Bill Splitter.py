import random

print("Enter the number of friends joining (including you):")
n = int(input())
dict_names = {}
print()
if int(n) <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")

    for i in range(int(n)):
        names = input()
        dict_names[names] = 0
    print()
    print("Enter the total bill value:")
    bill = int(input())
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    response = input()

    if response == 'Yes':
        name_list = list(dict_names.keys())
        pick_name = random.choice(name_list)
        print(pick_name + " is the lucky one!")
        x = int(n) - 1
        for name in dict_names:
            dict_names[name] = round(int(bill) / int(x), 2)
        if pick_name in dict_names.keys():
            dict_names[pick_name] = 0

    else:
        print("No one is going to be lucky")
        for name in dict_names:
            dict_names[name] = round(int(bill) / int(n), 2)

    print()
    print(dict_names)