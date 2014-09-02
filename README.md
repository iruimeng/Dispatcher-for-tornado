Dispatcher for tornado
======================

为tornado框架开发的url分发器，框架路由默认是用list，如handlers = [(r"/post_path", PostHandler), (r"/del", DeleteHandler), (r"/home",HomeHandler)]来配置路由规则，而此在访问http://localhst:8081/{controller}/{action} 的url时候，实际加载目录/appliaction/下面对应名字的控制器。即：/application/controller/{controller}Controller.py，然后执行里面的{action}方法，然后函数返回data，渲染模板。

####命名预定
* 1，控制器为 name+Controller.py
* 2，模板约定和控制器名字相同，在application/view下面，为{controller}/{action}.htm 如果实际中模板约定不同，在实际的控制器里面返回{'__tpl_file': 'name'}即可。

项目在tornado4.0测试通过。

####测试使用
* 1，启动web server
```Bash
python main.py
```
* 2，测试
```Bash
curl http://127.0.0.1:8081/test/action1
curl http://127.0.0.1:8081/test/action2
```


