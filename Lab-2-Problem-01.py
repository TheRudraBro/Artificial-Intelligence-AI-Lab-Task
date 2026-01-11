user_input = input("Enter numbers separated by spaces: ")
mylist = [int(x) for x in user_input.split()]

if len(mylist) < 2:
    print("Please enter at least two numbers to find the second largest.")
else:
    largest_nmb = max(mylist)
    smallest_nmb = min(mylist)
    
    sorted_list = sorted(mylist)
    second_largest = sorted_list[-2]
print(f"List: {mylist}")
print(f"Largest: {largest_nmb}")         
print(f"Second Largest: {second_largest}")
print(f"Smallest: {smallest_nmb}")        
