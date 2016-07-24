
# 数据结构与算法/leetcode/lintcode题解

[![Build Status](https://travis-ci.org/billryan/algorithm-exercise.svg?branch=master)](https://travis-ci.org/billryan/algorithm-exercise)
[![Slack Status](https://slackin4ds-algo.herokuapp.com/badge.svg)](https://slackin4ds-algo.herokuapp.com/)
[![Chat on Slack](https://img.shields.io/badge/chat-on_slack-orange.svg)](https://ds-algo.slack.com/)

- English via [Data Structure and Algorithm notes](http://algorithm.yuanbin.me/en/index.html)
- 简体中文请戳 [数据结构与算法/leetcode/lintcode题解](http://algorithm.yuanbin.me/zh-hans/index.html)
- 繁體中文請瀏覽 [資料結構與演算法/leetcode/lintcode題解](http://algorithm.yuanbin.me/zh-tw/index.html)

## 简介

本文档为数据结构和算法学习笔记，我们希望这个笔记能给你在学习算法的过程提供思路和源码方面的参考，但绝不鼓励死记硬背！全文大致分为以下三大部分：

1. Part I为数据结构和算法基础，介绍一些基础的排序/链表/基础算法
2. Part II为 OJ 上的编程题目实战，按题目的内容分章节编写，主要来源为 <https://leetcode.com/>, <http://www.lintcode.com/>, <http://www.geeksforgeeks.org/>, <http://hihocoder.com/>, <https://www.topcoder.com/>.
3. Part III 为附录部分，包含如何写简历和其他附加材料如系统设计

本文参考了很多教材和博客，凡参考过的几乎都给出明确链接，如果不小心忘记了，请不要吝惜你的评论和issue :)

你可以在线或者离线查看/搜索本文档，以下方式任选~

- 在线阅读(由 Gitbook 渲染) <http://algorithm.yuanbin.me>
- 离线阅读: 推送到GitHub后会触发 travis-ci 的编译，相应的部分编译输出提供 GitHub 和 GitCafe 下载。
    1. EPUB: [GitHub](https://raw.githubusercontent.com/sign4bill/algorithm-exercise/deploy/epub/algorithm-ebook_zh-hans.epub), [Gitbook](https://www.gitbook.com/download/epub/book/yuanbin/algorithm?lang=zh-hans), [七牛 CDN(中国大陆用户适用)](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/algorithm-ebook_zh-hans.epub) - 适合在 iPhone/iPad/MAC 上离线查看，实测效果极好。
    2. PDF: [GitHub](https://raw.githubusercontent.com/sign4bill/algorithm-exercise/deploy/pdf/algorithm-ebook_zh-hans.pdf), [Gitbook](https://www.gitbook.com/download/pdf/book/yuanbin/algorithm?lang=zh-hans), [七牛 CDN(中国大陆用户适用)](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/algorithm-ebook_zh-hans.pdf) - 推荐下载 GitHub 和 七牛 CDN 的版本，Gitbook 官方使用的中文字体为楷体。
    3. MOBI: [GitHub](https://raw.githubusercontent.com/sign4bill/algorithm-exercise/deploy/mobi/algorithm-ebook_zh-hans.mobi), [Gitbook](https://www.gitbook.com/download/mobi/book/yuanbin/algorithm?lang=zh-hans), [七牛 CDN(中国大陆用户适用)](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/algorithm-ebook_zh-hans.mobi) - Kindle 专用，未测试，感觉不适合在 Kindle 上看此类书籍，尽管 Kindle 的屏幕对眼睛很好...
- Google 站内搜索: `keywords site:algorithm.yuanbin.me`
- Swiftype 站内搜索: 可使用网页右下方的 `Search this site` 进行站内搜索
- 微信公众号搜索：此功能预计2016年1月下旬添加，借助 Swiftype 的 API，微信可以仅作为一个查询界面，我个人是不接受把这个文档的内容放在微信这种封闭平台上的。

### 订阅更新

本项目托管在 <https://github.com/billryan/algorithm-exercise> 由 [Gitbook](https://www.gitbook.com/book/yuanbin/algorithm/details) 渲染生成 HTML 页面。

你可以在 GitHub/GitBook 中 star 该项目查看更新，也可以订阅 <https://ds-algo.slack.com/messages/github_commit/> 中的 `#github_commit` channel 在邮件中查看更新细节，~~RSS 种子功能正在开发中~~。

Slack 的自助邀请注册功能已启用，访问 <http://slackin4ds-algo.herokuapp.com> 即刻开启~

**号外：Slack 的 [shua-shua-shua](https://ds-algo.slack.com/messages/shua-shua-shua/details/) channel 用于刷题小组讨论，大家可以在这个 channel 里一起讨论学习算法。**

## 许可证

本作品采用 **知识共享署名-相同方式共享 4.0 国际许可协议**  进行许可。**传播此文档时请注意遵循以上许可协议。** 关于本许可证的更多详情可参考 <http://creativecommons.org/licenses/by-sa/4.0/>

本着独乐乐不如众乐乐的开源精神，我将自己的算法学习笔记公开和小伙伴们讨论，希望高手们不吝赐教。

## 如何贡献

如果你发现任何有错误的地方或是想更新/翻译本文档，请毫不犹豫地猛击 [FAQ](http://algorithm.yuanbin.me/zh-hans/faq/index.html) 和 [贡献指南](http://algorithm.yuanbin.me/zh-hans/faq/guidelines_for_contributing.html).

## 如何练习算法

虽说练习算法偏向于算法本身，但是好的代码风格还是很有必要的。粗略可分为以下几点：

- 代码块可为三大块：异常处理（空串和边界处理），主体，返回
- 代码风格(**可参考Google的编程语言规范**)
    1. 变量名的命名(有意义的变量名)
    2. 缩进(语句块)
    3. 空格(运算符两边)
    4. 代码可读性(即使if语句只有一句也要加花括号)
- 《代码大全》中给出的参考

而对于实战算法的过程中，我们可以采取如下策略：

1. 总结归类相似题目
2. 找出适合同一类题目的模板程序
3. 对基础题熟练掌握

以下整理了一些最近练习算法的网站资源，和大家共享之。

## 在线OJ及部分题解

- [数据结构与算法 - 实验楼](https://www.shiyanlou.com/courses/484) - 本书的同步练习平台。
- [LeetCode Online Judge](https://leetcode.com/) - 找工作方面非常出名的一个OJ，每道题都有 discuss 页面，可以看别人分享的代码和讨论，很有参考价值，相应的题解非常多。~~不过在线代码编辑框不太好用，写着写着框就拉下来了~~，最近没有这个问题了，评测速度通常比 lintcode 快很多，而且做完后可以看自己代码的运行时间分布，首推此 OJ 刷面试相关的题。
- [LintCode](http://www.lintcode.com) - 和leetcode类似的在线OJ，但是筛选和写代码时比较方便，左边为题目，右边为代码框。还可以在`source`处选择 CC150 或者其他来源的题。会根据系统locale选择中文或者英文，可以拿此 OJ 辅助 leetcode 进行练习。
- [hihoCoder](http://hihocoder.com/) - 非常不错的一个 OJ，每周都会推出一个专题供你学习，都是干货。
- [LeetCode题解 - GitBook](https://www.gitbook.com/book/siddontang/leetcode-solution/details) - 题解部分详细，比较容易理解，但题目很不全。
- [FreeTymeKiyan/LeetCode-Sol-Res](https://github.com/FreeTymeKiyan/LeetCode-Sol-Res) - Clean, Understandable Solutions and Resources on LeetCode Online Judge Algorithms Problems.
- [soulmachine/leetcode](https://github.com/soulmachine/leetcode) - 含C++和Java两个版本的题解。
- [Acm之家,专业的ACM学习网站](http://www.acmerblog.com/) - 各类题解
- [牛客网](http://www.nowcoder.com/) - 国内一个IT求职方面的综合性网站，比较适合想在国内求职的看看。感谢某位美女的推荐 :)

## 其他资源

- [九章算法](http://www.jiuzhang.com/) - 代码质量大多不错，但是不太全。这家也同时提供有偿辅导。
- [刷题 | 一亩三分地论坛](http://www.1point3acres.com/bbs/forum-84-1.html) - 时不时就会有惊喜放出。
- [VisuAlgo - visualising data structures and algorithms through animation](http://www.comp.nus.edu.sg/~stevenha/visualization/index.html) - 相当厉害的数据结构和算法可视化网站。
- [Data Structure Visualization](http://www.cs.usfca.edu/~galles/visualization/Algorithms.html) - 同上，非常好的动画演示！！涵盖了常用的各种数据结构/排序/算法。
- [我的算法学习之路 - Lucida](http://zh.lucida.me/blog/on-learning-algorithms/) - Lucida(签约 Google) 的算法学习经验分享。
- [HiredInTech](http://www.hiredintech.com/) - System Design 的总结特别适合入门。

## 书籍推荐

- [挑战程序设计竞赛（第2版） (豆瓣)](http://book.douban.com/subject/24749842/) - ACM 高手总结的各类基础算法和经典问题，含金量非常高！算法进阶力荐！
- [Algorithm Design (豆瓣)](http://book.douban.com/subject/1475870/)
- [The Algorithm Design Manual](http://www.amazon.com/exec/obidos/ASIN/1848000693/thealgorithmrepo), 作者还放出了自己上课的视频和slides - [Skiena's Audio Lectures](http://www3.cs.stonybrook.edu/~algorith/video-lectures/)，[The Algorithm Design Manual (豆瓣)](http://book.douban.com/subject/3072383/)
- 大部头有 *Introduction to Algorithm* 和 TAOCP
- *Cracking The Coding Interview* - 著名的CTCI(又称CC150)，除了算法数据结构等题以外，还包含OO Design, Database, System Design, Brain Teaser等类型的题目。**准备技术面试的同学一定要看**

## Contribution

- [English](http://algorithm.yuanbin.me/en/index.html) is maintained by [@billryan](https://github.com/billryan)
- [简体中文](http://algorithm.yuanbin.zh-hans/index.html) is maintained by [@billryan](https://github.com/billryan), [@Shaunwei](https://github.com/Shaunwei)
- [繁體中文](http://algorithm.yuanbin.me/zh-tw/index.html) is maintained by [@CrossLuna](https://github.com/CrossLuna)

Other contributors can be found in [Contributors to algorithm-exercise](https://github.com/billryan/algorithm-exercise/graphs/contributors)

### Donation

#### 支付宝

![支付宝打赏](../shared-files/images/alipay_billryan_qr15x15.jpg)

账户名：yuanbin2014(at)gmail.com 金额随意

#### Wechat

![Red Packet](../shared-files/images/wechat_billryan_qr15x15.jpg)

金额随意

#### PayPal

账户名：yuanbin2014(at)gmail.com 金额随意，付款时选择 friends and family

隐私考虑，以下名单隐去了部分个人信息，有些名单若没来得及添加，可私下联系我加上。

- `taoli***@gmail.com`, 支付宝转账
- `张亚*`, 支付宝转账
- `俞卓*`, 支付宝转账
- `季*`, 支付宝转账
- `wen***@126.com`, 支付宝转账
- `she***@163.com`, 支付宝转账
- `185****0032`, 支付宝转账
- `136***0794`, 支付宝转账
- `187***2296`, 支付宝转账
- `don***@163.com`, 支付宝转账

所得捐款用于七牛 CDN 流量付费/激励 Contributors 写出更好的内容/购买书籍/西瓜/饮料

## To Do

- [ ] add multiple languages support, currently 繁體中文, 简体中文 are available
- [x] explore nice writing style
- [x] add implementations of `Python`, `C++`, `Java` code
- [x] add time and space complexity analysis
- [x] summary of basic data structure and algorithm
- [x] add CSS for online website <http://algorithm.yuanbin.me>
- [x] add proper Chinese fonts for PDF output
