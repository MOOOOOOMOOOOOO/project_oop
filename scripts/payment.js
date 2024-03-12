// import axios from "axios";

async function show_coin_transaction(){
    const input = document.getElementById("username").value;
    const content = document.getElementById("content");
    console.log(input);

    const response = await axios.get(`http://127.0.0.1:8000/get_coin_transaction?username=${input}`);
    
    console.log(response.data);

    // const coin_transaction_list = response.data.coin_transaction_list;//

    // for(let i = 0; i < coin_transaction_list.lenght; i++) {
    //     content.innerHTML += `<p> ${coin_transaction_list[i]}</p>`;
    // }


}