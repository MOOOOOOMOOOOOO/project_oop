const payment_data = {};

payment_data.username = "Mozaza"

document.getElementById('online_banking').addEventListener('click', function() {
    payment_data.payment_method = "OnlineBanking";
    console.log(payment_data.payment_method);
});

document.getElementById('debit_card').addEventListener('click', function() {
    payment_data.payment_method = "CreditCard";
    console.log(payment_data.payment_method);
});

document.getElementById('truemoney_wallet').addEventListener('click', function() {
    payment_data.payment_method = "TrueMoneyWallet";
    console.log(payment_data.payment_method);
});

const coin_boxes = document.querySelectorAll('.coin_box');

  coin_boxes.forEach(function(coin_box_click) {
      coin_box_click.addEventListener('click', function() {
          coin_boxes.forEach(function(box) {
            box.classList.remove('selected');
          });

          coin_box_click.classList.add('selected');
      });
  });

  const paymentButtons = document.querySelectorAll('.payment_button');

  paymentButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      paymentButtons.forEach(function(btn) {
        btn.classList.remove('selected');
      });

      button.classList.add('selected');
    });
  });

document.getElementById('coin_box_click_20').addEventListener('click', function() {
    payment_data.golden_coin_amount = 20;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_50').addEventListener('click', function() {
    payment_data.golden_coin_amount = 50;
    console.log(payment_data.golden_coin_amount);
});


document.getElementById('coin_box_click_100').addEventListener('click', function() {
    payment_data.golden_coin_amount = 100;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_500').addEventListener('click', function() {
    payment_data.golden_coin_amount = 500;
    console.log(payment_data.golden_coin_amount);
});

document.getElementById('coin_box_click_costom').addEventListener('click', function() {
    payment_data.golden_coin_amount = document.getElementById('golden_coin_amount').value;
    console.log(payment_data.golden_coin_amount);
});


payment_data.code = document.getElementById('promotion_code').value;
console.log(payment_data.code);

// submit
async function submit() {
    console.log(payment_data);

    // const response = await axios.post(`http://127.0.0.1:8000/get_coin_transaction?username=${input}`);
    // console.log(response.data);
    
}