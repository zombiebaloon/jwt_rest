$("#register").on("click",function(){
    let name = $("#f_name").val();
    let username = $("#username").val();
    let address = $("#address").val();
    let email = $("#email").val()
    let password = $("#password").val()
    let password1 = $("#password1").val()
    console.log(password1,password)
    if (email == "" && username == "" && address == "" && name == "" && password == "" && password1 == ""){
        window.alert("please fill all the details")
    }
    else if( password != password1){
        window.alert("password doesn't match")
    }
    else{

    data = {
        'first_name': name,
        "username": username,
        "address":address,
        "email":email,
        "password":password
    }
    console.log(data)
    $.ajax({
        url: "/signUpAPI/",
        method: "POST",
        data : data,
        // headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`},
        error : function(err) {
            console.log("error")
            window.alert("something went wrong")
        },
        dataType: "json",
        success: function (data) {
            if (data.error == "error"){
                window.alert(`${data.message}`)
            }
            else{
            console.log("data edited ")
            window.location.href= "/"
            }
        }
    })
}
})
