$(document).ready(function() {
    $('#event_announcement').click().change();
    var jVal = {
        'fullname' : function() {
            $('body').append('<div id="nameInfo" class="info"></div>');

            var nameInfo = $('#nameInfo');
            var ele = $('#fullname');
            var pos = ele.offset();
            
            nameInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+15
            });
            
            if (ele.val().length < 1) {
                jVal.errors = true;
                nameInfo.removeClass('correct').addClass('error').html('&larr; enter your full name').show();
                ele.removeClass('normal').addClass('wrong');
            } else {
                nameInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }
        },
        'headline' : function() {
            $('body').append('<div id="headlineInfo" class="info"></div>');

            var headlineInfo = $('#headlineInfo');
            var ele = $('#headline');
            var pos = ele.offset();
            
            headlineInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+15
            });
            
            if (ele.val().length < 1) {
                jVal.errors = true;
                headlineInfo.removeClass('correct').addClass('error').html('&larr; required').show();
                ele.removeClass('normal').addClass('wrong');
            } else {
                headlineInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }
        },
        'website' : function() {
            $('body').append('<div id="websiteInfo" class="info"></div>');

            var websiteInfo = $('#websiteInfo');
            var ele = $('#website');
            var pos = ele.offset();
            
            websiteInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+15
            });
            
            //var patt = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/i;
            
            var patt = new RegExp(
                        "^(http|https|ftp)\://([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$");
            
            if (!patt.test(ele.val())) {
                jVal.errors = true;
                websiteInfo.removeClass('correct').addClass('error').html('&larr; enter a valid link').show();
                ele.removeClass('normal').addClass('wrong');
            } else {
                websiteInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }
        },
        'location' : function() {
            $('body').append('<div id="locationInfo" class="info"></div>');

            var locationInfo = $('#locationInfo');
            var ele = $('#location');
            var pos = ele.offset();
            
            locationInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+15
            });
            
            if (ele.val().length < 1) {
                jVal.errors = true;
                locationInfo.removeClass('correct').addClass('error').html('&larr; required').show();
                ele.removeClass('normal').addClass('wrong');
            } else {
                locationInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }

        },
        'email' : function() {
            $('body').append('<div id="emailInfo" class="info"></div>');

            var emailInfo = $('#emailInfo');
            var ele = $('#email');
            var pos = ele.offset();
            
            emailInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+15
            });
            
            var patt = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/i;
            
            if(!patt.test(ele.val())) {
                jVal.errors = true;
                emailInfo.removeClass('correct').addClass('error').html('&larr; type in a valid email address').show();
                ele.removeClass('normal').addClass('wrong');
            } else {
                emailInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }
        },
        'starts' : function() {
            $('body').append('<div id="startsInfo" class="info"></div>');

            var startsInfo = $('#startsInfo');
            var ele = $('#starts');
            var pos = ele.offset();
            
            startsInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+40
            });
            
            var patt = /^(0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])[-](19|20)\d\d.*$/i;
            
            if(!patt.test(ele.val())) {
                jVal.errors = true;
                startsInfo.removeClass('correct').addClass('error').html('&larr; select a date').show();
                ele.removeClass('normal').addClass('wrong');
            } else {
                startsInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }
        },
        'ends' : function() {
            $('body').append('<div id="endsInfo" class="info"></div>');

            var endsInfo = $('#endsInfo');
            var ele = $('#ends');
            var pos = ele.offset();
            
            endsInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+40
            });
            
            var patt = /^(0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])[-](19|20)\d\d.*$/i;
            
            if(!patt.test(ele.val())) {
                jVal.errors = true;
                endsInfo.removeClass('correct').addClass('error').html('&larr; select a date').show();
                ele.removeClass('normal').addClass('wrong');
            } else {
                endsInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }
        },
        'details' : function() {
            $('body').append('<div id="detailsInfo" class="info"></div>');

            var detailsInfo = $('#detailsInfo');
            var ele = $('#details');
            var pos = ele.offset();
            
            detailsInfo.css({
                top: pos.top-3,
                left: pos.left+ele.width()+15
            });
            
            if (ele.val().length < 1) {
                jVal.errors = true;
                detailsInfo.removeClass('correct').addClass('error').html('&larr; required').show();
                ele.removeClass('normal').addClass('wrong');
            } else if (ele.val().length > 500) {
                 jVal.errors = true;
                 detailsInfo.removeClass('correct').addClass('error').html('&larr; enter less than 500 characters').show();
                 ele.removeClass('normal').addClass('wrong');
            } else {
                detailsInfo.removeClass('error').addClass('correct').html('&radic;').show();
                ele.removeClass('wrong').addClass('normal');
            }
        },
        'sendIt': function() {
            if (!jVal.errors) {
                $('#jform').submit();
            }
        },
    };

// ====================================================== //
    
    $('#send').click(function() {
        var obj = $.browser.webkit ? $('body') : $('html');
        obj.animate({ scrollTop: $('#jform').offset().top }, 750, function() {
            jVal.errors = false;
            jVal.fullname();
            jVal.email();
            jVal.details();
            jVal.starts();
            jVal.headline();
            jVal.website();
            
            if ($('#event_announcement').attr("checked") != "undefined" &&
                $('#event_announcement').attr("checked")) {
                jVal.location();
            }

            jVal.sendIt();
        });
        return false;
    });
    
    // bind jVal.fullName function to "Full name" form field
    $('#fullname').change(jVal.fullname);
    $('#email').change(jVal.email);
    $('#details').change(jVal.details);
    $('#starts').change(jVal.starts);
    $('#starts').click(jVal.starts);
    $('#starts').focus(jVal.starts);
    $('#headline').change(jVal.headline);
    $('#website').change(jVal.website);
    $('#location').change(jVal.location);


    $('#event_announcement').change(function() {
        $('#location_section').show();
        $('#locationInfo').show();
        $('#location').val('');
        $('#starts_label').text('Starts:');
        $('.info').remove();
    });
    $('#submission_deadline').change(function() {
        $('#location_section').hide();
        $('#locationInfo').hide();
        $('#location').val('');
        $('#starts_label').text('Deadline:');
        $('.info').remove();
    });
});

