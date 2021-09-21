


$("#login_btn").on("click",function(){
    let email = $("#email").val()
    let password = $("#password").val()
    console.log(email)
    console.log(password)
    data = {
        "email":email,
        "password":password
    }
    if (email == ""){
        window.alert("Enter email")
    }
    else if(password == ""){
        window.alert("Enter password")
    }
    else{
        $.ajax({
            url: "/api/token/",
            type: 'POST',
            data: data,
            error : function(err) {
                    window.alert("Wrong Credentials")
                  },
            success: function(data) {
                console.log(data,"#####")
                localStorage.setItem('token', data.access);
                window.location.href = "/userDetails/";
            }
        })
    }
})



// $.ajax({
//   url: "http://localhost:8080/api/login/",
//   type: 'POST',
// //   data: formData,
//   error : function(err) {
//     console.log('Error!', err)
//   },
//   success: function(data) {
//     console.log('Success!')
//     console.log(data)
//     // localStorage.setItem('token', data.);
//   }
// });