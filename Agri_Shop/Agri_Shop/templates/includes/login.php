<?php 



	include("connection.php");
	include("functions.php");

	if (isset($_POST["submit"])) {
 
		$host = "localhost";
		$name = "lname";
		$email ="email";
		$pwd = "password";
		$prenume = "fname";
		
		require_once 'connection.php';
		require_once 'functions.php';
		header("location: ../index.php");
	}


