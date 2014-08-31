Dispatcher for tornado

为tornado框架而定制的mvc路由，因为在写tornado的Handler的时候，只能写个get方法，这对历史写过php项目的童鞋不是习惯。那么引入dispatcher就可以方便的按照controller/action的方式写代码。


在访问http://localhst:8081/{controller}/{action} 的url时候，实际调用/appliaction/下面对应名字的controller。即：/application/controller/{controller}Controller.py
模板也是约定和controller名字相同，在application/view下面。
如果实际中模板约定不同，在实际的控制器里面返回{'__tpl_file': 'name'}即可。

项目在tornado4.0测试通过。
例子：
1,启动web server
>>> python main.py

2,测试
>>> curl http://127.0.0.1:8081/test/action1


