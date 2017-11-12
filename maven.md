# Maven Practice

https://maven.apache.org/

http://search.maven.org/

https://mvnrepository.com/

## Examples

### [archetype:generate](https://maven.apache.org/archetype/maven-archetype-plugin/generate-mojo.html)
```bash
mvn archetype:generate
```

Filtering to reduce archetype list
```
# With a mojo parameter:
mvn archetype:generate -Dfilter=org.apache:struts

# Through the prompt:
mvn archetype:generate
Choose a number or apply filter (format: [groupId:]artifactId, case sensitive contains): org.apache:struts
```

Generate project in batch mode
```bash
mvn archetype:generate -B \
-DarchetypeGroupId=org.apache.maven.archetypes \
-DarchetypeArtifactId=maven-archetype-quickstart \
-DarchetypeVersion=1.1 \
-DgroupId=com.company \
-DartifactId=project \
-Dversion=1.0-SNAPSHOT \
-Dpackage=com.company.project
```

创建 Web 项目（注意：包名不能用中划线 `- `，会出现编译错误，可以用下划线 `_`。）
```bash
mvn archetype:generate -B \
-DarchetypeGroupId=org.apache.maven.archetypes \
-DarchetypeArtifactId=maven-archetype-webapp \
-DgroupId=com.mycompany.app \
-DartifactId=my-webapp \
-Dversion=1.0-SNAPSHOT \
-Dpackage=com.mycompany.app.mywebapp
```

### Dependencies
```xml
<dependencies>
    <dependency>
        <groupId>javax.servlet</groupId>
        <artifactId>javax.servlet-api</artifactId>
        <version>3.1.0</version>
        <scope>provided</scope>
    </dependency>
    <dependency>
        <groupId>javax.servlet.jsp</groupId>
        <artifactId>javax.servlet.jsp-api</artifactId>
        <version>2.3.1</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```


## References

