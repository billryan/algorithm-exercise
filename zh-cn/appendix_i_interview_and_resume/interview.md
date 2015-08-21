# Interview

本小节主要总结一些面试相关的优质资源。

## Facebook workshop - Crush Your Coding Interview

Facebook 每年的5月份左右会在中国大陆的清北复交浙等高校做技术讲座，基本模式是两到三个工程师进行现场分享，Frank 会着重介绍一些面试流程和简历撰写的细节，信息量非常大！其他几个工程师则是介绍自己在 Facebook 所做的产品和企业文化，全程约两个半小时，后面是 Q & A 环节，对提问者有各种小礼物送出。我会说我拿到了F的官方T恤了吗 :) 质地还不错，布料摸起来比较舒服，logo 也不太明显。强烈推荐在这五所高校附近的 CSer 们前去围观！本校的就更不要错过了啦~

咳咳，进入正题，以下为自己对当晚 Facebook 工程师经验分享的一些总结，部分参考自浙大一位童鞋的总结[^Facebook 交流]。

大致的 slides 如下，没有在网上找到公开的，以下是自己根据照片总结的。

### Resume

#### What to include on your resume

1. University, degree, expected graduation date
    - Highly recommended including GPA with scale/ranking
2. Projects
    - Industry experience (internships, competition, full-time)
    - Interesting projects
    - Links where applicable (github, apps, websites)

学校/学位/毕业时间(方便 HR 知道你何时毕业筛选简历)，GPA 最好能附上权重，不同的学校 GPA 总分不一样。

#### Writing a great resume

1. Focus on what you did
2. Focus on Impact(metrics and numbers are a plus)
3. Be specific and concise (1 page if at all possible)
4. Pro tip: alawys start with an active verb
    - example: built, optimized, improved, doubled, etc
5. Don't include
    - Age, photo, ID number

提供客观数据，具体且简短，多使用动词如『优化』、『提高』等，不要在简历中包含年龄，照片，ID 号，有些东西与法律相关。

### Coding interview

#### Goals of a coding interview

Protip: Think out loud!

1. How you think and tackle technical problems
2. How you consider engineering trade offs (speed vs. time)
3. How you communicate in English about codes
4. Limits of what you know
    - Don't feel bad if you don't get all answers right

#### What is covered?

Use your comfortable coding language (C++ Java would be better)

之前听 Google 的工程师说是尽量使用 C++ 和 Java 实现。

1. Data structures and algorithms
    - implement, not memorize
    - discuss complexity (space and time trade-offs)
    - Common library functions are fair game
2. Specific questions about concepts are rare
    - Unless you claim to be an export or need the concept

#### During the interview

1. Clarify your understanding
    - ask questions until you fully understand problem space and constraints
    - validate or state any assumptions
    - draw pictures to help you better understand problems
2. Focus on getting a working solution first
    - handle corner cases
3. Iterate


1. 举一两个例子，有可能的话还可以在白板上画出来帮助理解。问题的限制不是那么明确，确定和面试官理解的是同一个问题。
2. 尝试获得一个能工作的 code
3. 进行迭代，寻找更好的方法。记住测试自己的代码，选择简单但是典型的测试案例。

不要立即写代码，先明确思路，再写代码。Done is better than perfect

能否修改原数组，空间限制，时间限制。

大体方案要和面试官讨论。一定要和面试官多交流，思考过程和方法。

be yourself, 坦白地说出自己不懂的地方，没什么不好的，把知道的地方说清楚。

最近做的/最喜欢的/最具挑战性的项目是什么，不只是要把项目背景说出来，还要说出为什么喜欢，有哪些挑战，推理过程。

#### 项目讨论的框架

1. context: 简要描述项目背景，为什么要做，意义和影响何在。让面试官快速了解。
2. action: 你在这个项目中做了什么，贡献是什么。
3. result: 项目的结果，失败的项目也可以讲，在这个项目中学到了什么，得到了什么样的成长。

简历中提到的技术一定要熟悉。站在面试官的角度问自己会问自己什么问题。

面试之后，可以问面试官问题，着重问自己关心的问题。

### behavior question

1. motivation：动机从何而来，整个过程中做了什么。
2. passion: 激情，哪种产品让你特别兴奋，为什么。
3. team pair: 团队合作? 这里忘了
4. disagreement: 怎么处理不同意见和冲突。

回答要具体，跟自己有关系，而不是泛泛而谈。

#### 总结

1. Think out loud, 不用担心自己的英语，把主要意思表达清楚就好了.
2. 面试中多问问题，充分理解题意。
3. 不要写 shit code, 提供典型案例测试自己的代码
4. 多练习，可以找几个小伙伴进行模拟面试，交换角色，在白板上多写代码。
5. 电话面试找一个安静的地方，把双手解放出来，便于写代码。

## Reference

本小节部分摘自九章微信的分享。

- [www.geeksforgeeks.org](http://www.geeksforgeeks.org/) -  非常著名的漏题网站之一。上面会时不时的有各种公司的面试真题漏出。有一些题也会有解法分析。
- [Programming Interview Questions | CareerCup](http://www.careercup.com/) -  CC150作者搞的网站，也是著名的漏题网站之一。大家会在上面讨论各个公司的面试题。
- [Glassdoor – Get Hired. Love Your Job.](http://www.glassdoor.com/index.htm) - 一个给公司打分的网站，类似yelp的公司版。会有一些人在上面讨论面试题，适合你在面某个公司的时候专门去看一下。
- [面经网 | 汇集热气腾腾的求职咨询](http://www.themianjing.com/) - 面经网。应该是个人经营的一个积累面经的网站。面经来源主要是一亩三分地，mitbbs之类的地方。
- [一亩三分地论坛-美国加拿大留学申请|工作就业|英语考试|学习生活信噪比最高的网站](http://www.1point3acres.com/bbs/) - 人气非常高的论坛。
- [待字闺中(JobHunting)版 | 未名空间(mitbbs.com)](http://www.mitbbs.com/bbsdoc/JobHunting.html)  jobhunting版，美华人找工作必上。
- [程序员面试：电话面试问答Top 50 - 博客 - 伯乐在线](http://blog.jobbole.com/84618/) - 其实不仅仅只是 Top 50，扩展连接还给出了其他参考。
- [想加入硅谷顶级科技公司，你该知道这些](http://mp.weixin.qq.com/s?__biz=MzA4ODM1MTMzMQ==&amp;mid=205185140&amp;idx=2&amp;sn=7682772b799b0542de2f1a5cd13ad292&amp;scene=1#rd) - 数据工程师董飞的求职分享，涵盖硅谷公司的招聘流程，简历的书写，面试中的考察内容，选拔标准等。Evernote [备份链接](https://www.evernote.com/shard/s165/sh/4ef5916a-2db5-4d2e-b71b-68da38a92d41/cb6705242283b700)
- [求职在美国，面试攻略我知道 on Vimeo](https://vimeo.com/113182965) - Coursera 数据工程师董飞的视频分享。
- [^Facebook 交流]: [Facebook学长交流分享 - biaobiaoqi - 博客园](http://www.cnblogs.com/biaobiaoqi/p/3753750.html) - Facebook 工程师的经验分享，Frank 对面试和简历部分的分享极其详细，信息量很大。
