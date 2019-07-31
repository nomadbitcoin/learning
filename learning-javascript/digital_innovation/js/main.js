function clicou(){
    document.getElementById('agradecimento').innerHTML = 'Obrigado por clicar';
}

function redirecionar(){
    window.open('https://github.com/yaaanhue');
    //window.location.href = 'https://github.com/yaaanhue';
}

function trocar(elemento){
    //document.getElementById('mousemove').innerHTML = 'Obrigado por passar o mouse'
    elemento.innerHTML = 'Obrigado por passar o mouse'
}

function voltar(elemento){
    //document.getElementById('mousemove').innerHTML = 'Passe o mouse aqui'    //pega o elemento com id mousemove e altera o html
    elemento.innerHTML = 'Passe o mouse aqui'   //ao colocar this la no html pra passar ele mesmo para a funcao a funcao recebe o elemento e faz a alteracao
}

function load(){    //onload adicionado como argumento ao body para que execute essa funcao quando o body for carregado
    alert('pagina carregada');
}

function funcaoChange(elemento){
    console.log(elemento.value)
}

/*function soma(n1,n2){
    return n1 + n2;
}

function validaIdade(idade){
    var validar;
    if (idade >= 18){
        validar = true;
    }else{
        validar = false;
    }
    return validar;
}


var idade = prompt('qual eh sua idade?');
console.log(validaIdade(idade));
//alert(soma(10,30))
*/


//var nome = 'Yan Luiz Coito';
/*
var idade = 22;
var idade2 = 22
//alert(nome + ' tem ' + idade + ' anos')
//alert(idade + idade2)

/*
var frase = 'Japao eh o melhor time do mundo' 
console.log(frase);
console.log(frase.replace('Japao', 'Brasil'))
alert(frase.replace('Japao', 'Brasil')) //substitui Japao por Brasil
alert(frase.toUpperCase('Japao', 'Brasil')) //letra grande
alert(frase.toLowerCase('Japao', 'Brasil')) //letra pequena
*/
/*
var lista = ['maca', 'pera', 'laranja']
console.log(lista[1]);
lista.push('uva');  //adiciona item na lista
console.log(lista)
lista.pop(); //remove item da lista
console.log(lista);
console.log(lista.length);   //tamanho da lista
console.log(lista.reverse());    //devolve a lista inversa, com laranja no ultimo indeice
console.log(lista.toString()[0]); //transforma lista em string e retorna a primeira letra que eh l
console.log(lista.join(' - ')) //transforma em string e define o separador de cada item da lista
*/

//var fruta = {nome:'maca', cor:'vermelho'};  //dict or JSON///
//var fruta = [{nome:'maca', cor:'vermelho'}, {nome:'uva', cor:'roxo'}];  //lista de dicionario
//console.log(fruta[1].nome);

/*
var idade = prompt('qual eh sua idade?') //coletar informacao do usuario
if (idade >= 18){
    alert('maior de idade');
}else{
    alert('menor de idade');
}
*/

/*
for (count=0; count<=5; count++){ //loop for
    alert(count)
}

var count = 0;
while (count <= 5){ //loop while
    console.log(count);
    count++;
};
*/

/*
var d = new Date(); //pegar a data
alert(d.getMonth()+1)   //devolve apenas o mes (mais um pq comeca do 0)
alert(d.getMinutes())   //devolve apenas o minuto
*/