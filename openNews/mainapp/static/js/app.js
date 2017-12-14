// app.js
image                = new Image();
image.src            = '/static/mainapp/robin.gif';
var hostname = document.location.hostname + '/';
var ajax = new XHR();

var sectionNames = [];

function handleLogin() {
    console.log("[EVENT] - click/handleLogin");
    
    var usr = $('#usernameLogin');
    var pwd = $('#passwordLogin');
    
    $.post("/api/login/",
        {
            Username: usr,
            Password: pwd
        },
        function(data, status) {
            console.log('[INFO] - data: [ ' + data + ' ], status [' + status + ' ]');
        }
    );

    return false;
}

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
    $.each(data, function(index, value) {
        itemName = value.name;
        var menuItem = '<li><a href="' + 
            'sections/' +itemName.toLowerCase() + '">' + itemName + '</a></li>';
        menu.append( menuItem );    
    });
}

function handleSectionDropdown() {
    var sectionDropdown = $("#dropdown-section");
    // Event handler for section dropdown (nav-bar).
    sectionDropdown.on("click", function() {
        console.log("[EVENT] - click/section-dropdown");
        // Only query API if not already loaded.
        if(sectionNames.length == 0) {
            ajax.open('GET', '/api/sections/');
            ajax.onload = function() {
                if(this.readyState == 4) {
                    console.log("[INFO] - XHR loaded data successfully.");
                    sectionNames = JSON.parse(ajax.responseText);
                    populateSectionDropdown(sectionNames);
                }
            }
            ajax.onerror = function() { 
                console.log("[WARN] - XHR failed to load data.");
            }
            ajax.send();
        }
    });
}

function showArticle() {
    var title = $(".blog-post-title");
    var section = $("#article-section");


}

function likeArticle() {
    var thumbsUpBtn = $(".fa-thumbs-up");
    console.log("[EVENT] - click/likeArticle");
    // get article number
    // 
}

function dislikeArticle() {
    var thumbsDownBtn = $(".fa-thumbs-down");
    console.log("[EVENT] - click/dislikeArticle");
}

$(document).ready(function() {
    
    console.log('[INFO] - Document loaded. Welcome to OpenNews!')
    console.log('[INFO] - Hostname: [' + hostname + ']');

    handleSectionDropdown();
    showArticle();

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
