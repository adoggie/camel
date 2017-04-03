
##发布配置

设置环境变量 CAMEL_HOME 为指定运行的主目录，如不设置 则默认目录为 /srv/camel

设置环境变量 APP_NAME 为项目名称,例如:  carrier ,driver 

    export CAMEL_HOME=/srv/camel
    export APP_NAME=carrier_server
    
   

##开发配置 

####1.设置环境变量 CAMEL_HOME 为开发项目的目录
    
    export CAMEL_HOME=/home/scott/projects/carrier
    
 程序启动时在$CAMEL_HOME中自动创建目录: run, data, etc, logs 

####2.删除环境变量 APP_NAME 设置
    

##发布和开发配置区别

发布目录：

    /srv/camel
    ├── data
    │   └── carrier_server
    ├── etc
    │   └── carrier_server
    │       └── settings.yaml
    ├── logs
    │   └── carrier_server
    │       ├── server.log
    │       └── trans.log
    ├── products
    │   └── carrier_server
    └── run
        └── carrier_server
    
####开发目录

    /home/project/carrier_server/
    ├── data
    │   └── data.01
    ├── etc
    │   └── settings.yaml
    ├── logs
    │   ├── server.log
    │   └── trans.log
    ├── run
    │   ├── carrier.pid
    │   └── start-carrier.sh
    └── src
        ├── server.py
        └── service


开发目录详细

    test_project/
    ├── README.md
    ├── data
    ├── etc
    │   └── settings.yaml
    ├── logs
    │   ├── server.log
    │   └── trans.log
    ├── run
    ├── scripts
    ├── src
    │   ├── model
    │   │   └── __init__.py
    │   ├── route
    │   │   ├── __init__.py
    │   │   └── v1
    │   │       ├── __init__.py
    │   │       └── car.py
    │   ├── server.py
    │   └── service
    │       └── __init__.py
    └── tests
        └── test_run.py


##Blueprint设置 

在项目代码 src 中 创建 route 目录：

     # route/__init__.py 
     
     import car      # 导入route 目录中的blueprint 模块
    __url__ = '/v1'  # 当前路由的url_prefix
    __app__ = 'app'  # blueprint 模块中的名称
    
    # route/v1/car.py 
    
    app = Blueprint('car',__name__)  # 'car' - 为blueprint模块的 url_prefix
    @app.route('/')
    def car():
        return 'okay'
        
    >>  wget http://127.0.0.1:5000/v1/car/
    >> 'okay'
    

flask-sqlalchemy