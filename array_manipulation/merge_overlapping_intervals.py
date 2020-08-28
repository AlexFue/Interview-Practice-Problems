Problem:
Given a collection of intervals, merge all overlapping intervals.

For example:
Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.




Solution:
def merge_overlapping_intervals(intervals):
  index = 0
  while index < len(intervals)-1:
    if intervals[index+1][0] > intervals[index][0] and intervals[index+1][0] < intervals[index][1]:
      intervals[index][1] = intervals[index+1][1]
      del intervals[index+1]
    else:
      index += 1
  return intervals




Process:
we want to merge every two intervals if the first number of the second intervals is in between the first interval. if not then just go one more interval to the right and check again
example: [1,4],[2,5] = 2 is inbetween 1 and 4 so we would merge, making the range of [1,4] to [1,5] and then delete the [2,5] interval


index = 0

loop while index is less than length of intervals list

	if the first number of the interval to the right is in between the numbers of the current interval

		set the current interval's last number to that of the interval on the right

		delete the interval to the right

	else then increment the index

return intervals list