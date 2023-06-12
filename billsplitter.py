import random
num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends.update({name: 0})
    print()
    amount = int(input("Enter the total bill value:"))
    ones_amount = amount/num_friends
    print()
    bill_splitting = round(ones_amount, 2)
    for person in friends:
        friends[person] = bill_splitting
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    response = input()
    if (response.upper() == "YES"):
        random_lucky = random.choice(list(friends))
        friends.update({random_lucky: 0})
        print("{} is the lucky one!".format(random_lucky))
    else:
        print("No one is going to be lucky")
    print(friends)