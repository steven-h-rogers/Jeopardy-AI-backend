import { Table } from "./Table.js";

class Game{
    constructor(round, difficulty, table){
        this.round = round;
        this.difficulty = difficulty;
        this.table = table;
        this.numDailyDouble = 1;
    }
}

export {Game}