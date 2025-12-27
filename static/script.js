document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chatMessages');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');

    // Function to add a message to the chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(sender + '-message');
        
        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.textContent = text;
        
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to add a GIF message to the chat
    function addGifMessage(gifUrl, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(sender + '-message');
        
        const gifDiv = document.createElement('div');
        gifDiv.classList.add('message-content');
        
        const gifImg = document.createElement('img');
        gifImg.src = gifUrl;
        gifImg.alt = 'Supportive GIF';
        gifImg.style.maxWidth = '100%';
        gifImg.style.borderRadius = '12px';
        gifImg.style.margin = '5px 0';
        
        gifDiv.appendChild(gifImg);
        messageDiv.appendChild(gifDiv);
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Function to send message to backend
    function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');
        
        // Clear input
        userInput.value = '';
        
        // Show typing indicator
        const typingIndicator = document.createElement('div');
        typingIndicator.id = 'typing-indicator';
        typingIndicator.classList.add('message', 'bot-message');
        typingIndicator.innerHTML = `
            <div class="message-content">
                <div class="typing-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        `;
        chatMessages.appendChild(typingIndicator);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        // Add a slight delay before showing typing indicator for more natural feel
        setTimeout(() => {
            typingIndicator.style.opacity = '1';
        }, 300);
        
        // Send to backend
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Remove typing indicator
            const typingIndicator = document.getElementById('typing-indicator');
            if (typingIndicator) {
                typingIndicator.remove();
            }
            
            // Add bot responses with variable delays for more natural feel
            let delay = 800; // Initial delay before first response
            const baseDelay = 800;
            const delayBetweenMessages = 600;
            
            data.responses.forEach((response, index) => {
                setTimeout(() => {
                    if (response.text) {
                        addMessage(response.text, 'bot');
                    } else if (response.gif) {
                        addGifMessage(response.gif, 'bot');
                    }
                }, delay);
                
                // Increase delay for next message
                delay += baseDelay + (index * delayBetweenMessages) + (Math.random() * 400);
            });
        })
        .catch(error => {
            // Remove typing indicator
            const typingIndicator = document.getElementById('typing-indicator');
            if (typingIndicator) {
                typingIndicator.remove();
            }
            
            console.error('Error:', error);
            addMessage("Sorry, I'm having trouble connecting. Please try again.", 'bot');
        });
    }

    // Event listeners
    sendButton.addEventListener('click', sendMessage);
    
    userInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Function for quick messages
    window.sendQuickMessage = function(message) {
        userInput.value = message;
        sendMessage();
    };

    // Initial scroll to bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
});