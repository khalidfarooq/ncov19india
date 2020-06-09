$(document).ready(function () {
  var url = "http://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    //TOTAL CASES
    dates = [];
    daily_confirmed = [];
    daily_recovered = [];
    daily_deceased = [];
    $.each(data.cases_time_series.slice(100), function (id, obj) {
      dates.push(obj.date);
      daily_confirmed.push(obj.dailyconfirmed);
      daily_recovered.push(obj.dailyrecovered);
      daily_deceased.push(obj.dailydeceased);
    });

    var total_chart = document.getElementById("total-chart").getContext("2d");

    var chart = new Chart(total_chart, {
      type: "line",
      data: {
        labels: dates,
        datasets: [
          {
            label: "Confirmed",
            data: daily_confirmed,
            backgroundColor: "#f1c40f",
            minBarLength: 0,
          },
          {
            label: "Recoverd",
            data: daily_recovered,
            backgroundColor: "#2ec771",
            minBarLength: 0,
          },

          {
            label: "Deaths",
            data: daily_deceased,
            backgroundColor: "#e74c3c",
            minBarLength: 0,
          },
        ],
      },
      options: {
        responsive:true,
        maintainAspectRatio:false,
         tooltips: {
         mode: 'index',
         intersect: false
      },
      hover: {
         mode: 'index',
         intersect: false
      },
      
      },
    });
  });
});
