$(function () {


    $('#subButton').on('click', function () {
         console.log('登录');
        temp1 = checkingAccount();//账户验证匹配返回结果
        temp2 = checkingPassword();
        if ( temp1 && temp2 ){
            $('.login form').submit()
        }
    });
    function checkingAccount() {
        // 数字、字母、下划线
        var reg = /^[A-Za-z0-9_]+$/;   //设置正则匹配规范
        var account_input = $('#account input');
        if (reg.test(account_input.val())) {  // 测试账户中的值是否符合正则
            $('#account i').html('');
            $('#account').removeClass('has-error').addClass('has-success');
            $('#account span').removeClass('glyphicon-remove').addClass('glyphicon-ok');

            return true

        } else {    // 不符合
            $('#account i').html('账号由数字、字母组成');
            $('#account').removeClass('has-success').addClass('has-error');
            $('#account span').removeClass('glyphicon-ok').addClass('glyphicon-remove');

            return false
        }
    }

    function checkingPassword() {
        // 数字
        var reg = /^[\d]{6,12}$/;
        var passwordInput = $('#password input');
        if (reg.test(passwordInput.val())) {  // 符合
            $('#password i').html('');
            $('#password').removeClass('has-error').addClass('has-success');
            $('#password span').removeClass('glyphicon-remove').addClass('glyphicon-ok');
            return true
        } else {    // 不符合
            $('#password i').html('6~12位纯数字');
            $('#password').removeClass('has-success').addClass('has-error');
            $('#password span').removeClass('glyphicon-ok').addClass('glyphicon-remove');
            return false
        }
    }
})