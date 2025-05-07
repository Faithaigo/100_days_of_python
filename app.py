logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

continue_play = True
bids = {}
while continue_play:
    name = input('What is your name?: ')
    price = int(input('What is your bid?: $'))
    bids[name] = price

    check = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()

    if check == 'yes':
        print('\n' * 100)
    elif check == 'no':
        continue_play = False
        highest_bidder = max(bids, key=bids.get)
        print(f"The winner is {highest_bidder} with a bid of {bids[highest_bidder]}")
    else:
        continue_play = False
        print('You entered a wrong value')


