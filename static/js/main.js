addEventListener("DOMContentLoaded", function() {
        
    const generate = document.getElementById("generate");
    const guessButton = document.getElementsByClassName("guess-form__button");
    const guessForm = document.getElementById("guess-form");
    const username = document.getElementById("generate").value;
    const word = document.getElementById("word"); 
    const score = document.getElementById("score");
    const winLoseMessage = document.getElementById("result-message");
    const image = document.getElementsByClassName("image__image")[0];
    let word_array = [];
    let dashes = [];


    //------------------------- FUNCTION DECLARATIONS ------------------------//

    const getRequest = (url) => {

        return new Promise((resolve, reject) => {

            const xhr = new XMLHttpRequest();

            xhr.open("GET",url, true)
            xhr.onload = function() {
        
                if (xhr.readyState == 4 && xhr.status == 200) { 

                    const response = xhr.responseText;
                    resolve(response)
               
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
             
                    const response = xhr.responseText;
                    resolve(response, guess_data)
                  
                } else {
                    const error = xhr.responseText;
                    reject(error)
                }
            };
            
            xhr.send(guess_data)
          
        })

    }

    const displayDashes = () => {

        word.innerHTML = dashes.join(" ");

    }

    const createDashes = (wordArray) => {

        dashes = [];
        for(letter = 0; letter < wordArray.length; letter++) {
            dashes.push(" _ ");
        }
        
        displayDashes();
       
    }

    const appendDashesWithGuess = (guessResponse) => {

        guessResult = guessResponse.displayGuess;
        dashes = [];
        dashes = guessResult;

        displayDashes();
        
    }

    const displayScore = (guessResponse) => {

        score.innerHTML = guessResponse.currentScore;;

    }

    const isGameWon = (guessResponse) => {

        if(guessResponse.win == true) {

            return true;

        } else {

            return false;
        }
    }

    const winMessage = (guessResponse) => {

        wordLength = wordArray.length; 
        const winMessageToUser = `You are correct! You get ${wordLength} points!`;
        const winLose = isGameWon(guessResponse);
        
        if (winLose == true) {

            winLoseMessage.innerHTML = winMessageToUser;

        } 
    }

    const loseMessage = (guessResponse) => {

        const theWordWas = wordArray.join("");
        const loseMessageToUser = `You LOSE! The word was ${theWordWas}. Hit GET WORD to play again.`
    
        if (guessResponse.guessCount == 1 ) {

            winLoseMessage.innerHTML = loseMessageToUser;
        }
    }

    const setImage = (guessResponse) => {

        const currentImageNumber = guessResponse.imageId;
        const currentImage = image.setAttribute("id", currentImageNumber);
        
    }

    const clearWinLoseMessage = () => {

        winLoseMessage.innerHTML = "";
    }

    const clearImage = () => {

        const currentImage = image.setAttribute("id", "");

    }

    const setGuessButtonsToFalse = () => {

        for (let i = 0; i < guessButton.length; i++) {

            guessButton[i].setAttribute("data", false);

        }
    }

    const setGuessButtonsToLetter = () => {

        for (let i = 0; i < guessButton.length; i++) {

            let letter = guessButton[i].value;
            guessButton[i].setAttribute("data", letter);

        }
    }

    const stopScoreSummingOnWin = (guessResponse) => {

        const result = isGameWon(guessResponse); 

        if (result == true) {

            setGuessButtonsToFalse();

        } else if (result == false) {

            setGuessButtonsToLetter();

        } 
    
    }
    
  
    //----------------- XHR REQUESTS ---------------------//

    generate.addEventListener("click", function() {
        
        getRequest(`/${username}/word`)
            .then((response) => {

                wordArray = JSON.parse(response);
                createDashes(wordArray);
                clearWinLoseMessage();
                clearImage();

            })
            .catch((error) => {

                console.log(error);
            })
                    
    });

    
    for (let i = 0; i < guessButton.length; i++){
    
        guessButton[i].addEventListener("click", function(e) {

            e.preventDefault();
            let guess_data = this.getAttribute('data');
            
            
            if (guess_data != false) {
                postRequest(`/${username}/${guess_data}`, guess_data)
                    .then((response, guess_data) => {
                        
                        let guessResponse = JSON.parse(response);
                        
                        appendDashesWithGuess(guessResponse);
                        displayScore(guessResponse);
                        winMessage(guessResponse);
                        loseMessage(guessResponse);
                        setImage(guessResponse);
                        stopScoreSummingOnWin(guessResponse);
                        
                    })
                    .catch((error) => {

                        console.log(error)

                    })
                }
        });
    }
   
});

