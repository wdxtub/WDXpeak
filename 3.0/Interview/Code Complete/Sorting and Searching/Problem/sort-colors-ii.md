给定一个有n个对象（包括k种不同的颜色，并按照1到k进行编号）的数组，将对象进行分类使相同颜色的对象相邻，并按照1,2，...k的顺序进行排序。

样例

    给出colors=[3, 2, 2, 1, 4]，k=4, 你的代码应该在原地操作使得数组变成[1, 2, 2, 3, 4]

注意

    不能使用代码库中的排序函数来解决这个问题

挑战

    一个相当直接的解决方案是使用计数排序扫描2遍的算法。这样你会花费O(k)的额外空间。你否能在不使用额外空间的情况下完成？

## 题解

inplace，并且O(N)时间复杂度的算法。

我们可以使用类似桶排序的思想，对所有的数进行计数。

1. 从左扫描到右边，遇到一个数字，先找到对应的bucket.比如 3 2 2 1 4 第一个3对应的bucket是index = 2 (bucket从0开始计算）
2. Bucket 如果有数字，则把这个数字移动到i的position(就是存放起来），然后把bucket记为-1(表示该位置是一个计数器，计1）。
3. Bucket 存的是负数，表示这个bucket已经是计数器，直接减1. 并把color[i] 设置为0 （表示此处已经计算过）
4. Bucket 存的是0，与3一样处理，将bucket设置为-1， 并把color[i] 设置为0 （表示此处已经计算过）
5. 回到position i，再判断此处是否为0（只要不是为0，就一直重复2-4的步骤）。
6.完成1-5的步骤后，从尾部到头部将数组置结果。（从尾至头是为了避免开头的计数器被覆盖）

例子(按以上步骤运算)：

    3 2 2 1 4
    2 2 -1 1 4
    2 -1 -1 1 4
    0 -2 -1 1 4
    -1 -2 -1 0 4
    -1 -2 -1 -1 0

## Code

```java
class Solution {
    /**
     * @param colors: A list of integer
     * @param k: An integer
     * @return: nothing
     */
    public void sortColors2(int[] colors, int k) {
        if (colors == null) {
            return;
        }

        int len = colors.length;
        for (int i = 0; i < len; i++) {
            // Means need to deal with A[i]
            while (colors[i] > 0) {
                int num = colors[i];
                if (colors[num - 1] > 0) {
                    // 1. There is a number in the bucket,
                    // Store the number in the bucket in position i;
                    colors[i] = colors[num - 1];
                    colors[num - 1] = -1;
                } else if (colors[num - 1] <= 0) {
                    // 2. Bucket is using or the bucket is empty.
                    colors[num - 1]--;
                    // delete the A[i];
                    colors[i] = 0;
                }
            }
        }

        int index = len - 1;
        for (int i = k - 1; i >= 0; i--) {
            int cnt = -colors[i];

            // Empty number.
            if (cnt == 0) {
                continue;
            }

            while (cnt > 0) {
                colors[index--] = i + 1;
                cnt--;
            }
        }
    }
}

```

