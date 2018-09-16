"""
這個模組讓您的程式可以支援國際化，不必設定複雜的 gettext，
就可以讓來自各個地方的人都可以把你的程式翻譯成他們的語言。

* 請透過 `I18N.I18N` 呼叫 I18N 函式。

作者：pan93412
"""
import os, json, sys
from I18N import theString

class I18N:
    '''
    * 請參閱 README.md
    
    這個模組讓您的程式可以支援國際化，不必設定複雜的 gettext，
    就可以讓來自各個地方的人都可以把你的程式翻譯成他們的語言。
    
    語言檔案格式
        {
            "string_id1": "string",
            "string_id2": "string"
        }
    
    origLangFile (JSON 檔案)
        原文語言檔案。若翻譯字串沒有某字串則使用此處
        的字串。origLangFile 是一個檔案路徑，該檔案
        必須是標準 JSON 格式。
        
    tranLangFile (JSON 檔案)
        翻譯語言檔案。優先套用此處已有的字串。
        tranLangFile 是一個檔案路徑，該檔案必須是
        標準 JSON 格式。
    
    字串優先級
        若翻譯語言檔案中沒有某字串 -> 使用原文語言檔案中的字串。
        若原文語言檔案沒有某字串 -> 發出 theString.py 中定義的錯誤字串至 stderr。
        
    字串 ID
        參閱語言檔案格式。string_id1 與 string_id2 就是字串 ID，
        string 則是字串。
    '''
    def __init__(self, origLangFile, tranLangFile):
        '''
        請參閱根函式說明。
        origLangFile (JSON 檔案)
            原文語言檔案。若翻譯字串沒有某字串則使用此處
            的字串。origLangFile 是一個檔案路徑，該檔案
            必須是標準 JSON 格式。
        
        tranLangFile (JSON 檔案)
            翻譯語言檔案。優先套用此處已有的字串。
            tranLangFile 是一個檔案路徑，該檔案必須是
            標準 JSON 格式。
        '''
        # 開啟兩個語言檔案
        oraw = open(origLangFile, "r", encoding="UTF-8")
        traw = open(tranLangFile, "r", encoding="UTF-8")
        # 讀取兩個語言檔案中的資料
        ocont = oraw.read()
        tcont = traw.read()
        # 將資料解析成 Python 接受的 Dict 格式
        # self.oJSON 與 self.tJSON 皆為要在 str() 函式中的
        # 變數。
        self.oJSON = json.loads(ocont)
        self.tJSON = json.loads(tcont)
        # 關閉兩個語言檔案，以防止佔用記憶體資源。
        oraw.close()
        traw.close()

    def str(self, string_id):
        """
        回傳 string_id 所對應的字串。
        
        字串優先級
            若翻譯語言檔案中沒有某字串 -> 使用原文語言檔案中的字串。
            若原文語言檔案沒有某字串 -> 發出 theString.py 中定義的錯誤字串至 stderr。

        string_id
            請參閱根函式說明。此處需輸入在語言檔案所指定的字串 ID。
        """
        if string_id in self.oJSON:
            if string_id in self.tJSON:
                return self.tJSON[string_id]
            else:
                return self.oJSON[string_id]
        else:
            sys.stderr.write(theString.err_stringIDinvaild.format(string_id))
            return ""
