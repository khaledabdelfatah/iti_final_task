function validateUserName(){
if(document.querySelector("#uname").value==""){
document.getElementById("unameinvalid").innerHTML
="PLEASE ENTER YOUR USERNAME *IT'S REQUIRED*";
}
}

// VALIDATE PASSWORD
function validatePassword(){
    if(document.querySelector("#pwd").value==""){
    document.getElementById("pwdinvalid").innerHTML
    ="PLEASE ENTER YOUR PASSWORD *IT'S REQUIRED* ";
    }
    }