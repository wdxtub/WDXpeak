# Java 概念/算法/设计模式 复习

面试中除了做题目，还有一些口头的交流是关于概念、算法对比、设计模式以及语言细节的，这里对 Java 部分做一个简单的总结。因为是在美国这边找工作比较需要，所以主要是英文为主。

## 概念

这一部分主要是 Java 中基本的概念以及常见的数据结构对比

### Object Oriented

+ model organized around objects rather than actions and data rather than logic
+ based on the concept of "objects"
+ contain data in the form of fields(attributes)
+ code in the form of procedures(methods)
+ object's procedures can access and modify the data fields of the associated object

**OOP**

+ polymorphism
  - define more than one function with the same name
  - compile time polymorphism(overloading) and runtime polymorphism(overriding)
  - method override: a class method has same name and signature as a method in parent class, JVM determines the proper method to call at runtime
  - method overloading: method with same name but different signature, determined at compile time
  
+ inheritance
  - allow a child class to inherit some properties from its parent class
  - use `extends` keyword
  - only public and protected access modifiers can be accessed in child class
  
+ multiple inheritance
  - Java does not support multiple inheritance
  - diamond problem
  - use of multiple interfaces (or extend a class and implement some interfaces)
  
    ```
      interface A{
         add();
      }
      interface B{
         add();
      }
      class C implements A,B{
         add();
      }
     ```
+ abstraction
  - convert real world objects in terms of class
  
+ encapsulation
  - achieved by combining the methods and attribute into a class
  - class acting like a container encapsulation the properties
  - hide how things work and expose the user requests

---

### Java Keywords

+ Access modifiers

  | modifier | access in same package | access in different package |
  | :------: | :--------------------: | :-------------------------: |
  | private  |         no             |          no                 |
  | public   |         yes            |         yes                 |
  | default  |         yes            |          no                 |
  | protected|         yes            |     only if extend class    |  
  
+ `final` keyword
  - can be assigned to variable, method, class, object
  - if assigned
     - variable: behave like a constant and cannot change value
     - method: cannot be overridden in its child class
     - class: no other class can extend it
     - object: only instantiated once

+ `synchronized` keyword
   - provide lock on the object and prevent race condition
   - can be applied to static/non-static methods or block of code
   - only one thread at a time can access synchronized methods
   - if multiple threads, need to wait for execution complete
   
+ `volatile` keyword
   - volatile variable stored in main memory
   - every thread can access 
   - local copy updated from main memory
   - has performance issues
   
+ `static` variable
   - `static` cannot be used for class
   - everything declared as `static` is related to class not object
   - multiple objects of a class share the same instance of static variable
   
+ `static` method
   - can be accessed without creating the objects
   - use class name to access static method
   - static method can only access static variables and not local or global non-static variable: because if the class is not instantiated and therefore the variables are not initialized and cannot be accessed from a static method
   - static method can only call static methods and not non-static methods
   - non-static methods can call static methods
   
+ static class
  - class cannot be declared as static
  - class is static if all variables and methods are static and constructor is private, so the only way to access is to use class name 

+ `throw` keyword
  - throw exception manually
  - used when program fails the condition and wants to give warning
  - throw the exception from a method to the calling method
  - calling method can decide to handle exception or throw to its calling method

---

### Concepts

+ object vs. class
  - an object is an instance of a class
     + object refers to an actual instance of a class
     + every object must belong to a class
     + objects are created and then destroyed, only live in the program for limited time
  - objects have a lifespan but classes do not
     + properties of objects can change while they live
  
+ `static` and `instance` method
   - instance method
     - belong to the instance of a class and require the instance before it can be called
     - dynamic binding
     - JVM selects the method to invoke based on the type of object reference, known at run time 
   - static method
     - belong to the class itself
     - static binding 
     - JVM selects the method to invoke based on the actual class of the object, known at compile time
     
