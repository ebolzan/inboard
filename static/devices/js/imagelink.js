
$.noConflict();
jQuery( document ).ready(function( $ ) {
 var myButton = '<a class=addlink id=asset>Patrimonio</a>';
  var serial_number_button = '<a class=addlink id=serial>Número serial</a>';
  var htmlEle = myButton + serial_number_button;

    $(htmlEle).insertAfter($('#id_tag_id'));

    $('#asset').click(function(){
     type_device = $('#id_asset_tag').val();
     $('#id_tag_id').val(type_device);
});

   $('#serial').click(function(){
     type_device = $('#id_serial_number').val();
     $('#id_tag_id').val(type_device);
});

});