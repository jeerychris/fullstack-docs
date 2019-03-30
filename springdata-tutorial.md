# Spring Data

<https://spring.io/projects/spring-data>

> Spring Data’s mission is to **provide a familiar and consistent, Spring-based programming model** for **data access** while still **retaining the special traits of the underlying data store**.
>
> It makes it easy to use data access technologies, **relational and non-relational databases, map-reduce frameworks, and cloud-based data services**. This is an umbrella project which contains many subprojects that are specific to a given database. The projects are developed by working together with many of the companies and developers that are behind these exciting technologies.

## Features

- Powerful repository and custom object-mapping abstractions
- Dynamic query derivation from repository method names
- Implementation domain base classes providing basic properties
- Support for transparent auditing (created, last changed)
- Possibility to integrate custom repository code
- **Easy Spring integration via JavaConfig and custom XML namespaces**
- Advanced integration with Spring MVC controllers
- Experimental support for **cross-store persistence**

# Main modules

Spring Data Commons - Core Spring concepts underpinning every Spring Data module.

Spring Data JDBC - Spring Data repository support for JDBC.

Spring Data JDBC Ext - Support for database specific extensions to standard JDBC including support for Oracle RAC fast connection failover, AQ JMS support and support for using advanced data types.

**Spring Data JPA** - Spring Data repository support for JPA.

Spring Data MongoDB - Spring based, object-document support and repositories for MongoDB.

**Spring Data Redis** - Easy configuration and access to Redis from Spring applications.

Spring Data REST - Exports Spring Data repositories as hypermedia-driven RESTful resources.

**Spring Data for Apache Solr** - Easy configuration and access to Apache Solr for your search oriented Spring applications.

## Community modules

**Spring Data Elasticsearch** - Spring Data module for Elasticsearch.