<?php
    $host='162.0.214.53';
    $username='nationenview';
    $password='sNwsmquxPB4sYQfj25jnZDKn5tyF7aA3HAiqvBu45gANfWiJm48mpMexJPerF7xAF5yJw9';
    $dbname = "nationen";
    $conn=mysqli_connect($host,$username,$password,"$dbname");
    if(!$conn)
        {
          die('Could not Connect MySql Server:' .mysql_error());
        }
?>
