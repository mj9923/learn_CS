<?php

$start = "http://localhost/se/test.html";


function follow_links($url){

  $doc = new DOMDocument();
  $doc->loadHTML(file_get_contents($url));

  
}

follow_links($start);
 ?>
