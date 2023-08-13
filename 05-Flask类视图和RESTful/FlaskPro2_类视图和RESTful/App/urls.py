# urls.py 路由文件

from .exts import api
from .apis import *

# 路由
api.add_resource(HelloResource, '/hello/')