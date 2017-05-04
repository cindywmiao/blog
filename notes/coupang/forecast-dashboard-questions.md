Q: Port 如果已经在备用?

=> lsof -i tcp:1099

Q: Project setting in Intellij?

=> Server VM options: -Dfile.encoding=UTF-8 -Xmx1024m -XX:PermSize=512m -XX:MaxPermSize=512m -Dspring.profiles.active=develop
=> Deployment: add artifact... scm-planning-inerfaces.war(explored)

Q: auto build?

=> Preferences -> Build, Execution, Deployment -> Complier -> Annotation Processors -> Enable annotation processing(checked)

Q: Postgre connection

```
 	<entry key="postGre.class.name">org.postgresql.Driver</entry>
    <entry key="postGre.url">jdbc:postgresql://10.213.161.20:5432/forecastdb</entry>
    <entry key="postGre.username">forecast</entry>
    <entry key="postGre.password">Aa111111</entry>
    <entry key="postGre.initialize.size">1</entry>
    <entry key="postGre.max.total">5</entry>
    <entry key="postGre.max.idle">2</entry>
```

Q: Mysql connection
10.213.161.25 3306 (RDS Aurora) 