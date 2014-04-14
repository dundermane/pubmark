$(function() {
  $('a#submit').bind('click', function() {
    $.getJSON('/admin/_add_merchant', {
      name: $('input[name="name"]').val(),
      tagline: $('input[name="tagline"]').val(),
      twitterhandle: $('input[name="handle"]').val()
    }, function(data) {
      $("#result").text(data.result);
    });
    return false;
  });
});


$('a#merchant_list').click( function() {
	$('div#adminMenu').css('display','none');
	$('a#back').css('display','block');
	$('#listMerchant').css('display','block');
});

$('a#merchant_menu').click( function() {
	$('div#adminMenu').css('display','none');
	$('a#back').css('display','block');
	$('#newMerchant').css('display','block');
});

$('a#category_menu').click( function() {
	$('div#adminMenu').css('display','none');
	$('a#back').css('display','block');
	$('#newCategory').css('display','block');
});

$('a#back').click( function() {
	$('div#listMerchant').css('display','none');
	$('div#newMerchant').css('display','none');
	$('div#newCategory').css('display','none');
	$('a#back').css('display','none');
	$('#adminMenu').css('display','block');
});

$(function() {
	$('a#save').bind('click', function() {
	//send this
	}, function(data) {
	//do this
	});
});

