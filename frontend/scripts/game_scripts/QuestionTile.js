class QuestionTile{
    constructor(value, isDailyDouble){
        this.displayValue = value; //TODO: Inclusion of this variable breaks other code
        this.realValue = value;
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
}

export {QuestionTile}