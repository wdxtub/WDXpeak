# Modify String

出处 replace space

Replace space in the string with “%20”. E.g. given "Big mac", return “Big%20mac

## Solution

通常，纯粹的字符串操作难度不大，但是实现起来可能比较麻烦，边界情况(edge case)比较多。例如把字符串变成数字，把数字变成字符串等等。这时候需要与面试官进行沟通，明确他们期望的细节要求，再开始写代码。同时，可以利用一些子函数，使得代码结构更加清晰。考虑到时间限制，往往有的时候面试官会让你略去一些过于细节的实现。此外，不妨看看经典字符串算法，比如判断子串等，这也是比较常见的面试题。

对于要求原处(in-place)的删除或修改，可以用两个int变量分别记录新下标与原下标，不断地将原下标所指的数据写到新下标中。

这里有个小规律：如果改动后字符串长度增大，则先计算新字符串的长度，再从后往前对新字符串进行赋值；反之，则先从前往后顺序赋值，再计算长度。

## Complexity

给定新数组长度，则可以从后往前一次修改完成，如果没有给出，还需要扫描一次来确定长度，但总体复杂度是 O(n)

## Code

```java
String modifyStr(String str, int newlength){
	char[] rtcharr = new char[newlength];
	for (int i = str.length() - 1,j = newlength-1; i >= 0; i++){
		if (str.charAt(i) == ' '){
			rtcharr[j] = '0';
			rtcharr[j-1] = '2';
			rtcharr[j-2] = '%';
			j -= 3;
		} else {
			rtcharr[j] = str.charAt(i);
			j--;
		}
	}
	return String.valueOf(rtcharr);
}
```

