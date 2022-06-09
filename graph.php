<?php
  include '../db.php';
  $sql = "select * from list";
  $result = $conn->query($sql);
  
  $data = array();
foreach ($result as $row) {
	$data[] = $row;
}

echo json_encode($data);
$conn->close();
?>
