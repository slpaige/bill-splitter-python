# write your code here
import random


def split_bill(bill, lucky="none"):

    global friends

    split_count = len(friends) if lucky == "none" else len(friends) - 1
    split_total = round(bill / split_count, 2)

    for def_friend in friends:
        if def_friend == lucky:
            friends[def_friend] = 0
        else:
            friends[def_friend] = split_total

    print(friends)


friends = {}

print("Enter the number of friends joining (including you):")
eaters = int(input())

if eaters <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for friend in range(0, eaters):
        friends[input()] = 0

    print("Enter the total bill value:")
    total_bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    is_lucky = input()

    if is_lucky.lower() == "no":
        print("No one is going to be lucky")
        split_bill(total_bill)
    else:
        pair = key, val = random.choice(list(friends.items()))
        print(f"{key} is the lucky one!")
        split_bill(total_bill, key)