+ `abstract` class and `interface`
   - abstract class
     + contain at least one abstract method
     + can contain numbers of concrete methods
     + variable can be `public`, `private`,`protected`, `default`, or constants
     + a class can only extend one abstract class
     + not compulsory to implement all methods
     + if want to add a new feature, simply implement in the abstract class and call it from subclass
   - interface
     + only contain abstract methods
     + variable is by default `public final`, only has constants
     + a class can implement multiple interfaces
     + compulsory to implement all methods
     + if want to add a new feature, need to implement the method in all classes implementing the interface
     
+ `instanceof` and `isInstance(Object obj)`
   - `instacneof` is a keyword but `isInstance()` is a method
   - `instanceof` check whether the object is type of particular class or subclass
   - `isInstance()` only used to identify if object is of a particular class
   
+ pass by value and pass by reference
  - Java only supports pass by value, actual value is passed
  - Java passes the references by value, the pointer to the object is passed as value
  - references passed to the method are actually copies of the original references
  
+ `==` and `equals()`
  - `==` is used to compare the references of the objects
  - `equals()` can compare the values of two objects
  
+ `StringBuffer` and `StringBuild`
  - `StringBuffer` is synchronized but `StringBuild` is not
  
+ `final`, `finally`,`finalize()`
  - `final`: a final variable acts like constant, a final method cannot be overridden, a final class is immutable
  - `finally`: handles exception, clean up after try block
  - `finalize()`: method helps in garbage collection, invoked before an object is discarded by the garbage collector, allowing it to clean up its state
  
+ static block and init block
  - static block is loaded when class is loaded by JVM for the first time
  - init block is loaded every time the class is loaded
+ object reflections
  - provide a way to get reflective information of class and object
  - perform operations such as
    + get information about methods and fields present inside the class at runtime
    + get a new instance of a class
    + get and set object fields directly by getting field reference, regardless what the access modifier is
  - advantage
    + help in observing or manipulating runtime behavior
    + help in debugging or testing programs
    + can call method by name when we do not know the method in advance  

- nested class
  + when make something a nested class, it is placed inside of another class which is the outer class
  + must use `static` to signify it is nested; without `static`, it would be inner class
  + nested class can be made private so that it is inaccessible from classes outside outer class
- inner class
  + when declare inner class, compiler adds implicit reference to outer class that caused the inner class's construction
  + The inner class is useful in a situation in which each inner class object is associated with exactly one instance of an outer class object. In such a case, the inner class object can never exist without having an outer class object with which to be associated

---

### List

**Iterator**

- if structural change is made(add, remove, clear), iterator is no longer valid
- if iterator invokes its remove method, then iterator is still valid
- main advantage of remove method from iterator is that Collection's remove method must first find the item to remove

**ArrayList**

- advantage
  + calls to get and set take constant time
- disadvantage
  + insertion and removal might be expensive unless changes are made at the end of arraylist
  + inefficient for search
  + notation of capacity(size of underlying array)
- operation
  + get, set: O(1)
  + insertion(add to front) and removal: O(n)


**LinkedList**

- advantage
  + insertion and removal is cheap(constant time), provided the position of the changes is known
- disadvantage
  + not easily indexable
  + calls to get and set might be expensive
  + inefficient for search
- operation
  + get, set: O(n)
  + insertion, removal: O(1)

**Stack**

- operation
  + push: O(1)
  + pop: O(1)
- implementation
  + list: push is to add node to the front of list and pop is to remove from front of list
  + array: topOfStack is initialized to -1, when push, arr[topOfStack++]=element; when pop, return arr[--topOfStack]; use topOfStack==-1 to check if emtpy
- applications
  + balance symbols
  + postfix expression
  + infix to postfix conversion
  + method calls

**Queue**

- idea
  + insertion is done at one end
  + deletion is doen at the other end
- operation
  + enqueue: O(1)
  + dequeue: O(1)

---

### Tree

**General trees**

- representation
  + first child + next sibling for tree node
  
  ``` 
      class TreeNode{
         Object element;
         TreeNode firstChild;
         TreeNode nextSibling;
  ```
