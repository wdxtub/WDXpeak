# Elevator

出处

Design an elevator bank for a building, with multiple elevators

## Solution

解题分析：我们尝试使用抽象->设计对象->设计接口的流程。

**抽象**

在这一步，我们重现现实中电梯间的工作原理：电梯间拥有多部电梯，当有用户需要乘坐电梯时，电梯间分配一个最优的电梯去用户所需的楼层。当电梯需要维修时，电梯间可以停止某部电梯。

**设计对象**

经过抽象分析，我们发现了电梯间和电梯这两个实体。对于每个实体，我们都应该构造一个类去描述它。我们考虑各个实体之间的从属关系：很明显，电梯间拥有一些电梯。因此，电梯间和电梯属于“Has-A”的关系 。对于一部电梯，它应该具有当前的运行状态，包括停止在某一层，向上运行和向下运行。电梯间可以根据当前各个电梯的位置和运行情况，选择最优的电梯去满足用户需求，可以采用下述选择逻辑， 计算一个“距离分”，距离分越低，则优先级越高：

1. 当电梯处于停止状态，距离分等于当前楼层和需求楼层的差
2. 当电梯处于上升状态，如果需求楼层高于当前楼层，则距离分等于当前楼层和需求楼层的差， 否则不考虑当前电梯
3. 当电梯处于下降状态，如果需求楼层低于当前楼层，则距离分等于当前楼层和需求楼层的差， 否则不考虑当前电梯
4.  算法开始时先随机选择一部电梯，当存在更好的电梯选择时，替代当前的候选电梯，这样确保至少会有一部电梯响应(在少数情况下这样做不一定是最优的，可以设想更好的算法解决这个问题)。

**设计接口**

用户所有的请求都应该与电梯间进行交互。电梯间再选择最恰当的电梯，去满足用户的请求。电梯也需要提供接口，以供电梯间设置一个请求。同时，电梯间依赖于电梯的当前位置和运行状况实现选择算法，所以电梯应该提供getter函数。此外，电梯间还应该提供启用／停止某台电梯的接口，以供管理员进行维护。至于电梯间选择电梯的算法函数等等，用户不需要知道这些信息，故应该作为私有函数。

**多线程**

电梯需要在后台不停地自动运行，同时还需要响应电梯间设置的用户请求。因此，我们需要考虑多线程。我们可以用主线程响应用户请求，同时建立另一个线程模拟电梯的运行过程。注意，由于使用了多线程，所有的线程共享变量都需要用锁保护起来，避免产生竞争(racing condition)。同时，考虑到打印调试信息也可能产生竞争，所以应该放到一个特定的打印线程处理所有输出。在参考解答中，我们给出在MacOS下利用dispatch_queue的实现方式。

## Complexity

设计题

## Code
 
```
// define some constants
enum ErrorCode {
    NO_ERROR,
    ERROR
};

enum SpotType {
    COMPACT,
    SUV,
    RESERVED
};
#define NO_PARKING (-1)

class Spot {
public:
    bool     available;
    SpotType type;
};

class Vehicle {
private:
    int     length;
    int     width;
    bool    parked;
    Spot    *spot;
public:
    // omit some setters / getters
    // virtual function here because subclasses will have different behavior
    virtual SpotType getRequiredSpotType() = 0;
    // no need for virtual functions here because subclasses will have the same "behavior"
    bool isParked();
    void parkVehicle(Spot *s);  // park at spot S;
    Spot *removeVehicle();      // move the vehicle away, return parked spot
};

//every type of vehicle has default value of length and width;
class Motor:public Vehicle{};
class Car:public Vehicle{};
class SUV:public Vehicle{};


class Level {
private:
    vector<Spot> spots;
public:
    // find an available spot for a vehicle
    // return NULL if all spots are taken
    Spot *findASpot(Vehicle *v);    
};

class ParkingLot {
private:
    vector<Level> levels;
    static ParkingLot *pInstance;
    unordered_map<Vehicle *, time_t> parkingInfo;

    ParkingLot();
    // Stop the compiler generating methods of copy the object
    ParkingLot(const ParkingLot &copy);    // Not Implemented
    ParkingLot& operator = (const ParkingLot & copy);    // Not Implemented

    time_t getCurrentTime();
    double calculateFee(Vehicle *v);

public:
    static ParkingLot *getInstance();
    // NOTE: vehicleEnter and leave is not thread safe!
    ErrorCode vehicleEnter(Vehicle *v);
    ErrorCode vehicleLeave(Vehicle *v, double *fee);
};

ErrorCode ParkingLot::vehicleEnter(Vehicle *v) {
    Spot *spot = NULL;
    for (int i = 0; i < levels.size();i++) {
        spot = levels[i].findASpot(v);
        if (spot)
            break;
    }
    if (!spot) {
        return ERROR;
    }
    v->parkVehicle(spot);
    spot->available = false;
    parkingInfo[v] = getCurrentTime();
    return NO_ERROR;
}

ErrorCode ParkingLot::vehicleLeave(Vehicle *v, double *fee) {
    *fee = 0;
    if (!v->isParked()) {
        return ERROR;
    }
    Spot *spot = v->removeVehicle();
    spot->available = true;
    *fee = calculateFee(v);
    parkingInfo.erase(v);
    return NO_ERROR;
}
```

