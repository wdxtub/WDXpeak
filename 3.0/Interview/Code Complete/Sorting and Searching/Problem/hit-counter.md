# Hit Counter

出处

Given a server that has requests coming in. Design a data structure such that you can fetch the count of the number requests in the last second, minute and hour.

## Solution

对于这个问题，比较容易想到的是对于每个request，我们都分配一个当时的时间戳(timestamp)，并且将request根据时间戳排序，则时间戳构成一个完全有序的序列。这样，当我们要搜索一分钟前的request时，可以用二分查找快速定位。其次，如果我们找到了对应的request，如何最快速地知道从这个request至现在一共发生了多少次其他请求？我们可以采用计数的方式，对于每个request，分配一个计数，用以表示这是第几个request。我们只需要用当前计数减去某个request的计数，就可以知道从那个request至现在一共发生了多少次其他请求。

## Complexity

我们应用二分查找寻找某个特定时间的request，算法涉及的时间复杂度为O(logn)。

## Code 

注意，我们简化了overflow的处理，采用long int并且默认整形数据不会越界。读者可以进一步考虑如何处理越界。

```
#include <time.h>
#include <sys/time.h>
long now() {
    struct timeval time;
    gettimeofday(&time, NULL);
    return (time.tv_sec * 1000000 + time.tv_usec);
}
class HitCounter {
private:
    deque<pair<long, int>> hits;
    long last_count = 0;
    const int second = 1000000;
    const int minute = 60 * second;
    const int hour = 60 * minute;

    void prune() {
        auto old = upper_bound(hits.begin(), hits.end(), make_pair(now() - 1 * hour, -1));
        if (old != hits.end()) {
            hits.erase(hits.begin(), old);
        }
    }

public:
    void hit() {
        hits.push_back(make_pair(now(), ++last_count));
        prune();
    }

    long hitsInLastSecond() {
        auto before = lower_bound(hits.begin(), hits.end(), make_pair(now() - 1 * second, -1));
        if (before == hits.end()) { return 0; }
        return last_count - before->second + 1;
    }

    long hitsInLastMinute() {
        auto before = lower_bound(hits.begin(), hits.end(), make_pair(now() - 1 * minute, -1));
        if (before == hits.end()) { return 0; }
        return last_count - before->second + 1;
    }
    long hitsInLastHour() {
        auto before = lower_bound(hits.begin(), hits.end(), make_pair(now() - 1 * hour, -1));
        if (before == hits.end()) { return 0; }
        return last_count - before->second + 1;
    }
};
```

