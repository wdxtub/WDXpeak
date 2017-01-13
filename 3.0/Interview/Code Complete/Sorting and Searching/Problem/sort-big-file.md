# Sort Big File

Imagine you have a 20 GB file with one string per line. Explain how you would sort the file

## Solution

As we can't store everything in the memory, we need to just store part of the data. Suppose we have 2 GB memory, we will split the data into 10 sets and each time we use in-place sorting algorithm to sort the 2GB data.

 After 10 times of sorting, now the 20GB data is partially in-order. What we need to do is merge these 10 sets one by one to get the whole data sorted.

