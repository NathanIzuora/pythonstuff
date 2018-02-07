coincount = 0
print("You have", coincount , "coins")
print ("Whould you like another coin?")

while True:
    answer = input("more coin?")

    if(answer == "yes"):
        coincount = coincount + 1
    else:
        break
print(coincount)