function validateUserName(){
    var username = document.getElementById("username");
    var namePattern = /^[A-Za-z0-9]+$/;
    var uname = document.getElementById("username").value
    var name_length=uname.length;
    if(username.value.match(namePattern)){
        if(name_length<30){
            return true;
        }
        else{
            alert("First_name length is too high");
            document.getElementById("username").value="";
            return false;
        }
    }
    else
    {
        alert("Invalid Username")
        document.getElementById("username").value="";
        return false;
    }

}

function validateFName(){
    var first_name=document.getElementById("first_name");
    var namePattern = /^[A-Za-z]+$/;
    var fname=document.getElementById("first_name").value;
    var fname_length=fname.length;
    if(first_name.value.match(namePattern)){
        if(fl<30){
            return true;
        }
        else{
            alert("First_name length is too high");
            document.getElementById("first_name").value="";
            return false;
        }
    }
    else
    {
        alert("Invalid First_Name")
        document.getElementById("first_name").value="";
        return false;
    }
}

function validateLName(){
    let ln=document.getElementById("last_name");
    let namePattern = /^[A-Za-z]+$/;
    let lname=document.getElementById("last_name").value;
    let ll=lname.length;
    if(ln.value.match(namePattern)){
        if(ll<30){
            return true;
        }
        else{
            alert("Last_name length is too high");
            document.getElementById("last_name").value="";
            return false;
        }
    }
    else
    {
        alert("Invalid Last_Name")        
        document.getElementById("last_name").value="";
        return false;
    }
}

function valEmail(){
    let e=document.getElementById("email");
    let namePattern = /^[A-Za-z0-9.&*+/=?^_-]+@[a-zA-Z]+(.[a-z])*$/;
    if(e.value.match(namePattern)){
        return true;
    }
    else{
        alert("Enter correct email");
        document.getElementById("email").value="";
        return false;
    }
}

function con_number(){
    let c_number=document.getElementById("contact_number");
    let numPattern = /^[0-9]+$/;
    let num=document.getElementById("contact_number").value;
    let ml=num.length;
    if(c_number.value.match(numPattern)){
        if(ml==10){
            return true;
        }
        else{
            alert("Enter valid Contact number");
            document.getElementById("contact_number").value="";
            return false;
        }
    }
    else
    {
        alert("Enter Valid Phone_number");
        document.getElementById("contact_number").value="";
        return false; 
    }
}

function val_password(){
    let password = document.getElementById("password").value;
    let password_len = password.length;
    if(password_len>=8){
        return true;
    }
    else{
        alert("Enter Minimum 8 Characters for Password 😊")
    }
}