- [Core Plug-ins List](https://maven.apache.org/plugins/index.html)
- [Maven Quick Reference Card](https://maven.apache.org/guides/MavenQuickReferenceCard.pdf)

### [Core Plug-ins List](https://maven.apache.org/plugins/index.html)

- #### [archetype](http://maven.apache.org/archetype/maven-archetype-plugin/)

  [archetype:generate](https://maven.apache.org/archetype/maven-archetype-plugin/generate-mojo.html)




## [Download](https://maven.apache.org/download.html)

[Maven Releases History](https://maven.apache.org/docs/history.html)

## Install

- ### [Binary](https://maven.apache.org/install.html)

[install-maven-bin.sh](https://github.com/mrhuangyuhui/maven/blob/master/install-maven-bin.sh)
```bash
sudo curl -L https://github.com/mrhuangyuhui/maven/raw/master/install-maven-bin.sh | sh
```

- ### [SDKMAN](https://github.com/mrhuangyuhui/sdkman)
```bash
sdk list maven
sdk install maven 3.5.0
```

- ### Package Manager

```bash
## APT ##
sudo apt update
apt show maven
sudo apt install maven -y
```

```bash
## YUM ##
yum info maven
sudo yum install maven -y
```

## [Documentation](https://maven.apache.org/guides/)

### Getting Started with Maven

#### [Getting Started in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)

https://preview.c9users.io/mrhuangyuhui/maven_practice/sample-quick-start

```bash
mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

cd my-app

mvn package

java -cp target/my-app-1.0-SNAPSHOT.jar com.mycompany.app.App
```

#### [Getting Started in 30 Minutes](https://maven.apache.org/guides/getting-started/index.html)

##### [How do I setup Maven?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_setup_Maven)

[Guide to Configuring Maven](https://maven.apache.org/guides/mini/guide-configuring-maven.html)

##### [How do I make my first Maven project?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_make_my_first_Maven_project)

https://preview.c9users.io/mrhuangyuhui/maven_practice/sample-first-project

```bash
mvn -B archetype:generate \
  -DarchetypeGroupId=org.apache.maven.archetypes \
  -DgroupId=com.mycompany.app \
  -DartifactId=my-app
```

[Introduction to Archetypes](https://maven.apache.org/guides/introduction/introduction-to-archetypes.html) \
[Introduction to the POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html) \
[POM Reference](https://maven.apache.org/ref/current/maven-model/maven.html) \
[Introduction to the Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)

##### [How do I compile my application sources?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_compile_my_application_sources)

```bash
mvn compile
```

##### [How do I compile my test sources and run my unit tests?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_compile_my_test_sources_and_run_my_unit_tests)

```bash
mvn test
```

If you simply want to compile your test sources (but not execute the tests), you can execute the following:
```bash
mvn test-compile
```

##### [How do I create a JAR and install it in my local repository?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_create_a_JAR_and_install_it_in_my_local_repository)

```bash
mvn package

mvn install
```

[Introduction to Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html)

##### [How do I use plugins?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_use_plugins)

```xml
...
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>3.3</version>
      <configuration>
        <source>1.5</source>
        <target>1.5</target>
      </configuration>
    </plugin>
  </plugins>
</build>
...
```

[Plugins List](https://maven.apache.org/plugins/) \
[Guide to Configuring Plugins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)

##### [How do I add resources to my JAR?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_add_resources_to_my_JAR)

You see below in our example we have added the directory `${basedir}/src/main/resources` into which we place any resources we wish to package in our JAR. The simple rule employed by Maven is this: any directories or files placed within the `${basedir}/src/main/resources` directory are packaged in your JAR with the exact same structure starting at the base of the JAR.

https://preview.c9users.io/mrhuangyuhui/maven_practice/sample-add-resources

```bash
my-app
|-- pom.xml
`-- src
    |-- main
    |   |-- java
    |   |   `-- com
    |   |       `-- mycompany
    |   |           `-- app
    |   |               `-- App.java
    |   `-- resources
    |       `-- META-INF
    |           `-- application.properties
    `-- test
        `-- java
            `-- com
                `-- mycompany
                    `-- app
                        `-- AppTest.java
```

So you can see in our example that we have a `META-INF` directory with an `application.properties` file within that directory. If you unpacked the JAR that Maven created for you and took a look at it you would see the following:
```bash
|-- META-INF
|   |-- MANIFEST.MF
|   |-- application.properties
|   `-- maven
|       `-- com.mycompany.app
|           `-- my-app
|               |-- pom.properties
|               `-- pom.xml
`-- com
    `-- mycompany
        `-- app
            `-- App.class
```

##### [How do I filter resource files?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_filter_resource_files)

- **Reference a property defined in `pom.xml`, the property name uses the names of the XML elements that define the value.**

https://preview.c9users.io/mrhuangyuhui/maven_practice/sample-filter-resources-1

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>
 
  <name>Maven Quick Start Archetype</name>
  <url>http://maven.apache.org</url>
 
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
 
  <build>
    <resources>
      <resource>
        <directory>src/main/resources</directory>
        <filtering>true</filtering>
      </resource>
    </resources>
  </build>
</project>
```

```
# application.properties
application.name=${project.name}
application.version=${project.version}
```

```bash
mvn process-resources
```

- **Reference a property defined in an external file**

https://preview.c9users.io/mrhuangyuhui/maven_practice/sample-filter-resources-2

```
# filter.properties
my.filter.value=hello!
```

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>
 
  <name>Maven Quick Start Archetype</name>
  <url>http://maven.apache.org</url>
 
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
 
  <build>
    <filters>
      <filter>src/main/filters/filter.properties</filter>
    </filters>
    <resources>
      <resource>
        <directory>src/main/resources</directory>
        <filtering>true</filtering>
      </resource>
    </resources>
  </build>
</project>
```

```
# application.properties
application.name=${project.name}
application.version=${project.version}
message=${my.filter.value}
```

- **Reference a property defined in the `properties` section of `pom.xml`**

https://preview.c9users.io/mrhuangyuhui/maven_practice/sample-filter-resources-3

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>
 
  <name>Maven Quick Start Archetype</name>
  <url>http://maven.apache.org</url>
 
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
 
  <build>
    <resources>
      <resource>
        <directory>src/main/resources</directory>
        <filtering>true</filtering>
      </resource>
    </resources>
  </build>
 
  <properties>
    <my.filter.value>hello</my.filter.value>
  </properties>
</project>
```

- **Reference a property defined in the system properties**

https://preview.c9users.io/mrhuangyuhui/maven_practice/sample-filter-resources-4

```
# application.properties
java.version=${java.version}
command.line.prop=${command.line.prop}
```

```bash
mvn process-resources "-Dcommand.line.prop=hello again"
```

##### [How do I use external dependencies?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_use_external_dependencies)

`workspace/sample-external-dependencies`

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>
 
  <name>Maven Quick Start Archetype</name>
  <url>http://maven.apache.org</url>
 
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>log4j</groupId>
      <artifactId>log4j</artifactId>
      <version>1.2.12</version>
      <scope>compile</scope>
    </dependency>
  </dependencies>
</project>
```

```bash
mvn compile
```

[Introduction to Dependency Mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html) \
[Project Descriptor Reference](https://maven.apache.org/ref/current/maven-model/maven.html) \
[Introduction to Repositories](https://maven.apache.org/guides/introduction/introduction-to-repositories.html) \
http://repo.maven.apache.org/maven2/

##### [How do I build other types of projects?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_build_other_types_of_projects)



```bash
mvn archetype:generate \
    -DarchetypeGroupId=org.apache.maven.archetypes \
    -DarchetypeArtifactId=maven-archetype-webapp \
    -DgroupId=com.mycompany.app \
    -DartifactId=my-webapp
```

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>my-webapp</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>war</packaging>
 
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
 
  <build>
    <finalName>my-webapp</finalName>
  </build>
</project>
```

```bash
mvn clean package
```

##### [How do I build more than one project at once?](https://maven.apache.org/guides/getting-started/index.html#How_do_I_build_more_than_one_project_at_once)

`workspace/sample-multi-project` \
`workspace/sample-multi-project-idea`

```
+- pom.xml
+- my-app
| +- pom.xml
| +- src
|   +- main
|     +- java
+- my-webapp
| +- pom.xml
| +- src
|   +- main
|     +- webapp
```

`app/pom.xml`
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>com.mycompany.app</groupId>
  <artifactId>app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>pom</packaging>
 
  <modules>
    <module>my-app</module>
    <module>my-webapp</module>
  </modules>
</project>
```

`my-webapp/pom.xml`
```xml
  ...
  <dependencies>
    <dependency>
      <groupId>com.mycompany.app</groupId>
      <artifactId>my-app</artifactId>
      <version>1.0-SNAPSHOT</version>
    </dependency>
    ...
  </dependencies>
```

`my-app/pom.xml` \
`my-webapp/pom.xml`
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <parent>
    <groupId>com.mycompany.app</groupId>
    <artifactId>app</artifactId>
    <version>1.0-SNAPSHOT</version>
  </parent>
  ...
```

```bash
mvn clean install
```

```bash
mvn idea:idea
```

### Introductions

#### [The Build Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)

- [Lifecycle Reference](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Lifecycle_Reference)
- [Built-in Lifecycle Bindings](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Built-in_Lifecycle_Bindings)
- [Maven Plugins](http://maven.apache.org/plugins/index.html)
- [org/apache/maven/plugins](https://repo.maven.apache.org/maven2/org/apache/maven/plugins/)




























## MISC


```
mvn -v
```
