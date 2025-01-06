<?php
  include '../db.php';
  $id = $_GET['id'];
  $sql = "delete from list where id=$id";
  $conn->query($sql);
  $conn->close();
  header("location: index.php");
?>
