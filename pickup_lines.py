import random

class PickupLineManager:
    """Manages pickup lines and conversation flow"""
    
    def __init__(self):
        self.conversations = [
            {
                "pickup_line": "I was having a normal day… and then you happened. Now nothing feels normal, but I kinda love it.",
                "responses": [
                    {"text": "Aww, that actually made me smile.", "score": 3},
                    {"text": "Smooth. Unexpected, but nice.", "score": 2},
                    {"text": "Tryna make me feel special? It's working... maybe.", "score": 1}
                ]   
            },

            {
                "pickup_line": "Do you have a map? Because I just got lost in your eyes 👀✨",
                "responses": [
                    {"text": "Aww, that's actually sweet! 😊", "score": 3},
                    {"text": "GPS might work better than a map 😏", "score": 2},
                    {"text": "I think you need glasses, not a map 🤓", "score": 1}
                ]
            },
            {
                "pickup_line": "Are you a magician? Because whenever I look at you, everyone else disappears 🎩✨",
                "responses": [
                    {"text": "That's the most romantic thing I've heard! 💕", "score": 3},
                    {"text": "Magic tricks are cool, but can you make my homework disappear? 📚", "score": 2},
                    {"text": "Abracadabra... nope, they're still here 😂", "score": 1}
                ]
            },
            {
                "pickup_line": "Is your name Google? Because you have everything I've been searching for 🔍💖",
                "responses": [
                    {"text": "That's actually really clever! 😍", "score": 3},
                    {"text": "Did you just compare me to a search engine? 🤔", "score": 2},
                    {"text": "Sorry, search results not found 404 😜", "score": 1}
                ]
            },
            {
                "pickup_line": "Do you believe in love at first sight, or should I walk by again? 😘",
                "responses": [
                    {"text": "One time was perfect! 💕", "score": 3},
                    {"text": "Maybe try a different angle this time? 😏", "score": 2},
                    {"text": "Walking is good exercise! Keep going 🚶‍♂️", "score": 1}
                ]
            },
            {
                "pickup_line": "Are you Wi-Fi? Because I'm feeling a connection 📶💕",
                "responses": [
                    {"text": "Strong signal detected! 💪📶", "score": 3},
                    {"text": "Password protected, sorry! 🔒", "score": 2},
                    {"text": "Connection timeout... try again later ⏰", "score": 1}
                ]
            },
            {
                "pickup_line": "If you were a vegetable, you'd be a cute-cumber! 🥒😄",
                "responses": [
                    {"text": "That's so silly it's adorable! 🥰", "score": 3},
                    {"text": "I prefer being a sweet potato 🍠", "score": 2},
                    {"text": "I'm more of a hot chili pepper 🌶️", "score": 1}
                ]
            },
                        {
                "pickup_line": "No games, no lines. Just thought you should know—you're kind of amazing.",
                "responses": [
                    {"text": "That's... unexpectedly genuine. I like that.", "score": 3},
                    {"text": "Is this your soft launch to my heart? 😄", "score": 2},
                    {"text": "Bold move. I respect it.", "score": 1}
                ]
            },
            {
                "pickup_line": "Are you a time traveler? Because I can see you in my future! ⏰💫",
                "responses": [
                    {"text": "I love a person with vision! 🔮", "score": 3},
                    {"text": "Time travel sounds exciting! When do we start? ⚡", "score": 2},
                    {"text": "My crystal ball says... maybe 🎱", "score": 1}
                ]
            },
            {
                "pickup_line": "Is your dad a boxer? Because you're a knockout! 🥊💥",
                "responses": [
                    {"text": "KO! You win this round! 🏆", "score": 3},
                    {"text": "He's actually a lawyer, but close enough! ⚖️", "score": 2},
                    {"text": "Nope, but I know how to throw a punch 👊", "score": 1}
                ]
            }
        ]
        
        # Shuffle conversations for variety
        random.shuffle(self.conversations)
    
    def get_conversation(self, index):
        """Get conversation at specified index"""
        if 0 <= index < len(self.conversations):
            return self.conversations[index]
        return None
    
    def get_total_conversations(self):
        """Get total number of conversations available"""
        return len(self.conversations)
    
    def get_random_pickup_line(self):
        """Get a random pickup line conversation"""
        return random.choice(self.conversations)
    
    def get_conversation_by_score_range(self, min_score, max_score):
        """Get conversations that can yield scores in the specified range"""
        suitable_conversations = []
        for conv in self.conversations:
            scores = [response['score'] for response in conv['responses']]
            if min(scores) >= min_score or max(scores) <= max_score:
                suitable_conversations.append(conv)
        return suitable_conversations if suitable_conversations else self.conversations
    
    def get_flirt_level_message(self, score_percentage):
        """Get personalized message based on flirt score"""
        if score_percentage >= 90:
            return "🔥 LEGENDARY FLIRTER! You're absolutely irresistible! 😍"
        elif score_percentage >= 80:
            return "💕 MASTER FLIRTER! You've got serious game! 😘"
        elif score_percentage >= 70:
            return "💖 GREAT FLIRTER! You know how to charm! 🥰"
        elif score_percentage >= 60:
            return "😊 GOOD FLIRTER! You've got potential! 💫"
        elif score_percentage >= 50:
            return "🙂 DECENT FLIRTER! Not bad at all! ⭐"
        elif score_percentage >= 40:
            return "😅 LEARNING FLIRTER! Practice makes perfect! 📚"
        else:
            return "😊 ADORABLE FLIRTER! You're cute even when shy! 💕"

    def get_response_feedback(self, score):
        """Get feedback message based on individual response score"""
        if score == 3:
            return "🔥 Perfect response! You're on fire!"
        elif score == 2:
            return "😊 Nice one! Good chemistry!"
        else:
            return "😅 Playing hard to get? I like the challenge!"
