# MongoDB

# Install

### Windows

> add mongo bin to **PATH**

**mongod.cfg**

```yaml
systemLog:
    destination: file
    path: d:\data\logs\mongodb.log
storage:
    dbPath: d:\data\db
```

**mkdir**

```shell
mkdir -p d:\data\db
mkdir -p d:\data\logs
```

**install service**

```shell
# must be absolute path
mongod --config "{absolute path of mongod.cfg}" --install

# start and stop
net start mongodb

# delete
sc delete MongoDB
```

another method to installs service

```shell
# sc, service control

```

