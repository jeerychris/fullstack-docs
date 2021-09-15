# npm

<https://www.npmjs.com/>

NPM是随同NodeJS一起安装的包管理工具，能解决NodeJS代码部署上的很多问题，常见的使用场景有以下几种：

- 允许用户从NPM服务器下载别人编写的第三方包到本地使用。
- 允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
- 允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。

## help 

<https://docs.npmjs.com/>

`npm -h`
```
Usage: npm <command>

where <command> is one of:
    access, adduser, bin, bugs, c, cache, completion, config,
    ddp, dedupe, deprecate, dist-tag, docs, doctor, edit,
    explore, get, help, help-search, i, init, install,
    install-test, it, link, list, ln, login, logout, ls,
    outdated, owner, pack, ping, prefix, profile, prune,
    publish, rb, rebuild, repo, restart, root, run, run-script,
    s, se, search, set, shrinkwrap, star, stars, start, stop, t,
    team, test, token, tst, un, uninstall, unpublish, unstar,
    up, update, v, version, view, whoami

npm <command> -h     quick help on <command>
npm -l           display full usage info
npm help <term>  search for help on <term>
npm help npm     involved overview

Specify configs in the ini-formatted file:
    C:\Users\hong\.npmrc
or on the command line via: npm <command> --key value
Config info can be viewed via: npm help config

npm@5.6.0 D:\developer\nodejs\node_modules\npm
```

```shell
# version
npm -v

npm -h
# npm help <topic, commnad>
npm help install
```

## Configure

**~/.npmrc**

```properties
# global install dir, default ${NODE_PATH}
prefix=D:\developer\nodejs\global
# mirror url, default 
registry=http://registry.npm.taobao.org/
proxy=null
```



### taobao mirror

大家都知道**国内直接使用 npm 的官方镜像是非常慢**的，这里推荐使用淘宝 NPM 镜像。
淘宝 NPM 镜像是一个完整 npmjs.org 镜像，你可以用此代替官方版本(只读)，同步频率目前为 10分钟 一次以保证尽量与官方服务同步。
你可以使用淘宝定制的 cnpm (gzip 压缩支持) 命令行工具代替默认的 npm:

<http://npm.taobao.org/>

