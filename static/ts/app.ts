const buttons = document.querySelectorAll<HTMLButtonElement>("[data-confirm]");

buttons.forEach(button => {
    button.addEventListener("click",()=>{
        const message = button.dataset.confirm;
        if(message && !window.confirm(message))
            return
    });
});