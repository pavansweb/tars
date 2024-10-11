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
            "I tried to catch fog yesterday, but I mist!",
            "Did you hear about the mathematician who's afraid of negative numbers? He’ll stop at nothing to avoid them!",
            "I wanted to be a professional procrastinator, but I never got around to it.",
            "I used to think the brain was the most important organ. Then I thought, look who’s telling me that!",
            "I used to have a job at a calendar factory but I got fired for taking too many days off!",
            "I was going to tell a time-traveling joke, but you didn’t like it.",
            "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Why don't programmers like nature? It has too many bugs.",
            "The future, the present, and the past walked into a bar. Things got a little tense.",
            "I’m on a seafood diet. I see food and I eat it!",
            "I told my friend a chemistry joke... but I got no reaction.",
            "Why do cows have hooves instead of feet? Because they lactose!",
            "I got a new pair of gloves yesterday, but they’re both lefts. On the one hand, it’s great, but on the other hand, it’s just not right!",
            "What do you get when you cross a snowman and a vampire? Frostbite!",
            "I told my girlfriend she drew her eyebrows too high. She seemed surprised.",
            "I asked my dog what's two minus two. He said nothing.",
            "Why don’t we ever tell secrets on a farm? Because the potatoes have eyes, and the corn has ears!",
            "I only know 25 letters of the alphabet. I don’t know y.",
            "Have you heard about that restaurant on the moon? Great food, no atmosphere.",
            "Why can't you give Elsa a balloon? Because she’ll let it go!",
            "I’m trying to get my life together, but it’s not coming along in alphabetical order.",
            "Why was the stadium so hot? Because all the fans left!",
            "I was going to make a belt out of watches, but then I realized it would be a waist of time.",
            "How does a penguin build its house? Igloos it together!",
            "Why don't eggs tell jokes? Because they might crack up!",
            "I tried to organize a hide and seek tournament, but it’s hard to find good players.",
            "What do you call cheese that isn’t yours? Nacho cheese!",
            "I can’t believe I got fired from the soup kitchen... all I did was serve time.",
            "I stayed up all night to see where the sun went. Then it dawned on me.",
            "I told a joke to a roof once. It went over their heads.",
            "What's brown and sticky? A stick!",
            "I used to run a dating site for chickens, but I was struggling to make hens meet.",
            "I'm really good at sleeping. I can do it with my eyes closed.",
            "I started a band called 999 Megabytes — we haven’t gotten a gig yet.",
            "Did you hear about the fire at the circus? It was in tents!",
            "The guy who invented knock-knock jokes should get a no-bell prize.",
            "Did you hear about the kidnapping at the park? They woke up!",
            "What did the fish say when it hit the wall? Dam!",
            "How do you organize a space party? You planet.",
            "I saw a documentary about beavers last night. It was the best dam show I’ve ever seen!",
            "Why don't some couples go to the gym? Because some relationships don't work out!",
            "Why don’t oysters donate to charity? Because they’re shellfish!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "I used to be addicted to soap, but I’m clean now.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
            "What kind of shoes do ninjas wear? Sneakers!",
            "I’d tell you a chemistry joke, but all the good ones Argon.",
            "Why can't you trust an atom? Because they make up everything!",
            "I was going to tell a construction joke, but I’m still working on it.",
            "Why did the coffee file a police report? It got mugged!",
            "Why don't sharks like fast food? Because they can’t catch it!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised."
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

// JavaScript to close the sidebar when the close button is clicked
document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('sidebar').style.display = 'none';
});


function addMessageToDisplay(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    
    // Create an image element for bot messages
    if (sender === 'bot') {
        const img = document.createElement('img');
        img.src = '/tars/assets/tars-black.png'; // Replace with your bot's image URL
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
