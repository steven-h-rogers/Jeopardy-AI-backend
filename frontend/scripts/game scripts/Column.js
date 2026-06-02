import { QuestionTile } from "./QuestionTile.js";
import { generate_random_indeces } from "../utils.js";

class Column{
    constructor(category){
        this.category = category;
        this.questionList = [];
        this.previouslyAsked = []; //store strings of previously asked topics
    }


    populateColumn(numDailyDoubles){
        let value = 200;
        daily_double_indeces = generate_random_indeces(6, numDailyDoubles);
        for (i = 0; i<=6; i++){
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