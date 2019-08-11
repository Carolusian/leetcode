"""
1155. Number of Dice Rolls With Target Sum

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""

def numRollsToTarget(d: int, f: int, target: int) -> int:
    # https://www.geeksforgeeks.org/dice-throw-dp-30/
    table=[[0]*(target+1) for i in range(d+1)] #Initialize all entries as 0 
      
    for j in range(1,min(f+1,target+1)): #Table entries for only one dice 
        table[1][j]=1
          
    # Fill rest of the entries in table using recursive relation  
    # i: number of dice, j: sum 
    for i in range(2,d+1): 
        for j in range(1,target+1): 
            for k in range(1,min(f+1,j)): 
                table[i][j]+=table[i-1][j-k] 
      
    # print(table) 
    # Uncomment above line to see content of table 
      
    return table[-1][-1] % 1000000007

print(numRollsToTarget(1, 6, 3))
print(numRollsToTarget(2, 6, 7))
print(numRollsToTarget(2, 5, 10))
print(numRollsToTarget(1, 2, 3))
print(numRollsToTarget(30, 30, 500))
