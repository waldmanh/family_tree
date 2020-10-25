function get_run_title(withRunButton) {
  var htmlString = "<h2>Run script:</h2>";
  if (withRunButton === true)
    htmlString +=
      '<h2><input type="submit" value="Run" id="run-script-submit"/></h2>';
  htmlString += "<h2>Instructions:</h2>";
  return htmlString;
}
