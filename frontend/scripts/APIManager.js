
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

async function getJudgement(judgePayload){
    try {
        const response = await fetch(`${baseURL}/judge/judge-answer/`,{
            method: 'POST', 
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify(judgePayload)
        });

        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Judgment Generation Failed: ', error);
    }
}

async function getQuestionSummary(questionText){
    const summaryPayload = {question: questionText};

    try{
        const response = await fetch(`${baseURL}/summarizer/summarize-question/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(summaryPayload)
        });

        if (!response.ok){
            throw new Error(`Server responded with status ${response.status}`);
        }
            const data = await response.json();
            console.log(data);
            return data;
        
    } catch (error) {
        console.error('Summary Generation Failed: ', error);
    }

}

async function getTopicExtraction(questionText){
    const topicPayload = {question: questionText};

    try {
        const response = await fetch(`${baseURL}/summarizer/extract-topic/`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(topicPayload)
        });

        if (!response.ok){
            throw new Error(`Server responded with status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Topic Extraction Failed: ', error);
    }
}

getQuestionSummary('Born in the tiny Vermont village of Plymouth Notch on July 4, 1872, he is the only U.S. president born on Independence Day.');
getTopicExtraction('Born in the tiny Vermont village of Plymouth Notch on July 4, 1872, he is the only U.S. president born on Independence Day.');

// ! fix judgement prompts so that incorrect answers are marked as so
getJudgement({question: 'Born in the tiny Vermont village of Plymouth Notch on July 4, 1872, he is the only U.S. president born on Independence Day.', answer: 'Who is Calvin Coolidge', provided_answer: 'Who is Calvin Coolidge'});
getJudgement({question: 'Born in the tiny Vermont village of Plymouth Notch on July 4, 1872, he is the only U.S. president born on Independence Day.', answer: 'Who is Teddy Roosevelt', provided_answer: 'Who is Calvin Coolidge'});
getJudgement({question: 'Born in the tiny Vermont village of Plymouth Notch on July 4, 1872, he is the only U.S. president born on Independence Day.', answer: 'Calvin Coolidge', provided_answer: 'Who is Calvin Coolidge'});


export {getClassicCategories, getQuestionAndAnswer, getQuestionSummary, getJudgement, getTopicExtraction}

