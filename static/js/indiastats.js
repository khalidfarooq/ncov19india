function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    total_active = data.statewise[0].active;
    total_recovered = data.statewise[0].recovered;
    total_deaths = data.statewise[0].deaths;
    total_confirmed = data.statewise[0].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#active").append(total_active);
    $("#recovered").append(total_recovered);
    $("#deaths").append(total_deaths);
    $("#confirmed").append(total_confirmed);
  });
});

$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});


/***************************************************************************/






