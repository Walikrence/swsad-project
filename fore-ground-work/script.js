$(document).ready(function(){
	$('#btn-login').click(function() {
	  var id = $("#input-id").val()
	  var password = $("#input-password").val()
	  if (id.length == 0) {
	    $("#warning").text("请填写账号！")
	  } else if (password.length == 0) {
	    $("#warning").text("请填写密码！")
	  } else {
	    var data = {
	      "account": id,
	      "password": password
	    }
	    var postData = JSON.stringify(data)
	    alert(postData)
	    var _self = this
	    $.ajax({
	      type: 'POST',
	      url: '/users/login',
	      data: postData,
	      contentType: 'application/json;charset=utf-8',
	      dataType: 'json',
	      timeout: 5000,
	      success: function(result, xhr) {
	        //
	      },
	      error: function(result, xhr) {
	        //
	      }
	    })
	  }
	});
})