# Guidelines for Contributing

- Access English via [Guidelines for Contributing](http://algorithm.yuanbin.me/en/faq/guidelines_for_contributing.md)
- 繁體中文請移步 [貢獻指南](http://algorithm.yuanbin.me/zh-tw/faq/guidelines_for_contributing.md)
- 简体中文请移步 [贡献指南](http://algorithm.yuanbin.zh-hans/faq/guidelines_for_contributing.md)

除去 [FAQ](http://algorithm.yuanbin.me/zh-hans/faq/index.html) 中提到的兩種輕量級貢獻方法外，你還可以採用 git 這種分佈式協作工具一起改進這個文檔。

如果你不確定自己是否會貢獻比較多的內容，那麼在 GitHub 上 fork 後發 Pull Reqeust 就好了。如果你想成爲 Collaborators 貢獻大量內容, 那麼請大膽發郵件到(yuanbin2014(at)gmail.com)，大歡迎~

總結一下 git 的工作流程就是：

1. 從遠端更新 - `git pull origin master`
2. commit 本機更改 - `git commit -a -m 'xxx'`
3. 推送回遠端 - `git push origin master`

有些時候在 commit 之前可能會忘記 pull, 那麼此時 pull 將會產生一個 merge commit, 這顯然是不太優雅的，建議使用`git rebase -i` 解決。

git 的簡明教學可參考 b哥的 [Git Manual](https://gist.github.com/bigeagle/3953973), 小清新極簡教程可參考 [git - the simple guide - no deep shit!](http://rogerdudler.github.io/git-guide/), rebase 的使用可參考 [1](http://stackoverflow.com/questions/21115596/remove-a-merge-commit-keeping-current-changes), [2](https://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E8%A1%8D%E5%90%88), [3](https://blog.yorkxin.org/posts/2011/07/29/git-rebase/)

既然涉及到文檔合作，那麼最好是能有個像樣的文檔規範之類的東西方便大家更好的合(ㄐㄧㄠ)作(ㄐ一ˋ)，目前想到的有如下幾點。

## 更新/翻譯特定語言

Gitbook 支持多語言書寫，具體通過根目錄下的 `LANGs.md` 目錄指定，目前根目錄下有`en`, `zh-hans`, `zh-tw` 三個子文件夾分別用於三種語言的書寫，每個子文件夾相當於一個單獨的 Gitbook, 與其他語言的文檔是獨立的，所以更新時只需在各自語言的目錄下工作就好了。各語言的 SUMMARY.md 文件內容保持一致，且均使用英文。

## 目錄生成

Gitbook 中使用`SUMMARY.md`這個文件控制生成目錄，添加新內容時最好使用 Gitbook 家自帶的編輯器添加，這樣省事一點點。

## 文檔格式及編輯工具 - GFM && kramdown Markdown

使用markdown編寫，只使用 Gitbook 支援的 markdown 語法。Gitbook 底層的 markdown renderer 爲改動的 kramdown，並增加了GFM支援, 支援的擴充 markdown 語法算是非常多了，具體特性詳見 [GitbookIO/kramed](https://github.com/GitbookIO/kramed)

推薦的 markdown 編輯器爲 Gitbook 自家的 [editor](https://www.gitbook.com/editor), 目前新版的 bug 太多，而且是自動 commit 的，不便於版本控制，希望他們後續能改進。所以目前推薦老版，老版的見 [editor-lagecy](https://github.com/GitbookIO/editor-legacy/releases), 支持 Windows/Linux/MAC 三大平臺，業界良心！但是實測在Arch Linux/OSX 下可能會出現佔用記憶體/CPU過高的情況... 編輯界面如下圖所示，最左邊爲章節預覽，中間爲 markdown 編輯框，右邊爲實時render頁面，可選擇使用全屏模式。

![Gitbook Editor](../../shared-files/images/gitbook_editor.png)

使用其他如 Mou/Vim/Emacs/Sublime Text也不錯，但是在新增Chapter/Section時就比較麻煩了，嗯，你也可以新建 Section 後再使用其他編輯器編輯。

對 Gitbook 不熟的建議看看 [Gitbook Documentation](http://help.gitbook.com/)，有助於瞭解 http://algorithm.yuanbin.me 網頁上的文字及各章節等是如何編輯及render的。

## 章節名及編號

章節等文件名全部採用英文，子章節最多到三級，章節編號無需操心，這種瑣事交給 Gitbook 去做就好，如果一定要手動調整，修改`SUMMARY.md`文件，注意其中的縮排關係，Gitbook就依靠這個自動給章節編號了。

舉個例子，我現在想新增「動態規劃」及其子章節。首先在 Gitbook 頂部menu欄「Book」中找到「Add Chapter」，填入「Dynamic Programming」。好了，在Gitbook左側章節欄中就能看到新生成的「10. Dynamic Programming」了，左鍵單擊，Gitbook 就會生成「dynamic_programming」目錄及本章的說明文件「dynamic_programming/README.md」。如果想在「10. Dynamic Programming」下新增子章節，右鍵單擊，「Add Section」即可，同上，子章節文件名仍然使用英文名，網頁顯示的標題可以通過 rename 更改再加入中文。

嗯，以上步驟均可直接新建文件夾及操作`SUMMARY.md`文件完成。

## 正文書寫風格

1. 中英文混排貫穿全文，優雅美觀起見，儘可能在英文單詞前後加空格，這個使用能在輸入法中英文間加入空格功能就好了。
2. 程式碼的函數名或短的程式碼建議使用 \`code\`
3. 使用空行進行分段，嗯，markdown通用

Part II爲leetcode/lintcode題解，這部分的風格相對容易統一，感覺還不錯的風格 - [Distinct Subsequences](https://github.com/billryan/algorithm-exercise/blob/master/zh-hans/dynamic_programming/distinct_subsequences.md)

大致遵循如下風格：

1. 給出題目鏈接及原文，引用的原文部分簡單起見我對題目使用了blockquote ，具體可參考我的那些markdown文本。
2. 給出自己的題解，儘可能清晰易懂。
3. 給出能AC的code, 如遇TLE或者錯誤的看情況給出錯誤的實現。使用blockquote, 給出語言類別以便highlight。具體可參看原markdown文件。
4. 題解中的核心部分對應的程式碼，程式碼中不能明顯看出來的邏輯和一些程式上常用的技巧。
5. 程式碼順序：Python => C++ => Java 因爲 Python 的程式碼一般最爲簡潔...
6. 如參考了其他資源，儘可能給出有用的參考鏈接，附簡單的說明。

通過github合作時，添加/修改內容時給出能看懂的commit就好了。暫時就想到這麼多，其實沒那麼多講究啦，感覺看著清楚就好，其他想到的再補充。:-)

### 數學公式

其實程式碼裡是用不著寫數學公式的，但是偶爾分析演算法可能會用著，用過 LaTeX 的都知道她生成的數學公式有多優雅，以至於不用她來寫數學公式都有點不舒服...

這個文檔裡對於較複雜的數學公式建議使用 LaTeX, 因爲託管在gitbook上，所以就用了輕量級的katex插件，沒有用重量級的 MathJax。行內(inline)和行間公式都是 兩個$, 區別在於行間公式寫到下一行行首，而行內公式不能寫在行首(廢話...)。katex非常脆弱，對一些高級的 LaTeX 語法不支援，否則無法編譯輸出到網站和pdf，儘量用簡單的 LaTeX 語法或者不用。

### 附件及圖片引用

圖片統一存放在`images`目錄下，其他附件存放在`docs`目錄下。引用圖片鏈接一般可以通過`![Caption](../../shared-files/images/xxx.png)`聲明。

圖片體積太大不利於頁面載入，建議先壓縮後再放入，如果是png圖片可考慮使用 [TinyPNG – Compress PNG images while preserving transparency](https://tinypng.com/)