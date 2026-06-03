import { QuestionTile } from "./QuestionTile.js";
import { generate_random_indeces } from "../utils.js";

/**
 * *NOTE: Jeopardy's rules DO NOT allow multiple daily doubles within the same categories and have a skewed distribution favoring higher value clues
 */

class Column{
    constructor(category){
        this.category = category;
        this.questionList = []; // store list of QuestionTile objects
        this.previouslyAsked = []; //store strings of previously asked topics
    }

    //TODO: allow this function to accept custom list of values for each category
    populateColumn(numDailyDoubles=0, startingValue=200){
        let value = startingValue;
        const daily_double_indeces = generate_random_indeces(6, numDailyDoubles); //TODO: Remove hardcoding of number of questions in column
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