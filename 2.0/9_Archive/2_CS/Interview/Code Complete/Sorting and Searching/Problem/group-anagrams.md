# Group Anagrams

出处

Write a method to sort an array of strings so that all the anagrams are next to each other

## Solution

这并不是一个完全排序的问题，而只要求分类，并且类别一定是有限个，选择用桶排序，类别数量等于桶的数量。对一般的桶排序，每一个不同的值就对应一个桶，而这里则是所有相同字母异序词(anagram)对应一个桶，因此需要找到一个哈希函数，要求是所有相同字母异序词的哈希值相同，对应同一个桶。一种做法是将字符串排序后的结果作为字符串的哈希值。

## Complexity

假定字符串平均长度为k，数量为n，那么平均复杂度为O(klogk*n)。

## Code 

```java
// Use the modification of the bucket sort
public void sort(String[] array){
    HashMapList<String, String> mapList = new HashMapList<String, String>();

    for (String s : array){
        String key = sortChars(s);
        mapList.put(key, s);
    }

    int index = 0;
    for (String key : mapList.keySet()){
        ArrayList<String> list = mapList.get(key);
        for (String t : list){
            array[index] = t;
            index++;
        }
    }

    String sortChars(String s){
        char[] content = sortChars.toCharArray();
        Arrays.sort(content);
        return new String(content);
    }
}
```

