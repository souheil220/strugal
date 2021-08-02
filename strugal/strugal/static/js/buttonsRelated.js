var url = window.location.href
url = url.substring(30)


function wichDiv(number) {
  var option = "0"
  switch (url) {
    case "extrusion":
      option = "1"
      break;
    case "laquageBlanc":
      option = "2"
      break;
    case "laquageCouleur":
      option = "3"
      break;
    case "anodisation":
      option = "4"
      break;
    default:
      option = "5"
  }
  return `<div id='div-num-` + number + `' class="suplementaire"'style="padding-bottom: 5%;">
  <hr>
<div class="input-group">
    
      <span class="input-group-addon">Ref</span>
    
    <input
      type="text"
      name="form-` + number + `-ref"
      class="form-control"
      required="true"
      maxlength="255"
      id="id_form-` + number + `-ref"
    />
</div>
<div class="input-group">
    
      <span class="input-group-addon">Qte</span>
    
    <input
      type="number"
      name="form-` + number + `-qte"
      class="form-control"
      required="true"
      id="id_form-` + number + `-qte"
    />
</div>
<input type="hidden" name="form-` + number + `-date_created" 
id="id_form-` + number + `-date_created" 
value="` + $('#id_form-0-date_created').val() + `"
>
<select name="form-` + number + `-typeP" 
  id="id_form-` + number + `-typeP" hidden>
    <option value="` + option + `" selected>` + url + `</option>
</select>
<div class="closeButton" id='test'>
<i class='ti-trash remove'id='remove_` +
    number +
    `'></i>
</div>
</div>`
}

$("#add_more").click(function () {
  $("#removeit").attr('disabled', false);
  var form_idx = $("#id_form-TOTAL_FORMS").val();

  $(wichDiv(form_idx)).insertBefore('#turningPoint');
  $("#id_form-TOTAL_FORMS").val(parseInt(form_idx) + 1);


});

$('#empty_form').on('click', '.remove', function () {
  var form_idx = $("#id_form-TOTAL_FORMS").val();
  console.log(this.id)
  var id = this.id;
  var split_id = id.split("_");
  var deleteindex = split_id[1];

  // Remove <div> with id
  $("#div-num-" + deleteindex).remove();
  $("#id_form-TOTAL_FORMS").val(parseInt(form_idx) - 1);
});

$('#add-one-more-ex').click(function () {
  var len = $('#lenData').val()
  $('#ourTable tr:last').after(`<tr>
  <td>
    <input
      type="text"
      name="ref-` + ((parseInt(len) + 1).toString()) +
    `"
      step="any"
      class="form-control"
      id="id_ref-` + (parseInt(len) + 1).toString() + `"

      
    />
  </td>
  <td>
    <input
      type="text"
      name="obj-` + ((parseInt(len) + 1).toString()) +
    `"
      step="any"
      class="form-control"
      id="id_obj-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="prod_physique-` + ((parseInt(len) + 1).toString()) + `"
      step="any"
      class="form-control"
      required=""
      id="id_prod_physique-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="prod_conforme-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_prod_conforme-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="prod_non_conforme-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_prod_non_conforme-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="deche_geometrique-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_deche_geometrique-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="nbr_barr-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_nbr_barre-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="text"
      name="n_of-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_n_of-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="checkbox"
      name="realise-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      id="id_realise-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
</tr>`);
  $('#lenData').val((parseInt(len) + 1).toString())
})

$('#add-one-more').click(function () {
  var len = $('#lenData').val()
  $('#ourTable tr:last').after(`<tr>
  <td>
    <input
      type="text"
      name="ref-` + ((parseInt(len) + 1).toString()) +
    `"
      step="any"
      class="form-control"
      id="id_ref-` + (parseInt(len) + 1).toString() + `"   
    />
  </td>
  <td>
    <input
      type="text"
      name="obj-` + ((parseInt(len) + 1).toString()) +
    `"
      step="any"
      class="form-control"
      id="id_obj-` + (parseInt(len) + 1).toString() + `"   
    />
  </td>
  <td>
    <input
      type="number"
      name="prod_physique_p_r-` + ((parseInt(len) + 1).toString()) + `"
      step="any"
      class="form-control"
      required=""
      id="id_prod_physique_p_r-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="prod_physique-` + ((parseInt(len) + 1).toString()) + `"
      step="any"
      class="form-control"
      required=""
      id="id_prod_physique-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="prod_conforme-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_prod_conforme-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="number"
      name="prod_non_conforme-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_prod_non_conforme-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  
  <td>
    <input
      type="text"
      name="n_of-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      required=""
      id="id_n_of-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
  <td>
    <input
      type="checkbox"
      name="realise-` + (parseInt(len) + 1).toString() + `"
      step="any"
      class="form-control"
      id="id_realise-` + (parseInt(len) + 1).toString() + `"
    />
  </td>
</tr>`);
  $('#lenData').val((parseInt(len) + 1).toString())
})