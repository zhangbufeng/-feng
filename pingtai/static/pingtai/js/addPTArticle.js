$=django.jQuery
$(function () {
    $("#id_c").on("change",function () {
        $.ajax({
            url:'/pingtai/getKeyword/',
            type:'post',
            data:{"c":$(this).val()},
            success:function (e) {
                $("#id_k>option").detach()
                let str=""
                for(i in e){
                    str+=`<option value='${i}'>${e[i]}</option>`
                }
                $("#id_k").html(str)
            }
        })
    })
})