废品回收系统
============
![](https://img.shields.io/badge/python-3.6.1-green.svg)
![](https://img.shields.io/badge/Django-2.1.7-green.svg)
![](https://img.shields.io/badge/python--alipay--sdk-1.10.0-green.svg)
![](https://img.shields.io/badge/aliyun--python--sdk--core-2.13.4-green.svg)
![](https://img.shields.io/badge/version-1.0.0-green.svg)   

废品回收系统是一个使用Python Django构建的网站，可以让社区用户随时随地下单，系统会通过短信的方式及时通知回收人员上门进行废品回收，回收人员回收废品后完善订单的信息，如回收的废品种类，废品重量等，系统会根据提交的信息进行金额计算，并通过支付宝的转账功能给社区用户转账，从而达到一体化回收废品的功能。   

核心功能点
----------
* 用户注册，登录，修改密码、账号、手机号
* 短信验证码，短信订单通知
* 支付宝转账
* xadmin后台管理
* 其他...

快速安装及启动
-------------
```bash
git clone git@github.com:BeyondLIG/WasteRecyclingSystem.git
cd WasteRecycleSystem 
pip freeze -> requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver 
```

FAQ
------
* [xadmin安装](https://www.twblogs.net/a/5c0160f6bd9eee7aec4ec301/zh-cn)
* [阿里云通信](https://help.aliyun.com/document_detail/55288.html)

