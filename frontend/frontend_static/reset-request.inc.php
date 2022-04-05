<?php

if (isset($_POST["send recovery link"])){
    $selector = bin2hex(random_bytes(8));
    $token = random_bytes(32);

    $url=


}else{
    header("location: ../forgot.html")
}