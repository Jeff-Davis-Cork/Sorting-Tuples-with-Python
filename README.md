# Sorting-Tuples-with-Python

An exercise in sorting tuples. sample data is names and ages of people stored in a list of tuples, such as:

[ (“Ann”,23),(“Tim”,18),(“Bob”,37),(“Ned”,51),(“Sue”,18) ]

Print( data )
this outputs the list ‘data’ of (name,age) tuples in the form of a headed table, allowing 7 spaces for each name and 3 spaces for each age, with 1 extra space between them. For example, the output for the above list:
Name Age
------- ---
Ann 23
Tim 18
Bob 37
Ned 51
Sue 18

InsertionSort( data, field )
Sorts the list ‘data’ of (name,age) tuples into ascending order of field ‘field’, which is either the string “name” or “age”, using the Insertion Sort algorithm.
For example, calling InsertionSort( data, “age” ) on the above list, and then calling Print( data ) produces the output:
Name Age
------- ---
Sue 18
Tim 18
Ann 23
Bob 37
Ned 51

SelectionSort( data, field )
Identical to InsertionSort( data, field ) but using the Selection Sort algorithm.
