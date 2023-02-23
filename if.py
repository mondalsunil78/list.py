indian = ["samosa", "rice", "potato"]
chinese = ["roll", "chaumin", "fried rice"]
italian = ["pizza", "pasta", "sping roll"]

dish = input("enter a dish name:")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")

else:
    print("i dont no about this cuisin", dish)


