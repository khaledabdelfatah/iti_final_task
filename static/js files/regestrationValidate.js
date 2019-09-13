function IsValidForName(){
    if(document.getElementById("name").value==" "){
     document.getElementById("namecheck2").innerHTML="&&Make Sure To Enter A VaLue";
    }
    var regex = /^[A-Za-z0-9 ]+$/;
var isValid = regex.test(document.getElementById("name").value);

if(document.getElementById("name").
value.length>3&&isValid
){
document.getElementById("namecheck1")
.hidden=true;
document.getElementById("name").
style.backgroundColor="white";

}
else{

    
    document.getElementById("namecheck1")
.hidden=false;
 
 
}


}
// END OF NAME;

function validateEmail() {

    if (document.getElementById("email").value == ""
     ) {
        document.getElementById("emailcheck1").innerHTML
        ="Please Enter Your Email *Required";
        
     }

}

// END OF EMAIL

function IsValidForUsername(){
    var regex = /^[A-Za-z0-9 ]+$/;
var isValid = regex.test(document.getElementById("name").value);
if(document.
    getElementById("address".value==" ")){
document.getElementById("usernamecheck2")
.innerHTML="Make Sure That You Enter a Value";

}
if(document.getElementById("address").
value.length>3&&isValid
){
document.getElementById("usernamecheck1")
.hidden=true;
document.getElementById("address").
style.backgroundColor="white";
}
else{

   
    document.getElementById("usernamecheck1")
.hidden=false;


document.getElementById("usernamecheck1")
.style.fontSize="12px";
}


}
// END OF USER NAME

function chckpasswoed(){
    var strongRegex = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
if(document.getElementById("password").value.length>7){
    document.getElementById("passwordcheck1")
    .innerHTML="GREAT!";
    document.getElementById("passwordcheck1").style.color="green";

}
else{
    document.getElementById("passwordcheck1")
    .innerHTML="Make Sure to type a strong password *more than 7 litters ";
    document.getElementById("passwordcheck1").style.color="red";
}
}


// 
function confirmvalidate(){
if(
document.getElementById("confirm").value != 
document.getElementById("password").value
 ){
document.getElementById("confirmcheck1")
.innerHTML="Make sure its same as password 1";
document.getElementById("confirmcheck1")
.style.color="red";

}


}

// START SUBMIT
function finalsubmit(){
    var regex = /^[A-Za-z0-9 ]+$/;

var checkStatus=true;
    var isValid = regex.test
    (document.getElementById("name")
    .value);
   
    var isValid3 = regex.test
    (document.getElementById("address")
    .value);


//Name

if(document.getElementById("name").value==" "){
    document.getElementById("namecheck2").innerHTML="&&Make Sure To Enter A VaLue";
   }
   var regex = /^[A-Za-z0-9 ]+$/;
var isValid = regex.test(document.getElementById("name").value);

if(document.getElementById("name").
value.length>3&&isValid
){
document.getElementById("namecheck1")
.hidden=true;
document.getElementById("name").
style.backgroundColor="white";

}
else{

   document.getElementById("namecheck1")
.hidden=false;


}
//
//EMail
if (document.getElementById("email").value == ""
) {
   document.getElementById("emailcheck1").innerHTML
   ="Please Enter Your Email *Required";
   checkStatus=false;
   
}
//
// Username
if(document.
    getElementById("username".value==" ")){
document.getElementById("usernamecheck2")
.innerHTML="Make Sure That You Enter a Value";
checkStatus=false;

}
if(document.getElementById("username").
value.length>3&&isValid3
){
document.getElementById("usernamecheck1")
.hidden=true;
document.getElementById("address").
style.backgroundColor="white";
}
else{

    checkStatus=false;
   
    document.getElementById("usernamecheck1")
.hidden=false;


document.getElementById("usernamecheck1")
.style.fontSize="12px";
}
// 
// password
if(document.getElementById("password").value.length>7){
    document.getElementById("passwordcheck1")
    .innerHTML="GREAT!";
    document.getElementById("passwordcheck1").style.color="green";

}
else{
    checkStatus=false;

    document.getElementById("passwordcheck1")
    .innerHTML="Make Sure to type a strong password *more than 7 litters ";
    document.getElementById("passwordcheck1").style.color="red";
}
// 
// Confirm pass
if(
    document.getElementById("confirm").value != 
    document.getElementById("password").value
    ){
    checkStatus=false;
 
        document.getElementById("confirmcheck1")
    .innerHTML="Make sure its same as password 1";
    document.getElementById("confirmcheck1")
    .style.color="red";
    
}
// 

if(checkStatus==true){
    if(confirm("By Continue you Agree To share your info with US!")){

        document.getElementById("wentWrong").innerHTML
        ="Data SENT";
    }
    else{
        alert("YOU HADE TO FINISH YOUR QUIRES");
        document.getElementById("wentWrong").innerHTML
        ="OoOoh Sorry ,Something went Wrong ,please Refresh the page and try again ";
    }
}
////////////////////////////////////////////////////////////////////////////////
if(checkStatus==true){

}

















}
