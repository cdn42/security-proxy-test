### **Security Proxy Test**

This is small Flask app for serving files used for testing a blocking policy on a web proxy.


It was also an exercise in creating different file types programmatically using python, providing a simple library for these functions.

The app can be brought up in docker as follows:

$ git clone https://github.com/cdn42/security-proxy-test.git

$ cd security-proxy-test

$ docker build --tag cdn42/sec-proxy-test .

$ docker run -d -p 9000:9000 --name security-proxy-test cdn42/security-proxy-test:latest


To generate a set of files:

$ curl http://localhost:9000/generate

You can then point a browser at http://localhost:9000

The concept for this app is as follows, however:

Client ---> Web Proxy Filter ---> SecurityProxyTestApp

It is recommended to place the app behind a reverse proxy, as Flask is not a production Internet facing web server.





