addEventListener("DOMContentLoaded", function() {
        
    const generate = document.getElementById("generate");
    const guessButton = document.getElementsByClassName("guess-button");
    const guessForm = document.getElementById("guess-form");
    const username = document.getElementById("generate").value;
    const wordRequestDiv = document.getElementById("word-request");
    const guessRequestDiv = document.getElementById("guess-request");
    
   // let guessInput = document.getElementById("guess-letter-{{ letter }}");
   // guessInput.value = "";
    //let data = guessInput;

    const getRequest = (url) => {

        return new Promise((resolve, reject) => {

            const xhr = new XMLHttpRequest();

            xhr.open("GET",url, true)
            xhr.responseType = "text";
            xhr.onload = function() {
        
                if (xhr.readyState == 4 && xhr.status == 200) { 
                    //template(JSON.parse(this.responseText));
                    const response = xhr.responseText;
                    resolve(response)
                    console.log(xhr.responseText);
                } else {
                    const error = xhr.responseText;
                    reject(error)
                }
            };
            
            xhr.send()  
        })
    }
    
    const postRequest = (url, guess_data) => {

        return new Promise((resolve, reject) => {

            const xhr = new XMLHttpRequest();
            
            xhr.open("POST", url, true)
            xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded")
            xhr.responseType = "text";
            xhr.onload = function() {
        
                if (xhr.readyState == 4 && xhr.status == 200) { 
                    //template(JSON.parse(this.responseText));
                    const response = xhr.responseText;
                    
                    resolve(response, guess_data)
                    console.log(xhr.responseText);
                } else {
                    const error = xhr.responseText;
                    reject(error)
                }
            };
            
            xhr.send(guess_data)
            console.log(guess_data);
        })

    }

    generate.addEventListener("click", function() {
        
        getRequest(`/${username}/word`)
            .then((response) => {
                wordRequestDiv.innerHTML = response;
            })
            .catch((error) => {

                console.log(`Could not get file ${error}`)
            })
                    
    });

    
    for (let i = 0; i < guessButton.length; i++){
    
        guessButton[i].addEventListener("click", function(e) {

            e.preventDefault();
            let guess = this.getAttribute('data');
            let guess_data = guess;

            postRequest(`/${username}/${guess_data}`, guess_data)
                .then((response, guess_data) => {
                    
                    guessRequestDiv.innerHTML = response;
                    console.log(`successful post of ${response} ${guess_data}`)

                })
                .catch((error) => {

                    console.log(`unsuccessful post ${error}`)

                })
            
        });
    }
   
});

