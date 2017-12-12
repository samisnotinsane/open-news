// app.js
image                = new Image();
image.src            = '/static/mainapp/robin.gif';
var hostname = document.location.hostname + '/';

function XHR() {
    try {
        var request = new XMLHttpRequest();
        console.log("[INFO] - XHR init successful.")
    } catch(e1) {
        request = false;
    }
    return request;
}

function populateSectionDropdown(data) {
    var menu = $( ".dropdown-menu" );
    menu.children().remove();
    $.each(data, function(index, value) {
        itemName = value.name;
        var menuItem = '<li><a href="' + 
            'sections/' +itemName.toLowerCase() + '">' + itemName + '</a></li>';
        menu.append( menuItem );    
    });
}

$(document).ready(function() {
    var ajax = new XHR();

    console.log('[INFO] - Document loaded. Welcome to OpenNews!')
    console.log('[INFO] - Hostname: [' + hostname + ']');

    var sectionDropdown = $("#dropdown-section");
    sectionDropdown.on("click", function() {
        console.log("[EVENT] - click/section-dropdown");

        var currentUrl = document.location.toString();
        console.log("[INFO] - current location: " + currentUrl);
        
        ajax.open('GET', 'api/sections/')
        ajax.onload = function() {
            if(this.readyState == 4) {
                console.log("[INFO] - XHR loaded data successfully.");

                var data = JSON.parse(ajax.responseText);
                populateSectionDropdown(data);
            }
        }

        ajax.onerror = function() { 
            console.log("[WARN] - XHR failed to load data.");
        }
        ajax.send();
    });

    

    // Populate 'Section' dropdown with topics.
    // $.getJSON("api/sections/", function(data) {
    //     $("#dropdown-section").on('click', 'a', function() {
    //         var buttonVal = $(this).html();
    //         var ul = $(".dropdown-menu").siblings();
    //         $(ul).empty();
    //         $.each(data[name], function(i, v) {
    //             $(ul).append('<li><a href="#">' + v.name + '</a></li>');
    //         var li = $(ul).children()[i];
    //         $(li).data(v);
    //         });
    //     });

    //     var sections = [];
    //     $.each(data, function(key, value) {
    //         sections.push( "<li><a href='" + value + "'>"
    //             + value + "</a></li>" );
    //     });
    //     $('.dropdown-menu', {
    //         "class": "dropdown-menu-item",
    //         html: sections.join( "" )
    //     }).appendTo( ".dropdown-menu" );
    // });

    $(".nav a").on("click", function() {
        $(".nav").find(".active").removeClass("active");
        $(this).parent().addClass("active");
    });
})
