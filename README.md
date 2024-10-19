# flask demo

集flask-sqlalchemy blueprint于一体的框架模板


# 安装
```
# windows powershell设置FLASK_APP变量，让接下来的flask命令知道调用的是那个flask app
# 在项目根目录运行
$env:FLASK_APP="app"
# 如果是macos或者linux系统
export FLASK_APP=app

flask shell

from app.extensions import db
from app.models.post import Post
db.create_all()

db.drop_all()
db.create_all()
```