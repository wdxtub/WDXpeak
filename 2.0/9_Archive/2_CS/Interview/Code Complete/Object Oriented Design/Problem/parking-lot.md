# Parking Lot

出处

## Solution

解题分析：我们尝试使用抽象->设计对象->设计接口的流程。

**抽象**

在这一步，我们重现现实中车库的工作原理。通常，车库可能有不同的层次，每层都有若干个车位，汽车可以停在车位上。车库的主要功能在于实现车辆入库和车辆出库，根据汽车在车库中停留的时间收费。

**设计对象**

经过抽象分析，我们发现了车位、层次、车库、汽车这些实体。对于每个实体，我们都应该构造一个类去描述它。我们考虑各个实体之间的从属，继承关系：很明显，车库拥有不同层次，每个层次拥有一些车位。因此，车库、层次、车位属于“Has-A”的关系。考虑我们可能希望车库是一个全局都可以访问的变量，而且程序中应该只有一个车库实例，所以我们可以利用单例模式，把车库作为一个单例。进一步考虑汽车实体，现实中，有各种类型的汽车，不同类型的车辆对车位的要求也不一样。然而，汽车具有一些共同属性，比如车长，车宽等等，特别地，对于本例，每辆车都需要记录停车的状态。所以，我们可以考虑从一个汽车基类派生出不同类型的汽车派生类。

**设计接口**

车库需要与用户进行交互，因此应该提供车辆入库和车辆出库的接口。车辆入库时，需要从最底层依次向上寻找可用的车位，因此，寻找车位应该一个是由层次提供的接口，返回一个车位。车库把这个车位提供给一个汽车实例，并且标记车位不可用。当车辆出库时，我们需要汽车提供它停车位置的信息(因此，车辆需要提供接口返回它停车的位置)，车库需要计算停车费，并且标记车位可用。

**进一步讨论**

我们提供的代码并不是线程安全的，当多个线程同时调用enter和leave的时候，可能造成停车状态的不一致，需要通过加锁解决。其次，查找车位的时候我们实现了最简单的线性查找。事实上，我们可以用一个队列记录可用的车位，每次只需要弹出一个即可。那对于不同的车位类型怎么处理？我们可以用多个队列记录可用的车位，每个队列对应一个车型。

## Complexity

设计题

## Code

```cpp
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

