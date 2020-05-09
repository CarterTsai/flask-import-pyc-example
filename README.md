Flask引用PYC檔案範例
===============


### 編譯出pyc檔案
```bash
$> python -m py_compile test.py
```

### 更名pyc
當編譯出pyc檔案要注意檔名要跟原本檔案一樣，但是副檔名還是pyc
接著將pyc檔案放在你想引用的地方，例如將pyc檔案放在專案底下有一個lib的目錄
使用方式

```python
from lib.test import Animal

@app.route("/")
def hello():
    x = Animal("dog")
    return jsonify({'who': x.who()})
```

### 啟動服務

```bash
$> docker-compose up -d
```

### 瀏覽網站
http://localhost:8881/