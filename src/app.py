import streamlit as st
from story_generator import generate_story
from image_generator import generate_image
from PIL import Image
import io

st.set_page_config(page_title="Creative Story Generator with Illustrations", layout="wide")
st.title("Creative Story Generator with Illustrations")
st.markdown("""
Welcome! Enter a story prompt and choose how many segments you want. The app will generate a creative story and a unique illustration for each segment using AI models—all running locally on your machine.
""")

with st.form("story_form"):
    prompt = st.text_input("Enter a story prompt:", "Once upon a time in a magical forest")
    num_segments = st.slider("Number of story segments:", min_value=1, max_value=10, value=3)
    submitted = st.form_submit_button("Generate Story & Illustrations")

if submitted:
    try:
        with st.spinner("Generating story..."):
            story_segments = generate_story(prompt, num_segments)
        st.success("Story generated!")
        images = []
        for idx, segment in enumerate(story_segments):
            st.markdown(f"---\n### Segment {idx+1}")
            st.write(segment)
            with st.spinner(f"Generating illustration for segment {idx+1}..."):
                try:
                    image = generate_image(segment)
                    images.append(image)
                    st.image(image, caption=f"Illustration {idx+1}", use_column_width=True)
                    buf = io.BytesIO()
                    image.save(buf, format="PNG")
                    st.download_button(
                        label=f"Download Illustration {idx+1}",
                        data=buf.getvalue(),
                        file_name=f"illustration_{idx+1}.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"Failed to generate illustration for segment {idx+1}: {e}")
    except Exception as e:
        st.error(f"Failed to generate story: {e}")

st.markdown("---")
st.caption("All processing is done locally. First-time model loading may take a few minutes.")