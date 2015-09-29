# Problem B. Numeric Keypad

## Source

- [hihoCoder](http://hihocoder.com/contest/mstest2015april2/problem/2)

### Problem

时间限制:10000ms

单点时限:1000ms

内存限制:256MB

### 描述

The numberic keypad on your mobile phone looks like below:



    1 2 3
    4 5 6
    7 8 9
      0


Suppose you are holding your mobile phone with single hand. Your thumb points
at digit 1. Each time you can 1) press the digit your thumb pointing at, 2)
move your thumb right, 3) move your thumb down. Moving your thumb left or up
is not allowed.

By using the numeric keypad under above constrains, you can produce some
numbers like 177 or 480 while producing other numbers like 590 or 52 is
impossible.

Given a number K, find out the maximum number less than or equal to K that can
be produced.

### 输入

The first line contains an integer T, the number of testcases.

Each testcase occupies a single line with an integer K.



For 50% of the data, 1 &lt;= K &lt;= 999.

For 100% of the data, 1 &lt;= K &lt;= 10500, t &lt;= 20.

### 输出

For each testcase output one line, the maximum number less than or equal to
the corresponding K that can be produced.

样例输入




    3
    25
    83
    131

样例输出




    25
    80
    129


