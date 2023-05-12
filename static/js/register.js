const show = document.getElementById('show');
const emailField = document.getElementById('email');
const password = document.getElementById('password');
const usernameField = document.getElementById('username');
const usernameError = document.getElementById('usernameerror');
const emailError = document.getElementById('emailerror');
const button = document.getElementById('button')
const passwordField = document.getElementById('password');
const passwordError = document.getElementById('passworderror');
const usernamed = usernameField.value.length
const emaillength = emailField.value.length
const formbutton = document.getElementById('sendEmail')


console.log(formbutton)




show.addEventListener('click', function(){
    if(show.innerHTML == 'Show'){
       password.type='text';
       show.innerHTML = 'Hide'

    }else{
        password.type='password';
        show.innerHTML = 'Show';
    }
})



if(usernamed > 0){
    // console.log('True')
    // console.log(usernamed)
    fetch("validate-username",{
        body: JSON.stringify({username: usernameField.value}),
        method: "POST",
    })
    .then(res=>res.json())
    .then(data=>{
    console.log('data', data)

    if(data.username_error){
        usernameField.style.borderColor="rgb(255, 14, 14)";
        // usernameField.style.color="rgb(255, 14, 14)"
        // usernameField.style.border="3px solid maroon";
        console.log(data.username_error);
        usernameError.innerText = data.username_error;
        usernameError.style.display="inline-block";
        button.disabled=true;
    }else{
        // usernameField.style.border="1px solid #cccccc";
        usernameError.style.display="none";
        usernameField.style.color=""
        usernameField.style.border="1px solid #cccccc";
    }
    if(usernameField.id != 'error' && emailField.id != 'error' && passwordValue.length > 6){
        button.disabled=false;
    };
});
}


if(emaillength > 0){
    // console.log('True')
    fetch("validate-email",{
        body: JSON.stringify({email: emailField.value}),
        method: "POST",
    })
    .then(res=>res.json())
    .then(data=>{
    console.log('data', data)

    if(data.email_error){
        emailField.style.borderColor="rgb(255, 14, 14)";
        console.log(data.email_error);
        emailError.innerText = data.email_error;
        emailError.style.display="inline-block";
        button.disabled=true;

    }else{
        emailField.style.border="1px solid #cccccc";
        emailError.style.display="none";
        emailField.style.color=""
    }
    if(usernameField.id != 'error' && emailField.id != 'error' && passwordValue.length > 6){
        button.disabled=false;
    };
});
}

email.addEventListener("keyup", (e)=>{
    const emailVal = e.target.value;
    if (emailVal.length > 0){
        fetch("validate-email", {
            body: JSON.stringify({email:emailVal}),
            method: "POST",
        })
        .then(res=>res.json())
        .then(data=>{
        console.log('data', data)
        if(data.email_error){
            emailField.style.borderColor="rgb(255, 14, 14)";
            emailField.setAttribute('id', 'error')
            console.log(emailField.id)
            // usernameField.style.color="rgb(255, 14, 14)"
            emailError.innerText = data.email_error;
            emailError.style.display="inline-block";
            button.disabled=true;
            console.log(emailField.id)
        }else{
            emailField.style.border="1px solid #cccccc";
            emailError.style.display="none";
            emailField.setAttribute('id', 'email')
            console.log(emailField.id)
        if(usernameField.id != 'error' && emailField.id != 'error' && passwordValue.length > 6){
            button.disabled=false;
        };
  
}
    });
}
});


passwordField.addEventListener("keyup", (e) =>{
    const passwordValue = e.target.value
    if (passwordValue.length >0){
        fetch("validate-password",{
            body: JSON.stringify({password: passwordValue}),
            method: "POST",
        })
        .then(res=>res.json())
        .then(data=>{
        console.log('data', data)
        if(data.password_error){
            passwordField.style.border="1px solid rgb(255, 14, 14)";
            // passwordField.style.color="maroon";
            console.log(data.password_error);
            passwordError.innerText = data.password_error;
            passwordError.style.display="inline-block";
            button.disabled=true;
        }else{
            console.log(data.password_valid)
            passwordField.style.border="1px solid #cccccc";
            passwordError.style.display="none";
            // passwordField.style.color="";
        if(usernameField.id != 'error' && emailField.id != 'error' && passwordValue.length > 6){
            button.disabled=false;
        };
        }
        });
    }
    });
        
    



usernameField.addEventListener("keyup", (e) =>{
    const usernameVal = e.target.value;
    if (usernameVal.length > 0){
        fetch("validate-username",{
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        })
        .then(res=>res.json())
        .then(data=>{
        console.log('data', data)

        if(data.username_error){
            usernameField.style.borderColor="rgb(255, 14, 14)";
            // usernameField.style.color="rgb(255, 14, 14)"
            console.log(data.username_error);
            usernameField.setAttribute('id', 'error')
            console.log(usernameField.id);
            usernameError.innerText = data.username_error;
            usernameError.style.display="inline-block";
            button.disabled=true;
            console.log(usernameField.id)
        }else{
            usernameField.setAttribute('id', 'username')
            console.log(usernameField.id)
            usernameField.style.border="1px solid #cccccc";
            usernameError.style.display="none";
            console.log(usernameField.id)
        if(usernameField.id != 'error' && emailField.id != 'error' && passwordValue.length > 6){
                button.disabled=false;
        };
//             usernameField.style.color="";  
}
    });
}
});
// console.log(usernameField.id != 'username');

console.log(usernameField.id)
console.log(emailField.id)







