# Maven cheat sheet

[![maven-cheat-sheet][]](images/maven-cheat-sheet.png)



## Change default jdk

> `$install/conf/settings.xml`

```xml
<profiles>
    <profile>
        <id>jdk1.8</id>
        <activation>
            <jdk>1.8</jdk>
            <activeByDefault>true</activeByDefault>
        </activation>
        <properties>
            <maven.compiler.source>1.8</maven.compiler.source>
            <maven.compiler.target>1.8</maven.compiler.target>
            <maven.compiler.compilerVersion>1.8</maven.compiler.compilerVersion>
            <maven.compiler.encoding>utf-8</maven.compiler.encoding>
        </properties>
    </profile>
</profiles>
```

## Configure local repository

```xml
<localRepository>D:\repo</localRepository>
```

## Configure remote Repositories and Mirrors

> for quick downloading, see also ==oneNote:== `java/grocery/maven*`

```xml
<profile>
    <repositories>
        <!-- 如有Nexus私服, 取消注释并指向正确的服务器地址.
        <repository>
            <id>nexus-repos</id>
            <name>Team Nexus Repository</name>
            <url>http://192.168.11.36:8888/nexus/content/groups/public</url>
        </repository> -->
        <repository>
            <id>oschina-repos</id>
            <name>Oschina Releases</name>
            <url>http://maven.oschina.net/content/groups/public</url>
        </repository>
        <repository>
            <id>aliyun-repos</id>
            <name>aliyun Releases</name>
            <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
        </repository>
        <repository>
            <id>java-repos</id>
            <name>Java Repository</name>
            <url>https://maven.java.net/content/repositories/public/</url>
        </repository>
        <repository>
            <id>JBoss-repos</id>
            <name>JBoss Repository</name>
            <url>http://repository.jboss.org/nexus/content/groups/public/</url>
        </repository>
        <repository>
            <id>springsource-repos</id>
            <name>SpringSource Repository</name>
            <url>http://repo.spring.io/release/</url>
        </repository>
        <repository>
            <id>central-repos</id>
            <name>Central Repository</name>
            <url>http://repo.maven.apache.org/maven2</url>
        </repository>
        <repository>
            <id>central-repos2</id>
            <name>Central Repository 2</name>
            <url>http://repo1.maven.org/maven2/</url>
        </repository>
        <repository>
            <id>activiti-repos</id>
            <name>Activiti Repository</name>
            <url>https://maven.alfresco.com/nexus/content/groups/public</url>
        </repository>
        <repository>
            <id>activiti-repos2</id>
            <name>Activiti Repository 2</name>
            <url>https://app.camunda.com/nexus/content/groups/public</url>
        </repository>
        <repository>
            <id>easonjim-repos</id>
            <name>EasonJim Repository</name>
            <url>https://raw.github.com/easonjim/repository/master</url>
        </repository>
    </repositories>
</profile>
```

```xml
<mirrors>
    <mirror>
        <id>aliyun-repos</id>
        <name>aliyun Releas</name>
        <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
        <mirrorOf>central</mirrorOf>
    </mirror>
</mirrors>
```



## Configure mirrors

> for quick downloading, 

## Add Tomcat plugin

```xml
<build>
		<plugins>
			<plugin>
				<groupId>org.apache.tomcat.maven</groupId>
				<artifactId>tomcat7-maven-plugin</artifactId>
				<version>2.2</version>
				<configuration>
					<port>8091</port>
					<path>/jt</path>
				</configuration>
			</plugin>
		</plugins>
</build>
```

# Maven Dependency Management

![maven-dependency-management][]

# pom.xml

> springboot's hello world pom

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>it.launch</groupId>
    <artifactId>spring-boot-helloworld</artifactId>
    <version>1.0-SNAPSHOT</version>

    <!-- Inherit defaults from Spring Boot -->
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.7.RELEASE</version>
    </parent>

    <!-- Add typical dependencies for a web application -->
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>

    <!-- Package as an executable jar -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
    
</project>
```



[maven-cheat-sheet]: images/maven-cheat-sheet.png
[maven-dependency-management]: images/maven-dependency-management.png

