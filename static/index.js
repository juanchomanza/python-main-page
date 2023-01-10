console.log("hello console")

function printMessage(mensaje){
    console.log(mensaje)
}

printMessage("perro")


let num1 = 300

let num2 = 200.6

let sum = num1 + num2


console.log(sum)



let i = 0
while (i < 5){
    printMessage(i) ; if (i == 3){console.log("es tres")} ;  i = i + 1 ; 
}

const prueba = document.get


const txtNum1 = document.getElementById('op1')
const txtNum2 = document.getElementById('op2')
const resultado = document.getElementById('resultado')

const suma = document.getElementById('suma')
const resta = document.getElementById('resta')
const div = document.getElementById('div')
const mult = document.getElementById('mult')


suma.addEventListener('click', sumar)
resta.addEventListener('click', restar)
div.addEventListener('click', dividir)
mult.addEventListener('click', multiplicar)


function sumar(){
    const op1 = parseFloat(txtNum1.value)
    const op2 = parseFloat(txtNum2.value)   
    let result = op1 + op2
    
    resultado.innerText = "la suma es: " + result
}

function restar(){
    const op1 = parseFloat(txtNum1.value)
    const op2 = parseFloat(txtNum2.value)   
    let result = op1 - op2
    
    resultado.innerText = "la resta es: " + result
}

function dividir(){
    const op1 = parseFloat(txtNum1.value)
    const op2 = parseFloat(txtNum2.value)   
    let result = op1 / op2
    
    resultado.innerText = "la división es: " + result
}

function multiplicar(){
    const op1 = parseFloat(txtNum1.value)
    const op2 = parseFloat(txtNum2.value)   
    let result = op1 * op2
    
    resultado.innerText = "la multiplicación es: " + result
}



var list = ["mono", "trolo", "rolo", "polo", "nodo", "codo", "polo"]


for (let i = 0 ; i < list.length; i++){
    console.log(list[i])
    
    

} 

console.log(list.length)
// let tiempo = document.getElementById('hora')

// setInterval(tiempo.innerHTML, 1000)
// // setInterval(function horas(){
// //     tiempo.innerHTML = tiempo

// // }, 1000)

// let segundos = document.getElementById('segs')
// setInterval(segundos.innerHTML, 1000)


// window.onload = horas() {

//     setInterval(tiempo, 1000);

// }