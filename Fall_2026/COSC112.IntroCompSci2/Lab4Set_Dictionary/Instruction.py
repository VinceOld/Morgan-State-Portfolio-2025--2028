Task 1(20 pts) Write a function called symmetric_set_difference(set1,set2)
1. The function accepts two sets as parameters and returns a new set containing their symmetric set difference (that is, the set of elements contained in either of the two sets but not in both). 

2.For example, the symmetric difference between the sets {1, 4, 7, 9} and {2, 4, 5, 6, 7}

output is {1, 2, 5, 6, 9}. 

Do not call the set’s symmetric_difference method or ^  operator in your solution. They are not allowed in Task 1.

Task 2 (20pts) Write a function called reverse(dict)
1. It accepts a dictionary as a parameter and 

2. Returns a new dictionary that is the reverse of the original. 

3. The reverse of a dictionary is a new dictionary that uses the values from the original as its keys and the keys from the original as its values. Since a dictionary’s values need not be unique but its keys must be, you should have each value map to a set of keys. 

For example, if passed the following dictionary:

{42: "Marty", 81: "Sue", 17: "Ed", 31: "Dave",
 56: "Ed", 3: "Marty", 29: "Ed"}

You should reverse it to become (the order of the keys and values does not matter):

{"Marty": [42, 3], "Sue": [81], "Ed": [17, 56, 29], "Dave": [31]}
