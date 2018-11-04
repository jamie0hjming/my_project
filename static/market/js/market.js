$(function () {

    //侧边栏， $(this).index 获取所点击的节点为同级节点位置的第几个，然后将该值存放到cookie中
    $('.type-item').click(function () {
        $.cookie('type_index', $(this).index(), {expires: 3, path: '/'})
    });

    type_index = $.cookie('type_index');

    console.log(type_index);

    if (type_index > 0) { // 已经有点击分类
        console.log('AAAAAAA');
        $('.type-slider .type-item').eq(type_index).addClass('active').siblings().removeClass('active')
    } else {    // 没有点击分类
        // 没有点击默认第一个
        console.log(type_index);
        $('.type-slider .type-item:first').addClass('active').siblings().removeClass('active')
    }
    // 分类按钮
    category_button = false ; // 默认是隐藏
    $('#category_button').click(function () {
        // 取反
        category_button = !category_button;

        category_button ? category_view_show() : category_view_hide()

    });


    // 排序按钮
    sort_button = false; // 默认是隐藏
    $('#sort_button').click(function () {
        // 取反
        sort_button = !sort_button;

        sort_button ? sort_view_show() : sort_view_hide()
    });

    // 灰色蒙层
    $('.bounce-view').click(function () {
        sort_button = false;
        sort_view_hide();
        category_button = false;
        category_view_hide()
    })


    function category_view_show() {
        sort_button = false;
        sort_view_hide();
        $('.bounce-view.category-view').show();
        $('#category_button i').removeClass('glyphicon-triangle-top').addClass('glyphicon-triangle-bottom')
    }

    function category_view_hide() {
        $('.bounce-view.category-view').hide();
        $('#category_button i').removeClass('glyphicon-triangle-bottom').addClass('glyphicon-triangle-top')
    }

    function sort_view_show() {
        category_button = false;
        category_view_hide();
        $('.bounce-view.sort-view').show();
        $('#sort_button i').removeClass('glyphicon-triangle-top').addClass('glyphicon-triangle-bottom')
    }

    function sort_view_hide() {
        $('.bounce-view.sort-view').hide();
        $('#sort_button i').removeClass('glyphicon-triangle-bottom').addClass('glyphicon-triangle-top')
    }


})