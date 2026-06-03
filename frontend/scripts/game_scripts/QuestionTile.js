class QuestionTile{
    constructor(displayValue, realValue, isDailyDouble){
        this.displayValue = displayValue; //TODO: Inclusion of this variable breaks other code
        this.realValue = realValue;
        this.isDailyDouble = isDailyDouble;
        this.text = null; 
        this.answered = false;
    }

    setText(text) {
        this.text = text;
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