(() => {

const playButton = document.getElementById("play");      

const addStyleOnClick = (documentElement, className) => {

    documentElement.addEventListener("click", () => {

        documentElement.classList.add(className);

    });
}

addStyleOnClick(playButton,"input-form__button--clicked");

})();