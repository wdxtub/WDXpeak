# 基础知识

## 解题策略

+ 一般来说，一旦出现“unique”，就落入使用哈希表或者bitset来判断元素出现与否的范畴。
+ 一旦需要统计一个元素集中元素出现的次数，我们就应该想到哈希表。

## 数组

在C／C++中，标准的数组可以通过在栈(Stack)上分配空间，或者通过先声明指针，然后用new关键字(或者C中的malloc函数)，在堆(Heap)上动态的分配空间。举例如下：

    // 在栈上定义长度为arraySize的整型数组
    int array[arraySize];    
    // 在堆上定义长度为arraySize的整型数组
    int *array ＝ new int[arraySize];    

使用完后需要释放内存：

    delete[] array;

访问数组时要注意越界问题。

数组可以通过下标随机访问元素，所以在修改、读取某个元素的时候效率很高，具有O(1)的时间复杂度。在插入、删除的时候需要移动后面的元素，所以平均时间复杂度O(n)。通常，数组这个数据结构不是很适合增减元素。如果你想要的操作需要大量在随机位置增减元素，可以考虑其他的数据结构。在C++中，标准库提供vector容器，其本质上相当于一个长度可变的动态数组。

## 哈希表

哈希表(Hash Table)几乎是最为重要的数据结构，主要用于基于“键(key)”的查找，存储的基本元素是键-值对(key-value pair)。逻辑上，数组可以作为哈希表 的一个特例：键是一个非负整数。注意，通常哈希表会假设键是数据的唯一标识，相同的键默认表示同一个基本存储元素。

哈希表的本质是当使用者提供一个键，根据哈希表自身定义的哈希函数(hash function)，映射出一个下标，根据这个下标决定需要把当前的元素存储在什么位置。在一些合理的假设情况下，查找一个元素的平均时间复杂度是O(1)，插入一个元素的平摊(amortized)时间复杂度是O(1)。

当对于不同的键，哈希函数提供相同的存储地址时，哈希表就遇到了所谓的冲突(collision)。解决冲突的方式有链接法(chaining)和开放地址法(open addressing)两种。简单来说，链接法相当于利用辅助数据结构(比如链表)，将哈希函数映射出相同地址的那些元素链接起来。而开放地址法是指以某种持续的哈希方式继续哈希，直到产生的下标对应尚未被使用的存储地址，然后把当前元素存储在这个地址里。

通常而言，链接法实现相对简便，但是可能需要附加空间，并且利用当前空间的效率不如开放地址法高。开放地址法更需要合理设计的连续哈希函数，但是可以获得更好的空间使用效率。需要注意的是，过于频繁的冲突会降低哈希表的搜索效率，此时需要哈希表的扩张。

C++标准库中提供map容器，可以插入、删除、查找键-值对，底层以平衡二叉搜索树的方式实现，根据键进行了排序。严格来说，map并不是一个哈希表，原因是查找时间从O(1)变为了O(log n)，但是好处在于能够根据键值，顺序地输出元素，对于某些应用场景可能更为合适。在C++11中，标准库添加了unordered_map，更符合哈希表的传统定义，平均查找时间O(1)。

## 字符串

在C语言中，字符串(string)指的是一个以‘\0’结尾的char数组。关于字符串的函数通常需要传入一个字符型指针。然而，在C++中，String是一个类，并且可以通过调用类函数实现判断字符串长度，字串等等操作。

## 工具箱

### 栈和堆

栈主要是指由操作系统自动管理的内存空间。当进入一个函数，操作系统会为该函数中的局部变量分配存储空间。事实上，系统会分配一个内存块，叠加在当前的栈上，并且利用指针指向前一个内存块的地址。函数的局部变量就存储在当前的内存块上。当该函数返回时，系统“弹出”内存块，并且根据指针回到前一个内存块。所以，栈总是以后进先出(LIFO)的方式工作。通常，在栈上分配的空间不需要用户操心。

堆是用来存储动态分配变量的空间。对于堆而言，并没有像栈那样后进先出的规则，程序员可以选择随时分配或回收内存。这就意味着需要程序员自己用命令回收内存，否则会产生内存泄漏(memory leak)。在C/C++中，程序员需要调用free/delete来释放动态分配的内存。在Java，Objective-C (with Automatic Reference Count)中，语言本身引入垃圾回收和计数规则帮助用户决定在什么时候自动释放内存。

