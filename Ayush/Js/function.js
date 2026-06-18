// function hero(a) {
//     console.log("Hello I'm hero")
// }

// function main(a, b) {
    // console.log(a + b)
//     console.log(b(a))
// }

// main(23, hero)

// function pass(a) {
//     a()
// }

// pass(function(){
//     console.log("I'm Inside a function")
// })

// ----------------------------------------------------------

// function side(a) {
    //     console.log("Hello, from side")
    //     return a
    // }
    
    // function main() {
        //     console.log("Hello, from main")
        // }
        
// side(main)()

// ----------------------------------------------------------


function dada() {
    console.log("Hello, I'm dada")

    function papa() {
        console.log("Hello, I'm papa")

        function child() {
            console.log("Hello, I'm child")
        }
        return child
    }
    return papa
}

dada()()()