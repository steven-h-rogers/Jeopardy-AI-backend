
function getClassicCategories(number=null){
    //! DUMMY FUNCTION FOR TESTING
    //TODO: Hook this up to API endpoint
    return ["US Presidents", "Before & After", "Oscar Winners", "Book to Screen", "Homophones", "US States"]; // this will actually be an object in the form {category-liat: [...]} NOTE: should change api output key to camelCase
}

function getQuestionAndAnswer(questionPayload){
    //! DUMMY FUNCTION FOR TESTING
    //TODO: Hook this up to API endpoint
    console.log(questionPayload);
    return {"question":"While he was vacationing at his father's Vermont home, word reached him that Harding had died", "answer": "Calvin Coolidge" };
}

function getQuestionSummary(){
    //! DUMMY FUNCTION FOR TESTING
    //TODO: Hook this up to API endpoint
}

export {getClassicCategories, getQuestionAndAnswer}