from flask import Flask, request, jsonify, render_template
import random
import re
import requests
from functools import lru_cache

app = Flask(__name__)

# TODO: Replace hardcoded mental_health_tips with real API during competition.
# Hardcoded mental health tips (fallback)
mental_health_tips = {
    "anxious": [
        "Try deep breathing: Inhale 4s, hold 7s, exhale 8s. 🫁",
        "Take a short walk to reset your mind. 🚶",
        "Listen to calming music or guided meditation. 🎵",
        "Write down your anxious thoughts and challenge them with rational responses. ✍️"
    ],
    "sad": [
        "Reach out to a close friend and talk about how you feel. 👤",
        "Write down 3 things you're grateful for today. ✍️",
        "Watch a comforting movie or listen to uplifting music. 🎬",
        "Create a mood journal to track your feelings and identify patterns. 📓"
    ],
    "stressed": [
        "Take a 5-minute break and stretch your body. 🧘",
        "Focus on what you can control right now. 🎯",
        "Break your task into smaller, manageable parts. 📋",
        "Journal about your stressors and brainstorm possible solutions. ✍️"
    ],
    "neutral": [
        "Keep up the good balance! Maybe try journaling today ✍️",
        "Reflect on something positive that happened this week. 🌟",
        "Start a daily gratitude journal to maintain your emotional well-being. 📖"
    ],
    "happy": [
        "That's wonderful! Keep sharing your positivity 🌞",
        "Celebrate small wins and spread the joy 💫",
        "Write about what made you happy today to reinforce positive experiences. ✍️"
    ]
}

# Example API endpoint for mental health tips
# In a real competition, this would be replaced with the actual provided API
EXAMPLE_API_URL = "http://localhost:5001/tips"

@lru_cache(maxsize=1)
def fetch_tips_from_api():
    """Fetch mental health tips from external API with fallback to hardcoded data"""
    try:
        # Try to fetch from the example API
        response = requests.get(EXAMPLE_API_URL, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            # If API returns error status, fall back to hardcoded data
            raise requests.RequestException(f"API returned status {response.status_code}")
    except requests.RequestException as e:
        # Log the error (in production, use proper logging)
        print(f"API fetch failed: {e}. Using hardcoded data as fallback.")
        # Fallback to hardcoded data if API fails
        return mental_health_tips

# Fetch tips from API (or use hardcoded as fallback)
# Uncomment the line below during competition and comment out the hardcoded assignment
# mental_health_tips = fetch_tips_from_api()
# For now, we're using the hardcoded data as the default
# mental_health_tips = mental_health_tips  # This line is just for clarity

# Keywords for mood detection
mood_keywords = {
    "anxious": ["anxious", "nervous", "worried", "panic", "scared", "fear"],
    "sad": ["sad", "depressed", "unhappy", "down", "blue", "cry"],
    "stressed": ["stressed", "overwhelmed", "pressure", "tense", "burnout"],
    "happy": ["happy", "joy", "excited", "glad", "pleased", "delighted"],
    "neutral": ["okay", "fine", "alright", "normal", "balanced"]
}

def detect_mood(message):
    """Detect user's mood based on keywords in their message"""
    message_lower = message.lower()
    
    # Check for each mood category
    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            if re.search(r'\b' + keyword + r'\b', message_lower):
                return mood
    
    # Default to neutral if no keywords match
    return "neutral"

# Sample GIF URLs for different moods (in a real implementation, these would come from a GIF API)
gif_urls = {
    "anxious": [
        "https://media.giphy.com/media/3o7TKsQ8UQ4l4LhGz6/giphy.gif",
        "https://media.giphy.com/media/l0HlG8vJXW0X5v3aY/giphy.gif"
    ],
    "sad": [
        "https://media.giphy.com/media/3o7TKS5wXFvD1nqDqM/giphy.gif",
        "https://media.giphy.com/media/3o7TKUe6IbGp2r6HbG/giphy.gif"
    ],
    "stressed": [
        "https://media.giphy.com/media/l0HlNaQ6gWfllcjDO/giphy.gif",
        "https://media.giphy.com/media/3o7TKU0v3ImJ2a4K2c/giphy.gif"
    ],
    "happy": [
        "https://media.giphy.com/media/3o7TKsQ8UQ4l4LhGz6/giphy.gif",
        "https://media.giphy.com/media/l0HlG8vJXW0X5v3aY/giphy.gif"
    ],
    "neutral": [
        "https://media.giphy.com/media/3o7TKU0v3ImJ2a4K2c/giphy.gif",
        "https://media.giphy.com/media/l0HlNaQ6gWfllcjDO/giphy.gif"
    ]
}

def get_empathetic_response(mood):
    """Generate an empathetic response based on detected mood"""
    responses = {
        "anxious": [
            "I hear you, that sounds really tough 💛",
            "It's okay to feel this way. You're doing your best 🌱",
            "Take a deep breath. You're stronger than you know 💪"
        ],
        "sad": [
            "I'm here for you. It's okay to feel sad sometimes 🤗",
            "Your feelings are valid. This too shall pass 🌈",
            "Sending you comfort and strength during this time 💙"
        ],
        "stressed": [
            "That sounds overwhelming. Remember to be kind to yourself 🌼",
            "You're doing your best, and that's enough ✨",
            "Take a moment to breathe. You've got this 🌿"
        ],
        "happy": [
            "That's beautiful to hear! Your happiness matters 🌟",
            "I'm glad you're feeling good today! Keep shining ☀️",
            "Your positive energy is contagious! Share it with the world 🌍"
        ],
        "neutral": [
            "Thanks for sharing how you feel 🙏",
            "I'm here whenever you need support 💛",
            "Checking in with yourself is a great habit 🌱"
        ]
    }
    
    return random.choice(responses.get(mood, responses["neutral"]))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Ensure request.json is not None before accessing get method
    if request.json is None:
        return jsonify({"error": "Invalid JSON"}), 400
    user_message = request.json.get('message', '')
    
    # Detect mood from user message
    mood = detect_mood(user_message)
    
    # Get empathetic response
    empathetic_response = get_empathetic_response(mood)
    
    # Get coping suggestion
    # Fetch fresh tips from API or use cached/fallback data
    current_tips = fetch_tips_from_api()
    tips = current_tips.get(mood, current_tips["neutral"])
    coping_suggestion = random.choice(tips)
    
    # Create bot responses
    bot_responses = [
        {"text": empathetic_response, "sender": "bot"},
        {"text": coping_suggestion, "sender": "bot"}
    ]
    
    # Randomly add a GIF reply (30% chance)
    if random.random() < 0.3:
        gif_url = random.choice(gif_urls.get(mood, gif_urls["neutral"]))
        bot_responses.append({"gif": gif_url, "sender": "bot"})
    
    return jsonify({"responses": bot_responses})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)