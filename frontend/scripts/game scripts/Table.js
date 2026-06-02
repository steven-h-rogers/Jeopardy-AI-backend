import { Column } from "./Column.js";

class Table{
    constructor(){
        this.columns = []; //list of column objects
    }

    populateTable(categoryList){
        for (i=0; i<=categoryList.length; i++){
            column = new Column(categoryList[i]);
            this.columns.push(column);
        }
    }
}

export {Table};