- traversal
  + preorder traversal
     - root->left->right
     - application in file system(list all files in directory)
    
     ```
     public void listAll(){
        listAll(0);
     }
     
     public void listAll(int depth){
        printFileName(depth);
        if(isDirectory()){
           for each file in the directory
               listAll(depth+1)
        }
     }
	 ```
  + postorder traversal
     - left->right->root
     - compute size of directory
    
    ```
    public int dirSize(){
        int totalSize = sizeOfFile();
        if(isDirectory()){
          for each file f in directory
              totalSize += c.dirSize()
        }
        return totalSize;
    }
   ```
   + levelorder traversal
   + inorder traversal
     - left->root->right

- application
  + file system


**Binary Tree**

- overview
  + average depth is O(sqrt(N)), worst case depth is N-1
  + for binary search tree, average depth is O(logN)
- representation
   
  ``` 
  class BinaryNode{
     Object element;
     BinaryNode left;
     BinaryNode right;
  }
  ```
- application
  + expression tree
    - push operands to stack while reading
    - if see an operator, pop two trees(operands) from stack, build a new tree and push onto the stack

**Binary Search Tree**

- overview
  + values in left subtree less than root value
  + values in right subtree larger than root value

- operations
  + time O(depth), for average depth, time O(logn)

- balance and self-adjusting


**AVL Tree**

- overview
  + almost identical to binary search tree
  + for every node, height of left and right subtree differ at most 1

- rotation

---

### Hashing

**overview**

+ perform insertion, deletion, searching in average O(1) time
+ print in sorted order in O(n) not supported
+ load factor: ratio of number of elements in the hash table to the table size

**hash function**

+ determinism: given an input, always generate the same value
+ uniformity: map inputs as evenly as possible over its output range
+ defined range: desirable that outputs of hash function have fixed size
+ continuity: a hash function that is used to search for similar data must be as continuous as possible, two inputs differing a little should be mapped to nearly equal hash values
+ non-invertible: impossible to reconstruct input from hash value

**collisions**

+ given inputs map to the same hash value
+ separate chaining
	- idea: keep a list elements that hash to the same value
	- operations
		+ search: first determine which list to traverse and then search appropriate list
		+ insertion: first check appropriate list to see whether element is already in place(if duplicates allowed, keep an extra field); if element is new, insert into the front of list because recently inserted elements are more likely to be used in the near future
  - disadvantage
     + using linkedlist
     + slow down time to allocate new cells
     + require implementation of another data structure

**rehashing**

+ when table gets too full, operations start taking too long
+ solution: build another table with twice size, compute new hash value for new table
+ running time: O(n)
+ options
	- rehash as soon as table is half full
	- rehash only when an insertion fails
	- rehash when table reaches a certain load factor

**hash tables with worst O(1) time**

---

### Heap(Priority Queue)

**structure property**

+ a heap is a binary tree that is completely filled(exception at the bottom level), the average height of complete binary tree is O(logN)
+ for any element in array position i
	- left child: 2i
	- right child: 2i+1
	- parent: floor(i/2)
+ heap consists of Comparable objects
 
**heap order property**

+ smallest(largest) element at the root
+ min-heap: for every node X, key in the parent of X is <= key in X
+ order property ensures findMin() in O(1) time

**operations**

+ insert()
	- create a hole in next available position, if order property not violated, done; otherwise, heapify up
	- time O(logN) if inserted element is new minimum(maximum)
+ deleteMin()
	- find minimum is easy
	- removing minimum will create a hole in the root, we must move last element X in the heap to correct position
	- put X in correct spot along a path from the root containing minimum children(heapify down)
	- time: worst O(logN), average O(logN)
+ decreaseKey()
	- lowers the value of item at position p by positive amount
	- if violate order property, heapify up
	- application: make something with higher priority
+ increaseKey()
	- increase the value of item at position p by positive amount
	- if violate order property, heapify down
	- application: scheduler drops the priority of a process that is consuming excessive CPU time
