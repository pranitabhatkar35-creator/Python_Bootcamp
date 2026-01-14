
print("Welcome to the Python restaurant")

print("Menu card:")
menu_card={
    "Pasta":70,
    "Burger":68,
    "Pizza":50,
    "Maggie":90,
}

for key,values in menu_card .items():
    print(f"{key}:{values}")

bill=0
bill=bill+menu_card["Maggie"]
print(f"your bill is {bill} RS")

print("Thank you visit again!")