# JSON 國際化工具 for Python
## 概述
您可以使用這個小工具來做 I18N。

## 使用方法
### 前置作業
1. 下載最新的 release，或者是下載 master 分支。
2. 將解壓縮後的資料夾名稱取為 `I18N`
3. 在您的 Python 程式最上面增加<br>
   `from I18N import I18N`
4. 可以使用 I18N 函式了。

### 製作語言檔案
格式如下：

```
{
    "string_id1": "string",
    "string_id2": "string"
}
```

而 string_id1 (string_id2) 就是「字串 ID」，string 就是字串。

而字串 ID 是稍候用來對應 `i18n.str()` 函式所需的代號，模組會
自動幫你把這一大串「代號」轉換成字串。

### 建立 i18n 處理函式
`i18n = I18N.I18N("原始語言檔案", "翻譯語言檔案")`

沒錯，有三個 I18N（

原始語言檔案就是這程式的對應字串，當翻譯語言檔案
沒有這個字串會優先使用原始語言檔案中的字串。

例如： `i18n = I18N.I18N("orig.json", "tran.json")`

如果你現在還不打算開放翻譯，但想先做到 I18N，<br>
那就這樣： `i18n = I18N.I18N("orig.json", "orig.json")`

Wait, 如果連原始語言檔案都沒有這個字串呢？

那這程式就會發出這個錯誤：

```
Error: The string id [xxxxx] isn't vaild! Please report this error to developer!
```

你肯定不希望看到這個錯誤，所以請確保你的每個字串 ID 都有正確對應到喔 :-)

### 開始對應翻譯
設定完之後該怎麼使用呢？

首先我們瞭解一下 i18n.str() 這個函式：

```
i18n.str(string_id):
    """
    回傳 string_id 所對應的字串。
        
    字串優先級
        若翻譯語言檔案中沒有某字串 -> 使用原文語言檔案中的字串。
        若原文語言檔案沒有某字串 -> 發出 theString.py 中定義的錯誤字串至 stderr。

    string_id
        請參閱根函式說明。此處需輸入在語言檔案所指定的字串 ID。
    """
```

從以上說明中，我們知道了使用方法就是 i18n.str("字串 ID")。

假如你的語言檔案長這樣：

```
{
    "str1_meow": "meeeeow"
}
```

那使用方法就是 `i18n.str("str1_meow")`

那什麼是回傳呢？講白話就是要你這樣用：<br>
`print(i18n.str("str1_meow"))` ，它就會輸出 `meeeeow` <br>
簡單來說，i18n.str("str1_meow") == "meeeeow"。

進階一點的應用， `print(i18n.str("str1_meow") + "!")` <br>
就會等於 `print("meeeeow" + "!")`

那這函式就只能用在 print 嗎？不只，你可以用在任何地方，舉個例子：<br>
`sys.stderr.write(i18n.str("str1_meow") + "!")` <br>
== `sys.stderr.write("meeeeow" + "!")` <br>
=> 向 stderr 管道輸入「meeeeow!」！

那我們再多加一個字串：

```
{
    "str1_meow": "meeeeow",
    "str2_meow": "cat"
}
```

接著輸入 `print(i18n.str("str1_meow") + i18n.str("str2_meow"))` <br>
呈現出了 `meeeeowcat`

酷吧！

### 多語言化
那我該怎麼製作出不同語言的語言檔案呢？

回到《建立 i18n 處理函式》的例子： `i18n = I18N.I18N("orig.json", "tran.json")`

假設 orig.json 長這樣：

```
{
    "hello_world": "Hello, World!",
    "copyright": "pan93412, 2018."
}
```

tran.json 長這樣：

```
{
    "hello_world": "哈囉，世界！"
}
```

執行 `print(i18n.str("hello_world") + i18n.str("copyright"))` <br>
出現 `哈囉，世界！pan93412, 2018.`

這個模組的邏輯就是假如 tran.json 沒有某字串，就去抓 orig.json 的字串來用。
因此假如你用 `i18n = I18N.I18N("orig.json", "orig.json")` 也就代表始終使用
orig.json 的字串了。

## 自訂程式
### 提示文字自訂
還記得在《建立 i18n 處理函式》中的這串錯誤訊息嗎？

```
Error: The string id [{:s}] isn't vaild! Please report this error to developer!\n
```

這段文字你可以修改。這段文字儲存在 `theString.py` 中，直接修改成你喜歡的文字就好。
唯獨「{:s}」這個必須在字串當中，否則可能會發生錯誤。(「{:s}」就是那個不存在的字串 ID。)

另外 `\n` 也建議保留，否則下一段文字可能會接到這錯誤訊息後，導致訊息可讀性降低。

# 推薦工具
- [JSON 語言檔案合併差異工具](https://github.com/pan93412/json-langfile-merge-tool)

# 作者
pan93412 <<pan93412@gmail.com>\>, 2018.