+ delete()
	- remove node at position p
	- first perform decreaseKey(p,infinity) then perform deleteMin()
	- application: process terminated by user
+ buildHeap()
	- done with N successive inserts
	- insert takes O(1) average, O(logN) worst
	- build takes O(N) average, O(NlogN) worst			
**applications**

+ selection problem
	- approach one(k smallest elements)
		+ read N elements into array and buildHeap
		+ perform k deleteMin()
		+ time: buildHeap O(N), deleteMin O(logN), total is O(N+klogN)
	- approach two(k largest elements)
		+ idea: at any time, maintain a set of k largest elements
		+ read first k elements
		+ when a new element is read, compare it with kth largest element Sk(Sk is the smallest element in set S)
			- if new element is larger, it replaces Sk
			- otherwise, do nothing
		+ finally, return the smallest element in S
		+ time: build with first k elements O(k), time to process remaining (N-k)O(logk), total is O(k+(N-k)logk) = O(Nlogk)
+ event simulation

---

### Collections

+ `ArrayList` vs. `vector`
  - synchronization
     + ArrayList is not thread-safe but vector is 
     + each method in vector class is surrounded by a synchronized block
  - data growth
     + both use arrays to store contents
     + enlarge array if not enough space
  - performance
     + vector is slower than arraylist because of thread-safe
    
+ Sort objects in lists
  - implement Comparable interface for the object class and override compareTo() method
  - if object class is a jar file, create Comparator and override compare() method
  - call Collection.sort()
  
+ `HashMap` vs. `HashTable`
  - HashMap is not synchronized but HashTable is
  - use Iterator for HashMap(fail-safe) and enumerator for Hashtable(not fail-safe)
  - HashMap allows null values and only one null key; Hashtable does not allow null key or null value
  
+ List interface
  - `ArrayList`
     + resizable array implementation
     + dynamic size
     + not thread-safe
  - `Vector`
     + ArrayList implementation
     + thread-safe
  - `LinkedList`
     + also implements Queue interface
     + FIFO
     + faster for insertion and deletion
    
+ Set interface
  - `SortedSet`
     + interface extends Set
     + allow data to be sorted
     + all elements inserted must implement Comparator or Comparable interface
  - `TreeSet`
     + implementation of SortedSet interface
     + O(logn) time for add, remove, contains operations
     + not synchronized
  - `HashSet`
     + implements Set interface
     + back up by hash table
     + no guarantee on constant order
     + allow null element
     + O(1) time for add,remove,contains
    
+ `Arrays` vs. `ArrayList`
  - arrays are fixed size but ArrayLists are dynamic
  - elements in the array list can be added or removed at runtime
  - array contains elements of same type but arraylist can contain elements of different type
  
+ `ArrayList` vs. `LinkedList`
  - both fast in insertion, inserting into arraylist and into first position of linkedlist takes O(1) time
  - random lookup in ArrayList is fast, but slow for LinkedList
  - remove is slow for ArrayList(elements need to be shifted) but fast for LinkedList
  
+ Advantage of iterator
   - used when no clue about object type
   - iterator allows updates
   
+ Preferred declaration
  - `List<String> list = new ArrayList<String>()` not `ArrayList<String> list = new ArrayList<String>()`
  - because function may take List as parameter
  - more flexible
  
+ Iterator access vs. index access
  - insert,update,or delete is faster for iterator access for elements in between the structure
  - insert,update,or delete is faster for index access for elements at the end
  - search is fast for index access

---

### Linkedlist vs. Arraylist vs. Vector

**Operations**

+ LinkedList
	+ get(index): O(n)
	+ add(element): O(1)
	+ add(index, element): O(n)
	+ remove(index): O(n)
	+ Iterator.remove(): O(1), main benefit
	+ Iterator.add(element): O(1), main benefit
