var colors = ["red", "black", "purple"];
var i = 0;

document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: "dayGridWeek",
    locale: "fr",
    themeSystem: "bootstrap",
    selectable: true,
    eventDisplay: 'block',

    select: function (arg) {
      $("#inquiryModal").modal("show");
      $("#inquiryModal").submit(function (event) {
        var totalForm = parseInt($("#id_form-TOTAL_FORMS").val());
        var value, qte, long;
        for (var j = 0; j < totalForm; j++) {

          value = $("#id_form-" + j.toString() + "-ref").val();
          qte = $("#id_form-" + j.toString() + "-qte").val();
          long = $("#id_form-" + j.toString() + "-longueur").val();

          if (value && qte && long) {
            if (i >= colors.length) {
              i = 0;
            } else {
              i++;
            }

            var test = calendar. value + "\n" + qte + "\n" + long
           


            // console.log(arg.startStr);
            calendar.addEvent({
              title: test,
              start: arg.start,
              end: arg.end,
              allDay: arg.allDay,
              color: colors[i],
            });


          }


          $("#id_form-" + j.toString() + "-ref").val("");
          $("#id_form-" + j.toString() + "-qte").val("");
          $("#id_form-" + j.toString() + "-longueur").val("");
        }
        //event.preventDefault();
        $("#inquiryModal").modal("hide");
      });
      calendar.unselect();
    },
  });
  calendar.render();
});