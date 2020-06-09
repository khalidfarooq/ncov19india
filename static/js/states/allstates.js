function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 11;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#apactive").append(total_active);
    $("#aprecovered").append(total_recovered);
    $("#apdeaths").append(total_deaths);
    $("#apconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[2].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#aptbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 18;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#asactive").append(total_active);
    $("#asrecovered").append(total_recovered);
    $("#asdeaths").append(total_deaths);
    $("#asconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[4].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#astbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 25;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#chactive").append(total_active);
    $("#chrecovered").append(total_recovered);
    $("#chdeaths").append(total_deaths);
    $("#chconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[6].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#chtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 3;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#dlactive").append(total_active);
    $("#dlrecovered").append(total_recovered);
    $("#dldeaths").append(total_deaths);
    $("#dlconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[8].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#dltbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 28;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#gaactive").append(total_active);
    $("#garecovered").append(total_recovered);
    $("#gadeaths").append(total_deaths);
    $("#gaconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[10].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#gatbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 23;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#hpactive").append(total_active);
    $("#hprecovered").append(total_recovered);
    $("#hpdeaths").append(total_deaths);
    $("#hpconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[12].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#hptbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 21;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#jhactive").append(total_active);
    $("#jhrecovered").append(total_recovered);
    $("#jhdeaths").append(total_deaths);
    $("#jhconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[14].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#jhtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    total_active = data.statewise[12].active;
    total_recovered = data.statewise[12].recovered;
    total_deaths = data.statewise[12].deaths;
    total_confirmed = data.statewise[12].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#kaactive").append(total_active);
    $("#karecovered").append(total_recovered);
    $("#kadeaths").append(total_deaths);
    $("#kaconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[16].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#katbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 27;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#laactive").append(total_active);
    $("#larecovered").append(total_recovered);
    $("#ladeaths").append(total_deaths);
    $("#laconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {
    var count = 0;

    $.each(data[18].districtData, function (id, obj) {

      if (count < 2) {
        var eachrow =
          "<tr>" +
          "<td>" +
          obj.district +
          "</a></td>" +
          "<td style = \"color:rgb(68, 155, 226);\">" +
          obj.confirmed +
          "</td>" +
          "<td style = \"color: rgb(101, 221, 155);\">" +
          obj.recovered +
          "</td>" +
          "<td style = \"color:#f65164;\">" +
          obj.deceased +
          "</td>" +
          "<td style = \"color:rgb(248, 245, 64);\">" +
          obj.active +
          "</td>" +
          "</tr>";
        $("#latbody").append(eachrow);

        count++;
      }
    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    a = 1
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#mhactive").append(total_active);
    $("#mhrecovered").append(total_recovered);
    $("#mhdeaths").append(total_deaths);
    $("#mhconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[20].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#mhtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 26;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#mnactive").append(total_active);
    $("#mnrecovered").append(total_recovered);
    $("#mndeaths").append(total_deaths);
    $("#mnconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[22].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#mntbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 35;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#mzactive").append(total_active);
    $("#mzrecovered").append(total_recovered);
    $("#mzdeaths").append(total_deaths);
    $("#mzconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[24].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#mztbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 17;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#oractive").append(total_active);
    $("#orrecovered").append(total_recovered);
    $("#ordeaths").append(total_deaths);
    $("#orconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[26].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#ortbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 29;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#pyactive").append(total_active);
    $("#pyrecovered").append(total_recovered);
    $("#pydeaths").append(total_deaths);
    $("#pyconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[28].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#pytbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 36;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#skactive").append(total_active);
    $("#skrecovered").append(total_recovered);
    $("#skdeaths").append(total_deaths);
    $("#skconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[30].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#sktbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    total_active = data.statewise[2].active;
    total_recovered = data.statewise[2].recovered;
    total_deaths = data.statewise[2].deaths;
    total_confirmed = data.statewise[2].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#tnactive").append(total_active);
    $("#tnrecovered").append(total_recovered);
    $("#tndeaths").append(total_deaths);
    $("#tnconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {

    count = 0
    $.each(data[32].districtData, function (id, obj) {

      if (count > 2) {
        var eachrow =
          "<tr>" +
          "<td>" +
          obj.district +
          "</a></td>" +
          "<td style = \"color:rgb(68, 155, 226);\">" +
          obj.confirmed +
          "</td>" +
          "<td style = \"color: rgb(101, 221, 155);\">" +
          obj.recovered +
          "</td>" +
          "<td style = \"color:#f65164;\">" +
          obj.deceased +
          "</td>" +
          "<td style = \"color:rgb(248, 245, 64);\">" +
          obj.active +
          "</td>" +
          "</tr>";
        $("#tntbody").append(eachrow);
      }
      count++;


    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 7;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#upactive").append(total_active);
    $("#uprecovered").append(total_recovered);
    $("#updeaths").append(total_deaths);
    $("#upconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[34].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#uptbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 8;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#wbactive").append(total_active);
    $("#wbrecovered").append(total_recovered);
    $("#wbdeaths").append(total_deaths);
    $("#wbconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[36].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#wbtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 4;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#gjactive").append(total_active);
    $("#gjrecovered").append(total_recovered);
    $("#gjdeaths").append(total_deaths);
    $("#gjconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {
    count = 0;

    $.each(data[11].districtData, function (id, obj) {

      if (count > 1) {
        var eachrow =
          "<tr>" +
          "<td>" +
          obj.district +
          "</a></td>" +
          "<td style = \"color:rgb(68, 155, 226);\">" +
          obj.confirmed +
          "</td>" +
          "<td style = \"color: rgb(101, 221, 155);\">" +
          obj.recovered +
          "</td>" +
          "<td style = \"color:#f65164;\">" +
          obj.deceased +
          "</td>" +
          "<td style = \"color:rgb(248, 245, 64);\">" +
          obj.active +
          "</td>" +
          "</tr>";
        $("#gjtbody").append(eachrow);
      }
      count++;

    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 5;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#rjactive").append(total_active);
    $("#rjrecovered").append(total_recovered);
    $("#rjdeaths").append(total_deaths);
    $("#rjconfirmed").append(total_confirmed);
  });
});

$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {
    $.each(data[29].districtData, function (id, obj) {
      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#rjtbody").append(eachrow);

    });
  });
});

$(document).ready(function () {
  $(".row").delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 6;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;


    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#mpactive").append(total_active);
    $("#mprecovered").append(total_recovered);
    $("#mpdeaths").append(total_deaths);
    $("#mpconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[23].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#mptbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 10;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#bractive").append(total_active);
    $("#brrecovered").append(total_recovered);
    $("#brdeaths").append(total_deaths);
    $("#brconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[5].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#brtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 15;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#hractive").append(total_active);
    $("#hrrecovered").append(total_recovered);
    $("#hrdeaths").append(total_deaths);
    $("#hrconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[13].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#hrtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 14;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#jkactive").append(total_active);
    $("#jkrecovered").append(total_recovered);
    $("#jkdeaths").append(total_deaths);
    $("#jkconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[15].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#jktbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 13;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#tgactive").append(total_active);
    $("#tgrecovered").append(total_recovered);
    $("#tgdeaths").append(total_deaths);
    $("#tgconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {
    count = 0;

    $.each(data[31].districtData, function (id, obj) {

      if (count > 1) {
        var eachrow =
          "<tr>" +
          "<td>" +
          obj.district +
          "</a></td>" +
          "<td style = \"color:rgb(68, 155, 226);\">" +
          obj.confirmed +
          "</td>" +
          "<td style = \"color: rgb(101, 221, 155);\">" +
          obj.recovered +
          "</td>" +
          "<td style = \"color:#f65164;\">" +
          obj.deceased +
          "</td>" +
          "<td style = \"color:rgb(248, 245, 64);\">" +
          obj.active +
          "</td>" +
          "</tr>";
        $("#tgtbody").append(eachrow);

      }
      count++;

    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 16;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#pbactive").append(total_active);
    $("#pbrecovered").append(total_recovered);
    $("#pbdeaths").append(total_deaths);
    $("#pbconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[27].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#pbtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 19;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#klactive").append(total_active);
    $("#klrecovered").append(total_recovered);
    $("#kldeaths").append(total_deaths);
    $("#klconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[17].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#kltbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 20;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#utactive").append(total_active);
    $("#utrecovered").append(total_recovered);
    $("#utdeaths").append(total_deaths);
    $("#utconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[35].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#uttbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;

    const a = 22;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#ctactive").append(total_active);
    $("#ctrecovered").append(total_recovered);
    $("#ctdeaths").append(total_deaths);
    $("#ctconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[7].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#cttbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 24;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#tractive").append(total_active);
    $("#trrecovered").append(total_recovered);
    $("#trdeaths").append(total_deaths);
    $("#trconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[33].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#trtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 30;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#nlactive").append(total_active);
    $("#nlrecovered").append(total_recovered);
    $("#nldeaths").append(total_deaths);
    $("#nlconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[25].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#nltbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 33;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#aractive").append(total_active);
    $("#arrecovered").append(total_recovered);
    $("#ardeaths").append(total_deaths);
    $("#arconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[3].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#artbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 32;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#mlactive").append(total_active);
    $("#mlrecovered").append(total_recovered);
    $("#mldeaths").append(total_deaths);
    $("#mlconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[21].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#mltbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 31;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#anactive").append(total_active);
    $("#anrecovered").append(total_recovered);
    $("#andeaths").append(total_deaths);
    $("#anconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[1].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#antbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 34;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#dnactive").append(total_active);
    $("#dnrecovered").append(total_recovered);
    $("#dndeaths").append(total_deaths);
    $("#dnconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[9].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#dntbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});
function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var total_active, total_recovered, total_deaths, total_confirmed;
    const a = 37;
    total_active = data.statewise[a].active;
    total_recovered = data.statewise[a].recovered;
    total_deaths = data.statewise[a].deaths;
    total_confirmed = data.statewise[a].confirmed;

    total_active = numberWithCommas(total_active);
    total_confirmed = numberWithCommas(total_confirmed);
    total_deaths = numberWithCommas(total_deaths);
    total_recovered = numberWithCommas(total_recovered);

    $("#ldactive").append(total_active);
    $("#ldrecovered").append(total_recovered);
    $("#lddeaths").append(total_deaths);
    $("#ldconfirmed").append(total_confirmed);
  });
});


$(document).ready(function () {
  var url = "https://api.covid19india.org/v2/state_district_wise.json";

  $.getJSON(url, function (data) {


    $.each(data[19].districtData, function (id, obj) {


      var eachrow =
        "<tr>" +
        "<td>" +
        obj.district +
        "</a></td>" +
        "<td style = \"color:rgb(68, 155, 226);\">" +
        obj.confirmed +
        "</td>" +
        "<td style = \"color: rgb(101, 221, 155);\">" +
        obj.recovered +
        "</td>" +
        "<td style = \"color:#f65164;\">" +
        obj.deceased +
        "</td>" +
        "<td style = \"color:rgb(248, 245, 64);\">" +
        obj.active +
        "</td>" +
        "</tr>";
      $("#ldtbody").append(eachrow);



    });
  });
});


$(document).ready(function () {
  $('.row').delay(100).fadeIn(300);
});

