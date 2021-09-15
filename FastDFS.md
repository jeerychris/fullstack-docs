Reference:

[用FastDFS一步步搭建文件管理系统](https://www.cnblogs.com/chiangchou/p/fastdfs.html)

# FastDFS

file servers:

​	small files:  FastDFS, TFS

​	large: MongoDB

## 图片服务器介绍

要实现图片上传功能，需要有一个图片服务器。图片服务器的特点：

1. 存储空间可扩展

2. 提供统一的访问方式

3. 访问效率高

## 什么是FastDFS
>FastDFS是用c语言编写的一款开源的分布式文件系统。FastDFS为互联网量身定制，充分考虑了冗余备份、负载均衡、横向扩展等机制，并注重高可用、高性能等指标，使用FastDFS很容易搭建一套高性能的文件服务器集群提供文件上传、下载等服务。

## FastDFS架构
FastDFS架构包括 Tracker server和Storage server。客户端请求Tracker server进行文件上传、下载，通过Tracker server调度最终由Storage server完成文件上传和下载。

**Tracker server**
作用是**负载均衡和调度**，通过Tracker server在文件上传时可以根据一些策略找到Storage server提供文件上传服务。可以将tracker称为追踪服务器或调度服务器。

**Storage server**
作用是文件存储，客户端上传的文件最终存储在Storage服务器上，Storage server没有实现自己的文件系统而是**利用操作系统的文件系统**来管理文件。可以将storage称为存储服务器。

![fastDFS-arch.png](images/fastDFS-arch.png)

**Tracker**
管理集群
收集信息，处理信息
为了保证高可用，可以搭建集群

**Storage**
保存文件
分为很多组，组和组之间的数据不一样
组内成员数据是一样的，保证数据的高可用
可以增加组，达到扩容的效果

## **FastDFS的存储策略**

为了支持大容量，存储节点（服务器）采用了**分卷**（或分组）的组织方式。存储系统由一个或多个卷组成，**卷与卷之间的文件是相互独立**的，所有卷的文件容量累加就是整个存储系统中的文件容量。一个卷可以由一台或多台存储服务器组成，**一个卷下的存储服务器中的文件都是相同的**，卷中的多台存储服务器起到了**冗余备份和负载均衡**的作用。

在卷中**增加服务器**时，**同步**已有的文件由系统自动完成，同步完成后，系统自动将新增服务器切换到线上提供服务。当存储空间不足或即将耗尽时，可以动态**添加卷**。只需要增加一台或多台服务器，并将它们配置为一个新的卷，这样就扩大了存储系统的容量。

## **FastDFS的文件同步**

写文件时，客户端将文件**写至group内一个storage server即认为写文件成功**，storage server写完文件后，会由后台线程将文件同步至同group内其他的storage server。

每个storage写文件后，同时会写一份binlog，binlog里不包含文件数据，只包含文件名等元信息，这份binlog用于后台同步，storage会记录向group内其他storage同步的进度，以便重启后能接上次的进度继续同步；进度以时间戳的方式进行记录，所以最好能保证集群内所有server的时钟保持同步。

storage的同步进度会作为元数据的一部分汇报到tracker上，tracke在选择读storage的时候会以**同步进度**作为参考

## ==文件上传流程==
文件上传流程如下图（时序图）：

![fastDFS-upload-sequence-chart.png](images/fastDFS-upload-sequence-chart.png)

客户端上传文件后存储服务器将文件ID返回给客户端，此文件ID用于以后访问该文件的索引信息。文件索引信息包括：组名，虚拟磁盘路径，数据两级目录，文件名。

## download sequence chart

![fastDFS-download.png](images/fastDFS-download.png)

![fastDFS-filename.png](images/fastDFS-filename.png)

- 组名：文件上传后所在的storage组名称
- 虚拟磁盘路径：storage配置的虚拟路径，与磁盘选项store_path*对应。如果配置了store_path0则是M00，如果配置了store_path1则是M01，以此类推。
- 数据两级目录：storage服务器在每个虚拟磁盘路径下创建的两级目录，用于存储数据文件。两级目录的范围都是 **00~FF**
- 文件名：与文件上传时不同。是由存储服务器根据特定信息生成，文件名包含：**源存储服务器IP地址、文件创建时间戳、文件大小、随机数和文件拓展名**等信息。



# INSTALL

details: see https://github.com/happyfish100/fastdfs

```shell
#step 1. download libfastcommon source package from github and install it,
   the github address:
   https://github.com/happyfish100/libfastcommon.git

#step 2. download FastDFS source package and unpack it, 
tar xzf FastDFS_v5.x.tar.gz
#for example:
tar xzf FastDFS_v5.08.tar.gz

#step 3. enter the FastDFS dir
cd FastDFS

#step 4. execute:
./make.sh

#step 5. make install
./make.sh install

#step 6. edit/modify the config file of tracker and storage

#step 7. run server programs
#start the tracker server:
/usr/bin/fdfs_trackerd /etc/fdfs/tracker.conf restart
#in Linux, you can start fdfs_trackerd as a service:
/sbin/service fdfs_trackerd start

#start the storage server:
/usr/bin/fdfs_storaged /etc/fdfs/storage.conf restart
#in Linux, you can start fdfs_storaged as a service:
/sbin/service fdfs_storaged start

#step 8. run test program
#run the client test program:
/usr/bin/fdfs_test <client_conf_filename> <operation>

#for example, upload a file:
/usr/bin/fdfs_test conf/client.conf upload /usr/include/stdlib.h

#step 9. run monitor program
#run the monitor program:
/usr/bin/fdfs_monitor <client_conf_filename>
```

## 默认安装方式安装后的相应文件与目录

```shell
# service script
/etc/init.d/fdfs_storaged
/etc/init.d/fdfs_tracker

# configration files
/etc/fdfs/client.conf.sample
/etc/fdfs/storage.conf.sample
/etc/fdfs/tracker.conf.sample

# !/usr/bin
fdfs_appender_test
fdfs_appender_test1
fdfs_append_file
fdfs_crc32
fdfs_delete_file
fdfs_download_file
fdfs_file_info
fdfs_monitor
fdfs_storaged
fdfs_test
fdfs_test1
fdfs_trackerd
fdfs_upload_appender
fdfs_upload_file
stop.sh
restart.sh 
```

## CONFIGURE

**tracker.conf**

```properties
# 提供服务的端口
port=22122

# Tracker 数据和日志目录地址(根目录必须存在,子目录会自动创建)
base_path=/home/data/fastdfs/tracker

# HTTP 服务端口
http.server_port=80
```

**storage.conf**

```properties
# storage server 服务端口
port=23000

# Storage 数据和日志目录地址(根目录必须存在，子目录会自动生成)
base_path=/home/data/fastdfs/storage

# 存放文件时 storage server 支持多个路径。这里配置存放文件的基路径数目，通常只配一个目录。
store_path_count=1

# 逐一配置 store_path_count 个路径，索引号基于 0。
# 如果不配置 store_path0，那它就和 base_path 对应的路径一样。
store_path0=/home/data/fastdfs/file

# tracker_server 的列表 ，会主动连接 tracker_server
# 有多个 tracker server 时，每个 tracker server 写一行
tracker_server=192.168.1.254:22122

# 访问端口
http.server_port=80
```

**client.conf**

```properties
# the base path to store log files
base_path=/home/data/fastdfs/client

# tracker_server can ocur more than once, and tracker_server format is
#  "host:port", host can be hostname or ip address
tracker_server=192.168.1.214:22122
```



# Nginx

1. [nginx 反向代理](https://www.cnblogs.com/ysocean/p/9392908.html)
2. [windows下nginx的安装及使用](https://www.cnblogs.com/jiangwangxiang/p/8481661.html)

## problems

将nginx配置到环境变量，结果命令行输入nginx启动时，提示

```bat
could not open error log file: CreateFile() "logs/error.log" failed
CreateFile() "C:\Users\xxxxxx/conf/nginx.conf" failed
```

原因是nginx默认是从当前目录找配置文件，结果找不到。 解决办法就是先进入nginx的安装目录，再执行nginx.exe

## install

```shell
# -c continue
wget -c https://nginx.org/download/nginx-1.12.1.tar.gz
tar -zxvf nginx-xxx.tar.gz
cd nginx-xxx

# 使用默认配置
./configure
# compile, install
make
make install

# location: /usr/local/nginx/
cd /usr/local/nginx
# start
./sbin/nginx

# test
curl http://localhost/

# other commands
nginx -s stop
nginx -s reload
```

## configure

**`/usr/local/nginx/conf/nginx.conf`**

```properties
http{
    server{
    	listen	80;
        server_name	localhost;
        
        # add fastdfs storage location
        location /group1/M00{
            alias /home/data/fastdfs/file/data;
        }
    }
}
```



# FastDFS Nginx module

see [FastDFS 配置 Nginx 模块](https://www.cnblogs.com/chiangchou/p/fastdfs.html#_label3)

**astdfs-nginx-module 模块说明**

　　FastDFS 通过 Tracker 服务器，将文件放在 Storage 服务器存储， 但是**同组存储服务器**之间需要进行文件复制， 有**同步延迟的问题**。

　　假设 Tracker 服务器将文件上传到了 192.168.51.128，上传成功后文件 ID已经返回给客户端。

　　此时 FastDFS 存储集群机制会将这个文件同步到同组存储 192.168.51.129，在文件还没有复制完成的情况下，客户端如果用这个文件 ID 在 192.168.51.129 上取文件,就会出现文件无法访问的错误。

　　而 fastdfs-nginx-module 可以重定向文件链接到源服务器取文件，避免客户端由于复制延迟导致的文件无法访问错误。

# Linux command

```shell
# make dir, if parent exists, no error
mkdir -p /home/data/fdfs

# start service, and other service command, like stop, status
service fdfs_trackerd start
/ect/init.d/fdfs_trackerd start

# start service on startup
chkconfig fdfs_trackerd on
# list all startup service
chkconfig --list

# netstat with grep

# see all opened ports
netstat -ano
# see specifical port
netstat -ano | grep 23000
# -u udp, -n numeric -l listening -t tcp -p program
netstat -unltp | grep fdfs

# create start.sh's symbolic link at /usr/local/bin/
ln -s /usr/bin/start.sh /usr/local/bin/
```

