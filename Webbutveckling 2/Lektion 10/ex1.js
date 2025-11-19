function hämtaBoktabell() {
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200) {
            myFunction(this.responseXML);
        }
    };

    xhttp.open("GET", "data.xml", true);
    xhttp.send();
}

function myFunction(xmltabell) {
    let table = "<table border='1'><tr><th>Titel</th><th>Författare</th></tr>";

    var bok = xmltabell.getElementsByTagName("bok");

    for (let i = 0; i < bok.length; i++) {
        var titel = bok[i].getElementsByTagName("titel")[0].textContent;
        var författare = bok[i].getElementsByTagName("författare")[0].textContent;
        table += `<tr><td>${titel}</td><td>${författare}</td></tr>`;
    }

    table += "</table>";

    document.getElementById("demo").innerHTML = table;
}