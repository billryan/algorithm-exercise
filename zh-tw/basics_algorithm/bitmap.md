# Bitmap

最開始接觸 bitmap 是在 Jon Bentley 所著《Programming Pearls》 (無繁體中文版，簡體中文版書名為《編程珠璣》) 這本書上，書中所述的方法有點簡單粗暴，不過思想倒是不錯——從 Information Theory 的角度來解釋就是信息壓縮了。即將原來32位表示一個 int 變爲一位表示一個 int. 從空間的角度來說就是巨大的節省了(1/32)。可能的應用有**大數據排序/查找（非負整數）**。

C++ 中有`bitset`容器，其他語言可用類似方法實現。

## Implementation

### C

```c
#include <stdio.h>
#include <stdlib.h>

/*
 * @param bits: uint array, i: num i of original array
 */
void setbit(unsigned int *bits, unsigned int i, int BIT_LEN)
{
        bits[i / BIT_LEN] |= 1 << (i % BIT_LEN);
}

/*
 * @param bits: uint array, i: num i of original array
 */
int testbit(unsigned int *bits, unsigned int i, int BIT_LEN)
{
        return bits[i / BIT_LEN] & (1 << (i % BIT_LEN));
}

int main(int argc, char *argv[])
{
        const int BIT_LEN = sizeof(int) * 8;
        const unsigned int N = 1 << (BIT_LEN - 1);
        unsigned int *bits = (unsigned int *)calloc(N, sizeof(int));
        for (unsigned int i = 0; i < N; i++) {
                if (i % 10000001 == 0) setbit(bits, i, BIT_LEN);
        }

        for (unsigned int i = 0; i < N; i++) {
                if (testbit(bits, i, BIT_LEN) != 0) printf("i = %u exists.\n", i);
        }
        free(bits);
        bits = NULL;

        return 0;
}
```

### 源碼分析

核心爲兩個函數方法的使用，`setbit`用於將非負整數`i`置於指定的位。可用分區分位的方式來理解位圖排序的思想，即將非負整數`i`放到它應該在的位置。比如16，其可以位於第一個 int 型的第17位，具體實現即將第17位置一，細節見上面代碼。測試某個數是否存在於位圖中也可以採用類似方法。
