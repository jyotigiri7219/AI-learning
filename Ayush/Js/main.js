// Different types of functions 

// ---------------------------------------------------------


function add(a,b) {
    console.log(a+b)
}

add(32,12)

// ---------------------------------------------------------

var subtract = function(a,b) {
    console.log(a-b)
}

subtract(32,11)

// ---------------------------------------------------------

var multiply = (a,b) => {
    console.log(a*b)
}

multiply(2,3)


// ---------------------------------------------------------

var print_name = name => console.log(`Hello ${name}`)

print_name("Ayush")