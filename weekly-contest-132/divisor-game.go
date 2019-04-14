/*
1025. Divisor Game

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Note:

1 <= N <= 1000
*/
package main

import "fmt"

func turnAlice(lastRound bool) bool {
    if lastRound == true { return false } else { return true }
} 

func isDivisible (n int) int {
    // 1 is always the optimal strategy
    if n > 1 { return 1} else { return 0 }
}

func divisorGame(N int) bool {
    lastRound, n := false, N
    for {
        thisRound := turnAlice(lastRound)
        x := isDivisible(n)
        n = n - x
        if x == 0 {
            if thisRound {
                return false
            } else {
                return true
            }
        }
        lastRound = thisRound
    }
}

func main() {
	fmt.Println(divisorGame(6))
	fmt.Println(divisorGame(7))
	fmt.Println(divisorGame(2))
	fmt.Println(divisorGame(3))
}
