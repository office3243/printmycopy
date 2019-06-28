var pages;
var bw_rate;
var color_rate;
// form upload
    $('#fileForm').submit(function(e){
        e.preventDefault();
        $form = $(this);
        var formData = new FormData(this);
        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: formData,
            success: function (response) {
                $('.error').remove();
                console.log(response);
                if(response.error){
                    formError(response.message);
                    $.each(response.errors, function(name, error){
                        error = '<small class="text-muted error">' + error + '</small>';
                        $form.find('[name=' + name + ']').after(error);

                    })
                }
                else{
                    $("#transactionForm").attr("action", ("/transactions/add/"+response.file_uuid + "/"));
                    alert(response.file_url);
                    $('#preview-btn').attr("fileUrl", response.file_url);
                    $("#transactionFormDiv").show();
                    pages = response.pages;
                    blackWhite = response.bw_rate;
                    bw_rate = response.bw_rate;
                    color_rate = response.color_rate;
                    calculateForm();
                }

            },
            cache: false,
            contentType: false,
            processData: false
        });
    });
    // end

function currentlink(element){
    defaultlink();
    document.getElementById(element).classList.add("tz-currentlink");
    displayNone();
    if(element == 'home-tab'){
        document.getElementById("home-section").style.display="block";
    }else if(element == 'upload-tab'){
        document.getElementById("upload-section").style.display="block";
    }else if(element == 'transaction-tab'){
        document.getElementById("transaction-section").style.display="block";
    }else{
        document.getElementById("account-section").style.display="block";
    }
    addingFooter();
}
function defaultlink(){
     check = document.getElementById("home-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("home-tab").classList.remove("tz-currentlink");
    }
     check = document.getElementById("upload-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("upload-tab").classList.remove("tz-currentlink");
    }
     check = document.getElementById("transaction-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("transaction-tab").classList.remove("tz-currentlink");
    }
     check = document.getElementById("account-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("account-tab").classList.remove("tz-currentlink");
    }
}
function displayNone(){
    document.getElementById("home-section").style.display="none";
    document.getElementById("upload-section").style.display="none";
    document.getElementById("transaction-section").style.display="none";
    document.getElementById("account-section").style.display="none";
}

function fileChange(){

    var allowed_types = ["jpg", "pdf", "png"];
    var input_field = document.querySelector("#file");
    file_name = input_field.files[0].name;
    if (allowed_types.includes(file_name.slice(file_name.lastIndexOf('.')+1, ))){
        $("#formErrorMessage").hide().text("");
        $("#file-input-msg").text(input_field.files[0].name);
    }
    else{
            $("#fileForm").trigger("reset");
            $("#file-input-msg").text("Choose File");
            $("#formErrorMessage").show().text("File Type Not Allowed");
    }

    // let fileName = document.querySelector('#file').value;
    // let lastIndex = fileName.lastIndexOf('.');
    // let fileExt = fileName.slice(lastIndex);
    // if(fileExt == '.pdf'){
    //     var input = document.getElementById("file");
    //     var reader = new FileReader();
    //     reader.readAsBinaryString(input.files[0]);
    //     reader.onloadend = function(){
    //         var count = reader.result.match(/\/Type[\s]*\/Page[^s]/g).length;
    //         document.querySelector("#file-input-msg-pages").innerHTML =" - " +count+ " pages";
    //         document.querySelector("#pages").innerHTML = count;
    //         getAmount();
    //     }
    // }
    // else if (fileExt == '.jpg' || fileExt == '.jpeg' || fileExt == '.png'){
    //     document.querySelector("#file-input-msg-pages").innerHTML =" - 1 page";
    //     document.querySelector("#pages").innerHTML = 1;
    //     getAmount();
    // }
    // else{
    //     //
    // }
    
    
}

function getAmount(){
    var pages =document.querySelector("#pages").innerHTML;
    var copies = document.querySelector("#copies").value;
    if(document.querySelector('#color').checked){
        document.querySelector("#amount").innerHTML = pages * rate.color * copies;
    }
    else{
        document.querySelector("#amount").innerHTML = pages * rate.blackWhite * copies;
    }
}
function changeTable(element){
    if(element.id == "printed-btn"){
        document.querySelector('#printed').style.display="block";
        document.querySelector('#not-printed').style.display="none";
        element.classList.add("tz-singlebtn-active");
        document.querySelector("#not-printed-btn").classList.remove("tz-singlebtn-active");
    }
    else{
        document.querySelector('#printed').style.display="none";
        document.querySelector('#not-printed').style.display="block";
        element.classList.add("tz-singlebtn-active");
        document.querySelector("#printed-btn").classList.remove("tz-singlebtn-active");
    }
}
function addingFooter(){
    // document.querySelector("#footer").style.display = "none";
    // document.querySelector("#footer").classList.remove("tz-footer1");
    // document.querySelector("#footer").classList.remove("tz-footer2");
    // var x = document.querySelector("body").clientHeight;
    // console.log(x);
    // x = x + 55 ;
    // var y = window.innerHeight;
    // console.log(y);
    // if(x < y){
    //     document.querySelector("#footer").classList.add("tz-footer1");
    //     document.querySelector("#footer").style.display = "block";
    // }
    // else{
    //     document.querySelector("#footer").classList.add("tz-footer2");
    //     document.querySelector("#footer").style.display = "block";
    // }
}
function calculateForm(){
    var copies = document.querySelector("#copies").value;
    var rate;
    if(document.querySelector('#color').checked){
        rate = color_rate;
    }
    else{
        rate = bw_rate;
    }
    document.querySelector("#pages").innerHTML = pages;
    document.querySelector("#amount").innerHTML = pages * rate * copies;
}
