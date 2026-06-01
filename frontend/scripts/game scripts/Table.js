import { Column } from "./Column.js";

class Table{
    constructor(columns){
        this.coulumn_headers; //list of column headers for easier saves
        this.columns = columns; //list of column objects
    }
}

export {Table};