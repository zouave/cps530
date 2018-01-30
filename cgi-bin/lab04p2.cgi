#!/usr/bin/perl

use CGI ':standard';
print "Content-Type: text/html \n\n";
@firstname = param('firstname');
@lastname = param('lastname');
@gender = param('gender');
@novel = param('novel');
@review = param('message');

print <<"EOF";
<html>
<head>
<link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>
<title>Modified Input</title>
</head>

<style>
body.pink {
	background-color: #ffc0cb;
}

h1.name {
	margin-top: 5px;
	margin-bottom: 5px;
	font-family: 'Sofia';
    font-size: 50px;
    text-align: center;
    color: #b8860b;
}

h1.gender {
	font-family: 'Sofia';
    font-size: 33px;
    text-align: center;
    color: #b8860b;
}

h1.novel {
	margin-top: 5px;
	margin-bottom: 5px;
	font-family: 'Sofia';
    font-size: 33px;
    text-align: center;
	color: #32cd32;
}

h1.review {
	margin-top: 5px;
	margin-bottom: 5px;
	font-family: 'Sofia';
    font-size: 33px;
    text-align: center;
    color: #ff0000;
}

hr.style {
	margin-top: 5px;
	margin-bottom: 5px;
	border-top: 1px solid #8c8b8b;
	border-bottom: 1px solid #fff;
}

img {
    display: block;
    margin: 0 auto;
}

</style>

<body class="pink">
<h1 class="name">Name: @firstname @lastname</h1><br>
<h1 class="gender">Gender: @gender<h1><br>
<hr class="style">
<br>
<h1 class="novel">Your favourite novel:</h1><br>
<img src="@novel" alt"Favourite Novel">
<br>
<hr class="style">
<br>
<br>
<h1 class="review">Review: <br>@review.<br></h1>

</body>

</html>
EOF
