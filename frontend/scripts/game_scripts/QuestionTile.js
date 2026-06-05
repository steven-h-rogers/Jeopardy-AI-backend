class QuestionTile{
    constructor(displayValue, realValue, isDailyDouble){
        this.displayValue = displayValue; //TODO: Inclusion of this variable breaks other code
        this.realValue = realValue;
        this.isDailyDouble = isDailyDouble;
        this.question = null; //text representing the question
        this.answer = null; //text representing the actual answer
        this.userAnswer = null; //text that the user entered as the answer
        this.answered = false; //boolean to mark whether the question has been answered or not
    }

    setQuestion(text) {
        this.question = text;
    }

    setAnswer(text){
        this.answer = text;
    }

    setAnswered(answered){
        this.answered = answered;
    }

    setRealValue(realValue){
        this.realValue = realValue;
    }

    setDisplayValue(displayValue){
        this.displayValue = displayValue;
    }
}

export {QuestionTile}