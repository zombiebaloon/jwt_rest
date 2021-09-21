
$.ajax({
    url: "/userAPI/",
    method: "GET",
    headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`},
    error : function(err) {
        $(".logout-btn").addClass("hidden")
        $("#details").html(`
        <p><b>Session Experired Login Again <a href="/" class="text-reset">Back To Login</a></p>
        `)
        localStorage.setItem('token',"")
      },
    dataType: "json",
    success: function (data) {
        console.log("success")
        console.log(data.payload)
        x = data.payload
        x.map(item =>{
            $('#details').append(`
            <tr>
            <td>${item.id}</td>
            <td>${item.first_name}</td>
            <td>${item.email}</td>
            <td>${item.username}</td>
            <td>${item.address}</td>
            <td>
            <button type="button" class="btn btn-warning btn-sm edit-data" data-sid = "${item.id}">Edit </button>
            <button type="button" class="btn btn-danger btn-sm delete-data" data-sid = "${item.id}">Delete</button>
            </td>
            </tr>
            `);

            $(".edit-data").on("click",function(){
                $("#exampleModalCenter").modal("show")
                let id = $(this).attr('data-sid');
                data_id = {
                    'id':id
                }
                $.ajax({
                    url: "/userAPI/",
                    method: "GET",
                    data : data_id,
                    headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`},
                    error : function(err) {
                        $(".modal-msg").html(`<p>Somthing Went Wrong</p>`)
                    },
                    dataType: "json",
                    success: function (data) {
                        let x = data.payload
                        console.log(x.email,"###")
                        $("#edit-email").val(x.email)
                        $("#edit-username").val(x.username)
                        $("#edit-name").val(x.first_name)
                        $("#edit-address").val(x.address)
                        $("#user_id").val(x.id)

                    }
                })
                
            })


            $(".delete-data").on("click",function(){
                let id = $(this).attr('data-sid');
                mythis = this;
                data_id = {
                    'id':id
                }
                $.ajax({
                    url: "/userAPI/",
                    method: "DELETE",
                    data : data_id,
                    headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`},
                    error : function(err) {
                        window.alert("something went wrong")
                    },
                    dataType: "json",
                    success: function (data) {
                        $(mythis).closest("tr").fadeOut();
                    }
                })
                
            })

            })



    }
})

$(".logout-btn").on('click',function(){
    localStorage.setItem("token","")
    window.location.href = "/"
})



$("#edit-save").on("click",function(){
    let id = $("#user_id").val();
    let name = $("#edit-name").val();
    let username = $("#edit-username").val();
    let address = $("#edit-address").val();
    let email = $("#edit-email").val()
    data = {
        'id':id,
        'first_name': name,
        "username": username,
        "address":address,
        "email":email
    }
    console.log(data)
    $.ajax({
        url: "/userAPI/",
        method: "PATCH",
        data : data,
        headers: {"Authorization": `Bearer ${localStorage.getItem('token')}`},
        error : function(err) {
            window.alert("something went wrong")
        },
        dataType: "json",
        success: function (data) {
            console.log(data)
            if (data.error == "error"){
                window.alert(`${data.message}`)
            }
            else{
                window.location.reload()
            }
        }
    })
})