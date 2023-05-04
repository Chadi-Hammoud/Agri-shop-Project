<?php

$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
$dbname = "agric";

if(!$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname))
{

	die("failed to connect!");
}
