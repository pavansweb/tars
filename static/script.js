document.getElementById('send-btn').addEventListener('click', function() {
    const message = document.getElementById('message-input').value;

    if (message.trim() !== '') {
        // Append user message to chat display with proper HTML tags
        const chatDisplay = document.getElementById('chat-display');
        const userMessage = `<p><strong>You:</strong> ${message}</p>`;
        chatDisplay.innerHTML += userMessage;

       
    }
});

// JavaScript to close the sidebar when the close button is clicked
document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('sidebar').style.display = 'none';
});

function resetChat() {
    document.getElementById('chat-display').innerHTML = '';
}
