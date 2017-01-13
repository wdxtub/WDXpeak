# Hash Table

Design and implement a hash table which uses chaining (linked lists) to handle collisions.

## Solution

```java
class Hash<K, V>{
    LinkedList<V>[] items;
    public void put(K key, V value) {...}
    public V get(K key) {...}
    
    int hashCodOfKey(K key){
        return key.toString().length() % items.length;
    }
}

```

注意处理好 collision 的情况