进一步讨论：

我们提供的代码并不是线程安全的，当多个线程同时调用enter和leave的时候，可能造成停车状态的不一致，需要通过加锁解决。其次，查找车位的时候我们实现了最简单的线性查找。事实上，我们可以用一个队列记录可用的车位，每次只需要弹出一个即可。那对于不同的车位类型怎么处理？我们可以用多个队列记录可用的车位，每个队列对应一个车型。

> Design an elevator bank for a building, with multiple elevators

解题分析：我们尝试使用抽象->设计对象->设计接口的流程。

**抽象**

在这一步，我们重现现实中电梯间的工作原理：电梯间拥有多部电梯，当有用户需要乘坐电梯时，电梯间分配一个最优的电梯去用户所需的楼层。当电梯需要维修时，电梯间可以停止某部电梯。

**设计对象**

经过抽象分析，我们发现了电梯间和电梯这两个实体。对于每个实体，我们都应该构造一个类去描述它。我们考虑各个实体之间的从属关系：很明显，电梯间拥有一些电梯。因此，电梯间和电梯属于“Has-A”的关系 。对于一部电梯，它应该具有当前的运行状态，包括停止在某一层，向上运行和向下运行。电梯间可以根据当前各个电梯的位置和运行情况，选择最优的电梯去满足用户需求，可以采用下述选择逻辑， 计算一个“距离分”，距离分越低，则优先级越高：

1. 当电梯处于停止状态，距离分等于当前楼层和需求楼层的差
2. 当电梯处于上升状态，如果需求楼层高于当前楼层，则距离分等于当前楼层和需求楼层的差， 否则不考虑当前电梯
3. 当电梯处于下降状态，如果需求楼层低于当前楼层，则距离分等于当前楼层和需求楼层的差， 否则不考虑当前电梯
4.  算法开始时先随机选择一部电梯，当存在更好的电梯选择时，替代当前的候选电梯，这样确保至少会有一部电梯响应(在少数情况下这样做不一定是最优的，可以设想更好的算法解决这个问题)。

**设计接口**

用户所有的请求都应该与电梯间进行交互。电梯间再选择最恰当的电梯，去满足用户的请求。电梯也需要提供接口，以供电梯间设置一个请求。同时，电梯间依赖于电梯的当前位置和运行状况实现选择算法，所以电梯应该提供getter函数。此外，电梯间还应该提供启用／停止某台电梯的接口，以供管理员进行维护。至于电梯间选择电梯的算法函数等等，用户不需要知道这些信息，故应该作为私有函数。

**多线程**

电梯需要在后台不停地自动运行，同时还需要响应电梯间设置的用户请求。因此，我们需要考虑多线程。我们可以用主线程响应用户请求，同时建立另一个线程模拟电梯的运行过程。注意，由于使用了多线程，所有的线程共享变量都需要用锁保护起来，避免产生竞争(racing condition)。同时，考虑到打印调试信息也可能产生竞争，所以应该放到一个特定的打印线程处理所有输出。在参考解答中，我们给出在MacOS下利用dispatch_queue的实现方式。

参考解答：

