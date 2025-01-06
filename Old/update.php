<?php
  include '../db.php';
  $id = $_POST['id'];
  $name = $_POST['name'];
  $age = $_POST['age'];
  $sql = "update list set name='$name', age='$age' where id=$id";
  $result = $conn->query($sql);
  $conn->close();
  header("location: index.php");
?>
