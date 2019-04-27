/*
1030. Matrix Cells in Distance Order

We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)



Example 1:

Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (r0, c0) to other cells are: [0,1]
Example 2:

Input: R = 2, C = 2, r0 = 0, c0 = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
Example 3:

Input: R = 2, C = 3, r0 = 1, c0 = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].


Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
*/
package main

import (
	"fmt"
	"sort"
	"sync"
)

type Iter chan interface{}
type Predicate func(interface{}) bool
type Mapper func(interface{}) interface{}
type MultiMapper func(...interface{}) interface{}
type Reducer func(memo interface{}, element interface{}) interface{}

func New(els ...interface{}) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}

func Int64(els ...int64) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}

func Int32(els ...int32) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}

func Float64(els ...float64) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}

func Float32(els ...float32) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}

func Uint(els ...uint) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}
func Uint64(els ...uint64) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}

func Uint32(els ...uint32) Iter {
	c := make(Iter)
	go func() {
		for _, el := range els {
			c <- el
		}
		close(c)
	}()
	return c
}

func List(it Iter) []interface{} {
	arr := make([]interface{}, 0, 1)
	for el := range it {
		arr = append(arr, el)
	}
	return arr
}

// Count from i to infinity
func Count(i int) Iter {
	c := make(Iter)
	go func() {
		for ; true; i++ {
			c <- i
		}
	}()
	return c
}

// Cycle through an iterator infinitely (requires memory)
func Cycle(it Iter) Iter {
	c, a := make(Iter), make([]interface{}, 0, 1)
	go func() {
		for el := range it {
			a = append(a, el)
			c <- el
		}
		for {
			for _, el := range a {
				c <- el
			}
		}
	}()
	return c
}

// Repeat an element n times or infinitely
func Repeat(el interface{}, n ...int) Iter {
	c := make(Iter)
	go func() {
		for i := 0; len(n) == 0 || i < n[0]; i++ {
			c <- el
		}
		close(c)
	}()
	return c
}

// Chain together multiple iterators
func Chain(its ...Iter) Iter {
	c := make(Iter)
	go func() {
		for _, it := range its {
			for el := range it {
				c <- el
			}
		}
		close(c)
	}()
	return c
}

// Elements after pred(el) == true
func DropWhile(pred Predicate, it Iter) Iter {
	c := make(Iter)
	go func() {
		for el := range it {
			if drop := pred(el); !drop {
				c <- el
				break
			}
		}
		for el := range it {
			c <- el
		}
		close(c)
	}()
	return c
}

// Elements before pred(el) == false
func TakeWhile(pred Predicate, it Iter) Iter {
	c := make(Iter)
	go func() {
		for el := range it {
			if take := pred(el); take {
				c <- el
			} else {
				break
			}
		}
		close(c)
	}()
	return c
}

// Filter out any elements where pred(el) == false
func Filter(pred Predicate, it Iter) Iter {
	c := make(Iter)
	go func() {
		for el := range it {
			if keep := pred(el); keep {
				c <- el
			}
		}
		close(c)
	}()
	return c
}

// Filter out any elements where pred(el) == true
func FilterFalse(pred Predicate, it Iter) Iter {
	c := make(Iter)
	go func() {
		for el := range it {
			if drop := pred(el); !drop {
				c <- el
			}
		}
		close(c)
	}()
	return c
}

// Sub-iterator from start (inclusive) to [stop (exclusive) every [step (default 1)]]
func Slice(it Iter, startstopstep ...int) Iter {
	start, stop, step := 0, 0, 1
	if len(startstopstep) == 1 {
		start = startstopstep[0]
	} else if len(startstopstep) == 2 {
		start, stop = startstopstep[0], startstopstep[1]
	} else if len(startstopstep) >= 3 {
		start, stop, step = startstopstep[0], startstopstep[1], startstopstep[2]
	}

	c := make(Iter)
	go func() {
		i := 0
		// Start
		for el := range it {
			if i >= start {
				c <- el // inclusive
				break
			}
			i += 1
		}

		// Stop
		i, j := i+1, 1
		for el := range it {
			if stop > 0 && i >= stop {
				break
			} else if j%step == 0 {
				c <- el
			}

			i, j = i+1, j+1
		}

		close(c)
	}()
	return c
}

// Map an iterator to fn(el) for el in it
func Map(fn Mapper, it Iter) Iter {
	c := make(Iter)
	go func() {
		for el := range it {
			c <- fn(el)
		}
		close(c)
	}()
	return c
}

