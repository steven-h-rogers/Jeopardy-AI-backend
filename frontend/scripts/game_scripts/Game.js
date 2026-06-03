import { QuestionTile } from "./QuestionTile.js";
import { Table } from "./Table.js";

class Game{
    constructor(round=1, difficulty='medium'){
        this.round = round;
        this.difficulty = difficulty;
        this.table = null; //list of columns
        this.numDailyDouble = 1;
        // TODO: add information about player and bots
    }

    initializeGame(categoryList, numDailyDoubles){
        this.table = new Table();
        this.table.initializeTable(categoryList, numDailyDoubles);
    }

    setNumDailyDouble(number){
        this.numDailyDouble = number;
    }

    askQuestion(columnIndex, rowIndex){
        //QuestionTile related
        const questionTile = this.table.columns[columnIndex].questionList[rowIndex];
        let value = questionTile.value;
        let isDailyDouble = questionTile.isDailyDouble;

        //Game related
        let round = this.round;
        let difficulty = this.difficulty;

        //Column Related
        let category = this.table.columns[columnIndex].category;
        let previouslyAsked = this.table.columns[columnIndex].previouslyAsked;

        //TODO: add actual api call to get the question and answer.
    }
}

export {Game}