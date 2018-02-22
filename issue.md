## Issue 001
```
models内from . import db一直存在错误，原因在于__init__初始化包中蓝图导入在文件首所以导致了循环导入查找db
所以把blueprints的载入放在db变量申明后就可以了。
```
## Issue 002
```
https://stackoverflow.com/questions/26516939/flask-blueprints-runtimeerror-application-not-registered-on-db
```
## Issue 003
```
windows 需要mysql驱动,linux不用
```