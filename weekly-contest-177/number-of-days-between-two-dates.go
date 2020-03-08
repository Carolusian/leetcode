/**
5169. Number of Days Between Two Dates
User Accepted:21
User Tried:34
Total Accepted:21
Total Submissions:35
Difficulty:Easy
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.



Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15


Constraints:

The given dates are valid dates between the years 1971 and 2100.
*/
package main

import (
	"fmt"
	"log"
	"math"
	"strconv"
	"time"
)

func dateStringToInts(date string) (int, int, int) {
	dt := []rune(date)
	year, err := strconv.Atoi(string(dt[:4]))

	month, err := strconv.Atoi(string(dt[5:7]))

	day, err := strconv.Atoi(string(dt[8:10]))

	if err != nil {
		log.Fatal(err)
	}

	return year, month, day
}

func date(year, month, day int) time.Time {
	return time.Date(year, time.Month(month), day, 0, 0, 0, 0, time.UTC)
}

func daysBetweenDates(date1 string, date2 string) int {
	y1, m1, d1 := dateStringToInts(date1)
	y2, m2, d2 := dateStringToInts(date2)

	dt1 := date(y1, m1, d1)
	dt2 := date(y2, m2, d2)

	return int(math.Abs(dt2.Sub(dt1).Hours() / 24))
}

func main() {
	fmt.Println(daysBetweenDates("2019-06-29", "2019-06-30"))
}
