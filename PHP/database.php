<?php

$mysqli = new mysqli('localhost', 'sp18kim', 'sp18kim', 'ResearchSP18');

if($mysqli ->connect_errno){
    prinf("Connection failed: %s\n", $mysqli ->connect_error);
    exit;
}

?>