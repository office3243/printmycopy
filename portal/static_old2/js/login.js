
function currentlink(element){
    defaultlink();
    document.getElementById(element).classList.add("tz-currentlink");
    document.getElementById("forget-section").style.display="none";
    if(element == 'login-tab'){
        document.getElementById("login-section").style.display="block";
        document.getElementById("sign-up-section").style.display="none";
    }
    else{
        document.getElementById("sign-up-section").style.display="block";
        document.getElementById("login-section").style.display="none";
    }
    addingFooter();
}
function defaultlink(){
    
     var check = document.getElementById("login-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("login-tab").classList.remove("tz-currentlink");
    }
     check = document.getElementById("sign-up-tab").classList.contains("tz-currentlink");
    if(check == true){
        document.getElementById("sign-up-tab").classList.remove("tz-currentlink");
    }  
}
function forgetPassword(element){
    defaultlink();
    document.getElementById("sign-up-section").style.display="none";
    document.getElementById("login-section").style.display="none";
    document.getElementById("forget-section").style.display="block";
    addingFooter();
}
function addingFooter(){
    document.querySelector("#footer").style.display = "none";
    document.querySelector("#footer").classList.remove("tz-footer1");
    document.querySelector("#footer").classList.remove("tz-footer2");
    var x = document.querySelector("body").clientHeight;
    x = x + 55 ;
    var y = window.innerHeight;
    if(x < y){
        document.querySelector("#footer").classList.add("tz-footer1");
        document.querySelector("#footer").style.display = "block";
    }
    else{
        document.querySelector("#footer").classList.add("tz-footer2");
        document.querySelector("#footer").style.display = "block";
    }
}