<?php
    $query = $_POST['query'];
    
    $mysql = new mysqli('sql4.freemysqlhosting.net', 'sql4103349', 'ugtSzWBZrY', 'sql4103349');
      
    $mysql->query($query);
    
    $error = $mysql->connect_error;
    if (!$error) {
        echo 'Success!';
    } else {
        echo $error;
    }
    echo $error;
?>
