$(document).ready(function () {
  var url = "http://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
  

    //DAILY CASES
    dates = [];
    daily_confirmed = [];
    daily_recovered = [];
    daily_deceased = [];
    count=0;
    $.each(data.cases_time_series, function (id, obj) {
      if(count>60){
      dates.push(obj.date);
      daily_confirmed.push(obj.dailyconfirmed);
      daily_recovered.push(obj.dailyrecovered);
      daily_deceased.push(obj.dailydeceased);
    }count++;
    });

    var daily_chart = document.getElementById("daily-chart").getContext("2d");

    var chart = new Chart(daily_chart, {
      type: "bar",
      data: {
        labels: dates,
        datasets: [
          {
            label: "Confirmed",
            data: daily_confirmed,
            backgroundColor: "#f1c40f",
            minBarLength: 1,
          },
          {
            label: "Recoverd",
            data: daily_recovered,
            backgroundColor: "#2ec771",
            minBarLength: 1,
          },

          {
            label: "Deaths",
            data: daily_deceased,
            backgroundColor: "#e74c3c",
            minBarLength: 1,
          },
        ],
      },
      options: {
        responsive:true,
        maintainAspectRatio:false,
        tooltips: {
          mode: "index",
          intersect: false,
        },
        hover: {
          mode: "index",
          intersect: false,
        },
      },
    });
  });
});
