$(document).ready(function () {
  var url = "http://api.covid19india.org/data.json";
  var colors = [
    "#003f5c",
    "#58508d",
    "#bc5090",
    "#ff6361",
    "#ffa600",
  ];
  $.getJSON(url, function (data) {
    //DAILY CASES
    stateName = [];
    active = [];
    count = 0;
    $.each(data.statewise, function (id, obj) {
      if (count > 0 && count < 6) {
        stateName.push(obj.state);
        active.push(obj.active);
      }
      count++;
    });

    var daily_chart = document.getElementById("chDonut1").getContext("2d");

    var chart = new Chart(daily_chart, {
      type: "pie",
      data: {
        labels: stateName,
        datasets: [
          {
            label: "Confirmed",
            data: active,
            backgroundColor: colors.slice(0, 5),
            borderWidth: 0,
          },
        ],
      },
      options: {
        responsive: true,
        maintainaAspectRatio: false,

        legend: {
          position: "bottom",
          padding: 5,

        },

      },
    });
  });

  /************************Recovered*************************/

  var colors = [
    "#003f5c",
    "#58508d",
    "#bc5090",
    "#ff6361",
    "#ffa600",
  ];
  $.getJSON(url, function (data) {
    //DAILY CASES
    stateName = [];
    recovered = [];
    count = 0;
    $.each(data.statewise, function (id, obj) {
      if (count > 0 && count < 6) {
        stateName.push(obj.state);
        recovered.push(obj.recovered);
      }
      count++;
    });

    var daily_chart = document.getElementById("chDonut2").getContext("2d");

    var chart = new Chart(daily_chart, {
      type: "pie",
      data: {
        labels: stateName,
        datasets: [
          {
            label: "Recovered",
            data: recovered,
            backgroundColor: colors.slice(0, 5),
            borderWidth: 0,
          },
        ],
      },
      options: {
        responsive: true,
        maintainaAspectRatio: false,

        legend: {
          position: "bottom",
          padding: 5,

        },
      },
    });
  });

  /************************Deaths*************************/

  var colors = [
    "#003f5c",
    "#58508d",
    "#bc5090",
    "#ff6361",
    "#ffa600",
  ];
  $.getJSON(url, function (data) {

    stateName = [];
    deceased = [];
    count = 0;
    $.each(data.statewise, function (id, obj) {
      if (count > 0 && count < 6) {
        stateName.push(obj.state);
        deceased.push(obj.deaths);
      }
      count++;
    });

    var daily_chart = document.getElementById("chDonut3").getContext("2d");

    var chart = new Chart(daily_chart, {
      type: "pie",
      data: {
        labels: stateName,
        datasets: [
          {
            label: "Deceased",
            data: deceased,
            backgroundColor: colors.slice(0, 5),
            borderWidth: 0,
          },
        ],
      },
      options: {
        responsive: true,
        maintainaAspectRatio: false,

        legend: {
          position: "bottom",
          padding: 5,

        },
      },
    });
  });
});