(() => {

const backToGame = document.getElementById("back-to-game");
const logOut = document.getElementById("log-out");  

const addStyleOnClick = (documentElement, className) => {

    documentElement.addEventListener("click", () => {

        documentElement.classList.add(className);

    });
}

addStyleOnClick(backToGame,"nav__back-to-game-link--clicked");
addStyleOnClick(logOut,"input-form__button--clicked");

})();