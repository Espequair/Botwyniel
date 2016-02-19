<?php
    $mysql = new mysqli('sql4.freemysqlhosting.net', 'sql4103349', 'ugtSzWBZrY', 'sql4103349');
    $query = "SELECT * FROM whitelist";

    $r = $mysql->query($query);

    echo "{";
    for ($a = 0; $a <= $r->num_rows - 2; $a++) {
        $user = $r->fetch_assoc();
        echo '"' . $user['id'] . '":"' . $user['username'] . '",';
    }
    $user = $r->fetch_assoc();
    echo '"' . $user['id'] . '":"' . $user['username'] . '"';
    echo "}";
?>
