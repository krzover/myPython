// 点击li的时候触发click
$('.dropdown-menu li').click(function() {
    // $(this)  当前点击的li
    // alert($(this).text())
    var content = $(this).text()
    $('.testbtn').text(content)

})

function removemodal(id, title) {
    // 设置弹框内容
    $('#myModal  .modal-body').text('确定要删除' + title)
        // 弹出模态框
    $('#myModal').modal()
        // 根据文档写的，当提交按钮点击的时候触发
    $('.remove').on('click', function() {

        $.post(
            '/commit_delete_course', { 'id': id },
            function(res) { //请求之后触发
                // 如果返回的是success，就刷新界面
                location.reload()
            }
        )

id
    })
}

function changemodal(id, title) {
    // 设置弹框内容
    $('#kindModalLabel').text('编辑' + title)
        // 弹出模态框
    $('#kindModal').modal()
        // 根据文档写的，当提交按钮点击的时候触发
    $('.remove').on('click', function() {

        var name = $('#course_name').val()
        var abs = $('#course_abstract').val()
        var addtime = $('#course_addtime').val()
        $.post(
            '/commit_change_course', { 'id': id, 'name': name, 'abs': abs, 'addtime': addtime },
            function(res) { //请求之后触发
                // 如果返回的是success，就刷新界面
                location.reload()
            }
        )


    })
}

function addcourse(id) {
    $('#addModal').modal()
    $('.remove').on('click', function() {
        var c_title = $('#add_name').val()
        var c_abstract = $('#add_abstract').val()

        $.post('/commit_addcourse', { 'k_id': id, 'c_title': c_title, 'c_abst': c_abstract }, function(res) { location.reload() })
    })
}

