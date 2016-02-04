# String 字串

String 相關的題很常出現在面試題中，實際開發也經常用到，這裡總結一下 C++, Java, Python 中字串常用的方法。

## Python

```python
s1 = str()
# in python `''` and `""` are the same
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

在Python裡面，沒有StringBuffer 或者 StringBuilder。 但是在Python 裡面處理String本身就比較 cheap。

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

StringBuffer 與 StringBuilder, 前者保證執行緒安全(Thread Safety)，後者不是，但單執行緒下效率高一些，一般使用 StringBuilder.
