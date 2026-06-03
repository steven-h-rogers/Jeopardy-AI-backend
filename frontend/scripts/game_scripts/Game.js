import { Table } from "./Table.js";

class Game{
    constructor(round=1, difficulty='medium'){
        this.round = round;
        this.difficulty = difficulty;
        this.table = null; //list of columns
        this.numDailyDouble = 1;
        //TODO: add UserPlayer and BotPlayer information
    }

    initializeGame(categoryList, numDailyDoubles){
        this.table = new Table();
        this.table.initializeTable(categoryList, numDailyDoubles);
    }


    getQuickplayCategories(){
        //TODO: Hook this up to the actual API eventually
        return ["US Presidents", "Before & After", "US States", "Homophones", "Book to Screen", "Oscar Winners"]; //temp just for testing
    }

    getCustomCategories(numCategories){
        //TODO: Hook this up to the actual API eventually
        return []; 
    }

    updateQuestionTileText(columnIndex, rowIndex, text){
        const questionTile = this.table.columns[columnIndex].questionList[rowIndex];
        questionTile.setText(text);
    }

    updateQuestionTileAnswered(columnIndex, rowIndex, answered){
        const questionTile = this.table.columns[columnIndex].questionList[rowIndex];
        questionTile.setAnswered(answered);
    }

}






export {Game}