import * as constants from "./constants";
import { SaveManager } from "./game_scripts/SaveManager";
import { Game } from "./game_scripts/Game";

// game state should be stored in a JSON primarily so that the game board can be re-rendered after 
// every question, but also so that a user could come back to their game later if they wanted


const saveManager = new SaveManager();
const game = new Game();

saveManager.setGame(game);



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
    return null;
}


