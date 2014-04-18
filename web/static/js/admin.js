$(function() {
  $('a#merchsubmit').bind('click', function() {
    $.getJSON('/admin/_add_merchant', {
      name: $('input[name="merchname"]').val(),
      tagline: $('input[name="merchtag"]').val(),
      twitterhandle: $('input[name="merchhand"]').val()
    }, function(data) {
      $("#merchreturn").text(data.result);
    });
    return false;
  });
});

//ON CHANGE
$(function() {
    $('#caticon').change(function() {
        var form_data = new FormData($('#catform')[0]);
        $.ajax({
            type: 'POST',
            url: '/admin/_preview_category',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                var value = 'url(\''+data['success']+'\')';
                console.log(value);
                $('div#catpic').css('background-image', value);
            },
        });
    });
});


//ON SUBMIT
$(function() {
	  $('#catsubmit').click(function() {
        var form_data = new FormData($('#catform')[0]);
        $.ajax({
            type: 'POST',
            url: '/admin/_add_category',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
            		if (!data['success']) {
            				console.log('Failed: ' + data['error']);
            		} else {
            		    console.log('Category Added');
            		}
            },
        });
	  });
});

$('a#merchant_list').click( function() {
	$('div#adminMenu').css('display','none');
	$('a#back').css('display','inline');
	$('#listMerchant').css('display','block');
});

$('a#category_list').click( function() {
	$('div#adminMenu').css('display','none');
	$('a#back').css('display','inline');
	$('#listCategory').css('display','block');
});

$('a#merchant_menu').click( function() {
	$('div#adminMenu').css('display','none');
	$('a#back').css('display','inline');
	$('#newMerchant').css('display','block');
});

$('a#category_menu').click( function() {
	$('div#adminMenu').css('display','none');
	$('a#back').css('display','inline');
	$('#newCategory').css('display','block');
});

$('a#back').click( function() {
	$('div#listMerchant').css('display','none');
	$('div#listCategory').css('display','none');
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

