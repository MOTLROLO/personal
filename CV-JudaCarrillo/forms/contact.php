<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
}

if(isset($_POST['submit'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];
    
    $to = "judacarrillot@gmail.com";
    $headers = "From: ".$email;
    $txt = "Has recibido un mensaje de ".$name.".\n\n".$message;
    
    mail($to, $subject, $txt, $headers);
    echo "¡Tu mensaje ha sido enviado con éxito!";
}
?>
