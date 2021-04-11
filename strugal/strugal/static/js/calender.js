//alert(productval)
$("#calendar").fullCalendar({
  themeSystem: 'bootstrap4',
  defaultView: "basicWeek",
  displayEventTime: false,
  events: "/planing/events",

  dayClick: function (date, jsEvent, view) {

    $("#inquiryModal").modal("show");
    $("#jour").val(date.format()),
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