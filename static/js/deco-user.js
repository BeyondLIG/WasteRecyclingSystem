// 个人中心 - 发送手机验证码（修改手机号）
function sendCodeChangePhone($btn){
    var verify = verifyDialogSubmit(
        [
          {id: '#jsChangePhone', tips: Dml.Msg.epPhone, errorTips: Dml.Msg.erPhone, regName: 'phone', require: true}
        ]
    );
    if(!verify){
       return;
    }
    $.ajax({
        cache: false,
        type: "post",
        dataType:'json',
        url:"/user/send_phone_code/",
        data:$('#jsChangePhoneForm').serialize(),
        async: true,
        beforeSend:function(XMLHttpRequest){
            $btn.val("发送中...").show(6000);
            $btn.attr('disabled',true);
        },
        success: function(data){
            if(data.phone){
                Dml.fun.showValidateError($('#jsChangePhone'), data.email);
            }else if(data.status == 'success'){
                Dml.fun.showErrorTips($('#jsChangePhoneTips'), "手机验证码已发送");
            }else if(data.status == 'failure'){
                 Dml.fun.showValidateError($('#jsChangePhone'), "手机验证码发送失败");
            }else if(data.status == 'success'){
            }
        },
        complete: function(XMLHttpRequest){
            $btn.val("获取验证码");
            $btn.removeAttr("disabled");
        }
    });

}

// 个人中心 - 发送手机验证码(修改账号)
function sendCodeChangeAccount($btn) {
    $.ajax({
        cache: false,
        type: "post",
        dataType: 'json',
        url: "/user/send_account_code/",
        data: $('#jsChangeAccountForm').serialize(),
        async: true,
        beforeSend: function (XMLHttpRequest) {
            $btn.val("发送中...").show(6000);
            $btn.attr('disabled', true);
        },
        success: function (data) {
            if (data.email) {
                Dml.fun.showValidateError($('#jsChangeAccount'), data.email);
            } else if (data.status == 'success') {
                Dml.fun.showErrorTips($('#jsChangeAccountTips'), "手机验证码已发送");
            } else if (data.status == 'failure') {
                Dml.fun.showValidateError($('#jsChangeAccount'), "手机验证码发送失败");
            } else if (data.status == 'success') {
            }
        },
        complete: function (XMLHttpRequest) {
            $btn.val("获取验证码");
            $btn.removeAttr("disabled");
        }
    });
}


// 个人中心 - 手机号修改
function changePhoneSubmit($btn){
var verify = verifyDialogSubmit(
        [
          {id: '#jsChangePhone', tips: Dml.Msg.epPhone, errorTips: Dml.Msg.erPhone, regName: 'phone', require: true},
        ]
    );
    if(!verify){
       return;
    }
    $.ajax({
        cache: false,
        type: 'post',
        dataType:'json',
        url:"/user/update_phone/ ",
        data:$('#jsChangePhoneForm').serialize(),
        async: true,
        beforeSend:function(XMLHttpRequest){
            $btn.val("发送中...");
            $btn.attr('disabled',true);
            $("#jsChangePhoneTips").html("验证中...").show(500);
        },
        success: function(data) {
            if(data.email){
                Dml.fun.showValidateError($('#jsChangePhone'), data.email);
            }else if(data.status == "success"){
                Dml.fun.showErrorTips($('#jsChangePhoneTips'), "手机号更新成功");
                setTimeout(function(){location.reload();},1000);
            }else{
                 Dml.fun.showValidateError($('#jsChangePhone'), "手机号更新失败");
            }
        },
        complete: function(XMLHttpRequest){
            $btn.val("完成");
            $btn.removeAttr("disabled");
        }
    });
}


// 个人中心 - 修改支付宝账号
function changeAccountSubmit($btn){
    $.ajax({
        cache: false,
        type: 'post',
        dataType:'json',
        url:"/user/update_account/ ",
        data:$('#jsChangeAccountForm').serialize(),
        async: true,
        beforeSend:function(XMLHttpRequest){
            $btn.val("发送中...");
            $btn.attr('disabled',true);
            $("#jsChangeAccountTips").html("验证中...").show(500);
        },
        success: function(data) {
            if(data.email){
                Dml.fun.showValidateError($('#jsChangeAccount'), data.email);
            }else if(data.status == "success"){
                Dml.fun.showErrorTips($('#jsChangeAccountTips'), "支付宝账号更新成功");
                setTimeout(function(){location.reload();},1000);
            }else{
                 Dml.fun.showValidateError($('#jsChangeAccount'), "支付宝账号更新失败");
            }
        },
        complete: function(XMLHttpRequest){
            $btn.val("完成");
            $btn.removeAttr("disabled");
        }
    });
}


