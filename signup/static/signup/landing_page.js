document.querySelector('form').addEventListener('submit', function (e) {
    const emailField = document.querySelector('input[name="email"]');
    if (!emailField.value.includes('@')) {
        e.preventDefault();
        alert('Please enter a valid email address.');
    }
});
