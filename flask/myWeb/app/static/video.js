function changechoselabel(name) {
    console.log(name)
    $('#choselabel').val(name)
}
function deletevideo(id){
    $.post('/deletevideo', { 'id': id, }, function(res) { location.reload() })
}

function editvideo(id){
    console.log(id)
    $('#myModal').modal()
}