+ ArrayList
	+ get(index): O(1), main benefit
	+ add(element): O(1) amortized, worst case O(n) because need to resize array and copy
	+ add(index, element): O(n-index) amortized, worst case O(n)
	+ remove(index): O(n-index), remove last is O(1)
	+ Iterator.remove(): O(n-index)
	+ Iterator.add(element): O(n-index)

**Compare**

+ Linkedlist
	+ O(1) time insertions or removals using iterator, but only sequential access
	+ finding a position in the linkedlist takes time O(n)
	+ each element of linkedlist have more memory overhead because pointers need to be stored
	+ linkedlist also implements queue interface which adds more methods such as offer(), peek(), poll()
+ Arraylist
	+ fast random read access in O(1)
	+ adding or removing element except at the end require shifting latter elements, if add more elements, need to allocate new array and copy old values
	+ iterating over arraylist is technically faster
	+ to avoid overhead of resizing, construct arraylist with initial capacity

**Similarities**

+ both are implementation of list interface
+ maintain elements in insertion order
+ non-synchronized, but can be made synchronized explicitly
+ if list is structurally modified after iterator is created, except through iterator's own remove or add method, iterator will throw exception

**When to use which**

+ frequent addition and deletion: linkedlist
+ frequent search: arraylist
+ less memory to store many elements: arraylist

**Vector**

+ almost identical to arraylist, but is synchronized
+ more overhead because of synchronization
+ still use arraylist because they can make it synchronized explicitly

---

### HashMap vs. TreeMap vs. HashTable vs. LinkedHashMap

**Overview**

- HashMap: implemented as a hash table, no ordering on keys or values
- TreeMap: implemented based on red-black tree, ordered by key
- LinkedHashMap: preserves insertion order
- HashTable: synchronized in constrast to HashMap

**HashMap**

- operation
	+ put(): average O(1), worst O(n) when collision
	+ get(), remove(): O(1)
- if key is self-defined objects, need to implement equals() and hashCode()
- iteration order not predictable
- does not allow two identical elements
	+ equals(): return true if two references refer to the same object
	+ hashCode(): return distinct integers for distinct objects
- allow null keys and values

**TreeMap**

- operation
	+ put(), get(), remove(): worst O(logn)
- sorted by keys
- object for key has to implement Comparable interface
- only allow values to be null

**HashTable**

- HashMap is roughly equivalent to HashTable, except hashmap is not synchronized and permits null

**LinkedHashMap**

- operation: see arraylist
- subclass of HashMap
- linkedlist preserves the insertion order
- allow null keys and values

---

### Set vs. List vs. Map

**Set**

- unordered collection
- unique objects (!e1.equals(e2))
- contains at most one null

**List**

- ordered collection(sequence)
- access by index and search
- may contain duplicates
- user has control over where element inserted

**Map**

- object that maps keys to values
- no duplicated allowed
- a key can map to at most one value

---

### Tree vs. Graph

- tree is restricted form of a graph(directed acyclic graph)
- trees have direction(parent/child relationship)
- tree does not contain cycles
- in trees, a child can only have one parent

---

### Threading

**Thread vs. Process**

- definition
	+ process: executing instance of an application
	+ thread: a path of execution within a process
- relationship
	+ a process can contain multiple threads
	+ thread considered as lightweight process
- comparison
	+ thread for small tasks, process for heavy tasks
	+ thread within the same process share the same address space(allow threads to read and write data to the same structures and variables, allow communication between threads), but different processes do not
	+ threads are easier to create than processes because they do not require a separate address space
	+ multi-threading: be careful that threads share structures that should be modified by one thread at a time
	+ processes are independent of each other

## 算法

这一部分主要是算法思路的对比

### BST vs. HashTable

**BST**

- insert and retrieve: O(logn)
- store data sorted
- no need to know size of input in advance
- memory efficient: do not reserve more memory than they need to

**HashTable**

- insert and retrieve: O(1)
- elements stored unsorted
- with more inputs, collisions may show up
- need more space than input data if to avoid collision
- need to know data size, otherwise might need to resize the table

---

### BFS vs. DFS

**Overview**

