# 如何貢獻

简体中文请移步 [贡献指南](https://github.com/billryan/algorithm-exercise/blob/master/contributing_zh-cn.md)

如果你發現本文檔有任何可以改進之處，歡迎提交你的改進，具體形式有如下幾種。

1. 在 <http://algorithm.yuanbin.me> 相應網頁下的disqus評論框中添加評論，指出一些typo或者可以改進的地方。
2. 在本文檔的GitHub repo 處提交 issue, 指出有問題的地方。
3. 提交 Pull Request, fork 本文檔的 GitHub repo, 發PR給我就好了。
4. 成為本項目的 contributor, 發郵件並把你的 GitHub 賬戶名告訴我就可以了，我收到郵件後把你的 GitHub 賬號加到Collaborators中。在對 git 操作不是特別熟悉的情況下建議通過方式3提交 PR，相對安全很多。

方式3 和4 push 到 GitHub 前都需要先更新-`git pull origin master`, 可能需要處理衝突和合併。對 git 不熟的可以看看 [git - the simple guide - no deep shit!](http://rogerdudler.github.io/git-guide/), 大概只用到了 `add & commit`, `pushing changes`, `update & merge`. 可以先在自己的 Repo 內玩玩後再在 GitHub 上提交 Pull Request, 等你有足夠信心掌握 git 的這些基本操作後可以大膽地申請為本項目的 Contributer, 這樣就不用頻繁提交 PR 啦~

既然涉及到文檔合作，那麼最好是能有個像樣的文檔規範之類的東西方便大家合作得更好，目前想到的有如下幾點。

## 更新/翻譯特定語言

Gitbook 支援多語言書寫，具體透過根目錄下的 `LANGs.md` 目錄指定，目前根目錄下有`en`, `zh-cn`, `zh-tw` 三個子文件夾分別用於三種語言的書寫，每個子文件夾相當於一個單獨的 Gitbook, 與其他語言的文檔是獨立的，所以更新時只需在各自語言的目錄下工作就好了。各語言的 SUMMARY.md 文件內容保持一致。

## 文檔格式及編輯工具 - GFM && kramdown Markdown

使用markdown編寫，只使用 Gitbook 支持的 markdown 語法。Gitbook 底層的 markdown renderer 為改動的 kramdown，並增加了GFM支援, 支援的擴展 markdown 語法算是非常多了，具體特性詳見 [GitbookIO/kramed](https://github.com/GitbookIO/kramed)

推薦的 markdown 編輯器為 Gitbook 自家的 [GitbookIO/editor](https://github.com/GitbookIO/editor), 支援 Windows/Linux/MAC 三大平台，業界良心！但是實測在Arch Linux/OSX 下可能會出現占用記憶體/CPU過高的情況... 編輯界面如下圖所示，最左邊為章節預覽，中間為 markdown 編輯框，右邊為實時渲染頁面，可選擇使用全螢幕模式。

![Gitbook Editor](./images/gitbook_editor.png)

使用其他如 Mou/Vim/Emacs/Sublime Text也不錯，但是在新增Chapter/Section時就比較麻煩了，嗯，你也可以新建 Section 後再使用其他編輯器編輯。

對 Gitbook 不熟的建議看看 [Gitbook Documentation](http://help.gitbook.com/)，有助於了解 http://algorithm.yuanbin.me 網頁上的文字及各章節等是如何編輯及渲染的。

## 章節名及編號

章節等文件名全部採用英文，子章節最多到三級，章節編號無需操心，這種瑣事交給 Gitbook 去做就好，如果一定要手動調整，修改`SUMMARY.md`文件，注意其中的縮排關係，Gitbook就指望這個自動給章節編號了。

舉個例子，我現在想新增「動態規劃」及其子章節。首先在 Gitbook 頂部menu bar「Book」中找到「Add Chapter」，填入「Dynamic Programming」。好了，在Gitbook左側章節欄中就能看到新生成的「10. Dynamic Programming」了，左鍵擊之，Gitbook 就會生成「dynamic_programming」目錄及本章的說明文件「dynamic_programming/README.md」。如果想在「10. Dynamic Programming」下新增子章節，右鍵擊之，「Add Section」即可，同上，子章節文件名仍然使用英文名，網頁顯示的標題可以通過 rename 更改再加入中文。

嗯，以上步驟均可直接新建資料夾及改寫`SUMMARY.md`文件完成。

## 正文書寫風格

1. 中英文混排貫穿全文，優雅美觀起見，儘可能在英文單詞前後加空格，這個使能輸入法的中英文間加入空格功能就好了。
2. 程式碼的函數名或短程式碼建議使用 \`code\`
3. 使用空行進行分段，嗯，markdown通用

Part II為leetcode/lintcode題解，這部分的風格相對容易統一，感覺還不錯的風格 - [Distinct Subsequences](https://github.com/billryan/algorithm-exercise/blob/master/zh-cn/dynamic_programming/distinct_subsequences.md)

大致遵循如下風格：

1. 給出題目連結及原文，引用的原文部分簡單起見我對題目使用了blockquote ，具體可參考我的那些markdown文本。
2. 給出自己的題解，儘可能清晰易懂。
3. 給出能AC的code, 如遇TLE或者錯誤的看情況給出錯誤的實現。使用blockquote, 給出語言類別以便highlight。具體可參看原markdown文件。
4. 題解中的核心部分對應的程式碼，程式碼中不能明顯看出來的邏輯和一些程式設計上常用的技巧。
5. 如參考了其他資源，盡可能給出有用的參考連結，附簡單的說明。

通過github合作時，添加/修改內容時給出能看懂的commit就好了。暫時就想到這麼多，其實沒那麼多講究啦，感覺看著清楚就好，其他想到的再補充。:-)

### 數學公式

其實程式碼裡是用不著寫數學公式的，但是偶爾分析演算法可能會用到，用過 LaTeX 的都知道她生成的數學公式有多優雅，以至於不用她來寫數學公式都有點不舒服...

這個文檔裏對於較複雜的數學公式建議使用 LaTeX, 因為托管在gitbook上，所以就用了輕量級的katex插件，沒有用重量級的 MathJax。行內和行間公式都是 兩個$, 區別在於行間公式寫到下一行行首，而行內公式不能寫在行首(廢話...)。katex非常脆弱，對一些高級的 LaTeX 語法不支持，否則無法編譯輸出到網站和pdf，盡量用簡單的 LaTeX 語法或者不用。

### 附件及圖片引用

圖片統一存放在`images`目錄下，其他附件存放在`docs`目錄下。引用圖片連結一般可以通過`![Caption](../images/xxx.png)`聲明。

圖片檔案太大不利於頁面加載，建議先壓縮後再放入，如果是png圖片可考慮使用 [TinyPNG – Compress PNG images while preserving transparency](https://tinypng.com/)
