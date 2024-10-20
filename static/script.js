document.getElementById('send-btn').addEventListener('click', function() {
    const message = document.getElementById('message-input').value;

    if (message.trim() !== '') {
        // Append user message to chat display
        const chatDisplay = document.getElementById('chat-display');
        const userMessage = `<p><strong>You:</strong> ${message}</p>`;
        chatDisplay.innerHTML += userMessage;

        // Send the user message to the backend for processing
        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: message }) // Send the user query to Flask
        })
        .then(response => response.json())
        .then(data => {
            // Append bot response to chat display
            const botResponse = `<p><strong>TARS:</strong> ${data.response}</p>`;
            chatDisplay.innerHTML += botResponse;

            // Clear input box
            document.getElementById('message-input').value = '';
            chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});

// JavaScript to close the sidebar when the close button is clicked
document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('sidebar').style.display = 'none';
});

function resetChat() {
    document.getElementById('chat-display').innerHTML = '';
}
