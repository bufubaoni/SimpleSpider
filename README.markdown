# www.zhihu.com spider

Simple Spider for zhihu in china

for use it ,you should create a file named **user_headers.py**

    ```python
    # the content of browser's headers,in you login zhihu
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://www.zhihu.com',
        'Connection': 'keep-alive',
        'Cookie': 'your cookies'
    }
    ```

    ```ruby
    require 'redcarpet'
    markdown = Redcarpet.new("Hello World!")
    puts markdown.to_html
    ```