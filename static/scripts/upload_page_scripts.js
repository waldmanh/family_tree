function changeScriptDescription() {
  var scriptToRun = document.getElementById("script-select").value;
  switch (scriptToRun) {
    case "noscript":
      document.getElementById(
        "script-selected-description"
      ).innerHTML = "<h2>No script was selected ...</h2>";
      break;
    case "script1":
      document.getElementById(
        "script-selected-description"
      ).innerHTML = load_script1();
      break;
    case "script2":
      document.getElementById("script-selected-description").innerHTML =
        "script2 was chosen";
      break;
    case "script3":
      document.getElementById("script-selected-description").innerHTML =
        "script3 was chosen";
      break;
  }
}
function runScript() {
  var select = document.getElementById("script-select");
  var scripToRun = select.options[select.selectedIndex].value;
  document.runscriptform.action =
    "http://localhost:5000/uploader?scriptToRun=" + scripToRun;
  runscriptform.submit();
}
