import { SaveManager } from "./SaveManager";
import { Game } from "./Game"
import { Table } from "./Table";
import { Column } from "./Column";
import { QuestionTile } from "./QuestionTile";


tile1 = QuestionTile(200, false);
tile2 = QuestionTile(200, false);
tile3 = QuestionTile(200, true);
tile4 = QuestionTile(400, false);

column1 = Column('Before & After', [tile1]);
column2 = Column('World Wonders', [tile2]);
column3 = Column('U.S. Presidents', [tile3, tile4]);


