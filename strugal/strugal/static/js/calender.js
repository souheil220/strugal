//alert(productval)
$("#calendar").fullCalendar({
  themeSystem: 'bootstrap4',
  defaultView: "basicWeek",
  displayEventTime: false,
  events: "/planing/events",
  header: {
    left: 'prev,next today',
    center: 'title',
    right: 'basicWeek,month'
  },

  eventClick: function (calEvent) {
    var today = aujourdhui()
    if (today <= calEvent.start._i) {
      var test = (calEvent.title).split('\n')

      $("#updateModal").modal("show");

      var newDiv = $(`<div id='jetable'><input
      type="hidden"
      name="form-TOTAL_FORMS"
      value="1"
      id="id_form-TOTAL_FORMS"
    /><input
      type="hidden"
      name="form-INITIAL_FORMS"
      value="0"
      id="id_form-INITIAL_FORMS"
    /><input
      type="hidden"
      name="form-MIN_NUM_FORMS"
      value="0"
      id="id_form-MIN_NUM_FORMS"
    /><input
      type="hidden"
      name="form-MAX_NUM_FORMS"
      value="1000"
      id="id_form-MAX_NUM_FORMS"
    />

<div>
    <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text">Ref</span>
        </div>
        <input
          type="text"
          name="form-0-ref"
          class="form-control"
          required="true"
          maxlength="255"
          id="id_form-0-ref"
        />
    </div>
    <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text">Qte</span>
        </div>
        <input
          type="number"
          name="form-0-qte"
          class="form-control"
          required="true"
          id="id_form-0-qte"
        />
    </div>
      <!-- <div class="closeButton" id="test">&times;</div> -->
    <input
        type="hidden"
        name="form-0-date_created"
        id="id_form-0-date_created"
      />
    
</div><div>`)

      newDiv.insertBefore('#sub_mod')


      $("#id_form-0-ref").val(test[0]);
      $("#id_form-0-qte").val(test[1]);

      console.log($("#id_form-0-ref").val())
      $("#day").val(today)
      $('#id').val(calEvent.id)
      $('#id_form-0-date_created').val($("#day").val())
      $("#updateModal").submit(function () {
        ref = $("#id_form-0-ref").val();
        qte = $("#id_form-0-qte").val();

        if (ref && qte) {

          calEvent.title = ref + "\n" + qte;
          $('#calendar').fullCalendar('updateEvent', calEvent);
        }
        $("#updateModal").modal("hide");
      })



    }

    // change the border color just for fun
    $(this).css('border-color', 'red');

  },


  dayClick: function (date, jsEvent, view) {
    $("#id_form-0-ref").val("");
    $("#id_form-0-qte").val("");
    var today = aujourdhui()

    if (today <= date.format()) {
      $('#add_more').show()
      $("#inquiryModal").modal("show");

      //por regler le probleme des id répliquer concernant le nombre de form
      $(`<div id='jetable'><input
      type="hidden"
      name="form-TOTAL_FORMS"
      value="1"
      id="id_form-TOTAL_FORMS"
    /><input
      type="hidden"
      name="form-INITIAL_FORMS"
      value="0"
      id="id_form-INITIAL_FORMS"
    /><input
      type="hidden"
      name="form-MIN_NUM_FORMS"
      value="0"
      id="id_form-MIN_NUM_FORMS"
    /><input
      type="hidden"
      name="form-MAX_NUM_FORMS"
      value="1000"
      id="id_form-MAX_NUM_FORMS"
    />
<div>
    <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text">Ref</span>
        </div>
        <input
          type="text"
          name="form-0-ref"
          class="form-control"
          required="true"
          maxlength="255"
          id="id_form-0-ref"
        />
    </div>
    <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text">Qte</span>
        </div>
        <input
          type="number"
          name="form-0-qte"
          class="form-control"
          required="true"
          id="id_form-0-qte"
        />
    </div>
      <!-- <div class="closeButton" id="test">&times;</div> -->
    <input
        type="hidden"
        name="form-0-date_created"
        id="id_form-0-date_created"
    />
    
</div></div>`).insertBefore('#turningPoint')


      $("#jour").val(date.format())
      $('#id_form-0-date_created').val($("#jour").val())
      console.log(jsEvent)
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
    }
  },

});

function aujourdhui() {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();

  today = yyyy + '-' + mm + '-' + dd;
  return today
}


$("body").on("hidden.bs.modal", () => {
  $('#jetable').remove()
});

$('.close').click(function (e) {
  $('#jetable').remove()
})