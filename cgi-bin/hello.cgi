#!/usr/bin/perl
use CGI':standard';
use strict;
print "Content-type: text/html\n\n";

print <<"EOF";
<html>

<head>
<link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>
<title>Hello, World!</title>
</head>
<style>
h1 {
	font-family: 'Sofia';
	font-size: 100px;
	text-align: center;
	color: #317e0d;
}
</style>
<body>
<h1>Hello, World!<h1>
</body>

</HTML>
EOF

