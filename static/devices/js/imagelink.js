
$.noConflict();
jQuery( document ).ready(function( $ ) {
  var myButton = '<a class=addlink id=evandro>Patrimonio</a>';
    const valor = $('#evandro');
    $(myButton).insertAfter($('#id_tag_id').html(valor.val()));
    $('#evandro').click(function(){
     type_device = $('#id_asset_tag').val();
     $('#id_tag_id').val(type_device);
});

});