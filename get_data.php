<!DOCTYPE html>
<?php
    $db_url = $_ENV['CLEARDB_DATABASE_URL'];
    $db_server = substr($db_url, strpos($db_url, "@") + 1, strpos($db_url, "/h") - strpos($db_url, "@") - 1);
    $db_username = substr($db_url, strpos($db_url, "//") + 2, strpos($db_url, ":1") - strpos($db_url, "//") - 2);
    $db_password = substr($db_url, strpos($db_url, ":1") + 1, strpos($db_url, "@") - strpos($db_url, ":1") - 1);
    $db_database = substr($db_url, strpos($db_url, "/h") + 1, strpos($db_url, "?") - strpos($db_url, "/h") - 1);
    
    $key = $_GET['name'];
    
    $mysql = new mysqli($db_server, $db_username, $db_password, $db_database);
    
    $query = "SELECT * FROM botwyniel_data WHERE name = '" . $key . "');";
    echo $query . "<br>";
    $r = $mysql->query($query);
    while($row = $r->fetch_assoc()) {
    echo $row['val'];
    }
    echo $mysql->error;
    $mysql->close();
?>