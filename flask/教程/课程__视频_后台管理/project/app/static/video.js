// 点击li的时候触发click
$('.dropdown-menu li').click(function(){

    // alert($(this).text())
    // trim 清楚字符开始和结束这两边的空格
    var content = $.trim($(this).text())
    // alert(content)
    // input标签的value的赋值方式
    $('.teachername').attr('value',content)
    // $(this)  当前点击的li
   

})

function removemodal(id,title){
    // 设置弹框内容
    $('#myModal  .modal-body').text('确定要删除'+title)
    // 弹出模态框
    $('#myModal').modal()
    // 根据文档写的，当提交按钮点击的时候触发
    $('.remove').on('click',function(){
        
        $.post(
            '/commit_delete_course',
            {'id':id},
            function(res){//请求之后触发
                // 如果返回的是success，就刷新界面
                location.reload()
            }
            )


    })
}