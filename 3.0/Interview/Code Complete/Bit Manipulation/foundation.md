# Bit Manipulation

对于网络、操作系统、嵌入式系统等职位的面试，位运算也是常见的题目类型之一。所谓的位运算，是指按二进制进行的运算。常见运算包括求反，与运算，或运算，异或运算及位移。关于位运算的真值表，请参考“工具箱”给出的链接。

在C/C++中，基本的位运算符总结如下，其中运算符优先级为从上到下递减，且<<，>>优先级相同：

| 操作符 | 功能 | 用法 |
| :--: | :--: | :--: |
| ~ | 位求反 | ~var |
| << | 左移(乘法) | var << position |
| >> | 右移(除法) | var >> position |
| & | 位与 | var1 & var2 |
| ^ | 位异或 | var1 ^ var2 |
| 一条竖线 | 位或 | var1 竖线 var2 |

需要注意的是，位运算符只能用在带符号或无符号的char、short、int与long类型上。在实际应用中，建议用unsigned整型操作数，以免带符号操作数因为不同机器导致的结果不同：无符号数左移／右移默认移入的新比特是0。对于符号数，当最高位是1(代表负数)时，有的机器认为右移移入的新比特是1。此外，复杂的位运算建议都用括号强制计算顺序，而不是依赖于优先级，这样做可以增加可读性并避免错误。

用十六进制(hex)定义一个变量如下所示：

    unsigned short value = 0xFFFF;

等价于二进制(binary)定义：

    unsigned short value = 0b1111111111111111;

等价于十进制定义：

    unsigned short value = 65535;
    
## 解题策略

### 基本的位运算

最基本的操作包括获取位、设置位和清除位。获取位可以利用&1：&(0x1 << pos) ；设置位可以利用|1: | (0x1 << pos) ；清除位可以利用&0: &(~(0x1 << pos))。判断某位是否相同用^：(A & (0x1 << pos)) ^ (B & (0x1 << pos))。

### 位掩码

选择合适的位掩码(bit mask)，然后与给定的二进制数进行基本位操作。而掩码，通常可以通过对~0，1 进行基本操作和加减法得到。例如，我们要构造一个第i到第j位为0，其他位为1的位掩码，则可以对~0进行左移操作获得形如111…0000的mask，再对~0进行右移操作，获得形如000…111的mask，最后通过位或(此处相当于相加)得到最终的位掩码。

在寻求得到一个特定的掩码时，还是利用最基本的获取位、设置位或清除位得到所需掩码的形态。另外，应当尽可能避免直接出现常数，比如使用32-i这样的情况(这里默认想要操作一个32bit的整型)，而应当定义一个意义明确的宏，以提高可读性：`#define INT_BIT_LENTH (32)`。

## XOR 异或

> 异或：相同为0，不同为1。也可用「不进位加法」来理解。

异或操作的一些特点：

    x ^ 0 = x
    x ^ 1s = ~x // 1s = ~0
    x ^ (~x) = 1s
    x ^ x = 0 // interesting and important!
    a ^ b = c => a ^ c = b, b ^ c = a // swap
    a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c // associative

## 移位操作

移位操作可近似为乘以/除以2的幂。0b0010 * 0b0110等价于0b0110 << 2. 下面是一些常见的移位组合操作。

1. 将x最右边的n位清零 `x & (~0 << n)`
2. 获取x的第n位值(0或者1) `x & (1 << n)`
3. 获取x的第n位的幂值 `(x >> n) & 1`
4. 仅将第n位置为1 `x | (1 << n)`
5. 仅将第n位置为0 `x & (~(1 << n))`
6. 将x最高位至第n位(含)清零 `x & ((1 << n) - 1)`
7. 将第n位至第0位(含)清零 `x & (~((1 << (n + 1)) - 1))`
8. 仅更新第n位，写入值为v; v为1则更新为1，否则为0 `mask = ~(1 << n); x = (x & mask) | (v << i)`

---

+ Two's Complement - 负数可以看作是最高位的 1 为负，其他位为正，相加得到最后的值
	+ 例如 -1 = (1111) 最高位的 1 表示 -8， 剩下三位等于 7，相加后等于 -1
+ logical right shift - put a `0` in the most significant bit - `>>>`
+ arithmetic right shift - put a `1` in the most significant bit - `>>`

## Get Bit

Shifts 1 over by `i` bits, creating a value that looks like `00010000`. AND operation

	boolean getBit(int num, int i){
		return ((num & (1 << i)) != 0);
	}

## Set Bit

Shifts 1 over by `i` bits, creating a value like `00010000`. OR operation

	int setBit(int num, int i){
		return num | (1 << i);
	}

## Clear Bit

Create a number like `11101111` by creating the reverse of it (`00010000`). AND operation.

	int clearBit(int num, int i){
		int mask = ~(1 << i);
		return num & mask;
	}

To clear all bits from the most significant bit through `i` (inclusive), we create a mask with a `1` at the ith bit(1 << i). Then we subtract 1 from it, giving us a sequence of 0s followed by i 1s. AND operation.

	int clearBitsMSBthroughI(int num, int i){
		int mask = (1 << i) - 1;
		return num & mask;
	}

To clear bits from i through 0 (inclusive), we take a sequence of 1s (which is -1) and shift it over by 31 - i bits.

	int clearBitsIthrough0(int num, int i){
		int mask = ~(-1 >>> (31 - i));
		return num & mask;
	}

## Update Bit

Set the ith bit to a value `v`

	int updateBit(int num, int i, boolean bitIs1){
		int value = bitIs1 ? 1 : 0;
		int mask = ~(1 << i);
		return (num & mask) | (value << i);
	}

## 工具箱

### 位运算的定义

[参考链接](http://en.wikipedia.org/wiki/Bitwise_operation)  给出的位运算定义。

### 关于位运算的深入讨论

请参考[链接](http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetTable)

