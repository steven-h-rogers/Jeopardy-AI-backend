
import { baseURL } from "./constants.js";


async function getClassicCategories(number=6){
    const payload = {
        num_categories: number
    };

    try {
        const response = await fetch(`${baseURL}/category-generator/generate-categories/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok){
            throw new Error(`Server responded with status: ${response.status}`);
        }
        const data = await response.json();

        const categories = data['category-list'];
        console.log(categories);
        return categories;

    } catch (error) {
        console.error('Category Generation Failed:', error);
    }
}

async function getQuestionAndAnswer(questionPayload){

    try {
        const response = await fetch(`${baseURL}/question-generator/generate-question/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(questionPayload)
        });

        if (!response.ok){
            throw new Error(`Server responded with status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Question Generation Failed: ', error);
    }
     
}

async function getQuestionSummary(questionText){
    //! DUMMY FUNCTION FOR TESTING
    //TODO: Hook this up to API endpoint

    const response = await fetch(`${baseURL}`)

}

getClassicCategories(7);


export {getClassicCategories, getQuestionAndAnswer, getQuestionSummary}

