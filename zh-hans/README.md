# 数据结构与算法/leetcode/lintcode题解

[![Build Status](https://travis-ci.org/billryan/algorithm-exercise.svg?branch=master)](https://travis-ci.org/billryan/algorithm-exercise)
[![Slack Status](https://slackin4ds-algo.herokuapp.com/badge.svg)](https://slackin4ds-algo.herokuapp.com/)
[![Chat on Slack](https://img.shields.io/badge/chat-on_slack-orange.svg)](https://ds-algo.slack.com/)

- [English](https://algorithm.yuanbin.me/en/), 极少更新
- [简体中文](https://algorithm.yuanbin.me/zh-hans/), 经常更新
- [繁體中文](https://algorithm.yuanbin.me/zh-tw/), 极少更新

## 简介

本文档为数据结构和算法学习笔记，主要作者 @billryan 并不是专业算法选手，希望有专业的小伙伴一起来改进。我们希望这个笔记能给你在学习算法的过程提供思路和源码方面的参考，但绝不鼓励死记硬背！全文大致分为以下三大部分：

1. Part I为数据结构和算法基础，介绍一些基础的排序/链表/基础算法
2. Part II为 OJ 上的编程题目实战，按题目的内容分章节编写，主要来源为 [leetcode](https://leetcode.com/), [lintcode](http://www.lintcode.com/), [geeksforgeeks](http://www.geeksforgeeks.org/), [hihocoder](http://hihocoder.com/), [topcoder](https://www.topcoder.com/).
3. Part III 为附录部分，包含如何写简历和其他附加材料如系统设计

本文参考了很多教材和博客，凡参考过的几乎都给出明确链接，如果不小心忘记了，请不要吝惜你的评论和issue :)

你可以在线或者离线查看/搜索本文档，以下方式任选~

- 在线阅读(由 GitBook 渲染) <https://algorithm.yuanbin.me>
    - Google 站内搜索: `keywords site:algorithm.yuanbin.me`
    - Algolia 站内搜索: 可使用网页左上方的 `输入并搜索` 进行站内搜索
- ~~微信公众号/小程序~~：微信可以仅作为一个查询和显示界面，我个人是不接受把这个文档的内容放在微信这种封闭平台上的
- 离线阅读: 推送到 GitHub 后会触发 travis-ci 的编译，相应的编译输出提供 GitHub 等多个网站镜像下载，不同镜像站点内容一致，国外请选择 GitHub, 中国大陆用户建议选择 Website 镜像站。
    1. EPUB: [GitHub](https://github.com/billryan/algorithm-exercise/raw/gh-pages/book_zh-hans.epub), [Website](https://algorithm.yuanbin.me/book_zh-hans.epub) - 适合在 iPhone/iPad/MAC 上离线查看，实测效果极好。
    2. PDF: [GitHub](https://github.com/billryan/algorithm-exercise/raw/gh-pages/book_zh-hans.pdf), [Website](https://algorithm.yuanbin.me/book_zh-hans.pdf) - 中文字体使用思源黑体优化。
    3. MOBI: [GitHub](https://github.com/billryan/algorithm-exercise/raw/gh-pages/book_zh-hans.mobi), [Website](https://algorithm.yuanbin.me/book_zh-hans.mobi) - Kindle 专用，未测试，感觉不适合在 Kindle 上看此类书籍，尽管 Kindle 的屏幕对眼睛很好...

### 订阅更新

本项目托管在 <https://github.com/billryan/algorithm-exercise> 由 GitBook 渲染生成 HTML/PDF/MOBI/EPUB 
你可以在 GitHub 中 star 该项目查看更新，也可以订阅 <https://ds-algo.slack.com/messages/github_commit/> 中的 `#github_commit` channel 在邮件中查看更新细节。
Slack 的自助邀请注册功能已启用，访问 <http://slackin4ds-algo.herokuapp.com> 即刻开启~

**号外：Slack 的 [shua-shua-shua](https://ds-algo.slack.com/messages/shua-shua-shua/details/) channel 用于刷题小组讨论，大家可以在这个 channel 里一起讨论学习算法。**

## 许可证

本作品采用 **知识共享署名-相同方式共享 4.0 国际许可协议**  进行许可。**传播此文档时请注意遵循以上许可协议。** 关于本许可证的更多详情可参考 <http://creativecommons.org/licenses/by-sa/4.0/>

本着独乐乐不如众乐乐的开源精神，我将自己的算法学习笔记公开和小伙伴们讨论，希望高手们不吝赐教。

## 如何贡献

如果你发现任何有错误的地方或是想更新/翻译本文档，请毫不犹豫地猛击 [FAQ](https://algorithm.yuanbin.me/zh-hans/faq/index.html) 和 [贡献指南](https://algorithm.yuanbin.me/zh-hans/faq/guidelines_for_contributing.html).

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

- [LeetCode Online Judge](https://leetcode.com/) - 找工作方面非常出名的一个OJ，每道题都有 discuss 页面，可以看别人分享的代码和讨论，很有参考价值，相应的题解非常多。~~不过在线代码编辑框不太好用，写着写着框就拉下来了~~，最近没有这个问题了，评测速度通常比 lintcode 快很多，而且做完后可以看自己代码的运行时间分布，首推此 OJ 刷面试相关的题。
- [LintCode](http://www.lintcode.com) - 和leetcode类似的在线OJ，但是筛选和写代码时比较方便，左边为题目，右边为代码框。还可以在`source`处选择 CC150 或者其他来源的题。会根据系统locale选择中文或者英文，可以拿此 OJ 辅助 leetcode 进行练习。
- [hihoCoder](http://hihocoder.com/) - 非常不错的一个 OJ，每周都会推出一个专题供你学习，基本都是干货。
- [LeetCode题解 - GitBook](https://www.gitbook.com/book/siddontang/leetcode-solution/details) - 题解部分详细，比较容易理解，但题目不全
- [FreeTymeKiyan/LeetCode-Sol-Res](https://github.com/FreeTymeKiyan/LeetCode-Sol-Res) - Clean, Understandable Solutions and Resources on LeetCode Online Judge Algorithms Problems.
- [soulmachine/leetcode](https://github.com/soulmachine/leetcode) - 含C++和Java两个版本的题解。

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

非常感谢以下小伙伴一起维护
- [@niangaotuantuan](https://github.com/niangaotuantuan) - 第一个邮件提出要一起维护的贡献者，现在潜心学术并维护了『程序媛的日常』微信公众号
- [@Shaunwei](https://github.com/Shaunwei) - 贡献了大量文档和代码，现在在 Google 美国工作
- [@CrossLuna](https://github.com/CrossLuna) - 开创了繁体中文版本

其他更多的贡献者可以点击 [Contributors](https://github.com/billryan/algorithm-exercise/graphs/contributors) 查看

### Donation

**目前部门招人，字节跳动非中(TikTok)广告数据应用方向，如广告诊断/画像/归因等，急需大数据和Java后端(社招/实习都要)，有想法的可以联系微信 @billryan**

历史上，也有部分网友进行了现金捐赠，这里还是继续补充上。隐私考虑，以下名单隐去了部分个人信息，有些名单若没来得及添加，可私下联系我加上，有些信息和金额因为时间久远可能有误，欢迎指正。

- 2015-09-16 支付宝 `taoli***@gmail.com` 20
- 2015-10-30 支付宝 `张亚*` 6.66
- 2015-11-19 支付宝 `wen***@126.com` 10
- 2015-12-25 支付宝 `石*` 50
- 2016-01-05 支付宝 `she***@163.com` 10
- 2016-01-24 支付宝 `187****2296` 20
- 2016-01-15 支付宝 `136****0794` 20
- 2016-03-08 支付宝 `don***@163.com` 5
- 2016-03-21 支付宝 `129***@qq.com` 50
- 2016-07-31 支付宝 `130****9675` 5
- 2016-08-16 PayPal `Tong W***` 20 $
- 2016-08-21 支付宝 `ee.***@gmail.com` 6.66
- 2016-10-09 支付宝 `abc***@126.com` 6.66
- 2016-09-01 明信片 `liaowen***@163.com`
- 2016-10-19 微信 6.66
- 2016-10-13 支付宝 `182****9133` 5
- 2016-11-17 支付宝 `tf.***@gmail.com` 10.24
- 2016-11-19 支付宝 `jat***@163.com` 20
- 2016-11-20 支付宝 `bao***@163.com` 10
- 2017-01-01 明信片 Berkeley CA USA - (智识)知识是不满足守恒律的事物
- 2017-01-09 微信 20
- 2017-01-20 支付宝 `xin***@sina.com` 10
- 2017-02-21 微信 10
- 2017-03-15 微信 10
- 2017-04-07 微信 10
- 2017-04-18 明信片 - @CrossLuna 非常感谢来自台湾的小伙伴维护繁体中文
- 2017-07-08 微信 13.14 - @盈盈 :)
- 2017-08-08 支付宝 `mut***@gmail.com` 10
- 2017-09-18 支付宝 `far***@sina.com` 66.66
- 2017-10-07 支付宝 `277***@qq.com` 6.08
- 2017-10-23 微信 6.66 # 加油啊!
- 2017-10-26 微信 10
- 2017-12-26 微信 50
- 2017-12-01 支付宝 `angel********@qq.com` 5
- 2018-01-13 微信 10
- 2018-02-25 支付宝 `111***@qq.com` 1
- 2018-03-09 微信 16.66 # 非常感谢算法项目!
- 2018-03-12 支付宝 `189*******91` 10
- 2018-04-15 支付宝 `150******18` 11.11 # 加油!
- 2018-06-09 微信 `*彪` 10 # 博士毕业，在准备面试

所得捐款用于 VPS 付费(优化大陆地区访问)/激励 Contributors 写出更好的内容/购买书籍/西瓜/饮料

## To Do

- [ ] 添加多国语言支持，尤其是英语
- [ ] 添加 `Python`, `C++` 和 `Java` 代码
- [x] 添加空间和时间复杂度分析
