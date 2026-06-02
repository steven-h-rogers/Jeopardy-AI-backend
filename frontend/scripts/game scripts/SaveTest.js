import { SaveManager } from "./SaveManager.js";
import { Game } from "./Game.js"
import { Table } from "./Table.js";
import { Column } from "./Column.js";
import { QuestionTile } from "./QuestionTile.js";


const saveManager = new SaveManager()

const tile1 = new QuestionTile(200, false);
const tile2 = new QuestionTile(200, false);
const tile3 = new QuestionTile(200, true);
const tile4 = new QuestionTile(400, false);

const column1 = new Column('Before & After', [tile1]);
const column2 = new Column('World Wonders', [tile2]);
const column3 = new Column('U.S. Presidents', [tile3, tile4]);

const table = new Table([column1, column2, column3]);

const game = new Game(1, "Medium", table);

saveManager.setGame(game);
console.log(saveManager.convertToJSON(saveManager.game));
console.log(saveManager.convertToObject(saveManager.jsonState));

console.log(tile1);
console.log(tile3);

console.log(column1);
console.log(column3);

console.log(table);

console.log(game);




