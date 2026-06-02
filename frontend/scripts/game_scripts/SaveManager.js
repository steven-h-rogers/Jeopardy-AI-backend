import {Game} from './Game.js'

class SaveManager{
    constructor(){
        this.game;
        this.gameTempObj;
        this.jsonState;
    }

    setGame(game){
        this.game = game;
    }

    setJsonState(jsonState){
        this.jsonState = jsonState;
    }


    convertToJSON(game){
        this.jsonState = JSON.stringify(game);
        return this.jsonState;
    }

    convertToObject(game_string){
        this.gameTempObj = JSON.parse(game_string);
        return this.gameTempObj;
    }

}

export {SaveManager}