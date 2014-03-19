<!DOCTYPE html>

<head>
	<title>Public Market</title>
	<link rel="stylesheet" href="styles/main.css" type="text/css" media="screen" />
	<link rel='stylesheet' media='screen and (max-device-width: 480px)' href='styles/mobile.css' type='text/css' />
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0"/>
	<script src="http://d3lp1msu2r81bx.cloudfront.net/kjs/js/lib/kinetic-v5.0.1.min.js"></script>
	<?php
		//Globals for whole site
		$URL = '66.66.103.33';
	
		// Connecting, selecting database
		$link = mysql_connect($URL , 'webuser', '')
			or die('Could not connect: ' . mysql_error());
		echo 'Connected successfully';
		mysql_select_db('pubmark') or die('Could not select database');
	?>
</head>

<body>
	<div id="container">
		<div id="content1">
			<header id="titleBlock">
				<h1>Public Market</h1>
				<h2 class="notMobile">"The Freshest Place in Rochester"</h2>
			</header>
			<div id="statusBlock">
				<h3><?php
						if ( intval(date('N')) == 6 && intval(date('H')) < 15 && intval(date('H')) > 8) {
							echo "The Public Market is Open";
						} else {
							echo "The Public Market is Closed";
						}
				  
				    ?></h3>
			</div>
			<div id="shoutBlock" class="notMobile">
				<div class="shout" id="shout1">
					<img src=""/>
					<p>"This is my message!"</p>
					<span class="shout-author">Mary's Farm</span>
					<span class="shout-time">1:10p<span>
				</div>
				<div class="shout" id="shout2">
					<img src=""/>
					<p>"I hate when it rains... :("</p>
					<span class="shout-author">Paul's Flowers</span>
					<span class="shout-time">2:41p<span>
				</div>
				<div class="shout" id="shout3">
					<img src=""/>
					<p>"I cut my finger off.  5.99/lb"</p>
					<span class="shout-author">Albert's Butcher Shop</span>
					<span class="shout-time">3:12p<span>
				</div>
				<div class="shout" id="shout4">
					<img src=""/>
					<p>"Mary's Farm is awesome! #hotfarmers"</p>
					<span class="shout-author">Paul's Flowers</span>
					<span class="shout-time">3:28p<span>
				</div>
				<div class="shout" id="shout5">
					<img src=""/>
					<p>"You'll super like our tomatos!"</p>
					<span class="shout-author">Mary's Farm</span>
					<span class="shout-time">3:43p<span>
				</div>
				<div class="shout" id="shout6">
					<img src=""/>
					<p>"pork pork pork pork pork"</p>
					<span class="shout-author">Albert's Butcher Shop</span>
					<span class="shout-time">4:02p<span>
				</div>
			</div>
		</div>
		<div id="content2">
			<script type="text/javascript" src="market.php" defer="defer"></script>
		</div>
		<footer class="notMobile">
		Public Market App | 2014
		<?php

		// Performing SQL query
		$lastSat->modify('this week');
		$lastSat->modify('this week +6 days');
		$query = 'SELECT ID, LastCheckIn FROM vendors\nWHERE LastCheckIn > ' . $lastSat;
		$result = mysql_query($query) or die('Query failed: ' . mysql_error());

		?>
		</footer>
	</div>
</body>
