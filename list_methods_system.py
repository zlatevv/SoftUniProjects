lst = input("Enter the data for the list (comma seperated): ").split(", ")
def list_append(ml):
    data = input("Enter the data to append: ")
    ml.append(data)
    print(*ml, sep = ", ")
def list_extend(ml):
    data = input("Enter the data for extension: ").split(", ")
    ml.extend(data)
    print(*ml, sep = ", ")
def list_insert(ml):
    data = input("Enter the data to insert and the index you want to insert at: ").split(", ")
    ml.insert(int(data[1]), data[0])
    print(*ml, sep = ", ")
def list_remove(ml):
    data = input("Enter the data to remove: ")
    ml.remove(data)
    print(*ml, sep = ", ")
def list_pop(ml):
    data = int(input("Enter the index you want to pop: "))
    ml.pop(data)
    print(*ml, sep = ", ")
def list_clear(ml):
    
    ml.clear()
    print("The list is empty now.")
def list_index(ml):
    index = int(input("Enter the index to find: "))
    a = ml[index]
    print(f"The value at index {index} is {a}")
def list_count(ml):
    data = input("Enter the data to count: ")
    a = ml.count(data)
    print(f"The number of times {data} is in the list is {a}")
def list_sort(ml):
    ml.sort()
    print("Here is the sorted list: ")
    print(*ml, sep = ", ")
def list_reverse(ml):
    ml.reverse()
    print("Here is the reversed list: ")
    print(*ml, sep = ", ")
def list_copy(ml):
    a = ml.copy()
    print(f"Here is the copied list: {a}")
    
while True:
    print("\nChoose a list operation:")
    print("1. Append")
    print("2. Extend")
    print("3. Insert")
    print("4. Remove")
    print("5. Pop")
    print("6. Clear")
    print("7. Index")
    print("8. Count")
    print("9. Sort")
    print("10. Reverse")
    print("11. Copy")
    print("12. Exit")   
    choice = input("Enter your choice (1-12): ")
    if choice == '1':
        list_append(lst)
    elif choice == '2':
        list_extend(lst)
    elif choice == '3':
        list_insert(lst)
    elif choice == '4':
        list_remove(lst)
    elif choice == '5':
        list_pop(lst)
    elif choice == '6':
        list_clear(lst)
    elif choice == '7':
        list_index(lst)
    elif choice == '8':
        list_count(lst)
    elif choice == '9':
        list_sort(lst)
    elif choice == '10':
        list_reverse(lst)
    elif choice == '11':
        list_copy(lst)
    elif choice == '12':
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please try again.")