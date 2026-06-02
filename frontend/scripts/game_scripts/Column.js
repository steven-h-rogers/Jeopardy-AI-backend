import { QuestionTile } from "./QuestionTile.js";
import { generate_random_indeces } from "../utils.js";

class Column{
    constructor(category){
        this.category = category;
        this.questionList = []; // store list of QuestionTile objects
        this.previouslyAsked = []; //store strings of previously asked topics
    }


    populateColumn(numDailyDoubles=0, startingValue=200){
        let value = startingValue;
        const daily_double_indeces = generate_random_indeces(6, numDailyDoubles);
        for (let i = 0; i<5; i++){
            if (daily_double_indeces.includes(i)){
                const question = new QuestionTile(value, true);
                this.questionList.push(question);
                value += 200;
            }
            else{
                const question = new QuestionTile(value, false);
                this.questionList.push(question);
                value += 200;
            }   
        }
    }

    setQuestionList(questionList){
        this.question_list = questionList
    }

}



export {Column}