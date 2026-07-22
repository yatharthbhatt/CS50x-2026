people = [
    {"name": "Yatharth", "number": "8755690000"},
    {"name": "Aarav", "number": "8732679347734"},
    {"name": "Rohan", "number": "8732234182734"}
]

inpName = input("Enter Name: ").capitalize()

for person in people:
    if (person["name"] == inpName):
        print(f"Number: {person["number"]}")
        break
else:
    print("Not Found")