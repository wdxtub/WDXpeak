# Merge Range

出处 Insert Interval

给出若干闭合区间，合并所有重叠的部分。

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].


## Solution

To check the intersections between interval [a,b] and [c,d],  there are four cases (equal not shown in the figures):

        a____b
    c____d

    a____b
         c____d

    a_______b
        c___d

       a___b
    c_______d

But we can simplify these into 2 cases when check the smaller (smaller start point) interval with the bigger interval.

For the problem, the idea is simple. First sort the vector according to the start value. Second, scan every interval, if it can be merged to the previous one, then merge them, else push it into the result vector.

---

1. compare [1,2] with [4,9], then insert [1,2];
2. merge [3,5] with [4,9], get newInterval = [3,9];
3. merge [6,7] with [3,9], get newInterval = [3,9];
4. merge [8,10] with [3,9], get newInterval = [3,10];
5. compare [12,16] with [3,10], insert newInterval [3,10], then all the remaining intervals...

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

+ Solution 1 : Time O(N).
+ Solution 2 : Time O(Log(N)).

```java
public List<Interval> insert_1(List<Interval> intervals, Interval newInterval) {
        List<Interval> res = new ArrayList<Interval>();
        boolean inserted = false;
        for (Interval it : intervals) {
            if (inserted || it.end < newInterval.start) {
                res.add(it);
            } else if (it.start > newInterval.end) {
                res.add(newInterval);
                res.add(it);
                inserted = true;
            } else {
                newInterval.start = Math.min(newInterval.start, it.start);
                newInterval.end = Math.max(newInterval.end, it.end);
            }
        }
        if (inserted == false) res.add(newInterval);
        return res;
    }
    
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> res = new ArrayList<Interval>();
        int n = intervals.size();
        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (intervals.get(mid).start > newInterval.start) right = mid - 1;
            else left = mid + 1;
        }
        int idxStart = right;
        left = 0; right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (intervals.get(mid).end < newInterval.end) left = mid + 1;
            else right = mid - 1;
        }
        int idxEnd = left;
        if (idxStart >= 0 && newInterval.start <= intervals.get(idxStart).end) {
            newInterval.start = intervals.get(idxStart--).start;
        }
        if (idxEnd < n && newInterval.end >= intervals.get(idxEnd).start) {
            newInterval.end = intervals.get(idxEnd++).end;
        }
        for (int i = 0; i <= idxStart; ++i) {
            res.add(intervals.get(i));
        }
        res.add(newInterval);
        for (int i = idxEnd; i < n; ++i) {
            res.add(intervals.get(i));
        }
        return res;
    }
```

