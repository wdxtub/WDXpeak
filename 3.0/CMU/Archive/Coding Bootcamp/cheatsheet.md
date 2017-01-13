# Cheat Sheet

## 输入输出/循环

```
input
6
1 2 3 4 5 6
```

Java

```java
Scanner in = new Scanner(System.in);
int n = in.nextInt();
int arr[] = new int[n];
for(int arr_i=0; arr_i < n; arr_i++){
  arr[arr_i] = in.nextInt();
}

int sum = 0;
for(int i : arr){
  sum += i;
}
System.out.println(sum);
```

Python

```python
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

sum = 0
for i in range(n):
	sum += arr[i]
```

Javascript

```javascript
var n = parseInt(readLine());
arr = readLine().split(' ');
arr = arr.map(Number);

var sum = 0;
for (var i = 0; i < n; i++){
   sum += arr[i];
}
console.log(sum)
```

