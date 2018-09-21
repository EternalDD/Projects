<?php

$email = $_POST['email'];
$password = $_POST['password'];
$password = md5($password);


$host = 'localhost';
$db   = 'Database';
$user = 'user';
$pass = 'pass';

$dsn = "mysql:host=$host;dbname=$db";
$pdo = new PDO($dsn, $user, $pass);

//Создание пользователя с проверкой на логин.
$statement = $pdo->prepare("SELECT*  FROM Users WHERE Email = :email");
$statement->execute(array(
    "email" => $email
));

$usersFound = $statement->fetchAll();

if ($usersFound == []){
    $statement = $pdo->prepare("INSERT INTO Users (Email, Password)
        VALUES(:email, :password)");
    $statement->execute(array(
        "email" => $email,
        "password" => $password
    ));
    print "Successful";
} else {
    print "Login taken";
}

