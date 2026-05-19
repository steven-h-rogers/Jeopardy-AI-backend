class QuestionTile{
    constructor(value, isDailyDouble){
        this.value = value;
        this.isDailyDouble = isDailyDouble;
        this.text; 
    }


    setText(text) {
        this.text = text;
    }
}

export {QuestionTile}