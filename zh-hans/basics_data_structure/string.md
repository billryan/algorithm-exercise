# String

String 相关的题常出现在面试题中，实际开发也经常用到，这里总结下 C++, Java, Python 中字符串常用的方法。

## C++
```C++
// string是C++的标准库类型，可表示变长的字符序列
// 头文件
#include <string>
// 1. 定义和初始化
string s // s是一个空串
string s = "value" // s被初始化为字面值"value"的副本
string s(n,'c') // s被初始化为n个字符c的字符串
// 2. 对字符串对象的操作
cin>>s // 读取到s，从第一个真正的字符开始读起，直到遇到空白停止
getline(cin, s) // 读取一整行到s
cout<<s // 输出s
s.size() // 返回s中字符的个数
s.empty() // 判断是否为空串，是空串返回true, 否则返回false
s.clear() // 清空s，变成空字符串
s[n] // 返回s中第n个字符的引用，n从0到N-1
s.back() // 取s的最后一个字符
s.pop_back() // 删除s的最后一个字符
s.substr(startpos, length); // 取从startpos到startpos+length的字符子串
s1+s2 // s1和s2拼接
// 3. 对字符的处理
// 头文件
#include <cctype>
isalpha(c) // c是字母时为真
isdigit(c) // c是数字时为真
islower(c) // c是小写字母时为真
isupper(c) // c是大写字母时为真
isspace(c) // c是空白时为真
tolower(c) // 输出c对应的小写字母
toupper(c) // 输出c对应的大写字母
// 4. 注意
// 用下标访问指定字符时，要先确认该位置上确实有值。
```
部分参考 《C++ Primer》（中文版）

## Python

```python
s1 = str()
# in python `''` or `""` is the same
s2 = "shaunwei" # 'shaunwei'
s2len = len(s2)
# last 3 chars
s2[-3:] # wei
s2[5:8] # wei
s3 = s2[:5] # shaun
s3 += 'wei' # return 'shaunwei'
# list in python is same as ArrayList in java
s2list = list(s3)
# string at index 4
s2[4] # 'n'
# find index at first
s2.index('w')  # return 5, if not found, throw ValueError
s2.find('w') # return 5, if not found, return -1
```

在Python里面，没有StringBuffer 或者 StringBuilder。 但是在Python 里面处理String本身就比较 cheap。

## Java

```java
String s1 = new String();
String s2 = "billryan";
int s2Len = s2.length();
s2.substring(4, 8); // return "ryan"
StringBuilder s3 = new StringBuilder(s2.substring(4, 8));
s3.append("bill");
String s2New = s3.toString(); // return "ryanbill"
// convert String to char array
char[] s2Char = s2.toCharArray();
// char at index 4
char ch = s2.charAt(4); // return 'r'
// find index at first
int index = s2.indexOf('r'); // return 4. if not found, return -1
```

StringBuffer 与 StringBuilder, 前者保证线程安全，后者不是，但单线程下效率高一些，一般使用 StringBuilder.
