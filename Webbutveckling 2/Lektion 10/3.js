function loadDoc() {
  // Skapa ett nytt XMLHttpRequest-objekt
  var xhttp = new XMLHttpRequest();

  // Använd onreadystatechange för att lyssna på förändringar i status
  xhttp.onreadystatechange = function() {
    // Kontrollera om förfrågan är klar (readyState === 4) och om status är OK (status === 200)
    if (this.readyState === 4 && this.status === 200) {
      myFunction(this.responseXML);
    }
  };

  // Öppna en GET-begäran till filen 2.xml och skicka den asynkront
  xhttp.open("GET", "2.xml", true);
  xhttp.send();
}

// xmlDoc är ett objekt som representerar ett XML-dokument som laddats från filen "2.xml".
function myFunction(xmlDoc) {
  // Starta en HTML-tabell
  let table = "<table border='1'><tr><th>Artist</th><th>Title</th></tr>";

  // Hämta alla <CD>-element
  var cds = xmlDoc.getElementsByTagName("CD");

  // Loopa igenom varje <CD> och hämta ut ARTIST och TITLE
  for (let i = 0; i < cds.length; i++) {
    var artist = cds[i].getElementsByTagName("ARTIST")[0].textContent;
    var title = cds[i].getElementsByTagName("TITLE")[0].textContent;
    table += `<tr><td>${artist}</td><td>${title}</td></tr>`;
  }

  // Avsluta tabellen
  table += "</table>";

  // Sätt in tabellen i elementet med id "demo"
  document.getElementById("demo").innerHTML = table;
}