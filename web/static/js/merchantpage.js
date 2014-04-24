//merchant page
function showpage(name) {
merchant = $.getJSON('/_get_merchant', {
	handle: name,
	}, function(data) {
		$('#shoutBlock').hide();
		$('#content1').append($('<div>').attr('id','merchpage'));
//		$('#merchpage').append($('<img>').attr('src','\"/images/icn/'+data.category+'.png\"');
		$('#merchpage').append($('<h2>').attr('class','merchtitle').append(data.name));
		$('#merchpage').append($('<span>').attr('class','merchhandle').append('@'+data.handle));
		$('#merchpage').append($('<p>').attr('class','merchdesc').append(data.description));
		$('#merchpage').append(
			$('<a>').attr('class','button back').attr('href','#').append('back').click(function() {
				$('#merchpage').remove();
				$('#shoutBlock').show();
			})
		);
	});
    return true;
};

$(function() {
	$('a.back').click(function() {

	});
});
