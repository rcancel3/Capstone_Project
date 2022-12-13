var socket = io.connect('http://' + document.domain + ':' + location.port + '/');

// if #comment clicked then
$('#submit_button').click(function() {
    // ignore default action
    event.preventDefault();
    
    text = $('#review_text').val();
    socket.emit('is_this_food_related', { text: text });
});


socket.on('is_this_food_related', function(msg) {
    if (msg.is_food_related) {
        $('.w-form-fail').css('display', 'block');
        $('.w-form-done').css('display', 'none');
        

    } else {
        $('.w-form-fail').css('display', 'none');
        $('.w-form-done').css('display', 'block');
    }
});