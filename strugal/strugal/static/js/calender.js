var url = window.location.href
url = url.substring(30)
console.log(url)

$("#calendar").fullCalendar({
  themeSystem: 'bootstrap4',
  defaultView: "basicWeek",
  displayEventTime: false,
  events: `/planing/a?palning=` + url + `/events`,
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



      if (url === 'anodisation') {
        anodisationLB(test, calEvent, 'anodisation')
      } else if (url === 'laquageCouleur') {
        anodisationLB(test, calEvent, 'laquageCouleur')
      } else if (url === 'rpt') {
        rpt(test, calEvent, 'rpt')
      } else {
        normal(test, calEvent, url)
      }

    }

    // change the border color just for fun
    $(this).css('border-color', 'red');

  },


  dayClick: async function (date, jsEvent, view, ) {
    var events = await getEventOfDay(date.format())
    var today = aujourdhui()
    if (url === 'anodisation') {
      dayClickAnnodisation(date)
      anodisationLB(test, calEvent, 'anodisation')
    } else if (url === 'laquageCouleur') {
      dayClicklaquageBlanc()
      anodisationLB(test, calEvent, 'laquageCouleur')
    } else if (url === 'rpt') {
      dayClickRPT()
      rpt(test, calEvent, 'rpt')
    } else {
      dayClickNormal()
      normal(test, calEvent, url)
    }







    $("#id_form-0-ref").val("");
    $("#id_form-0-qte").val("");
    var today = aujourdhui()

    if (today <= date.format()) {
      $('#add_more').show()
      $("#inquiryModal").modal("show");

      //pour regler le probleme des id répliquer concernant le nombre de form
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
    <input
        type="hidden"
        name="form-0-date_created"
        id="id_form-0-date_created"
    />
    </div></div>`).insertBefore('#turningPoint')


      $("#jour").val(date.format())
      $('#id_form-0-date_created').val($("#jour").val())

      $("#inquiryModal").submit(function (event) {
        var totalForm = parseInt($("#id_form-TOTAL_FORMS").val());
        var ref, qte;
        for (var j = 0; j < totalForm; j++) {
          ref = $("#id_form-" + j.toString() + "-ref").val();
          qte = $("#id_form-" + j.toString() + "-qte").val();

          var goodToGo = true

          events.forEach((e) => {
            if (e['title'] === ref) {
              goodToGo = false;
              alert('ref ' + e['title'] + ' already there')
              event.preventDefault();
              ref = $("#id_form-" + j.toString() + "-ref").val("");
              qte = $("#id_form-" + j.toString() + "-qte").val("");
            }
          })


          if (ref && qte && goodToGo) {
            console.log(goodToGo)
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

// rani habes hna 

function dayClickAnnodisation() {
  $("#id_form-0-ref").val("");
  $("#id_form-0-qte").val("");
  $("#id_form-0-ral").val("");

  if (today <= date.format()) {
    $('#add_more').show()
    $("#inquiryModal").modal("show");

    //pour regler le probleme des id répliquer concernant le nombre de form
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
        <span class="input-group-text">Ral</span>
      </div>
      <input
        type="text"
        name="form-0-ral"
        class="form-control"
        required="true"
        maxlength="255"
        id="id_form-0-ral"
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
  <input
      type="hidden"
      name="form-0-date_created"
      id="id_form-0-date_created"
  />
  </div></div>`).insertBefore('#turningPoint')

    $("#jour").val(date.format())
    $('#id_form-0-date_created').val($("#jour").val())

    $("#inquiryModal").submit(function (event) {
      var totalForm = parseInt($("#id_form-TOTAL_FORMS").val());
      var ref, qte, ral;
      for (var j = 0; j < totalForm; j++) {
        ref = $("#id_form-" + j.toString() + "-ref").val();
        qte = $("#id_form-" + j.toString() + "-qte").val();
        ral = $("#id_form-" + j.toString() + "-ral").val();

        var goodToGo = true

        events.forEach((e) => {
          if (e['title'] === ref) {
            goodToGo = false;
            alert('ref ' + e['title'] + ' already there')
            event.preventDefault();
            ref = $("#id_form-" + j.toString() + "-ref").val("");
            qte = $("#id_form-" + j.toString() + "-qte").val("");
            ral = $("#id_form-" + j.toString() + "-ral").val("");
          }
        })


        if (ref && qte && ral && goodToGo) {
          console.log(goodToGo)
          $("#calendar").fullCalendar(
              "renderEvent", {
                title: ref + "\n" + ral + "\n" + qte,
                start: $("#jour").val(),
                end: $("#jour").val(),
              },
              !0
            ),
            $;
          $("#id_form-" + j.toString() + "-ref").val("");
          $("#id_form-" + j.toString() + "-qte").val("");
          $("#id_form-" + j.toString() + "-ral").val("");

        }
        $("#inquiryModal").modal("hide");
        $(".fc-content .fc-time").remove();
      }
    });
  }
}


function aujourdhui() {
  var today = new Date();
  var dd = String(today.getDate()).padStart(2, '0');
  var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = today.getFullYear();

  today = yyyy + '-' + mm + '-' + dd;
  return today
}

async function getEventOfDay(day) {

  var json
  try {
    json = await $.ajax({
      url: `/planing/getdate/${day}`,
      type: "GET",
      cache: false,
      contentType: false,
      processData: false,
      dataType: 'JSON',

    })
    return json
  } catch (error) {
    console.log(error)
  };

}


$("body").on("hidden.bs.modal", () => {
  $('#jetable').remove()
});

$('.close').click(function (e) {
  $('#jetable').remove()
})


