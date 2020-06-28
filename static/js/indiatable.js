$(document).ready(function () {
  var url = "https://api.covid19india.org/data.json";

  $.getJSON(url, function (data) {
    var count = 0;
    var allStates = [];
    $.each(data.statewise, function (id, obj) {
      allStates.push(obj.statecode);
    });
    allStates.shift();
    var i = -1;
    var unassgn = 0;
    $.each(data.statewise, function (id, obj) {
      var reqstate = allStates[i];

      if (count > 0 && (count != 9)) {
        if (reqstate != 'UN') {
          var eachrow =
            "<tr>" +
            '<td><a href="' +
            reqstate +
            '" id="' +
            reqstate +
            '">' +
            obj.state +
            "</a></td>" +
            '<td style = "color:rgb(248, 245, 64);">' +
            obj.active +
            "</td>" +
            '<td style = "color: rgb(101, 221, 155);">' +
            obj.recovered +
            "</td>" +
            '<td style = "color:#f65164;">' +
            obj.deaths +
            "</td>" +
            '<td style = "color:rgb(68, 155, 226);">' +
            obj.confirmed +
            "</td>" +
            "</tr>";
          $("#indiatbody").append(eachrow);
        }
      }
      i++;
      count++;
      unassgn++;
    });
  });
});
// window.onload = function () {
//   if (document.getElementById('table-input').value != null) {
//     document.getElementById('table-input').value = '';
//   }
// }
$(document).ready(function () {
  $(".row").delay(100).fadeIn(300);
});

$(document).ready(function () {
  $("#table-input").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $(
      "#indiatbody tr ,#mhtbody tr,#gjtbody tr,#rjtbody tr,#tntbody tr,#dltbody tr,#mptbody tr,#uptbody tr,#wbtbody tr,#brtbody tr,#aptbody tr,#katbody tr,#tgtbody tr,#jktbody tr,#hrtbody tr,#pbtbody tr,#ortbody tr,#astbody tr,#kltbody tr,#uttbody tr,#jhtbody tr,#cttbody tr,#hptbody tr,#trtbody tr,#chtbody tr,#mntbody tr,#latbody tr,#gatbody tr,#pytbody tr,#nltbody tr,#antbody tr,#mltbody tr,#artbody tr,#dntbody tr,#mztbody tr,#sktbody tr,#ldtbody tr"
    ).filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});
