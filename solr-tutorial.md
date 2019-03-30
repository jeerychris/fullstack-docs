# Solr install and deploy

## Solr 

<http://lucene.apache.org/solr/guide/>

> Solr is a search server built on top of Apache Lucene, an open source, Java-based, information retrieval
> library. It is designed to drive powerful document retrieval applications - wherever you need to serve data to users based on their queries, Solr can work for you.

==A full-document search SaaS, using RESTful api==

**version: 4.10.3**

[solr-4.10.3 download](http://archive.apache.org/dist/lucene/solr/)

### Deploy inside Tomcat

1. 安装 Tomcat，解压缩即可。
2. 解压 solr。
3. 把 solr 下的dist目录`solr-4.10.3.war`部署到 Tomcat\webapps下(去掉版本号)。
4. 启动 Tomcat解压缩 war 包
5. 把solr下**example/lib/ext 目录下的所有的 jar 包**，添加到 solr 的工程中(\WEB-INF\lib目录下)。
6. 创建一个 solrhome 。solr 下的/example/solr 目录就是一个 `solrhome`。复制此目录到D盘改名为solrhome  
7. 关联 solr 及 solrhome。需要修改 solr 工程的 web.xml 文件。

```xml
<env-entry>
     <env-entry-name>solr/home</env-entry-name>
     <env-entry-value>d:\solrhome</env-entry-value>
     <env-entry-type>java.lang.String</env-entry-type>
</env-entry>
```

### Problems: multiple  tomcat instance

> change `conf/server.xml` port, and update `${instance}/bin/startup.bat` `CATALINA_HOME`, `CATALINA_BASE`.

## IKAnalyzer

> chinese words tokens semantic analyzer

IKAnalyzer `hot fix version` download: <https://code.google.com/archive/p/ik-analyzer/downloads>

1. add `ik-analyzer-xxx.jar` to `WEB-INF/lib/`
2. add `IKAnalyzer.cfg.xml`, `stopword.dic` to `WEB-INF/classes**/`**
3. **optional**: define yourself stop word and extended word

## use IKAnalyzer in Solr

**${collection-name}/conf/schema.xml**

**copyfield**: `stored=false`

```xml
<!-- use IKAnalyzer in selfdefined type text_ik-->
<fieldType name="text_ik" class="solr.TextField">
    <analyzer class="org.wltea.analyzer.lucene.IKAnalyzer" />
</fieldType>

<!-- configure document field, 设置业务系统 Field-->
<!-- business field -->
<field name="item_goodsid" type="long" indexed="true" stored="true" />
<field name="item_title" type="text_ik" indexed="true" stored="true" />
<field name="item_price" type="double" indexed="true" stored="true" />
<field name="item_image" type="string" indexed="false" stored="true" />
<field name="item_category" type="string" indexed="true" stored="true" />
<field name="item_seller" type="text_ik" indexed="true" stored="true" />
<field name="item_brand" type="string" indexed="true" stored="true" />
<!-- copyfield stored=false -->
<field name="item_keywords" type="text_ik" indexed="true" stored="false" multiValued="true" />
<copyField source="item_title" dest="item_keywords" />
<copyField source="item_category" dest="item_keywords" />
<copyField source="item_seller" dest="item_keywords" />
<copyField source="item_brand" dest="item_keywords" />
<!-- dynamic field -->
<dynamicField name="item_spec_*" type="string" indexed="true" stored="true" />
```
[关于schema.xml中的相关配置的详解](https://www.cnblogs.com/DASOU/p/5907645.html)

1. **name**：属性的名称，这里有个特殊的属性“_version_”是必须添加的。
2. **type**：字段的数据结构类型，所用到的类型需要在fieldType中设置。
3. **default**：默认值。
4. **indexed**：是否创建索引
5. **stored**：是否存储原始数据（如果不需要存储相应字段值，尽量设为false）

# Spring Data for Apache Solr

**xml**

```xml
<!-- solr服务器地址 -->
<solr:solr-server id="solrServer" url="http://127.0.0.1:8080/solr" />


<!-- solr模板，使用solr模板可对索引库进行CRUD的操作 -->
<bean id="solrTemplate" class="org.springframework.data.solr.core.SolrTemplate">
    <constructor-arg ref="solrServer" />
</bean>
```

```java
@Service
class A {
    @Autowired
    private SolrTemplate solrTemplate;
}
```

