function submitLogin() {
    username = document.querySelector("#form11").value 
    password = document.querySelector("#form12").value 
    // alert(username + " 12 " + password)
    fetch("../submit-dang-nhap", {
        method: "POST",
        credentials: "include",
        body: JSON.stringify({username: username, password: password}),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })      
    })
    .then(
        resp => {
            if (resp.status == 200) {
                resp.json()
                .then(
                    data => {
                        if (data.result == "Thành công") {
                            // alert("...")
                            location.href = '/';
                        } else {
                            alert(data.result)
                        }

                    }
                )
            }
        }
    )
}