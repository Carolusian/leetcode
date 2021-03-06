/*
1024. Video Stitching

You are given a series of video clips from a sporting event that lasted T seconds.  These video clips can be overlapping with each other and have varied lengths.

Each video clip clips[i] is an interval: it starts at time clips[i][0] and ends at time clips[i][1].  We can cut these clips into segments freely: for example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].

Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event ([0, T]).  If the task is impossible, return -1.



Example 1:

Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
Output: 3
Explanation:
We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
Then, we can reconstruct the sporting event as follows:
We cut [1,9] into segments [1,2] + [2,8] + [8,9].
Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
Example 2:

Input: clips = [[0,1],[1,2]], T = 5
Output: -1
Explanation:
We can't cover [0,5] with only [0,1] and [0,2].
Example 3:

Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], T = 9
Output: 3
Explanation:
We can take clips [0,4], [4,7], and [6,9].
Example 4:

Input: clips = [[0,4],[2,8]], T = 5
Output: 2
Explanation:
Notice you can have extra video after the event ends.


Note:

1 <= clips.length <= 100
0 <= clips[i][0], clips[i][1] <= 100
0 <= T <= 100
*/

package main

import (
	"fmt"
)

func findLongestClipStartWith(clips [][]int, start int) []int {
	s, e := start, start
	for _, clip := range clips {
		// find the longest clip which can link up with the previous clip
		clipStart, clipEnd := clip[0], clip[1]
		if clipStart <= s && clipEnd > e {
			e = clipEnd
		}
	}
	if s != e {
		return []int{s, e}
	}
	return nil
}

func videoStitching(clips [][]int, T int) int {
	// clips always start from 0
	s, filtered := 0, make([][]int, 0)
	clip := []int{}
	for {
		clip = findLongestClipStartWith(clips, s)
		if clip != nil {
			end := clip[1]
			s = end
			filtered = append(filtered, clip)
			// if last clip is found
			if end >= T {
				break
			}
		} else {
			// cannot find any clip
			break
		}
	}
	fmt.Println(filtered)
	// return the clips if the last clip covers the end of the event
	length := len(filtered)
	if length > 0 && filtered[length-1][1] >= T {
		return length
	} else {
		return -1
	}
}

func main() {
	clips1 := [][]int{{0, 2}, {4, 6}, {8, 10}, {1, 9}, {1, 5}, {5, 9}}
	clips2 := [][]int{{0, 1}, {6, 8}, {0, 2}, {5, 6}, {0, 4}, {0, 3}, {6, 7}, {1, 3}, {4, 7}, {1, 4}, {2, 5}, {2, 6}, {3, 4}, {4, 5}, {5, 7}, {6, 9}, {9, 100}}
	clips3 := [][]int{{5, 7}, {1, 8}, {0, 0}, {2, 3}, {4, 5}, {0, 6}, {5, 10}, {7, 10}}
	clips4 := [][]int{{0, 5}, {1, 6}, {2, 7}, {3, 8}, {4, 9}, {5, 10}, {6, 11}, {7, 12}, {8, 13}, {9, 14}, {10, 15}, {11, 16}, {12, 17}, {13, 18}, {14, 19}, {15, 20}, {16, 21}, {17, 22}, {18, 23}, {19, 24}, {20, 25}, {21, 26}, {22, 27}, {23, 28}, {24, 29}, {25, 30}, {26, 31}, {27, 32}, {28, 33}, {29, 34}, {30, 35}, {31, 36}, {32, 37}, {33, 38}, {34, 39}, {35, 40}, {36, 41}, {37, 42}, {38, 43}, {39, 44}, {40, 45}, {41, 46}, {42, 47}, {43, 48}, {44, 49}, {45, 50}, {46, 51}, {47, 52}, {48, 53}, {49, 54}}

	fmt.Println(videoStitching(clips1, 10))
	fmt.Println(videoStitching(clips2, 9))
	fmt.Println(videoStitching(clips3, 5))
	fmt.Println(videoStitching(clips4, 50))
}
