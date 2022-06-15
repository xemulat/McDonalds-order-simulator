Print("Welcome to McDonald's order simulator")
Print(" #WrittenInPython")
Print("")
Print("Order? (Y/N)
Order = Input("Responce: ")
If order == 'y':        #positive responce
    print("What do you want to order?")
    resp = Input("Responce: ")
    print("")
    print(resp + " Ordered!")
    exit(sleep(4))

If order == 'n':        #negative responce
    print("Ok")
    exit(sleep(2))
