// document.querySelector('.facebook').addEventListener('click', function() {
//     console.log('เข้าสู่ระบบด้วย Facebook clicked');
// });

// document.querySelector('.line').addEventListener('click', function() {
//     console.log('เข้าสู่ระบบด้วย Line clicked');
// });

// document.querySelector('.apple').addEventListener('click', function() {
//     console.log('เข้าสู่ระบบด้วย Apple clicked');
// });

// document.querySelector('.google').addEventListener('click', function() {
//     console.log('เข้าสู่ระบบด้วย Google clicked');
// });

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('login-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        // ส่งข้อมูล login ไปยังเซิร์ฟเวอร์โดยใช้ AJAX
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'login.php', true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
            if (xhr.status === 200) {
                // ตรวจสอบการเข้าสู่ระบบ
                var response = JSON.parse(xhr.responseText);
                if (response.success) {
                    alert('เข้าสู่ระบบสำเร็จ!');
                    // ดำเนินการต่อหลังจากเข้าสู่ระบบ เช่น การเปลี่ยนเส้นทางหน้าเว็บ
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

