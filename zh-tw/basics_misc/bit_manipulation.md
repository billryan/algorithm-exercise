# Bit Manipulation

位操作有按位與(bitwise and)、或(bitwise or)、非(bitwise not)、左移n位和右移n位等操作。

### XOR - 異或(exclusive or)

> 異或：相同為0，不同為1。也可用「不進位加法」來理解。

異或操作的一些特點：
```
x ^ 0 = x
x ^ 1s = ~x // 1s = ~0
x ^ (~x) = 1s
x ^ x = 0 // interesting and important!
a ^ b = c => a ^ c = b, b ^ c = a // swap
a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c // associative
```

### 移位操作(shift operation)

移位操作可近似為乘以/除以2的冪。`0b0010 * 0b0110`等價於`0b0110 << 2`. 下面是一些常見的移位組合操作。

1. 將`x`最右邊的`n`位清零 - `x & (~0 << n)`
2. 獲取`x`的第`n`位值(0或者1) - `x & (1 << n)`
2. 獲取`x`的第`n`位的冪值 - `(x >> n) & 1`
3. 僅將第`n`位置為`1` - `x | (1 << n)`
4. 僅將第`n`位置為`0` - `x & (~(1 << n))`
5. 將`x`最高位至第`n`位(含)清零 - `x & ((1 << n) - 1)`
6. 將第`n`位至第0位(含)清零 - `x & (~((1 << (n + 1)) - 1))`
7. 僅更新第`n`位，寫入值為`v`; `v`為1則更新為1，否則為0 - `mask = ~(1 << n); x = (x & mask) | (v << i)`

###實際應用

####位圖(Bitmap)

位圖一般用於替代flag array，節約空間。<br>
一個int型的陣列用位圖替換後，占用的空間可以縮小到原來的$$1/32$$.(若int類型是32位元)<br>
下面代碼定義了一個100萬大小的類圖，setbit和testbit函數
```c++
#define N 1000000 // 1 million
#define WORD_LENGTH sizeof(int) * 8 //sizeof返回字節數，乘以8，為int類型總位數

//bits為陣列，i控制具體哪位，即i為0~1000000
void setbit(unsigned int* bits, unsigned int i){
    bits[i / WORD_LENGTH] |= 1<<(i % WORD_LENGTH);  
}

int testbit(unsigned int* bits, unsigned int i){
    return bits[i/WORD_LENGTH] & (1<<(i % WORD_LENGTH));
}

unsigned int bits[N/WORD_LENGTH + 1];
```

## Reference

- [位運算應用技巧（1） » NoAlGo博客](http://noalgo.info/344.html)
- [位運算應用技巧（2） » NoAlGo博客](http://noalgo.info/353.html)
- [位運算簡介及實用技巧（一）：基礎篇 | Matrix67: The Aha Moments](http://www.matrix67.com/blog/archives/263)
- *cc150* chapter 8.5 and chapter 9.5
- 《編程珠璣2》
- 《Elementary Algorithms》 Larry LIU Xinyu
