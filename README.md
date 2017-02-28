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

if you want get someone followers

you can use it for this:

'''python
from followers import Followers

flers = Followers(url_token="chen-er-bai-18")

for i in flers.get_api_object():
    print i["name"], i["url_token"]
```
the same `following.py`, `question_api.py`, `voter_profile.py`, `comments.py`, `following_topic.py`

the `question.py` use old api it return html then parse pyquery.