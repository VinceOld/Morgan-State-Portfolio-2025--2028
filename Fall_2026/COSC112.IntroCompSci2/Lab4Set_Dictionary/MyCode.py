#Task 1(20 pts) symmetric set difference 
def symmetric_set_difference(set1,set2):
    result = set()
    for item in set1:
        if item not in set2:
            result.add(item)
    for item in set2:
        if item not in set1:
            result.add(item)
    return result

# Run the examples for testing
set1 = {1, 4, 7, 9}
set2 = {2, 4, 5, 6, 7}
output = symmetric_set_difference(set1, set2)
print(output)
# expected Output: {1, 2, 5, 6, 9}
print(output)
set3 = {1, 'a', 3.5}
set4 = {'b', 2, 3.5}
output1 = symmetric_set_difference(set3, set4)
print(output1)  # Output: {1, 2, 'a', 'b'}  

# Task2(20pts) Reverse Dictionaries
def reverse(dict):
    reversed_dict = {}
    
    for key, value in dict.items():
        if value not in reversed_dict:
            reversed_dict[value] = [key]
        else:
            reversed_dict[value].append(key)
    
    return reversed_dict

# run following examples to test your function   
dict = {
    42: "Marty", 81: "Sue", 17: "Ed", 
    31: "Dave", 56: "Ed", 3: "Marty", 29: "Ed"
}

# call the reverse function
print(reverse(dict))

# Expected Output: {"Marty": [42, 3], "Sue": [81], "Ed": [17, 56, 29], "Dave": [31]}
