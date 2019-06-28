var rate = {
    "blackWhite" : 1,
    "color" : 5
}
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

function fileChange(element){
    document.querySelector("#file-input-msg").innerHTML =   element.files[0].name;
    let fileName = document.querySelector('#file').value;
    let lastIndex = fileName.lastIndexOf('.');
    let fileExt = fileName.slice(lastIndex);
    if(fileExt == '.pdf'){
        var input = document.getElementById("file");
        var reader = new FileReader();
        reader.readAsBinaryString(input.files[0]);
        reader.onloadend = function(){
            var count = reader.result.match(/\/Type[\s]*\/Page[^s]/g).length;
            document.querySelector("#file-input-msg-pages").innerHTML =" - " +count+ " pages";
            document.querySelector("#pages").innerHTML = count;
            getAmount();
        }
    }
    else if (fileExt == '.jpg' || fileExt == '.jpeg' || fileExt == '.png'){
        document.querySelector("#file-input-msg-pages").innerHTML =" - 1 page";
        document.querySelector("#pages").innerHTML = 1;
        getAmount();
    }
    else{
        //
    }
    
    
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
    document.querySelector("#footer").style.display = "none";
    document.querySelector("#footer").classList.remove("tz-footer1");
    document.querySelector("#footer").classList.remove("tz-footer2");
    var x = document.querySelector("body").clientHeight;
    console.log(x);
    x = x + 55 ;
    var y = window.innerHeight;
    console.log(y);
    if(x < y){
        document.querySelector("#footer").classList.add("tz-footer1");
        document.querySelector("#footer").style.display = "block";
    }
    else{
        document.querySelector("#footer").classList.add("tz-footer2");
        document.querySelector("#footer").style.display = "block";
    }
}