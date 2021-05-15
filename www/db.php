<?php
    $host='IP';
    $username='user';
    $password='pass';
    $dbname = "db";
    $conn=mysqli_connect($host,$username,$password,"$dbname");
    if(!$conn)
        {
          die('Could not Connect MySql Server:' .mysql_error());
        }
?>
