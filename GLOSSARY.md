## TLE

Time Limit Exceeded 的简称。你的程序在 OJ 上的运行时间太长了，超过了对应题目的时间限制。

## DFS

Depth-First Search, 深度优先搜索

## BFS

Breadth-First Search, 广度优先搜索

## DP_Sequence

state: denote f[i] as the state of position, number or letter before index `i` 
function: f[i] = f[j] ... index `j` is before `i`
intialize: f[0]
answer: f[n-1]

按照动态规划的四要素，此类题可从以下四个角度分析:

1. State: f[i] 前i个位置/数字/字母...
2. Function: f[i] = f[i-1]... 找递推关系
3. Initialization: 根据题意进行必要的初始化
4. Answer: f[n-1]
