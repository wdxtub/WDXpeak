# Call Center

Imagine you have a call center with three levels of employee: respondent, manager, and director. An incoming telephone call must be first allocated to a respondent who is free. If the respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not free or not able to handle it, then the call should be escalated to a director. Design the classes and data structures for this problem. Implement a method dispatchCall() which assigns a call to the first available employee.

## Solution

Details can be seen in the code:

```java

public class CallHandler{
    private final int LEVELS = 3;
    
    private final int NUM_RESPONDENTS = 10;
    private final int NUM_MANAGERS = 4;
    private final int NUM_DIRECTORS = 2;
    
    List<List<Employee>> employeeLevels;
    
    List<List<Call>> callQueues;
    
    public void dispatchCall(Caller caller){
        Call call = new Call(caller);
        dispatchCall(call);
    }
    
    public void dispatchCall(Call call) {
        Employee emp = getHandlerForCall(call);
        if (emp != null){
            emp.receiveCall(call);
            call.setHandler(emp);
        } else {
            call.reply("xxx");
            callQueues.get(call.getRank().getValue()).add(call);
        }
    }
}

public class Call{
    private Rank rank;
    private Caller caller;
    private Employee handler;
    
    public Call(Caller c){
        rank = Rank.Responder;
        caller = c;
    }
    
    public void setHandler(Employee e) { handler = e; }
    
    public void reply(String message) {...}
    public Rank getRank() { return rank; }
    public Rank incrementRank() { ... }
    public void disconnect() {...}
}

abstract class Employee{
    private Call currentCall = null;
    protected Rank rank;
    
    public Employee(CallHandler handler) {...}
    
    public void receiveCall(Call call) {...}
    
    public void callCompleted() {...}
    
    public escalateAndReassign() {...}
    
    public boolean assignNewCall() {...}
    
    public boolean isFree() { return currentCall == null; }
    
    public Rank getRank() { return rank; }
}

class Director extends Employee {
    public Director() {
        rank = Rank.Director;
    }
}

class Manager extends Employee {
    public Manager() {
        rank = Rank.Manager;
    }
}

class Respondent extends Employee {
    public Respondent() {
        rank = Rank.Respondent;
    }
}

```


