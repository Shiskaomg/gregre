let loginButton = document.getElementById('loginButton');
let loginModal = document.getElementById('loginModal');
let closeButton = document.getElementsByClassName('close-button')[0];
let loginForm = loginModal.querySelector('form');

loginButton.addEventListener('click', function () {
    

    
    loginModal.style.display = 'block';
    

    closeButton.onclick = function() {
        loginModal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == loginModal) {
            loginModal.style.display = 'none';
        }
    }

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        // Додайте тут вашу логіку для входу
        alert('Форма надіслана!');
        loginModal.style.display = 'none';
    });
});
