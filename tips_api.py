from flask import Flask, jsonify

app = Flask(__name__)

# Example mental health tips API data
# This represents what might be provided during the competition
mental_health_tips = {
    "anxious": [
        "Practice the 3-3-3 rule: Name 3 things you see, 3 sounds you hear, and 3 things you can touch. 🌍",
        "Try progressive muscle relaxation: Tense and release each muscle group for 5 seconds. 💪",
        "Use aromatherapy with lavender or chamomile essential oils. 🌸",
        "Keep an anxiety journal to identify triggers and track your progress. 📓"
    ],
    "sad": [
        "Create a self-care playlist with songs that lift your spirit. 🎵",
        "Practice gratitude by writing down 3 good things that happened today. ✨",
        "Engage in acts of kindness, even small ones like complimenting someone. 💕",
        "Start a mood diary to understand your emotional patterns and growth. 📖"
    ],
    "stressed": [
        "Try the box breathing technique: Inhale for 4, hold for 4, exhale for 4, hold for 4. 📦",
        "Write down your worries and categorize them as 'within my control' or 'outside my control'. 📝",
        "Create a personal mantra like 'I am capable and resilient' to repeat during stress. 🧘",
        "Maintain a stress journal to identify patterns and effective coping strategies. ✍️"
    ],
    "neutral": [
        "Maintain your emotional balance with daily mindfulness practice. 🧘",
        "Try a new hobby or creative activity to explore your interests. 🎨",
        "Plan something to look forward to this week. 📅",
        "Begin a daily reflection journal to maintain your emotional awareness. 🌱"
    ],
    "happy": [
        "Share your joy with others to amplify positive feelings. 🌟",
        "Express gratitude to someone who has positively impacted your life. 💌",
        "Channel your energy into a passion project or creative endeavor. 💡",
        "Keep a happiness journal to capture and celebrate joyful moments. ✨"
    ]
}

@app.route('/tips', methods=['GET'])
def get_tips():
    """Return all mental health tips"""
    return jsonify(mental_health_tips)

@app.route('/tips/<mood>', methods=['GET'])
def get_tips_by_mood(mood):
    """Return tips for a specific mood"""
    tips = mental_health_tips.get(mood.lower(), mental_health_tips["neutral"])
    return jsonify({
        "mood": mood,
        "tips": tips
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(port=5001, debug=True)