// Map p, q, ... to fn(pEl, qEl, ...)
// Breaks on first closed channel
func MultiMap(fn MultiMapper, its ...Iter) Iter {
	c := make(Iter)
	go func() {
	Outer:
		for {
			els := make([]interface{}, len(its))
			for i, it := range its {
				if el, ok := <-it; ok {
					els[i] = el
				} else {
					break Outer
				}
			}
			c <- fn(els...)
		}
		close(c)
	}()
	return c
}

// Map p, q, ... to fn(pEl, qEl, ...)
// Breaks on last closed channel
func MultiMapLongest(fn MultiMapper, its ...Iter) Iter {
	c := make(Iter)
	go func() {
		for {
			els := make([]interface{}, len(its))
			n := 0
			for i, it := range its {
				if el, ok := <-it; ok {
					els[i] = el
				} else {
					n += 1
				}
			}
			if n < len(its) {
				c <- fn(els...)
			} else {
				break
			}
		}
		close(c)
	}()
	return c
}

// Map an iterator if arrays to a fn(els...)
// Iter must be an iterator of []interface{} (possibly created by Zip)
// If not, Starmap will act like MultiMap with a single iterator
func Starmap(fn MultiMapper, it Iter) Iter {
	c := make(Iter)
	go func() {
		for els := range it {
			if elements, ok := els.([]interface{}); ok {
				c <- fn(elements...)
			} else {
				c <- fn(els)
			}
		}
		close(c)
	}()
	return c
}

// Zip up multiple interators into one
// Close on shortest iterator
func Zip(its ...Iter) Iter {
	c := make(Iter)
	go func() {
		defer close(c)
		for {
			els := make([]interface{}, len(its))
			for i, it := range its {
				if el, ok := <-it; ok {
					els[i] = el
				} else {
					return
				}
			}
			c <- els
		}
	}()
	return c
}

// Zip up multiple iterators into one
// Close on longest iterator
func ZipLongest(its ...Iter) Iter {
	c := make(Iter)
	go func() {
		for {
			els := make([]interface{}, len(its))
			n := 0
			for i, it := range its {
				if el, ok := <-it; ok {
					els[i] = el
				} else {
					n += 1
				}
			}
			if n < len(its) {
				c <- els
			} else {
				break
			}
		}
		close(c)
	}()
	return c
}

// Reduce the iterator (aka fold) from the left
func Reduce(it Iter, red Reducer, memo interface{}) interface{} {
	for el := range it {
		memo = red(memo, el)
	}
	return memo
}

// Split an iterator into n multiple iterators
// Requires memory to keep values for n iterators
func Tee(it Iter, n int) []Iter {
	deques := make([][]interface{}, n)
	iters := make([]Iter, n)
	for i := 0; i < n; i++ {
		iters[i] = make(Iter)
	}

	mutex := new(sync.Mutex)

	gen := func(myiter Iter, i int) {
		for {
			if len(deques[i]) == 0 {
				mutex.Lock()
				if len(deques[i]) == 0 {
					if newval, ok := <-it; ok {
						for i, d := range deques {
							deques[i] = append(d, newval)
						}
					} else {
						mutex.Unlock()
						close(myiter)
						break
					}
				}
				mutex.Unlock()
			}
			var popped interface{}
			popped, deques[i] = deques[i][0], deques[i][1:]
			myiter <- popped
		}
	}
	for i, iter := range iters {
		go gen(iter, i)
	}
	return iters
}

// Helper to tee just into two iterators
func Tee2(it Iter) (Iter, Iter) {
	iters := Tee(it, 2)
	return iters[0], iters[1]
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func allCellsDistOrder(R int, C int, r0 int, c0 int) [][]int {
	allDist := make([][]int, 0)
	for r := 0; r < R; r++ {
		for c := 0; c < C; c++ {
			dist := abs(r0-r) + abs(c0-c)
			allDist = append(allDist, []int{r, c, dist})
		}
	}

	// sort by distance
	sort.SliceStable(allDist, func(i, j int) bool {
		return allDist[i][2] < allDist[j][2]
	})

	// remove distance from the slice
	ret := make([][]int, 0)
	for _, elem := range allDist {
		elem = elem[:2]
		ret = append(ret, elem)
	}
	return ret
}

func main() {
	fmt.Println(allCellsDistOrder(2, 3, 1, 2))
}
