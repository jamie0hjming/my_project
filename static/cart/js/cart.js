$(function () {
//单个
    total()  //调用js即计算总价
    $('.cart .confirm-wrapper').click(function () {
        var $cartid = $(this).attr('cartid')
        var $that = $(this)



        $.get('/changecartstatus/', {'cartid':$cartid},function (response) {
            console.log(response.mes)
            if (response.status == 1){
                var isselect = response.isselect
                console.log(isselect)
                $that.attr('isselect', isselect)
                $that.children().remove()   // 清空
                if (isselect){
                    $that.append('<span class="glyphicon glyphicon-ok"></span>')
                } else {
                    $that.append('<span class="no"></span>')
                }

                // 总计
                total()
            }
        })


    })

    // 全选/取消
    $('.cart .all').click(function () {
        var isselect = $(this).attr('isselect')
       // 将 isselect转化为布尔型
        isselect = (isselect == 'false') ? true : false
        $(this).attr('isselect', isselect)


        if (isselect){
            $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
        } else {
            $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
        }

        $.get('/changecartselect/', {'isselect':isselect}, function (response) {
            console.log(response)
            if (response.status == 1){
                // 遍历
                $('.confirm-wrapper').each(function () {
                    $(this).attr('isselect', isselect)
                    // 如果为true对应数据库中的true，删除xx，添加沟

                    if (isselect){
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    } else {
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                })

                // 总计
                total()
            }
        })
    })



    // 总计 计算总价格
    function total() {
        var sum = 0

        // 遍历操作
        $('.goods').each(function () {
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')
            if ($confirm.find('.glyphicon-ok').length) {
                var price = $content.find('.price').attr('price')
                var num = $content.find('.num').attr('num')
                sum += price * num
                console.log(sum)
            }
        })

        // 显示
        $('.bill .total b').html(parseInt(sum))
    }


    // 下单
    $('#generateorder').click(function () {
        $.get('/generateorder/', function (response) {
            if (response.status == 1){  // 跳转到订单详情

                console.log(response.msg)
                window.open('/order/'+response.identifier +
                '/', target='_self')
            }
        })
    })








})