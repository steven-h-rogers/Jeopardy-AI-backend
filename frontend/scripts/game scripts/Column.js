import { QuestionTile } from "./QuestionTile.js";

class Column{
    constructor(category, questionList){
        this.category = category;
        this.question_list = questionList;
        this.previouslyAsked = []; //store strings of previously asked topics
    }
}

export {Column}