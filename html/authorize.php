<?php

$email = $_POST['email2'];
$password = $_POST['password2'];
$password = md5($password);


$host = 'localhost';
$db   = 'Database';
$user = 'root';
$pass = '1234';

$dsn = "mysql:host=$host;dbname=$db";
$pdo = new PDO($dsn, $user, $pass);
//Вход на сайт с проверкой логин, пароль.
$statement = $pdo->prepare("SELECT * FROM Users WHERE Email = :email2 AND Password = :password2");
$statement->execute(array(
    "email2" => $email,
    "password2" => $password
));

$usersFound = $statement->fetchAll();

if ($usersFound == []){
    print "Login or password fail";
} else {
    print "Successful on site";
}