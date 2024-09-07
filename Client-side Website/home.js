

window.addEventListener("DOMContentLoaded", (Event) => {

    console.log("home.js loaded!");

    const loginButton = document.getElementById("loginbutton");
    const emailField = document.getElementById("emailfield");
    const passwordField = document.getElementById("passwordfield");
    const warningText = document.getElementById("warningText");
    

    loginButton.addEventListener("click", function(){
       
        async function LoginAttempt() {
            let res = await fetch("http://127.0.0.1:8000/login/", {
                method : "POST",
                body : JSON.stringify({
                    email: emailField.value,
                    password: passwordField.value
                }),
                headers:{
                    "Content-type":"application/json"
                    
                }
            });
            let result = await res.json();
            result = JSON.stringify(result)
            // console.log(result);
            

            if(result==='{"message":"CREDENTIALS VALID"}'){
                console.log("Credentials Correct")
            }else{
                console.log("Credentials Incorrect")
                warningText.style.visibility = "visible";
            };
        }
        

        LoginAttempt();




        
    });





})

