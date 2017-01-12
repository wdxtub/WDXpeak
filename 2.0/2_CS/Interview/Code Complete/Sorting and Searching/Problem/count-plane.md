+ 难度：中等

给出飞机的起飞和降落时间的列表，用 interval 序列表示. 请计算出天上同时最多有多少架飞机？

样例

    对于每架飞机的起降时间列表：[[1,10],[2,3],[5,8],[4,7]], 返回3。

注意

    如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。

## 题解

将interval的开始和结束都看做一个point，进行排序。对于排好序的数组遍历，如果当前point是interval的开始点，那么cur++，否则cur–-。

## Solution

```java
/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * @param intervals: An interval array
     * @return: Count of airplanes are in the sky.
     */
    public int countOfAirplanes(List<Interval> airplanes) {
        if (airplanes == null || airplanes.size() == 0) {
            return 0;
        }
        //this round of sort is to make sure landing takes place before flying, if
        //they happen at the same time
        Collections.sort(airplanes, new Comparator<Interval>() {
            public int compare(Interval i1, Interval i2) {
                return Integer.compare(i1.start, i2.start);
            }
        });
        Point[] points = new Point[airplanes.size()*2];
        for (int i = 0; i < airplanes.size(); i++) {
            points[i*2] = new Point(airplanes.get(i).start, true);
            points[i*2 + 1] = new Point(airplanes.get(i).end, false);
        }
        Arrays.sort(points, new Comparator<Point>(){
            public int compare(Point i1, Point i2) {
                return Integer.compare(i1.time, i2.time);
            }
        });
        int res = 0;
        int cur = 0;
        for (Point p : points) {
            if (!p.isStart) {
                cur--;
            } else {
                cur++;
                res = Math.max(res, cur);
            }
        }
        return res;
    }

    class Point {
        int time;
        boolean isStart;
        public Point(int time, boolean isStart) {
            this.time = time;
            this.isStart = isStart;
        }
    }
}

```