+ search algorithms for graphs and trees
+ used for unordered graph and tree
+ graph representation
	- adjacent list: space O(V+E)
	- adjacent matrix: space O(V^2)

**BFS**

+ start with root node
+ scan each node in the each level
+ while traversing each level, decide if target is found
  
**DFS**

+ start with root node
+ follow on branch as far as possible until target is found or hit a leaf node
+ if hit a leaf node, continue search at the nearest ancestor

**Comparison**

+ memory
	- BFS uses a large amount of memory because need to store pointers to a level(serious problem if the tree is very wide)
	- DFS uses less memory because no need to store all child pointers at a level
+ depend on the data you search for
	- look for people alive in family tree: DFS because targets are likely to be on the bottom of the tree
	- look for people who died: BFS
+ implementation
	- BFS: queue

    ```
      procedure BFS(G,v)
         initialize a queue Q
         Q.push(v)
         label v as visited
         while Q is not empty
            v <- Q.pop()
            for all edges from v to w in adjacent(v)
                if w is not visited
                   Q.push(w)
                   label w as visited
    ```

	- DFS: stack
		+ recursive

        ```
          procedure DFS(G,v)
             label v as visited
             for all edges from v to w in adjacent(v)
                 if w is not visited
                     DFS(G,w)
        ```
     + iterative

        ```
           procedure DFS(G,v)
              initialize stack S
              S.push(v)
              while S is not empty
                 v <- S.pop()
                 if v is not visited
                    label v as visited
                       for all edges from v to w in adjacent(v)
                           S.push(w)
        ```
+ solution
	- BFS: complete algorithm, give optimal solution
  - DFS: suboptimal solution
+ complexity
  - BFS: worst time O(V+E), worst space O(V)
  - DFS: worst time O(v+E), worst space O(V)

---

### Bubble Sort

**Idea**

- compare each item wth the item next to it, and swap positions if needed
- algorithm repeats until we have a pass without swapping any elements

**Implementation**

- for every step, move largest element in left unsorted array to the end; in this caes, avoid inner loop to iterate through right sorted subarray
- for every step, swap unordered adjacent pair until no swap is needed 
- note that in one pass, more than one element can be placed into their final positions, so the position after last swap is sorted and do not need to traverse again

**Application**

- to find k largest/smallest, use outer loop of bubble sort for k times

**Analysis**

- Time O(n^2)
- Space O(1)
- ability to detect that list is sorted is build into the algorithm
- large elements at the beginning get swapped quickly to the end, but small elements at the end get swapped very slowly to the beginning

**Variants**

- Odd Even Sort: compare all (odd,even) indexed pairs of adjacent elements, if a pair is in the wrong order, switch elements; then alternate between (odd,even) and (even,odd) pairs
- Cocktail Sort: solve the rabbit turtle problem

---

### Insertion Sort

+ The idea is to remove one entry at a time and insert it into the correct position in the sorted part.
+ Analysis 
  - Time O(n^2)
  - Space O(1)

### Selection Sort

+ The idea is to select the smallest element of remaining array and then swap it to the front.
+ Analysis 
  - Time O(n^2)
  - Space O(1)

---

### Merge Sort

+ Use divide and conquer paradigm
+ Procedure
  - divide array into two subarrays
  - sort each subarray
  - merge sorted subarrays into one
+ Analysis
  - Time O(nlogn)
  - Space O(nlogn)

### Bucket Sort

**Idea**

- partition array into buckets
- sort each bucket, or recursively call bucket sort
- merge sorted buckets

**Drawbacks**

- how to handle duplicates: store duplicates into linkedlist or counting sort
- must know min and max value in the original array
- enough memory

**Optimization**

- first partition into unsorted buckets, put unsorted elements in the buckets into the original array, then run insertion sort over the entire array
  + insertion sort's performance is based on how far element is from its final position in sorted order
  + cache friendly because of contiguous use of memory

**Variants**

