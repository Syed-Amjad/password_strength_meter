import streamlit as st
import re
import random
import string

# List of common weak passwords
COMMON_PASSWORDS = {"password", "123456", "password123", "qwerty", "abc123", "letmein"}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Upper and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    # Common Password Check
    if password.lower() in COMMON_PASSWORDS:
        return 1, ["Your password is too common. Choose a more secure one."]

    # Determine Strength Level
    if score == 1 or score == 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback

# Function to generate a strong password
def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(all_chars) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

# User input
password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength"):
    if password:
        score, strength, feedback = check_password_strength(password)

        st.subheader(f"Strength: {strength} ({score}/5)")
        
        if strength == "Weak":
            st.error("Your password is weak. Consider these improvements:")
            for tip in feedback:
                st.warning(f"- {tip}")

        elif strength == "Moderate":
            st.info("Your password is okay but could be improved:")
            for tip in feedback:
                st.warning(f"- {tip}")

        else:
            st.success("Your password is strong! ✅")

# Password Generator
st.subheader("Need a Strong Password?")
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"Suggested Password: `{strong_password}` (Copy & Use)")
