# Bitmap

最开始接触 bitmap 是在《编程珠玑》这本书上，书中所述的方法有点简单粗暴，不过思想倒是挺好——从信息论的角度来解释就是信息压缩了。即将原来32位表示一个 int 变为一位表示一个 int. 从空间的角度来说就是巨大的节省了(1/32)。可能的应用有**大数据排序/查找（非负整数）**。核心思想为根据最大非负整数确定位数，对应的位依次排序。

C++ 中有`bitset`容器，其他语言可用类似方法实现。

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
        unsigned int *bits = (unsigned int *)calloc(N / BIT_LEN, sizeof(int));
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

### 源码分析

核心为两个函数方法的使用，`setbit`用于将非负整数`i`置于指定的位。可用分区分位的方式来理解位图排序的思想，即将非负整数`i`放到它应该在的位置。比如16，其可以位于第一个 int 型的第17位，具体实现即将第17位置一，细节见上面代码。测试某个数是否存在于位图中也可以采用类似方法。
