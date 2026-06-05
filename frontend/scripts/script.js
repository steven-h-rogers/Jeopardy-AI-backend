import * as constants from "./constants.js";
import { SaveManager } from "./game_scripts/SaveManager.js";
import { Game } from "./game_scripts/Game.js";
import { getClassicCategories, getQuestionAndAnswer } from "./APIManager.js";

// game state should be stored in a JSON primarily so that the game board can be re-rendered after 
// every question, but also so that a user could come back to their game later if they wanted



const saveManager = new SaveManager();
const game = new Game();
saveManager.setGame(game);

// default initialization to prompt the user to select a game mode
// currently, the only allowed game mode is classic quickplay
const quickplayButton = document.querySelector("#quickplay-classic");
quickplayButton.addEventListener('click',()=>{
setGameQuickplayScreen();
} );
console.log(quickplayButton);


// used to set the everything-container to the game selection screen
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


// set the current gameboard to a new classic game
function setGameQuickplayScreen(){
    game.initializeGame(getClassicCategories(6), 1);
    const everythingContainer = document.querySelector("#everything-container");
    everythingContainer.replaceChildren();
    renderGameBoard();

}

// render the current loaded game board
function renderGameBoard(){
    const everythingContainer = document.querySelector("#everything-container");
    const gameTable = document.createElement("table");
    gameTable.id = "game-table";

    let rowIndex = 0;
    let table = game.table;
    let numRows = table.columns[0].questionList.length; // TODO: there's definitely a cleaner way to do this

    while (rowIndex<=numRows){
        const tableRow = document.createElement("tr");
        for (let i=0;i<table.columns.length;i++){ //col index
                if (rowIndex===0){
                    const header = document.createElement("th");
                    header.textContent = table.columns[i].category;
                    header.id = `col${i}-category`;
                    tableRow.append(header);
                }
                else{
                    const tableData = document.createElement("td");
                    tableData.textContent = table.columns[i].questionList[rowIndex-1].displayValue;
                    tableData.id = `col${i}-q${rowIndex}`;
                    tableData.class = "question-tile";
                    
                    tableData.addEventListener('click', (event)=>{ //TODO: create a separate function outside of this one to improve readability
                        const cell = event.target.closest("td");
                        if (!cell) return;

                        const row = cell.parentElement;
                        const columnIndex = cell.cellIndex;
                        const rowIndex = row.rowIndex -1; // -1 to account for index mismatch between table and questionList

                        const questionPayload = game.getQuestionPayload(columnIndex, rowIndex);
                        const questionAndAnswer = getQuestionAndAnswer(questionPayload);

                        //update questionTile through game object
                        game.setQuestionAndAnswer(columnIndex, rowIndex, questionAndAnswer.question, questionAndAnswer.answer);

                        console.log(game);

                        //render questionScene
                        renderQuestionScene(game.getQuestionTile(columnIndex, rowIndex));
                    });
                    tableRow.append(tableData);
                } 
        }
        gameTable.append(tableRow);
        rowIndex++;
    }
    everythingContainer.append(gameTable);
}

//TODO: add a function to show the answer if incorrect
function renderQuestionScene(questionTile){
    const everythingContainer = document.querySelector("#everything-container");
    everythingContainer.replaceChildren();

    const timerBar = document.createElement("div");
    timerBar.id = "timer-bar";

    const questionCard = document.createElement("div");

    const question = document.createElement("h1");
    question.textContent = questionTile.question;

    const inputDiv = document.createElement("div");
    inputDiv.id = "input-div";

    const answerInput = document.createElement("input");
    answerInput.id = "answer-input";
    answerInput.type = "text";

    const submitButton = document.createElement("button");
    submitButton.textContent = "Submit"; //maybe change to an arrow character in the future for simplicity and aesthetic

    inputDiv.append(answerInput, submitButton);
    questionCard.append(question, inputDiv);
    everythingContainer.append(timerBar, questionCard);

}

