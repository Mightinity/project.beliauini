<?php
session_start();

// check if user has submitted the login form
if(isset($_POST['password'])) {
    $password = $_POST['password'];

    if($password === 'fm_beliauini@31') {
        $_SESSION['_fm_allowed'] = true;
        header('Location: filemanager.php');
        exit();
    } else {
        $errorMessage = 'Invalid credentials';
    }
}

if(isset($_SESSION['_fm_allowed']) && $_SESSION['_fm_allowed'] === true) {
    header('Location: notes.php');
    exit();
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <link rel="stylesheet" href="assets/style_log.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">    
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <link rel="icon" type="image/png" href="favicon-16x16.png">
</head>
<body>
    <main>
        <div class="container">
            <h2>Login</h2>
            <?php if(isset($errorMessage)): ?>
                <p style="color: red;"><?php echo $errorMessage; ?></p>
            <?php endif; ?>
            <form method="post" action="login.php">
                <label for="password">Password:</label> 
                <input type="password" id="password" name="password"><br><br>
                <button type="submit">Login</button>
            </form>
        </div>
    </main>
    <footer>
        <p style="text-align: center;">&copy; 2023 PT Beliauini Makmur Sentosa</p>
    </footer>
</body>
</html>