```
// define some constants
dispatch_queue_t printingQueue;
enum ElevatorState {
    UP,           // moving up
    DOWN,    // moving down
    STAND    // stay at a level, waiting for request
};

class Elevator {
private:
    ElevatorState state;
    int id;
    int currentLevel;
    int maxLevel;
    int minLevel;
    // floor requests from low level to high level
    vector<int> requests;    
    pthread_mutex_t lock;
    // runLoop is called on this thread
    pthread_t runThread;    

    // utility methods to lock and unlock
    void mutexLock();       
    void mutexUnlock();

    // check if need to stop on current floor
    bool needStop();
    // switch to STAND if no request pending.
    // go DOWN if currently going UP, and no further higher level requests
    // go UP if currently going DOWN, and no further lower level requests
    void updateState();    

    // move one floor up/down. Open door if needed. Update state
    void move(); 
    // open door and close door, delete request from array
    void openDoor(); 
    // thread safe operation, main logic for elevator operation (move, open door)
    void runLoop();    
    
    static void *elevatorProc(void *parameter);

public:
    Elevator(int id, int minLevel, int maxLevel);
    ~Elevator();

    // thread safe operation, caller adds a new stop request
    ErrorCode addRequest(int newRequest);   
    // thread safe operation, start elevatorProc to activate elevator
    void startOperation();  
    // thread safe operation, stop elevatorProc to deactivate elevator
    void stopOperation();  
    // thread safe operation, get elevator state
    ElevatorState getState();  
    // thread safe operation, get elevator floor
    int getCurrentLevel();    

#pragma -mark Test Methods
    void printRequests() {
        // caller should have the data lock
        dispatch_async(printingQueue, ^{
            cout << "Elevator " << id << " current requests: ";
            for (int i = 0 ; i < requests.size(); i++) {
                cout << requests[i] << ' ';
            }
            cout << endl;
        });
    }
};

#pragma -mark Private Methods

bool Elevator::needStop() {
    for (int i = 0; i < requests.size(); i++) {
        if (requests[i] == currentLevel) {
            return true;
        }
    }
    return false;
}

void Elevator::updateState() {
    switch (state) {
        case UP:
            if (requests.size() == 0) {
                state = STAND;
            } else {
                if (requests.back() < currentLevel) {
                    state = DOWN;
                }
            }
            break;
        case DOWN:
            if (requests.size() == 0) {
                state = STAND;
            } else {
                if (requests.front() > currentLevel) {
                    state = UP;
                }
            }
            break;
        default:
            break;
    }

}

void Elevator::move() {
    switch (state) {
        case UP:
            if (needStop()) {
                openDoor();
                // flip state
                updateState();
            } else {
                dispatch_async(printingQueue, ^{
                    cout << "Elevator " << id << " move from " << currentLevel
                    << " to " << currentLevel + 1 << endl;
                });
                currentLevel++;
            }
            break;

        case DOWN:
            if (needStop()) {
                openDoor();
                // flip state
                updateState();
            } else {
                dispatch_async(printingQueue, ^{
                    cout << "Elevator " << id << " move from " << currentLevel
                    << " to " << currentLevel - 1 << endl;
                });
                currentLevel--;
            }
            break;
        default:
            break;
    }
}

void Elevator::openDoor() {
    dispatch_async(printingQueue, ^{
        cout << "Elevator " << id << " arriving at " << currentLevel << endl;
“        cout << "Elevator " << id << " door open" << endl;
    });
    for (vector<int>::iterator it = requests.begin(); it != requests.end(); ) {
        if (*it == currentLevel) {
            it = requests.erase(it);
        } else {
            ++it;
        }
    }
    dispatch_async(printingQueue, ^{
        cout << "Elevator " << id << " door close" << endl;
    });
    printRequests();
}

void Elevator::runLoop() {
    mutexLock();
    switch (state) {
        case UP:
        case DOWN:
            move();
            break;
        default:
            break;
    }
    mutexUnlock();
}

void *Elevator::elevatorProc(void *parameter) {
    Elevator *elevator = (Elevator *)parameter;
    while (1) {
        elevator->runLoop();
        usleep(4000000);
    }
    return NULL;
}

#pragma -mark Public Methods

Elevator::Elevator(int inID, int inMinLevel, int inMaxLevel) {
    state = STAND;
    id = inID;
    maxLevel = inMaxLevel;
    minLevel = inMinLevel;
    currentLevel = inMinLevel;
    pthread_mutex_init(&lock, NULL);
}

Elevator::~Elevator() {
    stopOperation();
    pthread_mutex_destroy(&lock);
}

void Elevator::mutexLock() {
    pthread_mutex_lock(&lock);
}

void Elevator::mutexUnlock() {
    pthread_mutex_unlock(&lock);
}

void Elevator::startOperation() {
    mutexLock();
    pthread_create(&runThread, NULL, elevatorProc, this);
    mutexUnlock();
}

void Elevator::stopOperation() {
    mutexLock();
    if (runThread) {
        pthread_cancel(runThread);
    }
    mutexUnlock();
}

ErrorCode Elevator::addRequest(int newRequest) {
    mutexLock();
    if (newRequest > maxLevel || newRequest < minLevel) {
        cerr << "Invalid request " << newRequest << endl;
        return ERROR;
    }
    if (requests.size() == 0) {
        requests.push_back(newRequest);
        if (newRequest > currentLevel) {
            dispatch_async(printingQueue, ^{
                cout << "Elevator " << id << " moving up" << endl;
            });
            state = UP;
        } else if (newRequest == currentLevel) {
            state = STAND;
            openDoor();
        } else {
            dispatch_async(printingQueue, ^{
                cout << "Elevator " << id << " moving down" << endl;
            });
            state = DOWN;
        }
        goto Done;
    }

    for (vector<int>::iterator i = requests.begin(); i != requests.end(); i++) {
        if (newRequest == *i) {
            goto Done;
        }
        if(*i > newRequest) {
            requests.insert(i, newRequest);
            goto Done;
        }
    }
    requests.push_back(newRequest);
Done:
    printRequests();
    mutexUnlock();
    return NO_ERROR;
}

ElevatorState Elevator::getState() {
    mutexLock();
    ElevatorState currentState = state;
    mutexUnlock();
    return currentState;
}

int Elevator::getCurrentLevel() {
    mutexLock();
    int level = currentLevel;
    mutexUnlock();
    return level;
}

class ElevatorBank {
private:
    int numberOfElevators;
    vector<Elevator> elevators;
    int calculateScore(int index, int level);
    bool isBetterNewCandidate(int currentCandidateIndex, int newCandidateIndex, int level);
    int selectAnElevator(int level);
“public:
    ElevatorBank(int numberOfElevators, int minFloor, int maxFloor);
    ~ElevatorBank();
    // index start from 0
    ErrorCode startAnElevator(int index);   
    // index start from 0
    ErrorCode stopAnElevator(int index);        
    ErrorCode setARequest(int level);
};

#pragma -mark Private Methods
int ElevatorBank::calculateScore(int index, int level) {
    if (elevators[index].getState() == STAND) {
        return abs(elevators[index].getCurrentLevel() - level);
    }

    if (elevators[index].getCurrentLevel() > level
        && elevators[index].getState() == DOWN) {
        return elevators[index].getCurrentLevel() - level;
    }

    if (elevators[index].getCurrentLevel() < level
        && elevators[index].getState() == UP) {
        return level - elevators[index].getCurrentLevel();
    }
    return INT_MAX;
}

bool ElevatorBank::isBetterNewCandidate(int currentCandidateIndex, int newCandidateIndex, int level) {
    return calculateScore(currentCandidateIndex, level) > calculateScore(newCandidateIndex, level);
}

int ElevatorBank::selectAnElevator(int level) {
    int selectedIndex = 0;
    for (int i = 1; i < numberOfElevators; i++) {
        if (isBetterNewCandidate(selectedIndex, i, level)) {
            selectedIndex = i;
        }
    }
    return selectedIndex;
}

#pragma -mark Public Methods

ElevatorBank::ElevatorBank(int inNumberOfElevators, int minFloor, int maxFloor) {
    numberOfElevators = inNumberOfElevators;
    for (int i = 0; i < inNumberOfElevators; i++) {
        elevators.push_back(Elevator(i, minFloor, maxFloor));
    }
}

ElevatorBank::~ElevatorBank() {
    elevators.clear();
}

ErrorCode ElevatorBank::startAnElevator(int index) {
    if (index > numberOfElevators || index < 0) {
        cerr << "Index " << index << " invalid!" << endl;
        return ERROR;
    }
    elevators[index].startOperation();
    return NO_ERROR;
}

ErrorCode ElevatorBank::stopAnElevator(int index) {
    if (index > numberOfElevators || index < 0) {
        cerr << "Index " << index << " invalid!" << endl;
        return ERROR;
    }
    elevators[index].stopOperation();
    return NO_ERROR;
}

ErrorCode ElevatorBank::setARequest(int level) {
    int index = selectAnElevator(level);
    return elevators[index].addRequest(level);
}

int main() {
    printingQueue = dispatch_queue_create("elevatorBank.printingQueue", NULL);
    ElevatorBank elevatorBank = ElevatorBank(2, 1, 10);
    for (int i = 0; i < 2; i++) {
        elevatorBank.startAnElevator(i);
    }
    int request;
    while (cin >> request) {
        elevatorBank.setARequest(request);
    };
    return 0;
}
```


