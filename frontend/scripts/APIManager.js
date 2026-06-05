
import { baseURL } from "./constants.js";


async function getClassicCategories(number=null){
    //! DUMMY FUNCTION FOR TESTING
    //TODO: Hook this up to API endpoint
    const categories = ["US Presidents", "Before & After", "Oscar Winners", "Book to Screen", "Homophones", "US States"]; // this will actually be an object in the form {category-liat: [...]} NOTE: should change api output key to camelCase
    return categories;
}

async function getQuestionAndAnswer(questionPayload){
    //! DUMMY FUNCTION FOR TESTING
    //TODO: Hook this up to API endpoint
    console.log(questionPayload);
    return {"question":"While he was vacationing at his father's Vermont home, word reached him that Harding had died", "answer": "Calvin Coolidge" };
}

async function getQuestionSummary(questionText){
    //! DUMMY FUNCTION FOR TESTING
    //TODO: Hook this up to API endpoint

    const response = await fetch(`${baseURL}`)

}



export {getClassicCategories, getQuestionAndAnswer, getQuestionSummary}