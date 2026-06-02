class QuestionTile{
    constructor(value, isDailyDouble){
        this.value = value;
        this.isDailyDouble = isDailyDouble;
        this.text = null; 
    }

    setText(text) {
        this.text = text;
    }
}

export {QuestionTile}