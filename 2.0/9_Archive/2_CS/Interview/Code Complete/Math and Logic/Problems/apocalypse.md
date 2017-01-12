# The Apocalypse

In the new post-apocalyptic world, the world queen is desperately concerned about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or else they face massive fines. If all families abide by this policy - that is, they have continue to have children until they have one girl, at which point they immediately stop - what will the gender ratio of the new generation be? (Assume that the odds of someone having a boy or a girl on any given pregnancy is equal). Solve this out logically and then write a computer simulation of it

## Solution

```java
public class q6_7 implements IAlgo{
   /**
    * ratio 1:1
    */
    private static int boys = 0;
    private static int girls = 0;
    private static int families = 10000;

    public static void testAlgo(){
        for (int i = 0; i < families; i++){
            Random r = new Random();
            int b = 0;
            int g = 0;
            while (g == 0){
                if (r.nextBoolean()){
                    g++;
                }
                else{
                    b++;
                }
            }
            boys += b;
            girls += g;
            float ratio = girls / (float)(boys + girls);
            System.out.println("#" + (i+1) + " family: G-" + girls + " B-" + boys + " Ratio:" + ratio);
        }
    }
}
```

