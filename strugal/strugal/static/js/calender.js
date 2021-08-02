var url = window.location.href
url = url.substring(30)
console.log(url)
var option = "0"
if (url === 'anodisation') {
  option = "4"
} else if (url === 'rpt') {
  option = "5"
} else if (url === 'laquageCouleur') {
  option = "3"
} else if (url === 'laquageBlanc') {
  option = "2"
} else {
  url = "extrusion"
  option = "1"
}

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
      if (url.length <= 0) {
        url = "extrusion"
      }
      console.log(url)
      normal(test, calEvent, url)



    }

    // change the border color just for fun
    $(this).css('border-color', 'red');

  },


  dayClick: async function (date, jsEvent, view) {
    var events = await getEventOfDay(date.format(), url)
    console.log(events)
    console.log("jsEvent " + Object.keys(jsEvent.originalEvent))
    var today = aujourdhui()
    dayClickP(date, today, events, url, option)

  },

});



$('#inquiryModal').on('hidden.bs.modal', function (e) {
  console.log('inquiryModal was hidden')
  $('.suplementaire').each(function (e) {
    $(this).remove()
  })
})

//coma back later to fix bugs
function dayClickP(date, today, events, url, option) {
  console.log("url " + url)
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
  <div class="input-group">
      
        <span class="input-group-addon">Ref</span>
      
      <input
        type="text"
        name="form-0-ref"
        class="form-control"
        required="true"
        maxlength="255"
        id="id_form-0-ref"
      />
  </div>
  <div class="input-group">
      
        <span class="input-group-addon">Qte</span>
      
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
  
  <select name="form-0-typeP" id="id_form-0-typeP" hidden>
  <option value="` + option + `" selected>` + url + `</option>
  </select>
      </div></div>`).insertBefore('#turningPoint')


    $("#jour").val(date.format())
    $('#id_form-0-date_created').val($("#jour").val())

    $("#inquiryModal").submit(function (e) {
      var totalForm = parseInt($("#id_form-TOTAL_FORMS").val());
      var ref, qte;
      for (var j = 0; j < totalForm; j++) {
        ref = $("#id_form-" + j.toString() + "-ref").val();
        qte = $("#id_form-" + j.toString() + "-qte").val();

        var goodToGo = true

        events.forEach((event) => {
          console.log(event)
          if (event.title === ref) {
            goodToGo = false;
            // demo.showSwal('error-message', 'La référence ' + e['title'] + ' existe déja !')
            // alert('La référence ' + e['title'] + ' existe déja !')
            alert(event)
            ref = $("#id_form-" + j.toString() + "-ref").val("");
            qte = $("#id_form-" + j.toString() + "-qte").val("");
            e.preventDefault();
            console.log("event " + e)
          }

        })

        if (ref && qte && goodToGo) {
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

          $("#inquiryModal").modal("hide");
          $(".fc-content .fc-time").remove();
        }
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

async function getEventOfDay(day, typeP) {

  var json
  try {
    json = await $.ajax({
      url: `/planing/getdate/${day}/${typeP}`,
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


function normal(test, calEvent, typeP) {
  var today = aujourdhui()
  $("#day").val(today)
  var newDiv = myDiv(test)
  newDiv.insertBefore('#sub_mod')
  deleteProduct(calEvent.id, typeP)
  $("#id_form-0-ref").val(test[0]);
  $("#id_form-0-qte").val(test[1]);


  $('#id').val(calEvent.id)
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




function deleteProduct(id) {
  $('#deleteProduct').click(function () {
    $("#calendar").fullCalendar('removeEvents', id);
    var csrf = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      url: `/planing/delete/${$("#id").val()}`,
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


function myDiv() {
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
    <div class="input-group">
      
        <span class="input-group-addon">Ref</span>

      <input
        type="text"
        name="form-0-ref"
        class="form-control"
        required="true"
        maxlength="255"
        id="id_form-0-ref"
      />
    </div>
    <div class="input-group ">
      
        <span class="input-group-addon">Qte</span>

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
      value = ` + $("#day").val() + `
    />
    <select name="form-0-typeP" 
  id="id_form-0-typeP" hidden>
    <option value="` + option + `" selected>` + url + `</option>
</select>
                    </div><div>`)

}