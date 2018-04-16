addEventListener("DOMContentLoaded", function() {

    const topScores = document.getElementById("top-scores");
    const logOut = document.getElementById("log-out");
    const backToGame = document.getElementById("back-to-game");
    const playButton = document.getElementById("play");         
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

    //--------------------------- XHR ----------------------------------------//

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

    //---------------------------------------------------------------//

    const displayDashes = () => {
        // JOIN THE LIST OF DASHES MADE BY THE FUNCTION BELOW //
        word.innerHTML = dashes.join(" ");

    }

    const createDashes = (wordArray) => {
        // CREATE AN ARRAY OF DASHES BASED ON THE LENGTH OF THE GENEREATED WORD //
        dashes = [];
        for(letter = 0; letter < wordArray.length; letter++) {
            dashes.push(" _ ");
        }
        
        displayDashes();
    }



    const appendDashesWithGuess = (guessResponse) => {
        // BASED ON THE GUESS RESPONSE LIST OF CORRECT GUESSES, REPLACE THE BLANK LIST WITH RETURNED GUESS LIST //
        guessResult = guessResponse.displayGuess;
        dashes = [];
        dashes = guessResult;

        displayDashes();
        
    }

    const displayScore = (guessResponse) => {
        // DISPLAY THE RETURNED SCORE //
        score.innerHTML = guessResponse.currentScore;;

    }

    const isGameWon = (guessResponse) => {
        // RETURN BOOLEAN BASED ON GAME WIN/LOSE STATE //
        if(guessResponse.win == true) {

            return true;

        } else {

            return false;
        }
    }

    const winMessage = (guessResponse) => {
        // IF THE GAME IS WON, DISPLAY THIS MESSAGE //
        wordLength = wordArray.length; 
        const winMessageToUser = `You are correct! You get ${wordLength} points! Hit GET WORD to play again.`;
        const winLose = isGameWon(guessResponse);
        
        if (winLose == true) {

            winLoseMessage.innerHTML = winMessageToUser;

        } 
    }

    const loseMessage = (guessResponse) => {
        // BASED ON THE FAIL COUNTER, IF THE COUNTER == 1 THEN DISPLAY LOSE MESSAGE //
        const theWordWas = wordArray.join("");
        const loseMessageToUser = `You LOSE! The word was ${theWordWas}. Hit GET WORD to play again.`
    
        if (guessResponse.guessCount == 1 ) {

            winLoseMessage.innerHTML = loseMessageToUser;
        }
    }

    const setImage = (guessResponse) => {
        // SET THE IMAGE DIV ID BASED ON THE FAIL COUNTER NUMBER //
        const currentImageNumber = guessResponse.imageId;
        const currentImage = image.setAttribute("id", currentImageNumber);
        
    }

    const clearWinLoseMessage = () => {
        // CLEAR THE WIN/LOSE MESSAGE DIV //
        winLoseMessage.innerHTML = "";
    }

    const clearImage = () => {
        // CLEAR THE IMAGE DIV //
        const currentImage = image.setAttribute("id", "");

    }

    const setGuessButtonsToFalse = () => {
        // SET THE GUESS BUTTON DATA ATTRIBUTE TO FALSE, USED LATER TO STOP BUTTONS MAKING REQUESTS BEFORE A WORD IS GENERATED //
        for (let i = 0; i < guessButton.length; i++) {

            guessButton[i].setAttribute("data", false);

        }
    }

    const setGuessButtonsToLetter = () => {
        // SETS THE DATA ATTRIBUTE TO THE LETTER STORED IN THE VALUE ATTRIBUTE, READY FOR DATA TO BE SENT TO THE SERVER //
        for (let i = 0; i < guessButton.length; i++) {

            let letter = guessButton[i].value;
            guessButton[i].setAttribute("data", letter);

        }
    }

    const stopScoreSummingOnWin = (guessResponse) => {
        // STOPS DATA BEING SENT ONCE THE GAME HAS BEEN WON, STOPS THE SCORE COUNTER SUMMING //
        const result = isGameWon(guessResponse); 

        if (result == true) {

            setGuessButtonsToFalse();

        } else if (result == false) {

            setGuessButtonsToLetter();

        } 
    
    }

    const stopSelectionsOnLoss = (guessResponse) => {

        if (guessResponse.guessCount == 1 ) {

            setGuessButtonsToFalse();
        }
    }
    
    //----------------- UI STYLE FUNCTIONS ------------------------//


   const mouseDownUp = (documentElement, className) => {

        documentElement.addEventListener("mousedown", () => {
            
            documentElement.classList.add(className);
     
        });

        documentElement.addEventListener("mouseup", () => {
            
            documentElement.classList.remove(className);
       
        });

    }

    const removeGuessButtonClickedStyle = () => {

        for (let i = 0; i < guessButton.length; i++){

            guessButton[i].classList.remove("guess-form__button--clicked");

        }

    }

    const addStyleOnClick = (documentElement, className) => {

        documentElement.classList.add(className);
    }

    //----------------- RESETS ---------------------------//

    setGuessButtonsToFalse(); // DEFAULT DATA ATTRIBUTE VALUE SET TO FALSE //

    //----------------- XHR REQUESTS ---------------------//

    generate.addEventListener("click", function() {
        
        setGuessButtonsToLetter();
        removeGuessButtonClickedStyle();

        // RETRIEVE WORD FROM SERVER AS JSON //
        getRequest(`/${username}/word`)
            .then((response) => {

                let wordRequest = JSON.parse(response);
                wordArray = wordRequest.guessWord;
                createDashes(wordArray);
                clearWinLoseMessage();
                clearImage();
                //console.log(wordArray);

            })
            .catch((error) => {

                console.log(error);
            })
                    
    });

    
    for (let i = 0; i < guessButton.length; i++){
    
        guessButton[i].addEventListener("click", function(e) {

            e.preventDefault();
            let guess_data = this.getAttribute('data');

            if ((guess_data != "false") && (this.classList.contains("guess-form__button--clicked") == false)) {

                this.classList.add("guess-form__button--clicked");

                // RETRIEVE GAME REPSONSE DATA AS JSON //
                postRequest(`/${username}/${guess_data}`, guess_data)
                    .then((response, guess_data) => {
                        
                        let guessResponse = JSON.parse(response);
                        
                        appendDashesWithGuess(guessResponse);
                        displayScore(guessResponse);
                        winMessage(guessResponse);
                        loseMessage(guessResponse);
                        setImage(guessResponse);
                        stopScoreSummingOnWin(guessResponse);
                        stopSelectionsOnLoss(guessResponse);
                        
                    })
                    .catch((error) => {

                        console.log(error)

                    })
                }
        });
    }

    //----------------------------- UI STYLING -------------------------//

    mouseDownUp(generate, "generate__button--clicked");
    addStyleOnClick(playButton,"input-form__button--clicked");
    addStyleOnClick(logOut,"input-form__button--clicked");
    addStyleOnClick(topScores,"input-form__button--clicked");
    addStyleOnClick(backToGame,"nav__back-to-game-link--clicked");
    
   
});