你可以使用我们定制的 [cnpm](https://github.com/cnpm/cnpm) (gzip 压缩支持) 命令行工具代替默认的 `npm`:

```bash
$ npm install -g cnpm --registry=https://registry.npm.taobao.org
```

或者你直接通过添加 `npm` 参数 `alias` 一个新命令:

```bash
alias cnpm="npm --registry=https://registry.npm.taobao.org \
--cache=$HOME/.npm/.cache/cnpm \
--disturl=https://npm.taobao.org/dist \
--userconfig=$HOME/.cnpmrc"

# Or alias it in .bashrc or .zshrc
$ echo '\n#alias for cnpm\nalias cnpm="npm --registry=https://registry.npm.taobao.org \
  --cache=$HOME/.npm/.cache/cnpm \
  --disturl=https://npm.taobao.org/dist \
  --userconfig=$HOME/.cnpmrc"' >> ~/.zshrc && source ~/.zshrc
```

## 全局安装与本地安装

npm 的包安装分为本地安装（local）、全局安装（global）两种，从敲的命令行来看，差别只是有没有-g而已，比如

```bash
npm install express          # 本地安装
npm install express -g   # 全局安装
```

### 本地安装

- \1. 将安装包放在 ./node_modules 下（运行 npm 命令时所在的目录），如果没有 node_modules 目录，会在当前执行 npm 命令的目录下生成 node_modules 目录。
- \2. 可以通过 require() 来引入本地安装的包。

### 全局安装

- \1. 将安装包放在 /usr/local 下或者你 node 的安装目录。
- \2. 可以直接在命令行里使用。



## package.json

[对package.json的理解和学习](https://www.cnblogs.com/whkl-m/p/6617540.html)

> package.json 位于模块的目录下，用于定义包的属性。

1. npm安装package.json时  直接转到当前项目目录下用命令npm install 或npm install --save-dev安装即可，自动将package.json中的模块安装到node-modules文件夹下
2. package.json 中添加中文注释会编译出错
3. 每个项目的根目录下面，一般都有一个package.json文件，定义了这个项目所需要的各种模块，以及项目的配置信息（比如名称、版本、许可证等元数据）。npm install 命令根据这个配置文件，自动下载所需的模块，也就是配置项目所需的运行和开发环境。

最简单的的一个package.json 文件（只有两个数据，项目名称和项目版本，他们都是必须的，如果没有就无法install）

```json
{
  "name": "app-name",
  "version": "1.0.0"
}
```

### scripts

指定了运行脚本命令的npm命令行缩写，比如start指定了运行npm run start时，所要执行的命令。

下面的设置指定了npm run dev、npm run bulid、npm run unit、npm run test、npm run lint时，所要执行的命令。　

```json
"scripts": {
    "dev": "node build/dev-server.js",
    "build": "node build/build.js",
    "unit": "cross-env BABEL_ENV=test karma start test/unit/karma.conf.js --single-run",
    "test": "npm run unit",
    "lint": "eslint --ext .js,.vue src test/unit/specs"
  },
```

### dependencies，devDependencies

`npm install --save`参数表示将该模块写入dependencies属性，
`npm install --save-dev`表示将该模块写入devDependencies属性。

`npm install` defaut is with `--save` option, write dependency to package.json and `npm uninstall` uninstall and remove from package.json

```json
"dependencies": {
    "vue": "^2.2.2",
    "vue-router": "^2.2.0"
  },
  "devDependencies": {
    "autoprefixer": "^6.7.2",
    "babel-core": "^6.22.1",
    "babel-eslint": "^7.1.1",
    "babel-loader": "^6.2.10",
    "babel-plugin-transform-runtime": "^6.22.0",
    "babel-preset-env": "^1.2.1",
    "babel-preset-stage-2": "^6.22.0",
    "babel-register": "^6.22.0",
    "chalk": "^1.1.3",
}
```
### 关于版本号的描述

[package.json's dependency version](https://www.jianshu.com/p/b3d86ddfd555)

使用NPM下载和发布代码时都会接触到版本号。NPM使用语义版本号来管理代码，这里简单介绍一下。
语义版本号分为X.Y.Z三位，分别代表主版本号、次版本号和补丁版本号。当代码变更时，版本号按以下原则更新。

- 如果只是修复bug，需要更新Z位。
- 如果是新增了功能，但是向下兼容，需要更新Y位。
- 如果有大变动，向下不兼容，需要更新X位。

##### 使用~表示版本范围

| 标识示例 |           描述           |         版本范围         |                                         说明                                         |
| :------: | :----------------------: | :----------------------: | :----------------------------------------------------------------------------------: |
|  ~2.3.4  | 主版本+次要版本+补丁版本 | 2.3.4 <= version < 2.4.0 | 在主版本+次要版本不允许变更的前提下，允许补丁版本升级（补丁板板号下限是4，无上限）。 |
|   ~2.3   |     主版本+次要版本      | 2.3.0 <= version < 2.4.0 |               在主版本+次要版本不允许变更的前提下，允许补丁版本升级。                |
|    ~2    |          主版本          | 2.0.0 <= version < 3.0.0 |               在主版本不允许变更的前提下，允许次要版本+补丁版本升级。                |

##### 使用^表示版本范围

| 标识示例 |     描述      |         版本范围         |                                        说明                                         |
| :------: | :-----------: | :----------------------: | :---------------------------------------------------------------------------------: |
|  ^1.3.4  | 主版本号不为0 | 1.3.4 <= version < 2.0.0 | 主版本不为0，允许次要版本+补丁版本升级（此例下限是1.3.4，上线是2.0.0但不匹配2.0.0） |

## most used command

```bash
npm -v
npm -h
npm help <module, topic-name>

npm search express
npm install express -g

npm list
npm list -g
npm list http

npm init
npm update
npm uninstall
```

```json
{
  "name": "runoob",
  "version": "1.0.0",
  "description": "Node.js 测试模块(www.runoob.com)"
}
```

# node module system

## 模块

- 系统模块
- 自定义模块

### most used system module

`fs`
`path`
`http`
`url`
`querystring`
`events`

## keywords and usages

require——引入其他模块
exports——输出
module——批量输出

exports.xxx=??;
exports.xxx=??;
exports.xxx=??;

module.exports={
​	xxx:	??,
​	xxx:	??,
​	xxx:	??
};

1.自己的模块
​	require
​	module
​	exports

2.引入模块	./	?
3.".js"可选


node_modules——放模块

---------------------------------------------------------------------------------------------------------------------

./
不加./		必须放在node_modules里面

---------------------------------------------------------------------------------------------------------------------
## resolve module
require
1.如果有"./"
​	从当前目录找

2.如果没有"./"
​	先从系统模块
​	再从node_modules找

自定义模块统一，都放到node_modules里面

---------------------------------------------------------------------------------------------------------------------

1.模块里面
​	require——引入
​	exports——输出
​	module.exports——批量输出

2.npm
​	帮咱们下载模块
​	自动解决依赖

3.node_modules
​	模块放这里

---------------------------------------------------------------------------------------------------------------------

npm init
npm publish
npm --force unpublish

---------------------------------------------------------------------------------------------------------------------

# express framework

like jquery, some basic enhancement, but it's **midleware** is powerful

> Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications.

## install

```shell
npm install express
# install midleware express-static
npm install express-static
```
## basic use

1. 依赖中间件

2. 接收请求
   get/post/use
   get('/地址', function (req, res){});

3. 非破坏式的, express保留了原生的功能，添加了一些方法(send)，增强原有的功能
   req.url

4. static用法
   const static=require('express-static');
   server.use(static('./www'));

```js
const express=require('express');
const expressStatic=require('express-static');

var server=express();
server.listen(8080);

//用户数据
var users={
  'blue': '123456',
  'zhangsan': '654321',
  'lisi': '987987'
};

server.get('/login', function (req, res){
  var user=req.query['user'];
  var pass=req.query['pass'];

  if(users[user]==null){
    res.send({ok: false, msg: '此用户不存在'});
  }else{
    if(users[user]!=pass){
      res.send({ok: false, msg: '密码错了'});
    }else{
      res.send({ok: true, msg: '成功'});
    }
  }
});

server.use(expressStatic('./www'));
```
----------------

## data resolution

### GET vs POST

GET-无需中间件
req.query

POST-需要"body-parser"
server.use(bodyParser.urlencoded({}));

server.use(function (){
​	req.body
});

### 链式操作：

```js
// 1.GET
// req.query

// POST
  server.use(bodyParser.urlencoded({limit: }));
  server.use(function (req, res, next){
    req.body
  });

// 2.链式操作
  server.use(function (req, res, next){});
  server.get('/', function (req, res, next){});
  server.post(function (req, res, next){});

  next();

  server.use('/login', function (){
    mysql.query(function (){
      if(有错)
        res.emit('error');
      else
        next();
    });
  });

// 3.中间件(body-parser)、自己写中间件
// next();

  server.use(function (req, res, next){
    var str='';
    req.on('data', function (data){
      str+=data;
    });
    req.on('end', function (){
      req.body=querystring.parse(str);
      next();
    });
  });
```
## cookie and session

### 中间件

```js
const cookieParser=require('cookie-parser');
const cookieSession=require('cookie-session');
```

### conceptions

http-**无状态的**

cookie、session

cookie：在浏览器保存一些数据，每次请求都会带过来
  *不安全、有限(4K)

session：保存数据，保存在服务端
  *安全、无限

session：基于cookie实现的
  *cookie中会有一个session的ID，服务器利用sessionid找到session文件、读取、写入

  隐患：session劫持

--------------

### cookie
1.读取——cookie-parser
2.发送——

session
cookie-session

cookie：
1.cookie空间非常小——省着用
2.安全性非常差

1.精打细算
2.校验cookie是否被篡改过

a.发送cookie
res.secret='字符串';
res.cookie(名字, 值, {path: '/', maxAge: 毫秒, signed: true});

```js
server.use(cookieParser('wesdfw4r34tf'));

server.use('/', function (req, res){
  req.secret='wesdfw4r34tf';
  res.cookie('user', 'blue', {signed: true});

  console.log('签名cookie：', req.signedCookies)
  console.log('无签名cookie：', req.cookies);

  res.send('ok');
});

// 删除cookie
res.clearCookie(名字);
```

### session
cookie-session

```js
const express=require('express');
const cookieParser=require('cookie-parser');
const cookieSession=require('cookie-session');

var server=express();

//cookie
var arr=[];

for(var i=0;i<100000;i++){
  arr.push('sig_'+Math.random());
}

server.use(cookieParser());
server.use(cookieSession({
  name: 'sess',
  keys: arr,
  maxAge: 2*3600*1000
}));

server.use('/', function (req, res){
  if(req.session['count']==null){
    req.session['count']=1;
  }else{
    req.session['count']++;
  }

  console.log(req.session['count']);

  res.send('ok');
});

server.listen(8080);
```

## template engine

- jade-破坏式、侵入式、强依赖
- ejs-温和、非侵入式、弱依赖

### jade

1. 根据缩进，规定层级

2. 属性放在()里面，逗号分隔
  - style={}
  - class=[]

3. 内容空个格，直接往后堆

**template**: `2.jade`

```jade
html
  head
    style
    script(src="a.js")
    link(href="a.css",rel="stylesheet")
  body
    div
      ul
        li
          input(type="text",id="txt1",value="abc")
        li
          input(type="text",id="txt2",value="111")
        li
          input(type="text",id="txt3",value="222")
    div
```

**jade-demo.js**
```js
const jade=require('jade');
const fs=require('fs');

var str=jade.renderFile('./views/2.jade', {pretty: true});

fs.writeFile('./build/2.html', str, function (err){
  if(err)
    console.log('写入失败');
  else
    console.log('写入成功');
});
```
**advanced**

```jade
doctype
html
  head
    meta(charset="utf-8")
    title jade测试页面
    style.
      div {width:100px;height:100px;background:#CCC;text-align:center;line-height:100px;float:left;margin:10px auto}
      div.last {clear:left}
  body
    -var a=0;
    while a<12
      if a%4==0 && a!=0
        div.last=a++
      else
        div=a++
jade
```

### ejs

like java **standard tag lib**, use `<% %>`

### consolidate

a unified interface for express template engine

## basic-middleware

### multer for multimedia

body-parser	解析post数据
`multer`		解析post文件

```html
    <form action="http://localhost:8080/" method="post" enctype="multipart/form-data">
      文件：<input type="file" name="f1" /><br>
      <input type="submit" value="上传">
    </form>
```

```js
const express=require('express');
const static=require('express-static');
const cookieParser=require('cookie-parser');
const cookieSession=require('cookie-session');
const bodyParser=require('body-parser');
const multer=require('multer');
const ejs=require('ejs');
const jade=require('jade');

var server=express();

server.listen(8080);

//1.解析cookie
server.use(cookieParser('sdfasl43kjoifguokn4lkhoifo4k3'));

//2.使用session
var arr=[];
for(var i=0;i<100000;i++){
  arr.push('keys_'+Math.random());
}
server.use(cookieSession({name: 'zns_sess_id', keys: arr, maxAge: 20*3600*1000}));

//3.post数据
server.use(bodyParser.urlencoded({extended: false}));
server.use(multer({dest: './www/upload'}).any());

//用户请求
server.use('/', function (req, res, next){
  console.log(req.query, req.body, req.files, req.cookies, req.session);
});

//4.static数据
server.use(static('./www'));
```

## database mysql

```js
const mysql = require('mysql');

//1.连接
//createConnection(哪台服务器, 用户名, 密码, 库)
var db = mysql.createConnection({ host: 'localhost', user: 'root', password: 'mysql57', database: 'pinyougoudb' });

//2.查询
//query(干啥, 回调)
db.query("SELECT * FROM `tb_user` limit 1;", (err, data) => {
  if (err)
    console.log('出错了', err);
  else
    console.log('成功了');
  console.log(data);
});
```

------------
- [x] 01.历史、优势、现状、前景、必备基础技能、和前台JS的关系及区别.mp4
- [x] 02.http系统模块使用.mp4
- [x] 03.fs文件模块.mp4
- [x] 04.http数据解析-get.mp4
- [x] 05.http数据解析-post.mp4
- [x] 06.实例&总结1：简易httpServer搭建.mp4
- [x] 07.NodeJS模块化1：系统模块介绍.mp4
- [x] 08.NodeJS模块化2：自定义模块.mp4
- [x] 09.Express框架1：介绍、配置安装.mp4
- [x] 10.Express框架2：数据解析[12580sky.com].mp4
- [x] 11.Express框架3：cookie、session.mp4
- [x] 12.jade模板库1：介绍、配置安装、基础语法.mp4
- [x] 13.jade模板库2：高级语法、简单实例.mp4
- [x] 14.ejs模板库1：介绍、配置安装、基础语法、高级语法、实例.mp4
- [x] 15.Express框架整合：express整合、multer使用、consolidate和route.mp4
- [x] 16.MySQL基本使用：安装、配置、数据库组成、Navicat使用.mp4
- [x] 17.MySQL基本使用：SQL基本写法(INSERT和SELECT)、NodeJS操作MySQL.mp4
- [ ] 18.实例：基于Express的blog 1-数据库构建.mp4
- [ ] 19.实例：基于Express的blog 2-NodeJS服务搭建.mp4
- [ ] 20.实例：基于Express的blog 3-banner部分.mp4
- [ ] 21.实例：基于Express的blog 3-banner文章列表.mp4
- [ ] 22.实例：基于Express的blog 3-banner文章详情.mp4
- [ ] 23.实例：基于Express的blog 3-banner转义输出.mp4
- [ ] 24.实例：基于Express的blog 3-banner点赞.mp4
- [ ] 25.SQL语句1：4大操作语句基本写法、WHERE子句、ORDER子句、GROUP.mp4
- [ ] 26.SQL语句2：GROUP子句应用.mp4
- [ ] 27.SQL语句3：LIMIT子句[12580sky.com].mp4
- [ ] 28.项目实战 - 教育网站1：数据字典、数据库结构.mp4
- [ ] 29.项目实战 - 教育网站2：Express结构搭建[12580sky.com].mp4
- [ ] 30.项目实战 - 教育网站3：router、后台管理结构.mp4
- [ ] 31.项目实战 - 教育网站5：banner数据添加、删除.mp4
- [ ] 32.项目实战 - 教育网站7：banner数据修改.mp4
- [ ] 33.项目实战 - 教育网站8：custom数据搭建、添加、文件上传.mp4
- [ ] 34.项目实战 - 教育网站10：custom数据删除、文件操作.mp4
- [ ] 35.项目实战 - 教育网站11：custom数据修改、文件替换.mp4
- [ ] 36.项目实战 - 教育网站12：前台接口-banner、custom、Angular.mp4