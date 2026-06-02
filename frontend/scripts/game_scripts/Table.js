import { Column } from "./Column.js";
import { generate_random_indeces } from "../utils.js";

class Table{
    constructor(){
        this.columns = []; //list of column objects
    }

    initializeTable(categoryList, numDailyDoubles){
        this.populateTable(categoryList);
        let dailyDoubleColumns = generate_random_indeces(this.columns.length, numDailyDoubles);
        console.log(dailyDoubleColumns);
        for (let i=0; i<this.columns.length; i++){
            if (dailyDoubleColumns.includes(i)){
                this.columns[i].populateColumn(1);
            }
            else(this.columns[i].populateColumn());
        }

        
    }

    populateTable(categoryList){
        for (let i=0; i<categoryList.length; i++){
            const column = new Column(categoryList[i]);
            this.columns.push(column);
        }
    }
}

export {Table};