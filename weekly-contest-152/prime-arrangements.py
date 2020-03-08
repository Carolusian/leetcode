"""
1175. Prime Arrangements

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015
 

Constraints:

1 <= n <= 100
"""
def numPrimeArrangements(n: int) -> int:
    r_lst = [1]
    all_lst = list(range(1,n+1))
    len_all_number = len(all_lst)

    if n >=2:       
        for j in range(2, n + 1):
            for i in range(2, j-1):
                if(j%i == 0):
                    if j not in r_lst:
                        r_lst.append(j)

    for num in r_lst:
        all_lst.remove(num)

    print(all_lst)

    len_num_pre = len(all_lst)
    print(all_lst)
    a = 1
    b = 1
    for x in list(range(1,len_num_pre+1)):
        a = a*x
    for y in list(range(1,len_all_number - len_num_pre+1)):
        b = b*y
    return (a*b) % 1000000007


print(numPrimeArrangements(100))
