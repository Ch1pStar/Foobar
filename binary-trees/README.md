Note: I didn't save the original problem description. Here is a summary of the original description.
====================================================================================================
You are given a perfect(each node can only have either 2 or 0 leafs) binary tree with height 'h'. The nodes of the tree are labeled by their post-order traversal index e.g:

     7 
  3      6
1   2  4   5

Write a function called answer(int h, int[] q), where 'h' is the height of the binary tree and 'q' is a list of positive integers, that returns a list of positive intergers for each element in 'q', containing the parent node label or -1 if the node doesn't have a parent. The value of 'h' will be less than 1073741824 and the size of 'q' will be less than or equal to 2000.

Test cases
==========
Inputs:
    (int) h = 3
    (int list) q = [7, 3, 5, 1]
Output:
    (int list) [-1, 7, 6, 3]

Inputs:
    (int) h = 5
    (int list) q = [19, 14, 28]
Output:
    (int list) [21, 15, 29]

Inputs:
    (int) h = 3
    (int list) q = [1, 4, 7]
Output:
    (int list) [3, 6, -1]