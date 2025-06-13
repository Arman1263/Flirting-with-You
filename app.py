import streamlit as st
import time
import random
from pickup_lines import PickupLineManager
from animations import AnimationManager

# Initialize session state variables
def initialize_session_state():
    if 'stage' not in st.session_state:
        st.session_state.stage = 'welcome'
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ''
    if 'conversation_index' not in st.session_state:
        st.session_state.conversation_index = 0
    if 'user_responses' not in st.session_state:
        st.session_state.user_responses = []
    if 'flirt_score' not in st.session_state:
        st.session_state.flirt_score = 0
    if 'show_exit_message' not in st.session_state:
        st.session_state.show_exit_message = False

def welcome_screen():
    """Display the welcome screen with animated greeting"""
    st.title("💖 FlirtMate 💖")
    
    # Animated welcome message
    AnimationManager.display_animated_text("Hey there, Pretty Little Baby ✨", 0.05)
    
    st.markdown("---")
    
    # Name input
    st.subheader("First things first... 😊")
    user_name = st.text_input("What's your lovely name?", placeholder="Enter your name here...")
    
    if st.button("Let's Start Flirting! 💕", type="primary"):
        if user_name.strip():
            st.session_state.user_name = user_name.strip()
            st.session_state.stage = 'greeting'
            st.rerun()
        else:
            st.error("Come on, don't be shy! Tell me your name 😉")

def greeting_screen():
    """Display personalized greeting after name input"""
    st.title(f"💖 Hey {st.session_state.user_name}! 💖")
    
    # Personalized greeting with animation
    greeting_messages = [
        f"Wow, {st.session_state.user_name}, even your name is gorgeous 😍",
        f"Beautiful name for a beautiful person, {st.session_state.user_name} 💕",
        f"{st.session_state.user_name}... I think I'm already falling for you 😘"
    ]
    
    selected_greeting = random.choice(greeting_messages)
    AnimationManager.display_animated_text(selected_greeting, 0.03)
    
    st.markdown("---")
    
    if st.button("Ready for some pickup lines? 😏", type="primary"):
        st.session_state.stage = 'conversation'
        st.rerun()

