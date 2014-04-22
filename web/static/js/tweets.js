var n = 0;
var filter = 'none';

$(function() {
  $('div#content1').ready( function() {
		getTweets(2, 'none');
    return false;
  });
});


function getTweets(more, tfilter) {
  m = n;
	for (n ; n<(m+more); n++) {
	  $.getJSON('/_get_tweets', {
	    filter: tfilter,
	    n: n,
	  }, function(data) {
	    appendList(data.text, data.merchant, data.created)
	  });
  }
};

function appendList(text, merchant, created) {
  $('li.showMore').remove();
	$('#content1 li:last-child').after(
		  $('<li>').attr('class','tweet').append(
		      $('<a>').attr('href','/user/messages').append(
		          $('<span>').attr('class', 'text').append(text)).after().append(
		          $('<span>').attr('class', 'date').append(created)).after().append(
		          $('<span>').attr('class', 'merchant').append(merchant))
	));
	$('#content1 li:last-child').after(
		  $('<li>').attr('class','showMore').append(
		      $('<span>').append('show more')
	));
	$(".showMore").click( function()  {
  getTweets(4, filter);
	});
};

function changeFilter(nfilter) {
	$('#content1 ul li.tweet').remove()
	getTweets(5, nfilter);
};

$("#filter").click( function()  {
changeFilter('somehandle');
});
