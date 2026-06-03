//TODO: add version with weights towards higher stop indeces
function generate_random_indeces(stop, numIndeces, start=0){
    let indices = [];
    for (let i=0; i<numIndeces; i++){
        let index = Math.floor(Math.random()*(stop-start)) + start;
        while (indices.includes(index)){
             index = Math.floor(Math.random()*(stop-start)) + start;
        }
        indices.push(index);
    }
    return indices;
}

export {generate_random_indeces}