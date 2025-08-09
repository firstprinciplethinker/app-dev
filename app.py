import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Way2Careers",
    page_icon="🎯",
    layout="wide"
)

# --- HOME PAGE CONTENT ---

# Title and Tagline
st.title("🎯 Welcome to Way2Careers")
st.markdown("#### Guiding Students Towards the Right Career Path")

# Banner Image (replace with your own URL or image file later)
st.image("https://via.placeholder.com/1000x300.png?text=Way2Careers+Career+Counselling+Platform", use_container_width=True)

# About Section
st.markdown("## About Way2Careers")
st.write("""
Way2Careers is your trusted partner in discovering the best academic and professional opportunities in India and abroad.  
We guide students and parents through every milestone — from selecting the right course to securing admissions.
""")

# Why Choose Us
st.markdown("## Why Choose Way2Careers?")
st.success("We make career decisions easier with:")
st.markdown("""
- ✅ Personalized one-on-one counselling  
- ✅ Expert advice on MBBS, BDS, Engineering, MBA, and Study Abroad  
- ✅ Data-backed college and course recommendations  
- ✅ Full support from career discovery to admission  
- ✅ Transparent, ethical guidance for every student  
""")

# Call to Action
st.markdown("---")
st.markdown("### 🗣️ Talk to a Career Expert Now")
st.button("📙 Book a Free Counselling Session")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ in India by manoj  \n© 2025 Way2Careers")
