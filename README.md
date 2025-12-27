# Mental Health Buddy

## Problem Statement Chosen
Build a chatbot that checks in on users' emotional state and recommends coping strategies, breathing exercises, or helplines. The bot detects mood from user input and responds empathetically with personalized mental health support.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript (no frameworks)
- **Backend**: Python Flask
- **Data**: Mental health tips API with hardcoded fallback

## API Used
- **Primary**: External mental health tips API (http://localhost:5001/tips)
- **Fallback**: Hardcoded mental health tips dictionary
- **GIF Support**: Sample GIF URLs for emotional support responses

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Run the example API server:
   ```bash
   python tips_api.py
   ```

3. Run the main application:
   ```bash
   python app.py
   ```

4. Access the chatbot at `http://localhost:5000`

## 🎯 Features

- **Mood Detection**: Detects user's emotional state through text (happy, sad, anxious, stressed, neutral)
- **Empathetic Replies**: Responds with warmth and understanding
- **Coping Suggestions**: Provides mental health tips based on detected mood
- **Quick Check-ins**: Buttons for instant mood sharing
- **Calming UI**: Soft colors, rounded chat bubbles, and smooth animations

## 🚀 Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Mental-Health-Buddy
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Run the example API server**:
   ```bash
   python tips_api.py
   ```

4. **Run the main application**:
   ```bash
   python app.py
   ```

5. **Access the chatbot**:
   Open your browser and go to `http://localhost:5000`

## 🧠 How It Works

1. **Mood Detection**: The bot analyzes user input for keywords associated with different emotions
2. **Empathetic Response**: Generates a caring response based on the detected mood
3. **Coping Suggestion**: Provides a relevant mental health tip from either:
   - External API (when available)
   - Hardcoded data (fallback when API is unavailable)

## 🎨 UI Features

- Calming gradient background (blues, purples, pinks)
- Rounded chat bubbles with soft shadows
- Smooth message animations
- Responsive design for mobile and desktop
- Quick action buttons for common moods
- Typing indicators for bot responses

## 📝 Example Conversation

**User**: "I'm feeling really stressed today."

**Bot**: "That sounds overwhelming. Remember to be kind to yourself 🌼"

**Bot**: "Here's something that might help: Take a 5-minute break and stretch your body. 🧘"

## 🧩 Mental Health Tips

The bot provides tips for:
- Anxious feelings
- Sadness
- Stress
- Neutral states
- Happiness

Tips include breathing exercises, journaling prompts, social connection suggestions, and mindfulness techniques.

## 🤝 Contributing

Feel free to fork the repository and submit pull requests to improve the Mental Health Buddy.

## 🔄 API Integration

During the competition, if an API for mental health tips is provided:

1. Update the `EXAMPLE_API_URL` in [app.py](file:///D:/Desktop1/Desktop/Mental-Health-Buddy/app.py) to point to the provided API endpoint
2. Ensure the API returns data in the same format as our hardcoded [mental_health_tips](file:///D:/Desktop1/Desktop/Mental-Health-Buddy/app.py#L12-L34) structure
3. The application will automatically use the API with fallback to hardcoded data if the API fails

An example API implementation is provided in [tips_api.py](file:///D:/Desktop1/Desktop/Mental-Health-Buddy/tips_api.py) for reference.

## 📄 License

This project is for educational purposes and mental health support.
=======
# Mental-Health-Buddy
A compassionate chatbot that checks in on users' emotional well-being and provides personalized coping strategies, breathing exercises, and mental health support.
>>>>>>> c2c6e1919e90df122077f8bc719a336b4d1144a2
