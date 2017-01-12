# Animal Shelter

出处

An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeuCat. You may use the built-in LinkedList data structure.

## Solution

设计题

## Complexity

设计题

## Code 

```java
public abstract class Animal{
    private int number;
    public Animal(int n){
        number = n;
    }

    public void setNumber(int n){
        number = n;
    }

    public int getNumber(){
        return number;
    }
}

public class Dog extends Animal{
    public Dog(int n){
        super(n);
    }
}

public class Cat extends Animal{
    public Cat(int n){
        super(n);
    }
}

private LinkedList<Dog> dogs = new LinkedList<Dog>();
private LinkedList<Dog> cats = new LinkedList<Dog>();
private int order = 0;

public void enqueue(Animal a){
    a.setNumber(order++);

    if (a instanceof Dog)
        dogs.addLast((Dog) a);
    else
        cats.addLast((Cat) a);
}

public Animal dequeueAny(){
    if (dogs.size() == 0 && cats.size() != 0){
        return cats.poll();
    }
    else if (dogs.size() != 0 && cats.size() == 0){
        return dogs.poll();
    }
    else if (dogs.size() == 0 && cats.size() == 0){
        return null;
    }

    if (dogs.peek().getNumber() < cats.peek().getNumber()){
        return dogs.poll();
    }
    else{
        return cats.poll();
    }
}
```

