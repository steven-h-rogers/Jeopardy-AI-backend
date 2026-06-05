class QuestionTile{
    constructor(displayValue, realValue, isDailyDouble){
        this.displayValue = displayValue; //TODO: Inclusion of this variable breaks other code
        this.realValue = realValue;
        this.isDailyDouble = isDailyDouble;
        this.question = null; 
        this.answer = null;
        this.answered = false;
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