## spring AOP(aspect oriented programming)

### Question & solution
**Question: wanna enhance save method, add some check**

```java
class UserDao{
    void save(){
            // save user
        }
}
```
**common solution**
```java
class UserDao{
    void save(){
            // save user
        }
}
class UserDaoChild extends UserDao{
        void check(){}

        void save(){
                check();
                // save user
            }
    }
```
but some class is final, can't be inherited, there two solution.
***Box design pattern, for class implements a interface***
```java
interface IUserDao{
        void save();
    }
final class UserDao implements IUserDao{
    @Override
    void save(){
            // save user
        }
}
class UserDaoBox implements IUserDao{
        UserDao userDao = null;

        UserDaoBox(UserDao userDao){
                this.userDao = userDao;
            }
        
        @Override
        void save(){
                check();
                userDao.save();
            }

        void check();
    }
···

### AOP termination
- **Joinpoint** 
>

```