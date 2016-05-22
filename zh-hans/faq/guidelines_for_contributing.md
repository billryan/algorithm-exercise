# Guidelines for Contributing

- Access English via [Guidelines for Contributing](http://algorithm.yuanbin.me/en/faq/guidelines_for_contributing.html)
- 繁體中文請移步 [貢獻指南](http://algorithm.yuanbin.me/zh-tw/faq/guidelines_for_contributing.html)
- 简体中文请移步 [贡献指南](http://algorithm.yuanbin.me/zh-hans/faq/guidelines_for_contributing.html)

除去 [FAQ](http://algorithm.yuanbin.me/zh-hans/faq/index.html) 中提到的两种轻量级贡献方法外，你还可以采用 git 这种分布式协作工具一起改进这个文档。

如果你不确定自己是否会贡献较多的内容，那么在 GitHub 上 fork 后给我发 Pull Reqeust 就好了。如果你想成为 Collaborators 贡献大量内容, 那么请大胆给我发邮件(yuanbin2014(at)gmail.com)，热烈欢迎~

总结一下 git 的工作流程就是：

1. 更新上游 - `git pull origin master`
2. commit 本地更改 - `git commit -a -m 'xxx'`
3. 推送到上游 - `git push origin master`

有些时候在 commit 之前可能会忘记 pull, 那么此时 pull 将会产生一个 merge commit, 这显然是不太优雅的，建议使用`git rebase -i` 解决。

git 的简明教程可参考 b哥的 [Git Manual](https://gist.github.com/bigeagle/3953973), 小清新极简教程可参考 [git - the simple guide - no deep shit!](http://rogerdudler.github.io/git-guide/), rebase 的使用可参考 [1](http://stackoverflow.com/questions/21115596/remove-a-merge-commit-keeping-current-changes), [2](https://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E8%A1%8D%E5%90%88), [3](https://blog.yorkxin.org/posts/2011/07/29/git-rebase/)

既然涉及到文档合作，那么最好是能有个像样的文档规范之类的东西方便大家更好的合(jiao)作(ji)，目前想到的有如下几点。

## 更新/翻译特定语言

Gitbook 支持多语言书写，具体通过根目录下的 `LANGs.md` 目录指定，目前根目录下有`en`, `zh-hans`, `zh-tw` 三个子文件夹分别用于三种语言的书写，每个子文件夹相当于一个单独的 Gitbook, 与其他语言的文档是独立的，所以更新时只需在各自语言的目录下工作就好了。各语言的 SUMMARY.md 文件内容保持一致，且均使用英文。

## 目录生成

Gitbook 中使用`SUMMARY.md`这个文件控制生成目录，添加新内容时最好使用 Gitbook 家自带的编辑器添加，这样省事一点点。

## 文档格式及编辑工具 - GFM && kramdown Markdown

使用markdown编写，只使用 Gitbook 支持的 markdown 语法。Gitbook 底层的 markdown renderer 为改动的 kramdown，并增加了GFM支持, 支持的扩展 markdown 语法算是非常多了，具体特性详见 [GitbookIO/kramed](https://github.com/GitbookIO/kramed)

推荐的 markdown 编辑器为 Gitbook 自家的 [editor](https://www.gitbook.com/editor), 目前新版的 bug 太多，而且是自动 commit 的，不便于版本控制，希望他们后续能改进。所以目前推荐老版，老版的见 [editor-lagecy](https://github.com/GitbookIO/editor-legacy/releases), 支持 Windows/Linux/MAC 三大平台，业界良心！但是实测在Arch Linux/OSX 下可能会出现占用内存/CPU过高的情况... 编辑界面如下图所示，最左边为章节预览，中间为 markdown 编辑框，右边为实时渲染页面，可选择使用全屏模式。

![Gitbook Editor](../../shared-files/images/gitbook_editor.png)

使用其他如 Mou/Vim/Emacs/Sublime Text也不错，但是在新增Chapter/Section时就比较闹心了，嗯，你也可以新建 Section 后再使用其他编辑器编辑。

对 Gitbook 不熟的建议看看 [Gitbook Documentation](http://help.gitbook.com/)，有助于了解 http://algorithm.yuanbin.me 网页上的文字及各章节等是如何编辑及渲染的。

## 章节名及编号

章节等文件名全部采用英文，子章节最多到三级，章节编号无需操心，这种琐事交给 Gitbook 去做就好，如果一定要手动调整，修改`SUMMARY.md`文件，注意其中的缩进关系，Gitbook就指望这个自动给章节编号了。

举个例子，我现在想新增「动态规划」及其子章节。首先在 Gitbook 顶部菜单栏「Book」中找到「Add Chapter」，填入「Dynamic Programming」。好了，在Gitbook左侧章节栏中就能看到新生成的「10. Dynamic Programming」了，左键击之，Gitbook 就会生成「dynamic_programming」目录及本章的说明文件「dynamic_programming/README.md」。如果想在「10. Dynamic Programming」下新增子章节，右键击之，「Add Section」即可，同上，子章节文件名仍然使用英文名，网页显示的标题可以通过 rename 更改再加入中文。

嗯，以上步骤均可直接新建文件夹及操作`SUMMARY.md`文件完成。

## 正文书写风格

1. 中英文混排贯穿全文，优雅美观起见，尽可能在英文单词前后加空格，这个使用能在输入法中英文间加入空格功能就好了。
2. 代码的函数名或短代码建议使用 \`code\`
3. 使用空行进行分段，嗯，markdown通用

Part II为leetcode/lintcode题解，这部分的风格相对容易统一，感觉还不错的风格 - [Distinct Subsequences](https://github.com/billryan/algorithm-exercise/blob/master/zh-hans/dynamic_programming/distinct_subsequences.md)

大致遵循如下风格：

1. 给出题目链接及原文，引用的原文部分简单起见我对题目使用了blockquote ，具体可参考我的那些markdown文本。
2. 给出自己的题解，尽可能清晰易懂。
3. 给出能AC的code, 如遇TLE或者错误的看情况给出错误的实现。使用blockquote, 给出语言类别以便高亮。具体可参看原markdown文件。
4. 题解中的核心部分对应的代码，代码中不能明显看出来的逻辑和一些编程上常用的技巧。
5. 代码顺序：Python => C++ => Java 因为 Python 的代码一般最为简洁...
6. 如参考了其他资源，尽可能给出有用的参考链接，附简单的说明。

通过github合作时，添加/修改内容时给出能看懂的commit就好了。暂时就想到这么多，其实没那么多讲究啦，感觉看着清楚就好，其他想到的再补充。:-)

### 数学公式

其实代码里是用不着写数学公式的，但是偶尔分析算法可能会用着，用过 LaTeX 的都知道她生成的数学公式有多优雅，以至于不用她来写数学公式都有点不舒服...

这个文档里对于较复杂的数学公式建议使用 LaTeX, 因为托管在gitbook上，所以就用了轻量级的katex插件，没有用重量级的 MathJax。行内和行间公式都是 两个$, 区别在于行间公式写到下一行行首，而行内公式不能写在行首(废话...)。katex非常脆弱，对一些高级的 LaTeX 语法不支持，否则无法编译输出到网站和pdf，尽量用简单的 LaTeX 语法或者不用。

### 附件及图片引用

图片统一存放在`images`目录下，其他附件存放在`docs`目录下。引用图片链接一般可以通过`![Caption](../../shared-files/images/xxx.png)`声明。

图片体积太大不利于页面加载，建议先压缩后再放入，如果是png图片可考虑使用 [TinyPNG – Compress PNG images while preserving transparency](https://tinypng.com/)
