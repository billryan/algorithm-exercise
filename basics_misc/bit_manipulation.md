# Bit Manipulation

位操作有按位与、或、非、左移n位和右移n位等操作。

### XOR - 异或

> 异或：相同为0，不同为1。也可用「不进位加法」来理解。

异或操作的一些特点：
```
x ^ 0 = x
x ^ 1s = ~x // 1s = ~0
x ^ (~x) = 1s
x ^ x = 0 // interesting and important!
a ^ b = c => a ^ c = b, b ^ c = a // swap
a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c // associative
```

### 移位操作

移位操作可近似为乘以/除以2的幂。`0b0010 * 0b0110`等价于`0b0110 << 2`. 下面是一些常见的移位组合操作。

1. 将`x`最右边的`n`位清零 - `x & (~0 << n)`
2. 获取`x`的第`n`位值(0或者1) - `x & (1 << n)`
2. 获取`x`的第`n`位的幂值 - `(x >> n) & 1`
3. 仅将第`n`位置为`1` - `x | (1 << n)`
4. 仅将第`n`位置为`0` - `x & (~(1 << n))`
5. 将`x`最高位至第`n`位(含)清零 - `x & ((1 << n) - 1)`
6. 将第`n`位至第0位(含)清零 - `x & (~((1 << (n + 1)) - 1))`
7. 仅更新第`n`位，写入值为`v`; `v`为1则更新为1，否则为0 - `mask = ~(1 << n); x = (x & mask) | (v << i)`

###实际应用
####位图(Bitmap)
位图一般用于替代flag array，节约空间。<br>
一个int型的数组用位图替换后，占用的空间可以缩小到原来的$$1/32$$.<br>
下面代码定义了一个100万大小的类图，setbit和testbit函数
```c++
#define N 1000000 // 1 million
#define WORD_LENGTH sizeof(int) * 8 //sizeof返回字节数，乘以8，为int类型总位数

//bits为数组，i控制具体哪位，即i为0~1000000
void setbit(unsigned int* bits, unsigned int i){
  bits[i / WORD_LENGTH] |= 1<<(i % WORD_LENGTH);  
}

int testbit(unsigned int* bits, unsigned int i){
  return bits[i/WORD_LENGTH] & (1<<(i % WORD_LENGTH));
}

unsigned int bits[N/WORD_LENGTH + 1];
```

## Reference

- [位运算简介及实用技巧（一）：基础篇 | Matrix67: The Aha Moments](http://www.matrix67.com/blog/archives/263)
- *cc150* chapter 8.5 and chapter 9.5
- 《编程珠玑2》
- 《Elementary Algorithms》 Larry LIU Xinyu
