$(function(){
    // create events when click in button Esconder text
    $('#hide').click(function(){
        $('#unico').hide(); // hide text 
    });

    // change color text
    $('#blue').click(function(){
        $('p').css('color', 'blue');    //change color text to blue
        $('p').css('background-color', 'white'); // keep background white
    });
    $('#red').click(function(){
        $('p').css('color', 'red');     //change color text to red
        $('p').css('background-color', 'white');    // keep background white
        $('button').removeClass('red'); //remove a classe que da cor ao background do botao red
    });
    
    // select option change background and choose a color
    $('#background').click(function(){
        $('p').css('background-color', 'grey');
        $('#blue').click(function(){
            $('p').css('color', 'black');
            $('p').css('background-color', 'blue');
            $('#message').text('(gambiarra aqui)') //se clicar primeiro no red e depois no azul ele mantem alteracao feita quando clicado em red
            $('#message').delay(3000)
            $('#message').fadeOut('fast')
        });
        // com encadeamento em bloco e declaracao multipla (sem chamar o seletor para cada alteracao)
        $('#red').click(function(){
            $('p').css({color:'black', backgroundColor:'red'}); //background eh entendido como variavel por isso muda a forma como eh chamado   
            $('#message')
                .text('background color changed sucefully')
                .css({color: 'red', border:'1px solid red'})
                .delay(3000)
                .fadeOut('fast')
                .addClass('green')  //adiciona a classe que da cor verde ao background da mensagem
            $('button').removeClass('red'); //remove a classe que da cor ao background do botao red
        });

        });
});

$(function(){
    $('#hideblue').click(function(){
        //hide using fade effect and changing background color
        $('p').css('background-color', 'blue');
        $('p').fadeOut(3000);     // hide text with fade effect
        $('p').fadeIn(5000);    //unhide text with delay style
        
    // $('p').fadeIn('fast'); // aditional argument
    // $('p').fadeIn('slow'); // aditional argument
    });
    $('#hidered').click(function(){
        //hide using fade effect and changing background color
        $('p').css('background-color', 'red');
        $('p').fadeOut();     // hide text with fade effect
        $('p').delay(2000);  //2s in milesegundos
        $('p').fadeIn();    //unhide text
    });
});


$(function(){
    $('#l1').click(function(){ //eventos para cliques no link 2
        $('#img2').hide()       //oculta a imagem 2
        $('#img3').hide()       //oculta a imagem 3
        $('#img4').hide()       //oculta a imagem 4
        $('#img1').show();      //mostra a imagem 1 
    })
    $('#l2').click(function(){ //eventos para cliques no link 2
        $('#img1').hide()       //oculta a imagem 1
        $('#img3').hide()       //oculta a imagem 3
        $('#img4').hide()       //oculta a imagem 4
        $('#img2').show();      //mostra a imagem 2 
    })
    $('#l3').click(function(){ //eventos para cliques no link 2
        $('#img1').hide()       //oculta a imagem 1
        $('#img2').hide()       //oculta a imagem 2
        $('#img4').hide()       //oculta a imagem 4
        $('#img3').show();      //mostra a imagem 3 
    })
    $('#l4').click(function(){ //eventos para cliques no link 2
        $('#img1').hide()       //oculta a imagem 1
        $('#img2').hide()       //oculta a imagem 2
        $('#img3').hide()       //oculta a imagem 3
        $('#img4').show();      //mostra a imagem 4 
    })
    
});

/*
$(function(){
    $('button').click(function(){
        $('h1').hide();
    });
});
*/

/*
$(document).ready(function(){
    $('button').click(function(){
        $('h1').hide();
    });
});
*/
