# Problem C. Islands Travel

## Source

- [hihoCoder](http://hihocoder.com/contest/mstest2015april/problem/3)

### Problem

时间限制:10000ms

单点时限:1000ms

内存限制:256MB

### 描述

There are N islands on a planet whose coordinates are (X1, Y1), (X2, Y2), (X3,
Y3) ..., (XN, YN). You starts at the 1st island (X1, Y1) and your destination
is the n-th island (XN, YN). Travelling between i-th and j-th islands will
cost you min{|Xi-Xj|, |Yi-Yj|} (|a| denotes the absolute value of a. min{a, b}
denotes the smaller value between a and b) gold coins. You want to know what
is the minimum cost to travel from the 1st island to the n-th island.

### 输入

Line 1: an integer N.

Line 2~N+1: each line contains two integers Xi and Yi.



For 40% data, N&lt;=1000，0&lt;=Xi,Yi&lt;=100000.

For 100% data, N&lt;=100000，0&lt;=Xi,Yi&lt;=1000000000.

### 输出

Output the minimum cost.

样例输入




    3
    2 2
    1 7
    7 6

样例输出




    2