- Generic bucket sort
  + find max, divide into n buckets with size M/n
  + use insertion sort in each bucket
  + expected linear time
  + bad performance when many elements fall into a single bucket(clustering)
- Histogram sort(counting sort)
  + first count the number of elements that will fall into each bucket
  + use the information to arrange buckets in place
  + no space overhead for bucket storage

**Analysis**

- Time O(n)
- Space O(n)
- when bucket size is 1, equivalent to counting sort
- when use two buckets, equivalent to quick sort, but random choice of pivot in quicksort makes it more resistant to clustering problem

## 设计模式

设计模式主要可以分为以下几个类别：

+ Creational Patterns
  - hide creation logic
+ Structural Patterns
  - class and object composition
+ Behavioral Patterns
  - communication between objects
+ J2EE Patterns

### Factory Pattern

+ create an interface

``` 
public interface Shape{
	 void draw();
}
```

+ create concrete classes

``` 
public class Rectangle implements Shape{
   @Override
   public void draw(){
      System.out.println("Inside Rectangle");
  }
}
```

``` 
public class Circle implements Shape{
   @Override
   public void draw(){
      System.out.println("Inside Circle");
  }
}
```

+ create factory to generate concrete classes

``` 
public class ShapeFactory{
   public Shape getShape(String type){
      if(type == null){
         return null;   
      }
      if(shape.equalsIgnoreCase("Rectangle")){
        return new Rectangle();
      }
      if(shape.equalsIgnoreCase("Circle")){
        return new Circle();
      }
      return null
   }
}
```

+ demo

``` 
public class Demo{
   ShapeFactory factory = new ShapeFactory();
   Shape circle = factory.getShape("Circle");
   circle.draw();
   Shape rectangle = factory.getShape("Rectangle");
   rectangle.draw();
}
```

---

### Singleton Pattern

+ create singleton class

``` 
public class SingleObject{
   private static SingleObject ins = new SingleObject();

   private SingleObject(){}

   public static SingleObject getInstance(){
   	   return ins;
   }

   public void show(){
   	   System.out.println("Hello");
   }
}
```

+ demo

``` 
public class Demo{
   public static void main(String[] args){
       SingleObject obj = SingleObject.getInstance();
       obj.show();
   }
}
```

---

### MVC Pattern

+ Model-View-Controller
  - Model: represent object, can have logic to update controller if its data changes
  - View: represent visualization of data from Model
  - Controller: act on Model and View, control data flow into Model and update View when data changes

+ Structure
  - app: models, views, controllers
  - config: global server configurations
  - lib: assorted libraries

+ Procedure
  - server routes the request to certain controller
  - controller interprets the request, load reqested information from models
  - controller passes information from model to view
  - final view is sent to user

+ Model

``` 
   public class Student{
       private String id;
       private String name;

       public String getId(){
           return id;
       }

       public String getName(){
           return name;
       }

       public void setId(String id){
           this.id = id;
       }

       public void setName(String name){
           this.name = name;
       }	
    }
```

+ View

``` 
public class StudentView{
   public void printInfo(String studentName, String studentId){
        System.out.println("Student: " + studentName);
        System.out.println("Student ID: " + studentId);
   }
}
```

+ Controller

``` 
public class StudentController{
   private Student model;
   private StudentView view;

   public StudentController(Student model, StudentView view){
   	   this.model = model;
   	   this.view = view;
   }

   public void setStudentName(String name){
   	   model.setName(name);
   }

   public void setStudentId(String id){
   	   model.setId(id);
   }

   public String getStudentName(){
   	   return model.getName();
   }

   public String getStudentId(){
   	   return model.getId();
   }

   public void updateView(){
   	   view.printInfo(model.getName(), model.getId());
   }
}	
```

+ Demo

``` 
public class Demo{
  public static void main(String[] args){
      Student model = getStudentFromDatabase();
      StudentView view = new StudentView();
      StudentController controller = new StudentController(model,view);

      controller.updateView();

      controller.setStudentName("Other name");
      controller.updateView();
  }
}
```