// 个人中心 - 修改密码
$(function(){
    //个人资料修改密码
    $('#jsUserResetPwd').on('click', function(){
        Dml.fun.showDialog('#jsResetDialog', '#jsResetPwdTips');
    });

    $('#jsResetPwdBtn').click(function(){
        $.ajax({
            cache: false,
            type: "POST",
            dataType:'json',
            url:"/user/update/pwd/",
            data:$('#jsResetPwdForm').serialize(),
            async: true,
            success: function(data) {
                if(data.password1){
                    Dml.fun.showValidateError($("#pwd"), data.password1);
                }else if(data.password2){
                    Dml.fun.showValidateError($("#repwd"), data.password2);
                }else if(data.status == "success"){
                    Dml.fun.showTipsDialog({
                        title:'提交成功',
                        h2:'修改密码成功，请重新登录!',
                    });
                    Dml.fun.winReload();
                }else if(data.msg){
                    Dml.fun.showValidateError($("#pwd"), data.msg);
                    Dml.fun.showValidateError($("#repwd"), data.msg);
                }
            }
        });
    });

    //个人资料头像
    $('.js-img-up').uploadPreview({ Img: ".js-img-show", Width: 94, Height: 94 ,Callback:function(){
        $('#jsAvatarForm').submit();
    }});

    // 修改手机号对话框: 在修改按钮上注册监听器，当点击修改时，弹出对话框
    $('.changephone_btn').click(function(){
        Dml.fun.showDialog('#jsChangePhoneDialog', '#jsChangePhoneTips' ,'jsChangeEmailTips');
    });
    // 修改支付宝账号对话框
    $('.changeaccount_btn').click(function () {
        Dml.fun.showDialog('#jsChangeAccountDialog', '#jsChangePhoneTips', 'jsChangeEmailTips');
    });
    // 在手机号对话框的jsChangePhoneCodeBtn按钮上添加监听器，当点击时触发sendCodeChangePhone函数（修改手机号）
    $('#jsChangePhoneCodeBtn').on('click', function(){
        sendCodeChangePhone($(this));
    });
    // 点击获取验证码时发送验证码(修改支付宝账号)
    $('#jsChangeAccountCodeBtn').on('click', function () {
        sendCodeChangeAccount($(this))
    });
    // 提交新手机号和验证码
    $('#jsChangePhoneBtn').on('click', function(){
        changePhoneSubmit($(this));
    });
    $('#jsChangeAccountBtn').on('click', function () {
        changeAccountSubmit($(this));
    });


    //input获得焦点样式
    $('.perinform input[type=text]').focus(function(){
        $(this).parent('li').addClass('focus');
    });
    $('.perinform input[type=text]').blur(function(){
        $(this).parent('li').removeClass('focus');
    });

    // verify(
    //     [
    //         {id: '#nick_name', tips: Dml.Msg.epNickName, require: true}
    //     ]
    // );

    //保存个人资料
    $('#jsEditUserBtn').on('click', function(){
        var _self = $(this),
            $jsEditUserForm = $('#jsEditUserForm')
        $.ajax({
            cache: false,
            type: 'post',
            dataType:'json',
            url: "/user/info/",
            data:$jsEditUserForm.serialize(),
            async: true,
            beforeSend:function(XMLHttpRequest){
                _self.val("保存中...");
                _self.attr('disabled',true);
            },
            success: function (data) {
                if (data.status == "failure") {
                    Dml.fun.showTipsDialog({
                        title: '保存失败',
                        h2: data.msg
                    });
                } else if (data.status == "success") {
                    Dml.fun.showTipsDialog({
                        title: '保存成功',
                        h2: '个人信息修改成功！'
                    });
                    setTimeout(function () {
                        window.location.href = window.location.href;
                    }, 1500);
                }
            },
            complete: function(XMLHttpRequest){
                _self.val("保存");
                _self.removeAttr("disabled");
            }
        });
    });


});