<html>
<head>
<title>RecipeConverter</title>
<link rel="stylesheet" type="text/css" href="recipestyle.css">
</head>
<body>

<h1>RecipeConverter</h1>
<div id="maincontent">
<div id="recipebox">
        <div id="recipecontent">
		<html>
			<body>
			<p>System: %measurementsystem%</p>
			<p>RecipeText: %recipetext%</p>
			</body>
		</html>
        </div>
</div>

<div id="controlsbox">
<div class="container">
<p>System</p>
<form method="POST" action=".">
<input type="radio" name="system" value="imperial" id="imperial" %imperialchecked%>
<label for="imperial">Imperial</label>
<input type="radio" name="system" value="metric" id="metric" %metricchecked%>
<label for="metric">Metric</label>
</div>


<div class="container">
<p>RecipeText</p>
<textarea id="recipetextinput" name="recipeText">%recipetext%</textarea>
</div>
<div class="container">
<label for="scaling">Scaling</label>
<input id="scaling" type="text" name="scaling" value="%scaling%">
</div>

<br>
<input type = "submit">
</form>
</div><!-- end controlsbox-->
</div><!-- end maincontent-->
</body>
</html>