def conversation_screen():
    """Main conversation screen with pickup lines and responses"""
    pickup_manager = PickupLineManager()
    
    st.title(f"💕 Chatting with {st.session_state.user_name} 💕")
    
    # Get current conversation data
    current_conversation = pickup_manager.get_conversation(st.session_state.conversation_index)
    
    if current_conversation is None:
        # End of conversation - show results
        show_results()
        return
    
    # Display pickup line with animation
    st.subheader("💬 FlirtMate says:")
    AnimationManager.display_animated_text(current_conversation['pickup_line'], 0.02)
    
    st.markdown("---")
    
    # Display response options
    st.subheader(f"💭 How does {st.session_state.user_name} respond?")
    
    response_choice = st.radio(
        "Choose your response:",
        options=list(range(len(current_conversation['responses']))),
        format_func=lambda x: current_conversation['responses'][x]['text'],
        key=f"response_{st.session_state.conversation_index}"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Send Response 💌", type="primary"):
            # Store the response and its score
            response_data = current_conversation['responses'][response_choice]
            st.session_state.user_responses.append({
                'pickup_line': current_conversation['pickup_line'],
                'response': response_data['text'],
                'score': response_data['score']
            })
            st.session_state.flirt_score += response_data['score']
            st.session_state.conversation_index += 1
            st.rerun()
    
    with col2:
        if st.button("I'm done flirting 😊"):
            show_results()
            return
    
    # Show conversation progress
    progress = (st.session_state.conversation_index + 1) / pickup_manager.get_total_conversations()
    st.progress(progress)
    st.caption(f"Conversation {st.session_state.conversation_index + 1} of {pickup_manager.get_total_conversations()}")

def show_results():
    """Display final results with flirt-o-meter score"""
    st.session_state.stage = 'results'
    
    st.title(f"💕 Results for {st.session_state.user_name} 💕")
    
    # Calculate final score percentage
    max_possible_score = len(st.session_state.user_responses) * 3  # Assuming max score per response is 3
    if max_possible_score > 0:
        score_percentage = (st.session_state.flirt_score / max_possible_score) * 100
    else:
        score_percentage = 0
    
    # Display animated flirt-o-meter
    st.subheader("💘 Flirt-o-Meter Results 💘")
    
    # Score display with visual meter
    st.metric(
        label="Your Flirt Score",
        value=f"{score_percentage:.1f}%",
        delta=f"{st.session_state.flirt_score}/{max_possible_score} points"
    )
    
    # Progress bar for visual appeal
    st.progress(score_percentage / 100)
    
    # Personalized message based on score
    if score_percentage >= 80:
        result_message = f"🔥 {st.session_state.user_name}, you're absolutely irresistible! I'm completely smitten! 😍"
        st.balloons()
    elif score_percentage >= 60:
        result_message = f"💕 {st.session_state.user_name}, you've got serious charm! I'm definitely crushing on you! 😘"
    elif score_percentage >= 40:
        result_message = f"😊 {st.session_state.user_name}, you're pretty sweet! There's definitely some chemistry here! 💫"
    else:
        result_message = f"😅 {st.session_state.user_name}, you're adorable even when you're playing hard to get! 💕"
    
    AnimationManager.display_animated_text(result_message, 0.03)
    
    st.markdown("---")
    
    # Show conversation summary
    if st.session_state.user_responses:
        with st.expander("💬 Our Conversation Summary"):
            for i, response in enumerate(st.session_state.user_responses, 1):
                st.write(f"**Round {i}:**")
                st.write(f"🗣️ FlirtMate: {response['pickup_line']}")
                st.write(f"💬 {st.session_state.user_name}: {response['response']}")
                st.write(f"⭐ Points: {response['score']}")
                st.write("---")
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Flirt Again! 💕", type="primary"):
            reset_conversation()
    
    with col2:
        if st.button("New Person 🔄"):
            reset_all()

def reset_conversation():
    """Reset conversation while keeping the same user"""
    st.session_state.stage = 'greeting'
    st.session_state.conversation_index = 0
    st.session_state.user_responses = []
    st.session_state.flirt_score = 0
    st.rerun()

def reset_all():
    """Reset everything including user name"""
    st.session_state.stage = 'welcome'
    st.session_state.user_name = ''
    st.session_state.conversation_index = 0
    st.session_state.user_responses = []
    st.session_state.flirt_score = 0
    st.rerun()

def handle_exit_attempt():
    """Handle when user tries to leave"""
    if st.session_state.stage != 'welcome' and not st.session_state.show_exit_message:
        st.session_state.show_exit_message = True
        st.error("Wait! Don't go 😢 I was just falling for you...")
        time.sleep(2)

def main():
    # Configure page
    st.set_page_config(
        page_title="FlirtMate - Interactive Flirting Experience",
        page_icon="💕",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .stButton > button {
        width: 100%;
        border-radius: 20px;
    }
    .animated-text {
        font-size: 1.2em;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        background: linear-gradient(45deg, #ff6b9d, #c44569);
        color: white;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Display appropriate screen based on stage
    if st.session_state.stage == 'welcome':
        welcome_screen()
    elif st.session_state.stage == 'greeting':
        greeting_screen()
    elif st.session_state.stage == 'conversation':
        conversation_screen()
    elif st.session_state.stage == 'results':
        show_results()
    
    # Sidebar with app info
    with st.sidebar:
        st.title("💖 FlirtMate Info")
        st.write("A fun, interactive flirting experience!")
        
        if st.session_state.user_name:
            st.write(f"**Current Player:** {st.session_state.user_name}")
            st.write(f"**Current Score:** {st.session_state.flirt_score} points")
        
        st.markdown("---")
        st.write("**How to Play:**")
        st.write("1. Enter your name")
        st.write("2. Respond to pickup lines")
        st.write("3. See your flirt score!")
        
        if st.button("🔄 Restart Game"):
            reset_all()

if __name__ == "__main__":
    main()
