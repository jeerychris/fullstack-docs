# Lucene

[lucene原理及java实现](<https://blog.csdn.net/liuhaiabc/article/details/52346493>)

> Lucene 是一个高效的，基于Java 的全文检索库。Both Solr and ElasticSearch is developed from it.

## 结构化数据 和非结构化数据

- 结构化数据： 指具有固定格式或有限长度的数据，如数据库，元数据等。
- 非结构化数据： 指不定长或无固定格式的数据，如邮件，word文档等。

按照数据的分类，搜索也分为两种：

- 对结构化数据的搜索 ：如对数据库的搜索，用SQL语句。再如对元数据的搜索，如利用windows搜索对文件名，类型，修改时间进行搜索等。
- 对非结构化数据的搜索 ：如利用windows的搜索也可以搜索文件内容，Linux下的grep命令，再如用Google和百度可以搜索大量内容数据。

对非结构化数据也即对全文数据的搜索主要有两种方法：

**顺序扫描法 (Serial Scanning)**

**全文检索(Full-text Search)**

全文检索的基本思路，也即将非结构化数据中的一部分信息提取出来，重新组织，使其变得有一定结构，然后对此有一定结构的数据进行搜索，从而达到搜索相对较快的目的。

这部分从非结构化数据中提取出的然后重新组织的信息，我们称之**索引** 。 这种先建立索引，再对索引进行搜索的过程就叫全文检索(Full-text Search) 。

![lucene-in-action.png](images/lucene-in-action.png)

## 全文检索

大体分两个过程，索引创建 (Indexing) 和搜索索引 (Search) 。

**索引创建**：将现实世界中所有的结构化和非结构化数据提取信息，创建索引的过程。
**搜索索引**：就是得到用户的查询请求，搜索创建的索引，然后返回结果的过程。
于是全文检索就存在三个重要问题：

1. 索引里面究竟存些什么？(Index)

2. 如何创建索引？(Indexing)

3. 如何对索引进行搜索？(Search)

### [倒排索引](https://www.cnblogs.com/zlslch/p/6440114.html)

### Tokens Analyzer

### [保持数据库与索引库的同步](https://www.cnblogs.com/sharpest/p/5991640.html)

> 对数据库进行增、删、改操作的同时对索引库也进行相应的操作

# Solr

# ElasticSearch