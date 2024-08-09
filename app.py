import streamlit as st
import time  # Import time to simulate image generation delay

'''Sidebar setup'''

st.sidebar.title("Visionary Diffusion")
st.sidebar.write("This app generates images based on the prompts you provide.")

# Add some space after the About message
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Form for user inputs
with st.sidebar.form("user_input_form", clear_on_submit=True, border=False):
    positive_prompt = st.text_area("Positive Prompt", placeholder="Enter your positive prompt here")
    
    model_options = ["Model A", "Model B", "Model C"]
    model_selection = st.selectbox("Select Model", model_options)
    
    num_images = st.number_input("Number of Images", min_value=1, max_value=8, value=4, step=1)
    
    with st.expander("Advanced Settings", expanded=False):
        negative_prompt = st.text_area("Negative Prompt", placeholder="Enter your negative prompt here")
    
    submitted = st.form_submit_button("Generate Images")


'''Main page content setup'''

st.subheader("Image Generation Results")
st.write("Below are the images generated based on your prompts. You can view and download each image by clicking the download button below.")

# Handle form submission
if submitted:
    # List of image URLs or paths
    image_urls = [
        "https://via.placeholder.com/1080?text=Image+1",
        "https://via.placeholder.com/1080?text=Image+2",
        "https://via.placeholder.com/1080?text=Image+3",
        "https://via.placeholder.com/1080?text=Image+4"
    ]
    
    # Determine the number of rows needed
    num_rows = (num_images + 1) // 2 
    
    with st.spinner(f"Generating {num_images} images with '{model_selection}' model."):
        # Simulate image generation delay
        time.sleep(3)
        
        for row in range(num_rows):
            cols = st.columns(2)
            start_idx = row * 2
            end_idx = min(start_idx + 2, num_images)

            for i in range(start_idx, end_idx):
                cols[i - start_idx].image(image_urls[i], use_column_width="auto")   # caption=f"Image {i+1}"
                cols[i - start_idx].download_button(
                    label="Download Image",
                    data=image_urls[i],
                    file_name=f"image_{i+1}.png",
                    mime="image/png",
                    use_container_width=True
                )
    
    st.success(f'Image generation completed successfully!')
