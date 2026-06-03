import * as constants from "./constants.js";
import { SaveManager } from "./game_scripts/SaveManager.js";
import { Game } from "./game_scripts/Game.js";
import { getClassicCategories } from "./APIManager.js";

// game state should be stored in a JSON primarily so that the game board can be re-rendered after 
// every question, but also so that a user could come back to their game later if they wanted



const saveManager = new SaveManager();
const game = new Game();
saveManager.setGame(game);

const quickplayButton = document.querySelector("#quickplay-classic");
quickplayButton.addEventListener('click',()=>{
setGameQuickplayScreen();
} );
console.log(quickplayButton);



//used to set the everything-container to the game selection screen
function setGameSelectionScreen(){
    const everythingContainer = document.querySelector("#everything-container");
    everythingContainer.replaceChildren();

    const classicHeader = document.createElement("h2");
    classicHeader.textContent = "Classic";

    const quickplayButton = document.createElement("button");
    quickplayButton.textContent = "Quickplay";
    quickplayButton.id = "quickplay-classic-button";

    everythingContainer.append(classicHeader, quickplayButton);
}


function setGameQuickplayScreen(){
    game.initializeGame(getClassicCategories(6), 1);
    const everythingContainer = document.querySelector("#everything-container");
    everythingContainer.replaceChildren();

    console.log(game);
}


