$('.dropdown-menu li').click(function(){

    $('.teacher_name').attr('value',$.trim($(this).text()))

})




function removemodel(id,name){
    $('#myModal .modal-body').text('点击确定将删除'+name)
    $('#myModal').modal()
    $('#myModal .commit').on('click',function(){
        $.post(
            '/delete_teacher',
            {'id':id},
            function(res){
                if (res=='success'){
                    location.reload()
                }
                else { 
                    alert(res)
                }
            }
            )
    // location.reload()
})
}

