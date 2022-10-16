async function getTheme() {
    let ele = document.getElementById("theme");
    await fetch(window.origin + "/email/" + ele.value, {method: "GET"})
            .then((res) => {
                if (res.status == 200)
                    return res.text();
            }).then((res)=>document.getElementById("email").innerHTML = res);
}

async function getEvidence() {
    let ele = document.getElementById("theme");
    await fetch(window.origin + "/evidence/" + ele.value, {method: "GET"})
            .then((res) => {
                if (res.status == 200)
                    return res.text();
            }).then((res)=>document.getElementById("evidence-img").src = res);
}