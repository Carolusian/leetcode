"""
1169. Invalid Transactions

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
from typing import List


def invalidTransactions(transactions: List[str]) -> List[str]:
    ret = []
    txs = [tx.split(',') for tx in transactions]
    for i, _ in enumerate(txs):
        if int(txs[i][2]) > 1000:
            ret.append(','.join(txs[i]))

        for j, tx in enumerate(txs[i + 1:]):
            if not tx: break
            if (txs[i][0] == tx[0] and txs[i][-1] != tx[-1] and abs(int(txs[i][1]) - int(tx[1])) <= 60):
                ret.append(','.join(txs[i]))
                ret.append(','.join(tx))

    return list(dict.fromkeys(ret))
            



print(invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))
print(invalidTransactions(["alice,20,800,mtv","alice,50,1200,mtv"]))
print(invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"]))
print(invalidTransactions(["alex,676,260,bangkok","bob,656,1366,bangkok","alex,393,616,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]))
