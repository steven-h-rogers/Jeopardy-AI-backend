import { Table } from "./Table.js";

class Game{
    constructor(round=1, difficulty='medium'){
        this.round = round;
        this.difficulty = difficulty;
        this.table = null; //list of columns
        this.numDailyDouble = 1;
        // add information about player and bots
    }

    initializeGame(categoryList, numDailyDoubles){
        this.table = new Table();
        this.table.initializeTable(categoryList, numDailyDoubles);
    }
}

function getQuickplayCategories(){
    //TODO: Hook this up to the actual API eventually
    return ["US Presidents", "Before & After", "US States", "Homophones", "Book to Screen", "Oscar Winners"]; //temp just for testing
}

function getCustomCategories(numCategories){
    //TODO: Hook this up to the actual API eventually
    return []; 
}

export {Game}