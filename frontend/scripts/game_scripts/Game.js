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

    setQuestionAndAnswer(columnIndex, rowIndex, questionText, answerText){
        const questionTile = this.table.columns[columnIndex].questionList[rowIndex];
        questionTile.setQuestion(questionText);
        questionTile.setAnswer(answerText);
    }

    getQuestionPayload(columnIndex, rowIndex){
        //QuestionTile related
        const questionTile = this.table.columns[columnIndex].questionList[rowIndex];
        let realValue = questionTile.realValue;
        let isDailyDouble = questionTile.isDailyDouble;

        //Game related
        let round = this.round;
        let difficulty = this.difficulty;

        //Column Related
        let category = this.table.columns[columnIndex].category;
        let previouslyAsked = this.table.columns[columnIndex].previouslyAsked;

        //in snake case to make it compatible with api endpoint
        return {"category": category, "difficulty": difficulty, "value": realValue, "round": round, "is_daily_double": isDailyDouble, "previous_answers_in_category": previouslyAsked};
    }

    //! currently for debugging. Not sure if frontend should work with classes or if classes should simply return any relevant data
    getQuestionTile(columnIndex, rowIndex){
        const questionTile = this.table.columns[columnIndex].questionList[rowIndex];
        return questionTile;
    }
}

export {Game}