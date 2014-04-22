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
}
</script>
<link rel="stylesheet" type="text/css" href="recipestyle.css">
</head>
<body>

<h1>Recipe Converter</h1>
<div id="maincontent">
<div id="recipebox">
        <div id="recipecontent"><div id="recipecontentinner"><pre>
%recipetext%
        </pre></div></div>
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
<p>Recipe Text</p>
<input type="radio" name="uploadtype" id="pasted" value="pasted" checked onclick="javascript:showPasted();">
<label for="pasted">Pasted</label>
<input type="radio" name="uploadtype" id="fileupload" value="fileupload" onclick="javascript:showFileUpload();">
<label for="fileupload">File Upload</label>
<input type="radio" name="uploadtype" id="url" value="url" onclick="javascript:showUrlUpload();">
<label for="url">Url</label>
<textarea id="recipetextinput" name="recipeText">%recipetext%</textarea>
<input type="file" name="fileuploadinput" id="fileuploadinput" style="display:none;">
<input type="text" name="urluploadinput" id="urluploadinput" style="display:none;">
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
</form>
<p class="errortext">%errortext%</p>
</div><!-- end controlsbox-->
</div><!-- end maincontent-->
</body>
</html>
