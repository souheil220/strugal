//alert(productval)
$("#calendar").fullCalendar({
  defaultView: "basicWeek",
  displayEventTime: false,
  // events: productval, //produit('{{product}}'),
  events: {
    url: "/planing/events"
  },

  dayClick: function (date, jsEvent, view) {

    $("#inquiryModal").modal("show");
    $("#jour").val(date),
      $('#id_form-0-date_created').val($("#jour").val())
    $("#inquiryModal").submit(function () {
      var totalForm = parseInt($("#id_form-TOTAL_FORMS").val());
      var ref, qte;
      for (var j = 0; j < totalForm; j++) {
        ref = $("#id_form-" + j.toString() + "-ref").val();
        qte = $("#id_form-" + j.toString() + "-qte").val();

        if (ref && qte) {
          $("#calendar").fullCalendar(
              "renderEvent", {
                title: ref + "\n" + qte,
                start: $("#jour").val(),
                end: $("#jour").val(),
              },
              !0
            ),
            $;
          $("#id_form-" + j.toString() + "-ref").val("");
          $("#id_form-" + j.toString() + "-qte").val("");

        }
        $("#inquiryModal").modal("hide");
        $(".fc-content .fc-time").remove();
      }
    });
  },
});

// [{
//   'id': 1,
//   'ref': 'd',
//   'qte': 4654.0,
//   'date_created': 'Wed Apr 07 2021 00:00:00 GMT+0000'
// }, {
//   'id': 2,
//   'ref': 'this is a test',
//   'qte': 123456.0,
//   'date_created': 'Sat Apr 10 2021 00:00:00 GMT+0000'
// }, {
//   'id': 3,
//   'ref': 'Please work',
//   'qte': 951357.0,
//   'date_created': 'Sat Apr 10 2021 00:00:00 GMT+0000'
// }]

$('.fc-button').click(function () {
  $.ajax({
    url: "/planing/events",
    type: "GET",
    success: function (res) {
      console.log(res);
      // alert(res);
    }
  });
  console.log('yo')
});