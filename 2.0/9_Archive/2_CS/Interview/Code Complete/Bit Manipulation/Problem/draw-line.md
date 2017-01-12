# Draw Line

A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows). The height of the screen, of course, can be derived from the length of the array and the width. Implement a function that draws a horizontal line from (x1, y) to (x2, y).

The method signature should look something like:

    drawLine(byte[] screen, int width, int x1, int x2, int y)

## Solution

按照题意进行计算

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public static void drawLIne(byte[] screen, int width, int x1, int x2, int y){
    int startOffset = x1 % 8;
    int endOffset = x2 % 8;

    int firstFullByte = x1 / 8;
    if (startOffset != 0){
        firstFullByte++;
    }

    int lastFullByte = x2 / 8;
    if (endOffset != 7){
        lastFullByte--;
    }

    for (int i = firstFullByte; i < lastFullByte; i++){
        screen[(width/8) * y + i] = (byte) 0xFF;
    }

    byte startMask = (byte) (0xFF >> startOffset);
    byte endMask = (byte) ~(0xFF >> (endOffset+1));

    if ((x1/8) == (x2/8)){
        byte mask = (byte) (startMask & endMask);
        screen[(width/8)*y + (x1/8)] |= mask;
    }
    else{
        if (startOffset != 0){
            int number = (width/8)*y + firstFullByte - 1;
            screen[number] |= startMask;
        }
        if (endOffset != 7){
            int number = (width/8)*y + lastFullByte + 1;
            screen[number] |= endMask;
        }
    }
}
```

