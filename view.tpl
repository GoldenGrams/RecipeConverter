<html>
<head>
<title>RecipeConverter</title>
<link rel="stylesheet" href="//code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
<script type="text/javascript">
function showPasted() {
        document.getElementById('fileuploadinput').style.display = "none";
        document.getElementById('urluploadinput').style.display = "none";
        document.getElementById('recipetextinput').style.display = "block";
}
function showFileUpload() {
        document.getElementById('recipetextinput').style.display = "none";
        document.getElementById('urluploadinput').style.display = "none";
        document.getElementById('fileuploadinput').style.display = "block";
}
function showUrlUpload() {
        document.getElementById('fileuploadinput').style.display = "none";
        document.getElementById('recipetextinput').style.display = "none";
        document.getElementById('urluploadinput').style.display = "block";
	document.getElementById('urluploadinput').focus();
	// move cursor to end of field
	document.getElementById('urluploadinput').selectionStart = document.getElementById('urluploadinput').selectionEnd = document.getElementById('urluploadinput').value.length;
}
function showConverted() {
	document.getElementById('originalrecipecontentinner').style.display = "none";
	document.getElementById('convertedrecipecontentinner').style.display = "block";
	document.getElementById('original').style.fontWeight = "normal";
	document.getElementById('converted').style.fontWeight = "bold";
}
function showOriginal() {
        document.getElementById('convertedrecipecontentinner').style.display = "none";
        document.getElementById('originalrecipecontentinner').style.display = "block";
        document.getElementById('converted').style.fontWeight = "normal";
        document.getElementById('original').style.fontWeight = "bold";
}

</script>
<link rel="stylesheet" type="text/css" href="recipestyle.css">
</head>
<body>

<h1>Recipe Converter</h1>
<div id="maincontent">
<form enctype="multipart/form-data" method="POST" action=".">

<div>
	<a style="%originalbuttonstyle%" href="#" id="original" class="button" onclick="javascript:showOriginal();">Original</a>
	<a style="%convertedbuttonstyle%" href="#" id="converted" class="button" onclick="javascript:showConverted();">Converted</a>
</div>

<div id="recipebox">
        <div id="recipecontent">
		<div id="originalrecipecontentinner" style="display:%originalrecipecontentinnerstyledisplay%">
			<textarea id="recipetextinput" name="recipeText">%originalrecipetext%</textarea>
        	</div>
		<div id="convertedrecipecontentinner" style="display:%convertedrecipecontentinnerstyledisplay%">
			<pre>%convertedrecipetext%</pre>
		</div>
	</div>
</div>

<div id="controlsbox">
<div class="container">
<p>System</p>
<input type="radio" name="system" value="imperial" id="imperial" %imperialchecked%>
<label for="imperial">Imperial</label>
<input type="radio" name="system" value="metric" id="metric" %metricchecked%>
<label for="metric">Metric</label>
</div>


<div class="container">
<p>Recipe Text</p>
<input type="radio" name="uploadtype" id="pasted" value="pasted" checked onclick="javascript:showPasted();">
<label for="pasted">Pasted</label>
<input type="radio" name="uploadtype" id="fileupload" value="fileupload" onclick="javascript:showFileUpload();">
<label for="fileupload">File Upload</label>
<input type="radio" name="uploadtype" id="url" value="url" onclick="javascript:showUrlUpload();">
<label for="url">Url</label>
<input type="file" name="fileuploadinput" id="fileuploadinput" style="display:none;">
<input type="text" name="urluploadinput" id="urluploadinput" style="display:none;" value="http://">
</div>
<div class="container">
<label for="scaling">Scaling</label>

<input id="scaling" type="text" name="scaling" value="%scaling%">
<div class="container"><div id="defaultslide"></div></div>

<script type="text/javascript">
$(function(){
  $('#defaultslide').slider({ 
    max: 10,
    min: .125,
    value: %scaling%,
    step: .125,
    slide: function(e,ui) {
      document.forms[0].scaling.value = ui.value;
    }
  });
});
</script>

<br>
<input type="submit" name="submit" value="submit">
<p class="errortext">%errortext%</p>
</div><!-- end controlsbox-->
</form>
</div><!-- end maincontent-->
</body>
</html>
