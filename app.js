console.log("hello world")

window.onload = function(){

    let slider = document.getElementById("range-slider")
    let theme_displayer = document.getElementById("theme-displayer")
    let email_button = document.getElementById("email_button") 
    let email_area = document.getElementsByClassName("email-box")[0] 
    let evidence_btn = document.getElementById("evidence-btn") 
    let evidence_img = document.getElementById("evidence-img")


    let theme = ""

    // Slider logic
    slider.addEventListener('input', function(){
        if (slider.value == "1"){
            theme_displayer.innerHTML = "Please Choose a theme"
        }
        else if (slider.value == "2"){
            theme_displayer.innerHTML = "Hospital"
            theme = "Hospital"
        }
        else if (slider.value == "3"){
            theme_displayer.innerHTML = "Sick"
            theme = "Sick"
        }
        else if (slider.value == "4"){
            theme_displayer.innerHTML = "Random" 
            theme = "Random"
        }
        else if (slider.value == "5"){
            theme_displayer.innerHTML = "Death"
            theme = "Death"
        }
    })


    // Generates email
    email_button.addEventListener('click', function(){
        //Front end logic
        $('html, body').animate({ scrollTop: $("#email-area").offset().top}, 'fast');
        email_area.classList.add("email-box-activate")
        evidence_btn.classList.add("evidence-active")

        //Back end logic


    })

    evidence_btn.addEventListener('click', function(){
        // Frontend logic
        if (theme != ""){
            $('html, body').animate({ scrollTop: $("#evidence-area").offset().top}, 'fast');
            evidence_img.classList.add("evidence-img-active")
        }


       






        // Backend logic
    })

}