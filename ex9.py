weights = []
for weight in range(4):
    x=int(input("Enter the weights:"))
    weights.append(x)
    print("Lbs list:", weights)
    kilograms = []
    for w in weights:
        kgs=(w/2.205)
        kilograms.append(kgs)
        print("KGs list:", kilograms)



