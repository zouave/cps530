<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-type"
	content="text/html; charset=utf-8" />
<title>Generates Multiplcation Tablle 3x3-12x12</title>
<style>
body {
	background-color: #bdb76b;
	align: center;
}

table, td, tr{
      border:2px solid black;
      color:#000000;
}

</style>
</head>

<body>

<?php
	session_start();
	if(isset($_SESSION['views']))
		$_SESSION['views'] = $_SESSION['views'] + 1;
	else
		$_SESSION['views'] = 1;
	echo "Page view(s) = ". $_SESSION['views']."<br>";
	
	$table = $_POST['table'];
	
	echo "Table value: ".$table."X".$table."<br>";
	echo "<table>";

        for ($row =1; $row <= $table; $row++){
            echo'<tr>';
            for ($col = 1; $col <= $table; $col++)
                echo '<td>'.$row*$col.'</td>';
           echo '</tr>'; // close tr tag here

        }

	echo "</table>";
?>

</body>
</html>
