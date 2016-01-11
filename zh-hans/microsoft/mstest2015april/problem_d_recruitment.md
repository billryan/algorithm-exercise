# Problem D. Recruitment

## Source

- [hihoCoder](http://hihocoder.com/contest/mstest2015april/problem/4)

### Problem

时间限制:10000ms

单点时限:1000ms

内存限制:256MB

### 描述

A company plans to recruit some new employees. There are N candidates (indexed
from 1 to N) have taken the recruitment examination. After the examination,
the well-estimated ability value as well as the expected salary per year of
each candidate is collected by the Human Resource Department.

Now the company need to choose their new employees according to these data. To
maximize the company's benefits, some principles should be followed:

1\. There should be exactly X males and Y females.

2\. The sum of salaries per year of the chosen candidates should not exceed
the given budget B.

3\. The sum of ability values of the chosen candidates should be maximum,
without breaking the previous principles. Based on this, the sum of the salary
per year should be minimum.

4\. If there are multiple answers, choose the lexicographically smallest one.
In other words, you should minimize the smallest index of the chosen
candidates; If there are still multiple answers, then minimize the second
smallest index; If still multiple answers, then minimize the third smallest
one; ...

Your task is to help the company choose the new employees from those
candidates.

### 输入

The first line contains four integers N, X, Y, and B, separated by a single
space. The meanings of all these variables are showed in the description
above. 1 &lt;= N &lt;= 100, 0 &lt;= X &lt;= N, 0 &lt;= Y &lt;= N, 1 &lt;= X +
Y &lt;= N, 1 &lt;= B &lt;= 1000.

Then follows N lines. The i-th line contains the data of the i-th candidate: a
character G, and two integers V and S, separated by a single space. G
indicates the gender (either "M" for male, or "F" for female), V is the well-
estimated ability value and S is the expected salary per year of this
candidate. 1 &lt;= V &lt;= 10000, 0 &lt;= S &lt;= 10.

We assure that there is always at least one possible answer.

### 输出

On the first line, output the sum of ability values and the sum of salaries
per year of the chosen candidates, separated by a single space.

On the second line, output the indexes of the chosen candidates in ascending
order, separated by a single space.

样例输入




    4 1 1 10
    F 2 3
    M 7 6
    M 3 2
    F 9 9

样例输出




    9 9
    1 2



