

$(document).ready(function(){
    $('#signupform').validate({
        rules: {
           firstname:"required",
           lastname:"required",
           owners:"required",
           email:"required",
           password: {
            required: true,
            minlength: 5,
           },
           conpassword:{
            required: true,
            minlength: 5,
            equalTo: '[name="password"]'
           },
        },
        messages: {
           firstname: "Please enter a valid Firstname",
           lastname:"Please enter a valid Lastname",
           owners:"Please choose a valid Role",
           email:"Please enter a valid Email",
           password:{
            required:"please enter a valid Password",
            minlength:"password should be 5 characters"
           },
           conpassword:{
            required:"please enter a valid Confirm Password",
            minlength:"password should be 5 characters",
            equalTo: "Password and Confirm Password should be equal"
           }
        }
    });
});

