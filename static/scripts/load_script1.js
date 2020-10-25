function load_script1() {
  return (
    get_run_title(true) +
    '<ul>\
          <li>File has to be xlsx type</li>\
          <li>The first sheet contains the date and it\'s name is "Sheet1"</li>\
          <li>The xlsx file should be in the following structure:</li>\
        </ul>\
        <div class="table">\
          <table>\
            <tr>\
              <th>id</th>\
              <th>data</th>\
            </tr>\
            <tr>\
              <td>1</td>\
              <td>dd/MM/yyyy</td>\
            </tr>\
            <tr>\
              <td>2</td>\
              <td>dd/MM/yyyy</td>\
            </tr>\
          </table>\
        </div>'
  );
}
