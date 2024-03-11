document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('login-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'login.php', true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    alert('เข้าสู่ระบบสำเร็จ!');
                    window.location.href = 'index.html'; 
                } else {
                    alert('เข้าสู่ระบบล้มเหลว! กรุณาตรวจสอบชื่อผู้ใช้และรหัสผ่านของคุณ');
                }
            } else {
                alert('การส่งคำขอล้มเหลว');
            }
        };
        xhr.send('username=' + username + '&password=' + password);
    });
});

// เมื่อคลิกที่ปุ่ม "ส่งข้อมูล"
document.querySelector('button[type="submit"]').addEventListener('click', function(event) {
    event.preventDefault(); // หยุดการทำงานของฟอร์มเพื่อป้องกันการรีเฟรชหน้าเว็บ

    // ดึงค่าที่กรอกในแบบฟอร์ม
    var writingTitle = document.getElementById('writing-title').value;
    var caption = document.getElementById('caption').value;
    var penName = document.getElementById('pen-name').value;
    var profileImage = document.getElementById('profile-image').value;
    var category = document.getElementById('category').value;

    var rating;
    var ratingInputs = document.querySelectorAll('input[name="rating"]');
    for (var i = 0; i < ratingInputs.length; i++) {
        if (ratingInputs[i].checked) {
            rating = ratingInputs[i].value;
            break;
        }
    }
    var tags = document.getElementById('tag-input').value;
});