function anodisationLB(test, calEvent, typeP) {
  var today = aujourdhui()
  var newDiv = myDiv(test)
  newDiv.insertBefore('#sub_mod')
  deleteProduct(calEvent.id, typeP)
  $("#id_form-0-ref").val(test[0]);
  $("#id_form-0-ral").val(test[1]);
  $("#id_form-0-qte").val(test[2]);

  $("#day").val(today)
  $('#id').val(calEvent.id)
  $('#id_form-0-date_created').val($("#day").val())

  $("#updateModal").submit(function () {
    ref = $("#id_form-0-ref").val();
    qte = $("#id_form-0-qte").val();
    ral = $("#id_form-0-ral").val();

    if (ref && qte && ral) {


      calEvent.title = ref + "\n" + ral + "\n" + qte;

      $('#calendar').fullCalendar('updateEvent', calEvent);
    }
    $("#updateModal").modal("hide");
  })
}

function rpt(test, calEvent, typeP) {
  var today = aujourdhui()
  var newDiv = myDiv(test)
  newDiv.insertBefore('#sub_mod')
  deleteProduct(calEvent.id, typeP)

  $("#id_form-0-ref01").val(test[0]);
  $("#id_form-0-ref02").val(test[1]);
  $("#id_form-0-ral01").val(test[2]);
  $("#id_form-0-ral02").val(test[3]);
  $("#id_form-0-qte").val(test[4]);

  $("#day").val(today)
  $('#id').val(calEvent.id)
  $('#id_form-0-date_created').val($("#day").val())

  $("#updateModal").submit(function () {
    ref01 = $("#id_form-0-ref01").val(test[0]);
    ref02 = $("#id_form-0-ref02").val(test[1]);
    ral01 = $("#id_form-0-ral01").val(test[2]);
    ral02 = $("#id_form-0-ral02").val(test[3]);
    qte = $("#id_form-0-qte").val(test[4]);

    if (ref01 && ref02 && ral01 && ral02 && qte) {


      calEvent.title = ref01 + "\n" + ref02 + "\n" + ral01 + "\n" + ral02 + "\n" + qte;

      $('#calendar').fullCalendar('updateEvent', calEvent);
    }
    $("#updateModal").modal("hide");
  })

}

function normal(test, calEvent, typeP) {
  var today = aujourdhui()
  var newDiv = myDiv(test)
  newDiv.insertBefore('#sub_mod')
  deleteProduct(calEvent.id, typeP)
  $("#id_form-0-ref").val(test[0]);
  $("#id_form-0-qte").val(test[1]);

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




function deleteProduct(id, ppt) {
  $('#deleteProduct').click(function () {
    $("#calendar").fullCalendar('removeEvents', id);
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      url: `/planing/delete/${$("#id").val()}?ppt=${ppt}`,
      type: "POST",
      cache: false,
      data: {
        'csrfmiddlewaretoken': csrf
      },
      success: function (response) {},
    });

    $("#updateModal").modal("hide");
  })
}


function myDiv(test) {
  if (url === 'anodisation') {
    return $(`<div id='jetable'><input
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
      <span class="input-group-text">Ral</span>
    </div>
    <input
      type="text"
      name="form-0-ral"
      class="form-control"
      required="true"
      maxlength="255"
      id="id_form-0-ral"
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
    
    <button id="deleteProduct" type="button" class="btn btn-danger">
                  Spprimer Product
                </button>
    <input
        type="hidden"
        name="form-0-date_created"
        id="id_form-0-date_created"
      />
    
                      </div><div>`)

  } else if (url === 'laquageCouleur') {
    return $(`<div id='jetable'><input
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
          <span class="input-group-text">Ral</span>
        </div>
        <input
          type="text"
          name="form-0-ral"
          class="form-control"
          required="true"
          maxlength="255"
          id="id_form-0-ral"
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
    <button id="deleteProduct" type="button" class="btn btn-danger">
                  Spprimer Product
                </button>
    <input
        type="hidden"
        name="form-0-date_created"
        id="id_form-0-date_created"
      />
    
                      </div><div>`)
  } else if (url === 'rpt') {
    return $(`<div id='jetable'><input
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
        <span class="input-group-text">Ref01</span>
      </div>
      <input
        type="text"
        name="form-0-ref01"
        class="form-control"
        required="true"
        maxlength="255"
        id="id_form-0-ref01"
      />
  </div>
  <div>
  <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text">Ref02</span>
      </div>
      <input
        type="text"
        name="form-0-ref02"
        class="form-control"
        required="true"
        maxlength="255"
        id="id_form-0-ref02"
      />
  </div>
  <div>
  <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text">Ral01</span>
      </div>
      <input
        type="text"
        name="form-0-ral01"
        class="form-control"
        required="true"
        maxlength="255"
        id="id_form-0-ral01"
      />
  </div>
  <div>
  <div class="input-group mb-3">
      <div class="input-group-prepend">
        <span class="input-group-text">Ral02</span>
      </div>
      <input
        type="text"
        name="form-0-ral02"
        class="form-control"
        required="true"
        maxlength="255"
        id="id_form-0-ral02"
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
  <button id="deleteProduct" type="button" class="btn btn-danger">
                Spprimer Product
              </button>
  <input
      type="hidden"
      name="form-0-date_created"
      id="id_form-0-date_created"
    />
  
                    </div><div>`)
  } else {
    return $(
      `<div id='jetable'><input
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
    <button id="deleteProduct" type="button" class="btn btn-danger">
                Spprimer Product
              </button>
    <input
      type="hidden"
      name="form-0-date_created"
      id="id_form-0-date_created"
    />
    
                    </div><div>`)
  }
}