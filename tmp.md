# [Vert.x core examples](https://github.com/vert-x3/vertx-examples/tree/master/core-examples)

<!-- TOC -->

- [[Vert.x core examples](https://github.com/vert-x3/vertx-examples/tree/master/core-examples)](#vertx-core-exampleshttpsgithubcomvert-x3vertx-examplestreemastercore-examples)
    - [[Dependencies required](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#dependencies-required)](#dependencies-requiredhttpsgithubcomvert-x3vertx-examplestreemastercore-examplesdependencies-required)
    - [[Embedding](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#embedding)](#embeddinghttpsgithubcomvert-x3vertx-examplestreemastercore-examplesembedding)
    - [HTTP examples [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#http-examples)](#http-examples-httpsgithubcomvert-x3vertx-examplestreemastercore-exampleshttp-examples)
        - [Simple [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#simple)](#simple-httpsgithubcomvert-x3vertx-examplestreemastercore-examplessimple)
        - [Sendfile [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#sendfile)](#sendfile-httpsgithubcomvert-x3vertx-examplestreemastercore-examplessendfile)
        - [Simple form [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#simple-form)](#simple-form-httpsgithubcomvert-x3vertx-examplestreemastercore-examplessimple-form)
        - [Simple form file upload [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#simple-form-file-upload)](#simple-form-file-upload-httpsgithubcomvert-x3vertx-examplestreemastercore-examplessimple-form-file-upload)
        - [Http request body upload [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#http-request-body-upload)](#http-request-body-upload-httpsgithubcomvert-x3vertx-examplestreemastercore-exampleshttp-request-body-upload)
    - [Event bus examples [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#event-bus-examples)](#event-bus-examples-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesevent-bus-examples)
        - [Point to point [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#point-to-point)](#point-to-point-httpsgithubcomvert-x3vertx-examplestreemastercore-examplespoint-to-point)
        - [Publish / Subscribe [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#publish--subscribe)](#publish--subscribe-httpsgithubcomvert-x3vertx-examplestreemastercore-examplespublish--subscribe)
        - [MessageCodec [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#messagecodec)](#messagecodec-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesmessagecodec)
    - [Future [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#future)](#future-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesfuture)
    - [Verticle examples [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#verticle-examples)](#verticle-examples-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesverticle-examples)
        - [Deploy example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#deploy-example)](#deploy-example-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesdeploy-example)
        - [Asynchronous deployment example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#asynchronous-deployment-example)](#asynchronous-deployment-example-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesasynchronous-deployment-example)
        - [Worker Verticle example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#worker-verticle-example)](#worker-verticle-example-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesworker-verticle-example)
    - [Execute blocking example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#execute-blocking-example)](#execute-blocking-example-httpsgithubcomvert-x3vertx-examplestreemastercore-examplesexecute-blocking-example)

<!-- /TOC -->

运行示例代码的两种方式

- 在 IDE 上执行 `main` 方法
- 在终端上执行以下命令

```bash
mvn clean compile
vertx run fully-qualified-name-of-the-example -cp target/classes
```

## [Dependencies required](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#dependencies-required)

Maven 依赖 [`pom.xml`](https://github.com/vert-x3/vertx-examples/blob/master/core-examples/pom.xml)

```xml
<dependency>
  <groupId>io.vertx</groupId>
  <artifactId>vertx-core</artifactId>
  <version>3.5.1</version>
</dependency>
```

## [Embedding](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#embedding)

Java API

- [Interface Vertx](http://vertx.io/docs/apidocs/io/vertx/core/Vertx.html)
- [Interface HttpServer](http://vertx.io/docs/apidocs/io/vertx/core/http/HttpServer.html)
- [Interface Handler<E>](http://vertx.io/docs/apidocs/io/vertx/core/Handler.html)
- [Interface HttpServerRequest](http://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerRequest.html)
- [Interface HttpServerResponse](http://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerResponse.html)
- [Interface ReadStream<T>](http://vertx.io/docs/apidocs/io/vertx/core/streams/ReadStream.html)
- [Interface WriteStream<T>](http://vertx.io/docs/apidocs/io/vertx/core/streams/WriteStream.html)

[Java Code](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/embed)

```java
Vertx.vertx().createHttpServer().requestHandler(req -> req.response().end("Hello World!")).listen(8080);
```

## HTTP examples [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#http-examples)

### Simple [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#simple)

**API**

Java
- [Class AbstractVerticle](https://vertx.io/docs/apidocs/io/vertx/core/AbstractVerticle.html)
- [Interface Verticle](https://vertx.io/docs/apidocs/io/vertx/core/Verticle.html)
- [Interface Future<T>](https://vertx.io/docs/apidocs/io/vertx/core/Future.html)
- [Interface AsyncResult<T>](http://vertx.io/docs/apidocs/io/vertx/core/AsyncResult.html)

**Codes**
- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/http/simple)
- [Kotlin](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/kotlin/io/vertx/example/core/http/simple)

### Sendfile [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#sendfile)

**Codes**
- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/http/sendfile)
- [Kotlin](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/kotlin/io/vertx/example/core/http/sendfile)


### Simple form [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#simple-form)

**API**
- [Interface MultiMap](http://vertx.io/docs/apidocs/io/vertx/core/MultiMap.html)
- [setChunked](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerResponse.html#setChunked-boolean-)
- [setExpectMultipart](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerRequest.html#setExpectMultipart-boolean-)
- [endHandler](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerRequest.html#endHandler-io.vertx.core.Handler-)
- [formAttributes](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerRequest.html#formAttributes--)

**Codes**
- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/http/simpleform)
- [Kotlin](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/kotlin/io/vertx/example/core/http/simpleform)

### Simple form file upload [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#simple-form-file-upload)

**API**
- [Interface HttpServerFileUpload](http://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerFileUpload.html)
- [uploadHandler](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerRequest.html#uploadHandler-io.vertx.core.Handler-)
- [exceptionHandler](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerFileUpload.html#exceptionHandler-io.vertx.core.Handler-)
- [endHandler](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerFileUpload.html#endHandler-io.vertx.core.Handler-)
- [streamToFileSystem](https://vertx.io/docs/apidocs/io/vertx/core/http/HttpServerFileUpload.html#streamToFileSystem-java.lang.String-)

**Codes**
- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/http/simpleformupload)
- [Kotlin](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/kotlin/io/vertx/example/core/http/simpleformupload)

### Http request body upload [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#http-request-body-upload)

**API**

- [Interface FileSystem](http://vertx.io/docs/apidocs/io/vertx/core/file/FileSystem.html)
- [Interface AsyncFile](http://vertx.io/docs/apidocs/io/vertx/core/file/AsyncFile.html)
- [Interface Pump](http://vertx.io/docs/apidocs/io/vertx/core/streams/Pump.html)
- [open](https://vertx.io/docs/apidocs/io/vertx/core/file/FileSystem.html#open-java.lang.String-io.vertx.core.file.OpenOptions-io.vertx.core.Handler-)

**Codes**

- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/http/upload)
- Kotlin 跳过

## Event bus examples [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#event-bus-examples)

### Point to point [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#point-to-point)

**API**

- [Interface EventBus](https://vertx.io/docs/apidocs/io/vertx/core/eventbus/EventBus.html)
- [Interface Message<T>](https://vertx.io/docs/apidocs/io/vertx/core/eventbus/Message.html)
- [Interface MessageConsumer<T>](https://vertx.io/docs/apidocs/io/vertx/core/eventbus/MessageConsumer.html)
- [send](https://vertx.io/docs/apidocs/io/vertx/core/eventbus/EventBus.html#send-java.lang.String-java.lang.Object-io.vertx.core.Handler-)
- [consumer](https://vertx.io/docs/apidocs/io/vertx/core/eventbus/EventBus.html#consumer-java.lang.String-io.vertx.core.Handler-)

**Codes**

- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/eventbus/pointtopoint)
- [Kotlin](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/kotlin/io/vertx/example/core/eventbus/pointtopoint)
```bash
vertx run Receiver.kt -cluster
vertx run Sender.kt -cluster
```

### Publish / Subscribe [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#publish--subscribe)

**API**

- [publish](https://vertx.io/docs/apidocs/io/vertx/core/eventbus/EventBus.html#publish-java.lang.String-java.lang.Object-)

**Codes**

- [Java](https://github.com/vert-x3/vertx-examples/blob/master/core-examples/src/main/java/io/vertx/example/core/eventbus/pubsub)
- [Kotlin](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/kotlin/io/vertx/example/core/eventbus/pubsub)

### MessageCodec [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#messagecodec)

**API**

- [Interface MessageCodec<S,R>](https://vertx.io/docs/apidocs/io/vertx/core/eventbus/MessageCodec.html)

**Codes**

- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/eventbus/messagecodec)

## Future [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#future)

**API**

- [compose](https://vertx.io/docs/apidocs/io/vertx/core/Future.html#compose-java.util.function.Function-)

**Codes**

- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/future)

## Verticle examples [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#verticle-examples)

### Deploy example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#deploy-example)

**API**

- [Class DeploymentOptions](https://vertx.io/docs/apidocs/io/vertx/core/DeploymentOptions.html)

**Codes**

- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/verticle/deploy)
- Kotlin 跳过

### Asynchronous deployment example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#asynchronous-deployment-example)

**API**

- [start](https://vertx.io/docs/apidocs/io/vertx/core/AbstractVerticle.html#start-io.vertx.core.Future-)

**Codes**

- [Java](https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/verticle/asyncstart)
- Kotlin 跳过

学习到这

### Worker Verticle example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#worker-verticle-example)

[setWorker](https://vertx.io/docs/apidocs/io/vertx/core/DeploymentOptions.html#setWorker-boolean-)

https://github.com/vert-x3/vertx-examples/tree/master/core-examples/src/main/java/io/vertx/example/core/verticle/worker

对Event Loop和Worker Pool两个线程要深入了解

## Execute blocking example [>>](https://github.com/vert-x3/vertx-examples/tree/master/core-examples#execute-blocking-example)

[executeBlocking](https://vertx.io/docs/apidocs/io/vertx/core/Vertx.html#executeBlocking-io.vertx.core.Handler-io.vertx.core.Handler-)

[setWorkerPoolName](https://vertx.io/docs/apidocs/io/vertx/core/DeploymentOptions.html#setWorkerPoolName-java.lang.String-)

[setMaxWorkerExecuteTime](https://vertx.io/docs/apidocs/io/vertx/core/DeploymentOptions.html#setMaxWorkerExecuteTime-long-)

[setWorkerPoolSize](https://vertx.io/docs/apidocs/io/vertx/core/DeploymentOptions.html#setWorkerPoolSize-int-)
