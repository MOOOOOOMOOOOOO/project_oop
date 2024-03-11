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

document.addEventListener('DOMContentLoaded', function() {
    const addTagButton = document.getElementById('add-tag-button');
    const tagInput = document.getElementById('tag-input');
    const tagsContainer = document.querySelector('.tags-input');

    addTagButton.addEventListener('click', function() {
        const tagValue = tagInput.value.trim();
        if (tagValue !== '') {
            const tagElement = document.createElement('span');
            tagElement.textContent = tagValue;
            tagElement.classList.add('tag');
            tagsContainer.insertBefore(tagElement, tagInput);
            tagInput.value = '';
        }
    });

    tagsContainer.addEventListener('click', function(event) {
        if (event.target.classList.contains('tag')) {
            event.target.remove();
        }
    });
});
