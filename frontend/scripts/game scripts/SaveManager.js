import {Game} from './Game'

class SaveManager{
    constructor(){
        this.game;
        this.jsonState;
    }

    convertToJSON(game){
        return JSON.stringify(game_obj);
    }

    convertToObject(game_string){
        return JSON.parse(game_string);
    }

}

export {SaveManager}