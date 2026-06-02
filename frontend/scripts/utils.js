
function generate_random_indeces(start=0, stop, numIndeces){
    let indeces = [];
    for (i=0; i<numIndeces; i++){
        index = Math.floor(Math.random()*(stop-start+start));
        while (indeces.includes(index)){
             index = Math.floor(Math.random()*(stop-start+start));
        }
        indeces.push(index);
    }
    return indeces;
}

export {generate_random_indeces}