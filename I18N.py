"""
I18N 簡易實作函式。

請透過 `I18N.I18N` 呼叫 I18N 函式。
"""
import os, json, sys
from I18N import theString

class I18N:
    '''
    此函式作為 I18N 用途，輸入 string_id 之後
    會優先回傳目標語言 (tranLangFile) 的字串，而後
    再回傳原始語言 (origLangFile) 的字串。

    origLangFile
        原始語言檔案，格式為 json。
    
    tranLangFile
        目標語言檔案，格式為 json。

    語言檔案格式
    {
        "string_id": "應出現字串"
    }
    '''
    def __init__(self, origLangFile, tranLangFile):
        # Open both language files.
        oraw = open(origLangFile, "r", encoding="UTF-8")
        traw = open(tranLangFile, "r", encoding="UTF-8")
        # Read both language files.
        ocont = oraw.read()
        tcont = traw.read()
        # Decode both language files.
        self.oJSON = json.loads(ocont)
        self.tJSON = json.loads(tcont)
        # Close both language files.
        oraw.close()
        traw.close()

    def str(self, string_id):
        """
        回傳 string_id 所對應的字串。

        string_id
            請參閱 LangHandler 說明。欲顯示的字串所對應之字串 ID。
            例如 "string_id": "字串"
        """
        if string_id in self.oJSON:
            if string_id in self.tJSON:
                return self.tJSON[string_id]
            else:
                return self.oJSON[string_id]
        else:
            sys.stderr.write(theString.err_stringIDinvaild.format(string_id))
            return ""