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

# Syntax

**shell**: mongo

see  doc `mogodb-ReferenceCards15.pdf`

```js
// use, show, help

// show basic command
help;

show dbs;
use test;
show collections();

// db.createCollection("users");
// if collection not exists, create 
db.users.insert({name: "Bob", age: 20});

db.users.find();
db.users.find({name: "Bob"});
```

