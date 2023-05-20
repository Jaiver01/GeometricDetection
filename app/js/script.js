const apiUrl = 'http://127.0.0.1:5000';

const result = document.getElementById("result");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const clean = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawingcanvas.clear();
    result.innerHTML = '';
    drawingcanvas.backgroundColor = "white";
}

const predict = async () => {
    let img = canvas.toDataURL('image/jpeg', 1.0);
    img = img.replace('data:image/jpeg;base64,', '');

    const request = { base64_img: img };

    const response = await fetch(apiUrl + '/classifier/geometric/predict', {
        method: "POST",
        cache: "no-cache",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(request),
    });

    const data = await response.json();
        
    console.log("Prediccion", data);
    result.innerHTML = data.prediction;
}