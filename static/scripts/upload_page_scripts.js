function changeScriptDescription() {
  var scriptToRun = document.getElementById("script-select").value;
  switch (scriptToRun) {
    case "noscript":
      document.getElementById("script-selected-description").innerHTML =
        "<h2>No script was selected ...</h2>";
      break;
    case "script1":
      document.getElementById(
        "script-selected-description"
      ).innerHTML = load_script1();
      break;
    case "script2":
      document.getElementById(
        "script-selected-description"
      ).innerHTML = load_script2();
      break;
    case "script3":
      document.getElementById(
        "script-selected-description"
      ).innerHTML = load_script3();
      break;
  }
}
function runScript() {
  var select = document.getElementById("script-select");
  var scriptToRun = select.options[select.selectedIndex].value;
  var formToSubmit = document.getElementsByName("runscriptform")[0];
  document.runscriptform.action =
    "http://localhost:5000/uploader?scriptToRun=" + scriptToRun;
  formToSubmit.submit();
  window.location.href = window.location.href;
}
