function hämtaStudenter() {
   var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200) {
            myFunction(this.responseXML);
        }
    };

    xhttp.open("GET", "studenter.json", true);
    xhttp.send(); 
}

function myFunction(studenttabell) {
    let table = "<table border='1'><tr><th>Namn</th><th>Ålder</th></tr>";

    var stud = studenttabell.getElementsByTagName("studenter.json");

    for (let i = 0; i < bok.length; i++) {
        var namn = stud[i].getElementsByTagName("namn")[0].textContent;
        var ålder = stud[i].getElementsByTagName("ålder")[0].textContent;
        table += `<tr><td>${namn}</td><td>${ålder}</td></tr>`;
    }

    table += "</table>";

    document.getElementById("demo").innerHTML = table;
}