print("Menu Based Program")
items = []

try:
    with open("items.txt", "r") as file:
        for line in file:
            items.append(line.strip())
except FileNotFoundError:
    pass

add = None
delete = None

print(
    "1. Add item\n"
    "2. View item\n"
    "3. Delete item\n"
    "4. Exit"
)

while True:
    choice = int(input("Choose an option between 1-4 : "))
    if choice == 1:
        add = input("what item do u want to add : ")
        items.append(add)
        with open("items.txt", "w") as file:
            for item in items:
                file.write(item + '\n') 
    elif choice == 2:
        print(items)
    elif choice == 3:
        delete = input("what item do u want to delete : ")
        if delete in items:
            items.remove(delete)
            with open("items.txt", "w") as file:
                for item in items:
                    file.write(item + '\n')
        else:
            print("No item called ", delete)
    elif choice == 4:
        break
    else:
        print("invalid choice, pick a number between 1-4 dumbass")
    
