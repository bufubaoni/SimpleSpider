# www.zhihu.com spider

Simple Spider for zhihu in china

for use it ,you should create a file named **user_headers.py**

### user_headers.py

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the content of browser's request headers, after you login zhihu.com
headers = {
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.zhihu.com',
    'Connection': 'keep-alive',
    'X-Xsrftoken': 'your xsrf token',
    'Cookie': 'your cookies'
}
```

happy new year