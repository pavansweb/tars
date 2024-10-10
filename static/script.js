document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('reset-btn').addEventListener('click', resetChat);

function sendMessage() {
    const input = document.getElementById('message-input');
    const messageText = input.value.trim();

    if (messageText) {
        // Add user message to the chat display
        addMessageToDisplay(messageText, 'user');
        
        // Array of bot responses
        const botResponses = [
            "Why did the robot go on a diet? Because he had too many bytes!",
            "I'm not saying I'm a genius, but I did just teach my toaster how to make bread.",
            "If I had a dollar for every time I got a question, I’d be a rich chatbot!",
            "I'm great at multitasking: I can waste time, be unproductive, and procrastinate all at once!",
            "Did you hear about the claustrophobic astronaut? He just needed a little space!",
            "I wanted to learn about time travel, but I couldn’t find the right portal!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I'm just a bot, but if you need advice, I can tell you my favorite pie flavor: 3.14!",
            "If you see a crime at an Apple Store, does that make you an iWitness?",
            "I asked the librarian if the library had any books on paranoia. She whispered, 'They're right behind you!'",
            "Why did the computer keep freezing? It left its Windows open!",
            "I have a fear of elevators, but I'm taking steps to avoid them.",
            "If at first you don’t succeed, then skydiving definitely isn’t for you!",
            "I told my friend 10 jokes to get him to laugh. Sadly, no pun in ten did.",
            "I used to play piano by ear, but now I use my hands!",
            "Why don’t scientists trust atoms? Because they make up everything!",
            "I can't believe I got fired from the calendar factory. All I did was take a day off!",
            "I went to buy some camo pants but couldn't find any!",
            "What do you call fake spaghetti? An impasta!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet!",
            "Why did the math book look sad? It had too many problems.",
            "I’m on a whiskey diet. I’ve lost three days already!",
            "I told my computer I needed a break, and now it won't stop sending me beach wallpapers!",
            "Why did the bicycle fall over? It was two-tired!",
            "I told my friend to stop impersonating a flamingo. He took a step back!",
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "What’s orange and sounds like a parrot? A carrot!",
            "I would tell you a joke about an elevator, but it's an uplifting experience!",
            "I tried to catch fog yesterday, but I mist!"
        ];
        
        // Get a random response
        const randomIndex = Math.floor(Math.random() * botResponses.length);
        const botResponse = botResponses[randomIndex];

        // Simulate bot response
        setTimeout(() => {
            addMessageToDisplay(botResponse, 'bot');
        }, 500);

        // Clear the input box
        input.value = '';
    }
}

function addMessageToDisplay(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    
    // Create an image element for bot messages
    if (sender === 'bot') {
        const img = document.createElement('img');
        img.src = '/tars_v1/assets/tars-black.png'; // Replace with your bot's image URL
        messageDiv.appendChild(img);
    }

    // Add the text content
    const textNode = document.createTextNode(text);
    messageDiv.appendChild(textNode);
    
    // Append message to chat display
    document.getElementById('chat-display').appendChild(messageDiv);
    document.getElementById('chat-display').scrollTop = document.getElementById('chat-display').scrollHeight;
}

function resetChat() {
    document.getElementById('chat-display').innerHTML = '';
}
