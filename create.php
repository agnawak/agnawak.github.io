<?php
  include '../db.php';
  $name = $_POST["name"];
  $age = $_POST["age"];
  $sql = "insert into list(name, age) values ('$name', '$age')";
  $conn->query($sql);
  $conn->close();
  header("location: index.php");
?>
