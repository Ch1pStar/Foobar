Note: I didn't save the original problem description. Here is a summary of the original description.
====================================================================================================
Minion workers are given each an ID. At the end of every day guards need to verify that every worker is present, to avoid counting they are using a checksum method.
Workers form a line(ordering with ascending IDs) and only 'n' amount of workers fit at one time. When the line is full a guard writes down all the worker IDs. The line is filled again with the next batch of workers and the guard notes one less worker ID. This continues untill no worker IDs are noted in the line. After all the needed IDs are noted the guard ORs all the noted IDs together to get the checksum for the day.

Write a function answer(start, length), where 'start' is the ID of the first worker to be noted and 'length' is the amount of workers that fit in a line. It should return the guard checksum.

Test cases
==========
Inputs:
    (int) start = 0
    (int) length = 3
Output:
    (int) 2

Inputs:
    (int) start = 17
    (int) length = 4
Output:
    (int) 14