# Huffman Compression - 霍夫曼壓縮

主要思想：放棄文本文件的普通保存方式：不再使用7位或8位二進制數表示每一個字符，而是**用較少的比特表示出現頻率最高的字符，用較多的比特表示出現頻率低的字符**。

使用變動長度編碼(variable-length code)來表示字串，勢必會導致編解碼時碼字的唯一性問題，因此需要一種編解碼方式唯一的前綴碼(prefix code)，而表示前綴碼的一種簡單方式就是使用單詞搜尋樹，其中最優前綴碼即為Huffman首創。

以符號F, O, R, G, E, T為例，其出現的頻次如以下表格所示。

| Symbol | F | O | R | G | E | T |
| -- | -- | -- | -- | -- | -- | -- |
| Frequence | 2 | 3 | 4 | 4 | 5 | 7 |
| Code | 000 | 001 | 100 | 101 | 01 | 11 |

則對各符號進行霍夫曼編碼的動態示例如下圖所示。基本步驟是將出現頻率由小到大排列，組成子樹後頻率相加作為整體再和其他未加入二元樹中的節點頻率比較。加權路徑長為節點的頻率乘以樹的深度。

![Huffman](../../shared-files/images/huffman_algorithm.gif)

有關霍夫曼編碼的具體步驟可參考 [Huffman 編碼壓縮算法 | 酷 殼 - CoolShell.cn](http://coolshell.cn/articles/7459.html) 和 [霍夫曼編碼 - 維基百科，自由的百科全書](http://zh.wikipedia.org/wiki/%E9%9C%8D%E5%A4%AB%E6%9B%BC%E7%BC%96%E7%A0%81)，清晰易懂。
