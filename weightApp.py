# weight converter Lbs to Kg


print("Enter your weight");
weight = int(input())

print("Is this is (L)bs or (K)gs")
measure = input()


if measure == "L" or measure == "l":
    print(f" your weigth is {weight * 0.45} Kgs")

elif measure == "K" or measure == "k":
    print(f" your weigth is {weight / 0.45} LBS")

else :
    print(f"enter proper weight")
