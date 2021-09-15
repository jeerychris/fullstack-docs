# errors when install and test

## redis cluster

### create cluster err

**detail**

```shell
[ERR] Node 192.168.1.254:7001 is not empty. Either the node already knows other nodes (check with CLUSTER NODES) or contains some key in database 0.
```

1. already created.
2. pesistence files is not deleted in `$NODE/bin`

**get key**

```shell
127.0.0.1:7003> get count
(error) MOVED 8188 192.168.1.254:7002
```

- not connected in cluster mode

```shell
# -c, cluster mode
./bin/redis-cli -p 7003 -c
```



## VMWare虚拟机

### 无法打开内核设备"\\.\Global\vmx86"

```bash
net start vmx86
```

