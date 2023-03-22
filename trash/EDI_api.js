var xhttp = new XMLHttpRequest;

xhttp.open('GET','https://my.api.mockaroo.com/edi.json?key=12a6d260',true);
xhttp.send();

xhttp.onload = () => {
    if(xhttp.status == 200){
        console.log(xhttp.response)
    } else{
        console.log(`error ${xhttp.status}`)
    }
}
