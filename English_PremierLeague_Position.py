def premiership(top4):
    if top4 == "Chelsea":
        print("1st")
    elif top4 == "ManCity":
        print("2nd")
    elif top4 == "Liverpool":
        print("3rd")
    elif top4 == "Brighton":
        print("4th")
    else:
        print("Not in top 4 position on the English Premier League.")


def team():
    fan = input("Enter the name of English Premiership Club you support: ")
    premiership (fan)

team()


print("As at Saturday, 23rd October 2021, 11:40pm.")