### 需要了解的常见容器及方法

+ Vector / ArrayList
+ HashSet, HashTable
+ Map / Dictionary

### C 字符串常见函数

“相关函数通常定义在string.h中，简要介绍如下常见函数，更多信息请参考[这里](http://www.cplusplus.com/reference/cstring/)：

```
//copy source string to destination string
char *strcpy ( char *destination, const char *source );    

Example:
char str1[] = "Sample string";
char str2[SAMPLE_STRING_SIZE];
strcpy (str2,str1);

//Appends a copy of the source string to the destination string.
char *strcat ( char *destination, const char *source );    

Example:
char str[STRING_SIZE] = "string is ";
strcat(str, "concatinated");    //str becomes "string is concatinated

// Returns a pointer to the first occurrence of character in the C string str (NULL if not found).
char *strchr ( const char *str, int character );    

Example:
char string[STRING_LENGTH] = "This is a string";
int firstOccurPos = (int)(strchr(string, 'i') – string);    // firstOccurPos equals to 2 (here we assume string contains character 'i')

// Returns a pointer to the last occurrence of character in the C string str.
char *strrchr ( char *str, int character );    

// Returns a pointer to the first occurrence of str2 in str1, or a NULL pointer if str2 is not part of str1.
char *strstr (char *str1, const char *str2 );    

// Returns the length of the C string str.
size_t strlen ( const char *str );    

Example:
char string[STRING_LENGTH] = "This is a string";
int length = strlen(string);    // length equals to 16

// convert char string to a double
double atof (const char *str);    

// convert char string to an int
int atoi (const char *str);    
```

### C++ String 类常见函数

由于String类重载了+, <, >, =, ==等运算符，故复制，比较是否相等，附加子串等都可以用运算符直接实现。简要介绍其他常见函数如下，更多信息请参考[这里](http://www.cplusplus.com/reference/string/string/ )：

```
// Searches the string for the first occurrence of the str, returns index
size_t find (const string& str, size_t pos = 0) const;    

// Returns a newly constructed string object with its value initialized to a copy of a substring starting at pos with length len.
string substr (size_t pos = 0, size_t len = npos) const; 

Example:
string str("This is a string");
string subStr = str.substr(10,6);    // subStr equals to "string", with length 6

// erase characters from pos with length len
string &erase (size_t pos = 0, size_t len = npos); 

Example:
string str("This is a string");
str.erase(0,10);    // str becomes "string", with length 6 after erasure

// Returns the length of the string, in terms of bytes.
size_t length();    

Example:
string str ("This is a string");
int length = str.length();    // length equals to 16
```

### String Matching 的常见算法

简单介绍两种比较易于实现的字符串比较算法，下述算法假设在长度为n的母串中匹配长度为m的子串。更详细的解释请见[这里](http://en.wikipedia.org/wiki/String_searching_algorithm)。

Brute-Force算法： 顺序遍历母串，将每个字符作为匹配的起始字符，判断是否匹配子串。时间复杂度 O(mn)。

Rabin-Karp算法：将每一个匹配子串映射为一个哈希值。例如，将子串看做一个多进制数，比较它的值与母串中相同长度子串的哈希值，如果相同，再细致地按字符确认字符串是否确实相同。顺序计算母串哈希值的过程中，使用增量计算的方法：扣除最高位的哈希值，增加最低位的哈希值。因此能在平均情况下做到O(m+n)。

Example:

为描述简单，假设字符串只含有十进制数字，母串为"1234"待匹配子串为"23"，定义hash函数把字符串转成整数值。

首先计算子串hash：值为23。

然后计算母串前两个字符的hash：值为12，与子串不符合，需要后移。此时我们扣除最高位"1"的“hash，增加新的最低位"3"的hash，得到新的hash值23，与子串相符。

通过按字符比较发现的确匹配成功，可以返回母串匹配上的下标。

伪代码：

```
int RabinKarp(string s[1..n], string pattern[1..m])
hpattern = hash(pattern[1..m]);  hs = hash(s[1..m]);
for i from 1 to n-m+1
if hs = hpattern
     if s[i..i+m-1] = pattern[1..m]
return i
hs = hash(s[i+1..i+m])
       return not found
```

