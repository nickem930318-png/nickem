// Hämtar elementet med id 'theme-switcher' och tilldelar det till variabeln themeSwitcher.
const themeSwitcher = document.getElementById('theme-switcher');

// Lägger till en händelselyssnare för klick på themeSwitcher-elementet.
//addEventListener är en metod som används för att lägga till en händelselyssnare till ett DOM-element.
/*'click', () => { ... } innebär att vi lägger till en händelselyssnare för klick på ett DOM-element
och specificerar att den här funktionen ska köras när detta klick inträffar.*/
themeSwitcher.addEventListener('click', () => {
// classList är en egenskap på ett DOM-element som ger dig tillgång till en lista över alla klasser som finns tilldelade elementet.
//toggle är en metod som används med classList. Den växlar klassen 'theme2' på body-elementet när themeSwitcher klickas.
  document.body.classList.toggle('theme2');
});

