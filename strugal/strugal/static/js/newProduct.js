$("#add_more").click(function () {
  var form_idx = $("#id_form-TOTAL_FORMS").val();

  $("#empty_form").append(
    `<p>
        <label for="id_form-` +
      parseInt(form_idx).toString() +
      `-ref">Ref:</label>
        <input
          type="text"
          name="form-` +
      parseInt(form_idx).toString() +
      `-ref"
          class="form-control"
          maxlength="255"
          id="id_form-` +
      parseInt(form_idx).toString() +
      `-ref"
        />
      </p>
      <p>
        <label for="id_form-` +
      parseInt(form_idx).toString() +
      `-qte">Qte:</label>
        <input
          type="text"
          name="form-` +
      parseInt(form_idx).toString() +
      `-qte"
          class="form-control"
          id="id_form-` +
      parseInt(form_idx).toString() +
      `-qte"
        />
      </p>
      <p>
        <label for="id_form-` +
      parseInt(form_idx).toString() +
      `-longueur">Longueur:</label>
        <input
          type="text"
          name="form-` +
      parseInt(form_idx).toString() +
      `-longueur"
          class="form-control"
          id="id_form-` +
      parseInt(form_idx).toString() +
      `-longueur"
        /><input type="hidden" name="form-` +
      parseInt(form_idx).toString() +
      `-id" id="id_form-` +
      parseInt(form_idx).toString() +
      `-id"/>
      </p>
      <button type="button" class="btn btn-link">Add Field</button>`.replace(
        /__prefix__/g,
        form_idx
      )
  );
  $("#id_form-TOTAL_FORMS").val(parseInt(form_idx) + 1);
});
