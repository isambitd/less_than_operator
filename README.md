## What it is all about

if you have an array of n numbers where you have first m elements are decreasing and the last n-m elements are increasing
This lib able to find the minimum in less time then the default functions available with python lib

Time complexity is O(n/2)

Spece Complexity is O(1)

```
$ python3

>>>import lessthanop

>>>l= [6,5,4,3,2,1,2,3,4,5,6]

>>>lessthanop.get_index(l)

# 5
