<?php
require_once 'inc/pages.php';
require_once 'inc/functions/routing.php'

$route = ""
$data = ""

foreach($pages as $key => $value) {
  if(getPageName(0) == $key) {
    $route = $value
    $data = data[$value]
  }
}
echo system("python -m lavla/__init__.py " . $route . " " . data);
?>
