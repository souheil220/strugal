$("#add_more").click(function () {
  $("#removeit").attr('disabled', false);
  var form_idx = $("#id_form-TOTAL_FORMS").val();

  $("#empty_form").append(
    `
    <div id='div-num-` + form_idx + `'>
      <hr>

      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text">Ref</span>
        </div>
        <input
          type="text"
          name="form-` + parseInt(form_idx).toString() + `-ref"
          class="form-control"
          required="true"
          maxlength="255"
          id="id_form-` + parseInt(form_idx).toString() + `-ref"
        />
      </div>
      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text">Qte</span>
        </div>
        <input
          type="text"
          name="form-` +
    parseInt(form_idx).toString() +
    `-qte"
          class="form-control"
          required="true"
          id="id_form-` +
    parseInt(form_idx).toString() +
    `-qte"
        />
      </div>
      <input type="hidden" name="form-` +
    parseInt(form_idx).toString() +
    `-date_created" id="id_form-` +
    parseInt(form_idx).toString() +
    `-date_created" value="` + $("#jour").val() + `">
    </div>
     `.replace(
      /__prefix__/g,
      form_idx
    )
  );
  $("#id_form-TOTAL_FORMS").val(parseInt(form_idx) + 1);
});


$("#removeit").click(function () {
  var form_idx = $("#id_form-TOTAL_FORMS").val();
  if (parseInt(form_idx) > 1) {
    $(`#div-num-` + (parseInt(form_idx) - 1).toString()).remove();
    $("#id_form-TOTAL_FORMS").val(parseInt(form_idx) - 1);
    if (parseInt($("#id_form-TOTAL_FORMS").val()) <= 1) {
      $("#removeit").attr('disabled', true);
    }
  } else {
    $("#removeit").attr('disabled', true);
  }

})