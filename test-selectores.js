const selectores = [
    '#user-name','#password','#login-button'
]

selectores.forEach(selector => {
    console.log(selector);
    const el = document.querySelector(selector);
    if (el){
        el.style.backgroundColor = 'red';
    }
    else{
        console.log("Error: ", selector);
    }
});