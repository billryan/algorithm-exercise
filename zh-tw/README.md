# 資料結構與演算法/leetcode/lintcode題解

[![Build Status](https://travis-ci.org/billryan/algorithm-exercise.svg?branch=master)](https://travis-ci.org/billryan/algorithm-exercise)
[![Slack Status](https://slackin4ds-algo.herokuapp.com/badge.svg)](https://slackin4ds-algo.herokuapp.com/)
[![Chat on Slack](https://img.shields.io/badge/chat-on_slack-orange.svg)](https://ds-algo.slack.com/)

- English via [Data Structure and Algorithm notes](http://algorithm.yuanbin.me/en/index.html)
- 简体中文请戳 [数据结构与算法/leetcode/lintcode题解](http://algorithm.yuanbin.me/zh-hans/index.html)
- 繁體中文請瀏覽 [資料結構與演算法/leetcode/lintcode題解](http://algorithm.yuanbin.me/zh-tw/index.html)

## 簡介

本文檔為資料結構和演算法學習筆記，全文大致分為以下三大部分：

1. Part I為資料結構和演算法基礎，介紹一些基礎的排序/鏈表/基礎演算法
2. Part II為 OJ 上的程式設計題目實戰，按題目的內容分章節編寫，主要來源為 <https://leetcode.com/> 和 <http://www.lintcode.com/>.
3. Part III 為附錄部分，包含如何寫履歷和其他附加資料

本文參考了很多教材和部落格，凡參考過的幾乎都給出明確超連結，如果不小心忘記了，請不要吝惜你的評論和issue :)

本項目保管在 <https://github.com/billryan/algorithm-exercise> 由 [Gitbook](https://www.gitbook.com/book/yuanbin/algorithm/details) 渲染生成 HTML 頁面。你可以在 GitHub(不是 Gitbook) 中 star 該項目查看更新，也可以訂閱 <https://ds-algo.slack.com/messages/github_commit/> 中的 `#github_commit` channel 在郵件中查看更新細節。~~RSS 種子功能正在開發中。~~

Slack 的自助邀請註冊功能已啟用，訪問 <http://slackin4ds-algo.herokuapp.com> 即刻開啟~

你可以線上或者離線查看/搜索本文檔，以下方式任君選擇~

- 線上閱讀(由 Gitbook 渲染) <http://algorithm.yuanbin.me>
- 離線閱讀: 推送到GitHub後會觸發 travis-ci 的編譯，相應的部分編譯輸出提供七牛的靜態文件加速下載。
    1. EPUB. [GitHub](https://raw.githubusercontent.com/billryan/algorithm-exercise/deploy/epub/algorithm-ebook_zh-tw.epub), [Gitbook](https://www.gitbook.com/download/epub/book/yuanbin/algorithm?lang=zh-tw), [七牛 CDN(中国大陆用户适用)](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/algorithm-ebook_zh-tw.epub) - 適合在 iPhone/iPad/MAC 上離線查看，實測效果極好。
    2. PDF. [GitHub](https://raw.githubusercontent.com/billryan/algorithm-exercise/deploy/pdf/algorithm-ebook_zh-tw.pdf), [Gitbook](https://www.gitbook.com/download/pdf/book/yuanbin/algorithm?lang=zh-tw), [七牛 CDN(中国大陆用户适用)](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/algorithm-ebook_zh-tw.pdf) - 推薦下載適合電子屏閱讀的版本，Gitbook 官方使用的中文字體有點問題。
    3. MOBI. [GitHub](https://raw.githubusercontent.com/billryan/algorithm-exercise/deploy/mobi/algorithm-ebook_zh-tw.mobi), [Gitbook](https://www.gitbook.com/download/mobi/book/yuanbin/algorithm?lang=zh-tw), [七牛 CDN(中国大陆用户适用)](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/algorithm-ebook_zh-tw.mobi) - Kindle 專用. 未測試，感覺不適合在 Kindle 上看此類書籍，儘管 Kindle 的屏幕對眼睛很好...

- Google 站內搜索: `keywords site:algorithm.yuanbin.me`
- Swiftype 站內搜索: 可使用網頁右下方的 `Search this site` 進行站內搜索

## 授權條款

本作品採用 **創用CC 姓名標示-相同方式分享 4.0 國際許可協議**  進行許可。**傳播此文檔時請注意遵循以上許可協議。** 關於本授權的更多詳情可參考 <http://creativecommons.org/licenses/by-sa/4.0/>

本著獨樂樂不如眾樂樂的開源精神，我將自己的演算法學習筆記公開和小夥伴們討論，希望高手們不吝賜教。

## 多國文字

- [English](http://algorithm.yuanbin.me/en/index.html) maintained by [@billryan](https://github.com/billryan)
- [简体中文](http://algorithm.yuanbin.me/zh-hans/index.html) maintained by [@billryan](https://github.com/billryan)
- [繁體中文](http://algorithm.yuanbin.me/zh-tw/index.html) maintained by [@CrossLuna](https://github.com/CrossLuna)

## 如何貢獻

如果你發現任何有錯誤的地方或是想更新/翻譯本文檔，請毫不猶豫地猛點擊 [貢獻指南](http://algorithm.yuanbin.me/zh-tw/faq/guidelines_for_contributing.md).

## 如何練習演算法

雖說練習演算法偏向於演算法本身，但是好的程式碼風格還是很有必要的。粗略可分為以下幾點：

- 程式碼可為三大塊：異常處理（空串和邊界處理），主體，返回
- 程式碼風格(**可參考Google的程式設計語言規範**)
    1. 變量名的命名(有意義的變數名)
    2. 縮排(語句塊)
    3. 空格(運算子兩邊)
    4. 程式碼可讀性(即使if語句只有一句也要加花括號)
- 《Code Complete》中給出的參考

而對於實戰演算法的過程中，我們可以採取如下策略：

1. 總結歸類相似題目
2. 找出適合同一類題目的模板程序
3. 對基礎題熟練掌握

以下整理了一些最近練習演算法的網站資源，和大家共享之。

## 線上OJ及部分題解

- [LeetCode Online Judge](https://leetcode.com/) - 找工作方面非常出名的一個OJ，每道題都有 discuss 頁面，可以看別人分享的程式碼和討論，很有參考價值，相應的題解非常多。不過線上程式碼編輯框不太好用，寫著寫著框就拉下來了，最近評測速度比 lintcode 快很多，而且做完後可以看自己程式碼的運行時間分布，首推此 OJ 刷面試相關的題。
- [LintCode | Coding interview questions online training system](http://www.lintcode.com) - 和leetcode類似的在線OJ，但是篩選和寫程式碼時比較方便，左邊為題目，右邊為程式碼框。還可以在`source`處選擇 CC150 或者其他來源的題。會根據系統locale選擇中文或者英文，可以拿此 OJ 輔助 leetcode 進行練習。
- [LeetCode題解 - GitBook](https://www.gitbook.com/book/siddontang/leetcode-solution/details) - 題解部分十分詳細，比較容易理解，但部分題目不全。
- [FreeTymeKiyan/LeetCode-Sol-Res](https://github.com/FreeTymeKiyan/LeetCode-Sol-Res) - Clean, Understandable Solutions and Resources on LeetCode Online Judge Algorithms Problems.
- [soulmachine/leetcode](https://github.com/soulmachine/leetcode) - 含C++和Java兩個版本的題解。
- [Woodstock Blog](http://okckd.github.io/) - IT，演算法及面試。有知識點及類型題總結，特別贊。
- [ITint5 | 專注於IT面試](http://www.itint5.com/) - 文章品質很高，也有部分公司面試題評測。
- [Acm之家,專業的ACM學習網站](http://www.acmerblog.com/) - 各類題解
- [牛客網-專業IT筆試面試備考平台,最全求職題庫,全面提升IT程式設計能力](http://www.nowcoder.com/) - 中國一個IT求職方面的綜合性網站，比較適合想在中國求職的看看。感謝某位美女的推薦 :)

## 其他資源

- [九章算法](http://www.jiuzhang.com/) - 程式碼品質不錯，整理得也很好。
- [七月算法 - julyedu.com ](http://julyedu.com/) - july大神主導的在線演算法輔導。
- [刷題 | 一畝三分地論壇 ](http://www.1point3acres.com/bbs/forum-84-1.html) - 時不時就會有驚喜放出。
- [VisuAlgo - visualising data structures and algorithms through animation](http://http://visualgo.net/) - 相當猛的資料結構和演算法可視化。
- [Data Structure Visualization](http://www.cs.usfca.edu/~galles/visualization/Algorithms.html) - 同上，非常好的動畫示例！！涵蓋了常用的各種資料結構/排序/演算法。
- [結構之法 算法之道](http://blog.csdn.net/v_JULY_v) - 不得不服！
- [julycoding/The-Art-Of-Programming-By-July](https://github.com/julycoding/The-Art-Of-Programming-By-July) - 程序員面試藝術的電子版
- [程序員面試、算法研究、程式設計藝術、紅黑樹、數據挖掘5大系列集錦](http://blog.csdn.net/v_july_v/article/details/6543438)
- [專欄：算法筆記——《算法設計與分析》](http://blog.csdn.net/column/details/lf-algoritnote.html) - CSDN上對《算法設計與分析》一書的學習筆記。
- [我的算法學習之路 - Lucida](http://zh.lucida.me/blog/on-learning-algorithms/) - Google 工程師的演算法學習經驗分享。

## 書籍推薦

本節後三項參考自九章微信分享，謝過。

- [Algorithm Design (豆瓣)](http://book.douban.com/subject/1475870/)
- [The Algorithm Design Manual](http://www.amazon.com/exec/obidos/ASIN/1848000693/thealgorithmrepo), 作者還放出了自己上課的影片和slides - [Skiena's Audio Lectures](http://www3.cs.stonybrook.edu/~algorith/video-lectures/)，[The Algorithm Design Manual (豆瓣)](http://book.douban.com/subject/3072383/)
- 大部頭有 *Introduction to Algorithm* 和 TAOCP
- *Cracking The Coding Interview*. 著名的CTCI(又稱CC150)，Google, Mircosoft, LinkedIn 前HR離職之後寫的書，從很全面的角度剖析了面試的各個環節和題目。除了演算法資料結構等題以外，還包含OO Design, Database, System Design, Brain Teaser等類型的題目。準備北美面試的同學一定要看。
- *劍指Offer*。適合中國找工作的同學看看，英文版叫Coding Interviews. 作者是何海濤(Harry He)。Amazon.cn上可以買到。有大概50多題，題目的分析比較全面，會從面試官的角度給出很多的建議和show各種坑。
- *進軍矽谷* -- 程序員面試揭秘。有差不多150題。


## 學習資源推薦(繁體中文譯者)
###入門
- [Data Structures and Algorithms in C++](http://www.wiley.com/WileyCDA/WileyTitle/productCd-EHEP001657.html)
-by Michael T. Goodrich, Roberto Tamassia and David M. Mount

    台大資工系的**資料結構與演算法**上課用書，內容好懂易讀，習題量大且深度廣度兼具，程式碼風格俐落而不失功能完整性，對C++背景的同學來說是良好的資料結構入門書。

- [Data Structures • 數據結構](https://www.edx.org/course/data-structures-shu-ju-jie-gou-tsinghuax-30240184x-2)(MOOC)

    北京清華大學的鄧俊輝老師開設的中文MOOC，以C++為主要的程式語言，對於一上來就看書覺得枯燥的同學是一帖入門良藥，講解深入淺出，投影片視覺化做得極好，程式作業禁用了部分STL如vector、list、set等，要求學生必須自己實現需要用的資料結構，程式作業使用清華自建的OJ平台，可以同時跟其他線上學習的同學競爭，作業表現優良的同學還可以加入清華內部的討論群組與清華的學生切磋，相當受用。



###進階
