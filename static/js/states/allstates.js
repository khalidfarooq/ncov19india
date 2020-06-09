function numberWithCommas(number) {
  var parts = number.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
}
$(document).ready(function () {
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
  var url = "http://api.covid19india.org/data.json";

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
