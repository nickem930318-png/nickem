//jQuery (JavaScript)
//Nu lägger vi till funktionalitet för att ändra text och färg när användaren klickar på knappen.

/* $(document).ready(function().. 
är ett sätt att tala om för webbläsaren att koden inuti funktionen ska köras först när hela dokumentets struktur (DOM) har laddats.*/

$(document).ready(function() {
    $('#changeButton').click(function() {
        $('#text').text('Texten har ändrats!').css('color', 'red'); 
    });
});
