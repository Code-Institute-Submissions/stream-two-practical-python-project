addEventListener("DOMContentLoaded", function() {
        
    const generate = document.getElementById("generate");
    const guessButton = document.getElementsByClassName("guess-form__button");
    const guessForm = document.getElementById("guess-form");
    const username = document.getElementById("generate").value;
    //const wordRequestDiv = document.getElementById("word-request");
    const guessRequestDiv = document.getElementById("guess-request");

    const word = document.getElementById("word"); 
    const score = document.getElementById("score");
    let word_array = "";
    let dashes = [];
   // let guessInput = document.getElementById("guess-letter-{{ letter }}");
   // guessInput.value = "";
    //let data = guessInput;

    //------------------------- FUNCTION DECLARATIONS ------------------------//

    const getRequest = (url) => {

        return new Promise((resolve, reject) => {

            const xhr = new XMLHttpRequest();

            xhr.open("GET",url, true)
           // xhr.responseType = "json";
            xhr.onload = function() {
        
                if (xhr.readyState == 4 && xhr.status == 200) { 
                    //template(JSON.parse(this.responseText));
                    //console.log(this.responseText)
                    const response = xhr.responseText;
                    resolve(response)
                    //console.log(response);
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
                    //console.log(xhr.responseText);
                } else {
                    const error = xhr.responseText;
                    reject(error)
                }
            };
            
            xhr.send(guess_data)
            console.log(guess_data);
        })

    }

    const displayDashes = () => {

        word.innerHTML = dashes.join(" ");

    }

    const displayDashes = (wordArray) => {

        dashes = [];
        for(letter = 0; letter < wordArray.length; letter++) {
            dashes.push(" _ ");
        }
        
        joinDashes();
       
    }

    const appendDashesWithGuess = (guessResponse) => {

        guessResult = guessResponse.displayGuess;
        dashes = [];
        dashes = guessResult;
        
    }

    const displayScore = (guessResponse) => {

        score = guessResponse.currentScore;


    }

    //----------------- XHR REQUESTS ---------------------//

    generate.addEventListener("click", function() {
        
        getRequest(`/${username}/word`)
            .then((response) => {

                wordArray = JSON.parse(response);//wordRequestDiv.innerHTML = response;
                
                displayDashes(wordArray);

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
                    
                    let guessResponse = JSON.parse(response);

                    appendDashesWithGuess(guessResponse);
                 
                })
                .catch((error) => {

                    console.log(`unsuccessful post ${error}`)

                })
            
        });
    }
   
});

