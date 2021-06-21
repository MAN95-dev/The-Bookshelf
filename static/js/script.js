// Flash messages //
var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
        var div = this.parentElement;
        div.style.opacity = "0";
        setTimeout(function () { div.style.display = "none"; }, 600);
    };
}
// End of Flash messages //

/* Login / Registration page */
$("#signup").click(function () {
    $("#first").fadeOut("fast", function () {
        $("#second").fadeIn("fast");
    });
});

$("#signin").click(function () {
    $("#second").fadeOut("fast", function () {
        $("#first").fadeIn("fast");
    });
});

$(function () {
    $("form[name='login']").validate({
        rules: {
            username: {
                required: true,
                username: true
            },
            password: {
                required: true,
            }
        },
        messages: {
            email: "Please enter a valid email address",
            password: {
                required: "Please enter password",
            }
        },
        submitHandler: function (form) {
            form.submit();
        }
    });
});

$(function () {
    $("form[name='registration']").validate({
        rules: {
            firstname: "required",
            lastname: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 5
            }
        },

        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            email: "Please enter a valid email address"
        },

        submitHandler: function (form) {
            form.submit();
        }
    });
});
/* End of Login / Registration page */
