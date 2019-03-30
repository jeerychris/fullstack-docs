# Samples

## zookeeper service

```bash
#!/usr/bin/bash
# chkconfig:2345 20 90
# description:zookeeper
# processname:zookeeper

export JAVA_HOME=/usr/local/src/java/jdk1.8.0_192/jre
export ZOO_LOG_DIR=/usr/local/zookeeper-3.4.12
EXEC=/usr/local/zookeeper-3.4.12/bin/zkServer.sh

case "$1" in
    start) 
        $EXEC start
        ;;
    stop) 
        $EXEC stop
        ;;
    status) 
        $EXEC status
        ;;
    restart)
        $EXEC restart
        ;;
    *) 
        echo "require start|stop|status|restart" >&2 
        exit 1
        ;;
esac
```

> `# chkconfig:2345 20 90` chkconfig enabled

## redis service

```bash
#!/usr/bin/bash
# chkconfig: 2345 10 90  
# description: Start and Stop redis   
  
PATH=/usr/local/bin:/sbin:/usr/bin:/bin   
REDISPORT=6379  
EXEC=/usr/local/redis/bin/redis-server
REDIS_CLI=/usr/local/redis/bin/redis-cli   
 
PIDFILE=/var/run/redis.pid   
CONF="/usr/local/redis/bin/redis.conf"  
AUTH="1234"  

case "$1" in   
    start)   
        if [ -f $PIDFILE ]   
        then   
            echo "$PIDFILE exists, process is already running or crashed."  
        else  
            echo "Starting Redis server..."  
            $EXEC $CONF   
        fi   
        if [ "$?"="0" ]   
        then   
            echo "Redis is running..."  
        fi   
        ;;   
    stop)   
        if [ ! -f $PIDFILE ]   
        then   
            echo "$PIDFILE exists, process is not running."  
        else  
            PID=$(cat $PIDFILE)   
            echo "Stopping..."  
            $REDIS_CLI -p $REDISPORT  SHUTDOWN    
            sleep 2  
            while [ -x $PIDFILE ]   
            do  
                echo "Waiting for Redis to shutdown..."  
                sleep 1  
            done   
            echo "Redis stopped"  
        fi   
        ;;   
    restart|force-reload)   
        ${0} stop   
        ${0} start   
        ;;   
    *)   
        echo "Usage: /etc/init.d/redis {start|stop|restart|force-reload}" >&2  
        exit 1  
esac
```

