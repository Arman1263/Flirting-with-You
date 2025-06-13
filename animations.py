import streamlit as st
import time
import random

class AnimationManager:
    """Handles animations and visual effects for the FlirtMate app"""
    
    @staticmethod
    def display_animated_text(text, delay=0.05):
        """Display text with typewriter animation effect"""
        placeholder = st.empty()
        displayed_text = ""
        
        for char in text:
            displayed_text += char
            placeholder.markdown(f'<div class="animated-text">{displayed_text}▌</div>', unsafe_allow_html=True)
            time.sleep(delay)
        
        # Final display without cursor
        placeholder.markdown(f'<div class="animated-text">{text}</div>', unsafe_allow_html=True)
    
    @staticmethod
    def display_heart_animation():
        """Display animated hearts"""
        hearts = ["💕", "💖", "💗", "💘", "💝", "💞", "💟", "❤️", "🧡", "💛", "💚", "💙", "💜", "🤍", "🖤"]
        selected_hearts = random.sample(hearts, 5)
        
        cols = st.columns(5)
        for i, heart in enumerate(selected_hearts):
            with cols[i]:
                st.markdown(f"<div style='text-align: center; font-size: 2em; animation: bounce 1s infinite;'>{heart}</div>", 
                           unsafe_allow_html=True)
    
    @staticmethod
    def display_sparkle_effect():
        """Display sparkle animation"""
        sparkles = ["✨", "⭐", "🌟", "💫", "⚡", "🎆", "🎇"]
        selected_sparkles = random.sample(sparkles, 3)
        
        for sparkle in selected_sparkles:
            st.markdown(f"<div style='text-align: center; font-size: 1.5em;'>{sparkle}</div>", 
                       unsafe_allow_html=True)
    
    @staticmethod
    def display_flirt_meter_animation(score_percentage):
        """Display animated flirt meter"""
        meter_emojis = {
            (0, 20): "😴",
            (20, 40): "😐",
            (40, 60): "🙂",
            (60, 80): "😊",
            (80, 90): "😍",
            (90, 100): "🔥"
        }
        
        emoji = "😐"
        for (min_score, max_score), meter_emoji in meter_emojis.items():
            if min_score <= score_percentage < max_score:
                emoji = meter_emoji
                break
        
        st.markdown(f"""
        <div style='text-align: center; font-size: 3em; margin: 20px 0;'>
            {emoji}
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def display_loading_animation(message="Loading..."):
        """Display loading animation with message"""
        placeholder = st.empty()
        loading_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        
        for _ in range(10):  # Show animation for 1 second
            for char in loading_chars:
                placeholder.markdown(f"<div style='text-align: center; font-size: 1.5em;'>{char} {message}</div>", 
                                   unsafe_allow_html=True)
                time.sleep(0.1)
        
        placeholder.empty()
    
    @staticmethod
    def display_celebration_animation():
        """Display celebration animation"""
        celebration_emojis = ["🎉", "🎊", "🥳", "🎈", "🎁", "🏆", "⭐", "🌟"]
        
        cols = st.columns(len(celebration_emojis))
        for i, emoji in enumerate(celebration_emojis):
            with cols[i]:
                st.markdown(f"<div style='text-align: center; font-size: 2em;'>{emoji}</div>", 
                           unsafe_allow_html=True)
    
    @staticmethod
    def display_typing_indicator():
        """Display typing indicator animation"""
        placeholder = st.empty()
        dots = ["💭", "💭.", "💭..", "💭..."]
        
        for _ in range(3):  # Show animation 3 times
            for dot_pattern in dots:
                placeholder.markdown(f"<div style='text-align: center; font-size: 1.2em; color: #888;'>{dot_pattern}</div>", 
                                   unsafe_allow_html=True)
                time.sleep(0.3)
        
        placeholder.empty()
    
    @staticmethod
    def display_score_reveal_animation(score):
        """Display score reveal with dramatic effect"""
        placeholder = st.empty()
        
        # Build up suspense
        for i in range(3):
            placeholder.markdown(f"<div style='text-align: center; font-size: 2em;'>{'.' * (i + 1)}</div>", 
                               unsafe_allow_html=True)
            time.sleep(0.5)
        
        # Reveal score
        placeholder.markdown(f"<div style='text-align: center; font-size: 3em; color: #ff6b9d;'>{score}%</div>", 
                           unsafe_allow_html=True)
        time.sleep(1)
    
    @staticmethod
    def add_custom_css():
        """Add custom CSS for animations"""
        st.markdown("""
        <style>
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-10px);
            }
            60% {
                transform: translateY(-5px);
            }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
            100% {
                transform: scale(1);
            }
        }
        
        .animated-text {
            animation: fadeIn 0.5s ease-in;
        }
        
        .pulse-element {
            animation: pulse 2s infinite;
        }
        
        .bounce-element {
            animation: bounce 2s infinite;
        }
        </style>
        """, unsafe_allow_html=True)
