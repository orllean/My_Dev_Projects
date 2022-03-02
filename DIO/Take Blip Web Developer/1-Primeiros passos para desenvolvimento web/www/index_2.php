<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Site em PHP v2.0</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
    <style>
        .linha {
            font-weight: bold;
            padding-left: 10px;
            line-height: 30px;
            color: red;
        }
    </style>
</head>

<body>
    <?php
    for ($i = 1; $i <= 15; $i++) {
        print("<span class=\"linha\">Linha número " . $i . "</span><br />");
    }
    ?>
</body>
<script>
    $(document).ready(function() {
        alert("Wohoooooo!");
    });
</script>

</html>