import { SaveManager } from "./SaveManager.js";
import { Game } from "./Game.js"
import { Table } from "./Table.js";
import { Column } from "./Column.js";
import { QuestionTile } from "./QuestionTile.js";


const saveManager = new SaveManager();
const game = new Game();

game.initializeGame(["U.S. Presidents", "Pop Culture", "Wonders of the World"], 2);

console.log(game.table.columns[0].questionList[1]);




