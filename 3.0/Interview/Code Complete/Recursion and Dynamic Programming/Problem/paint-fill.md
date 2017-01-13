# Paint Fill

Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color.

## Solution 

DFS 遍历一次即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
// can also be done with BFS

enum Color {Red, Orange, Yellow, Green, Blue, Purple}

private static void PaintFill(Color[][] screen, int r, int c, Color color){
    if (screen[r][c] == color)
        return;
    PaintFill(screen, r, c, screen[r][c], color);
}

private static void PaintFill(Color[][] screen, int r, int c, Color o, Color n){
    if (r < 0 || r >= screen.length || c < 0 || c >= screen[0].length){
        return;
    }
    if (screen[r][c] == o){
        screen[r][c] = n;
        PaintFill(screen, r-1, c, o, n);
        PaintFill(screen, r+1, c, o, n);
        PaintFill(screen, r, c-1, o, n);
        PaintFill(screen, r, c+1, o, n);
    }
}
```

