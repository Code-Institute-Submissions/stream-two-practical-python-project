(() => {

    const dropDown = document.getElementById("drop-down-menu");
    const dropDownIcon = document.getElementById("drop-down-icon");
    const moreIcons = document.getElementsByClassName("mobile-more__icon");
                            // Click Element, Affected Element, Class //
    addRemoveClassOnClick(dropDownIcon, dropDown, "drop-down-menu--show");
    addRemoveClassOnClick(dropDownIcon, dropDownIcon, "mobile-more--rotate")

    for(let i = 0; i < moreIcons.length; i++ ) {
       
        addRemoveClassOnClick(dropDownIcon, moreIcons[i], "mobile-more--clicked-color");

    }
    
})();