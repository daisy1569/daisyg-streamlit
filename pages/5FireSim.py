import streamlit as st
import base64
from PIL import Image, ImageEnhance
import io


st.title("Fire Simulation")
st.write("*showing options for the user interaction")

# Load and display the initial GIF
file_path = "/workspaces/daisyg-streamlit/giphy.gif"
file_ = open(file_path, "rb")
contents = file_.read()
file_.close()

# Display the initial GIF
gif_img = st.markdown(
    f'<img src="data:image/gif;base64,{base64.b64encode(contents).decode("utf-8")}" alt="cat gif">',
    unsafe_allow_html=True,
)

# Function to apply color tint to the GIF
def apply_color_tint(color):
    # Load the GIF image
    img = Image.open(io.BytesIO(contents))

    # Convert the image to RGBA mode for color adjustments
    img = img.convert("RGBA")

    # Apply the color tint
    if color == "Blue":
        img = apply_color_filter(img, (0, 0, 255))  # Apply blue tint
    elif color == "Green":
        img = apply_color_filter(img, (0, 255, 0))  # Apply green tint
    elif color == "Red":
        img = apply_color_filter(img, (255, 0, 0))  # Apply red tint

    # Convert the modified image back to GIF format
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='GIF')
    img_byte_arr = img_byte_arr.getvalue()

    # Update the displayed GIF with the new tint
    gif_img.markdown(
        f'<img src="data:image/gif;base64,{base64.b64encode(img_byte_arr).decode("utf-8")}" alt="cat gif">',
        unsafe_allow_html=True,
    )

# Function to apply a color filter to an image
def apply_color_filter(img, color):
    data = img.getdata()
    new_data = []
    for item in data:
        # Apply color filter (tint) to each pixel
        new_data.append(tuple([min(255, max(0, item[i] + color[i])) for i in range(3)]) + (item[3],))
    img.putdata(new_data)
    return img

# Add a selection dropdown for color tint
color_option = st.selectbox("Choose a color tint:", ["None", "Blue", "Green", "Red"])

# Apply color tint when the button is clicked
if st.button("   GO   "):
    if color_option != "None":
        apply_color_tint(color_option)


# Display second GIF w/ radio buttons
gif_img = st.markdown(
    f'<img src="data:image/gif;base64,{base64.b64encode(contents).decode("utf-8")}" alt="cat gif">',
    unsafe_allow_html=True,
)

# Function to apply color tint to the GIF
def apply_color_tint(color):
    # Load the GIF image
    img = Image.open(io.BytesIO(contents))

    # Convert the image to RGBA mode for color adjustments
    img = img.convert("RGBA")

    # Apply the color tint
    if color == "Blue":
        img = apply_color_filter(img, (0, 0, 255))  # Apply blue tint
    elif color == "Green":
        img = apply_color_filter(img, (0, 255, 0))  # Apply green tint
    elif color == "Red":
        img = apply_color_filter(img, (255, 0, 0))  # Apply red tint

    # Convert the modified image back to GIF format
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='GIF')
    img_byte_arr = img_byte_arr.getvalue()

    # Update the displayed GIF with the new tint
    gif_img.markdown(
        f'<img src="data:image/gif;base64,{base64.b64encode(img_byte_arr).decode("utf-8")}" alt="cat gif">',
        unsafe_allow_html=True,
    )

# Function to apply a color filter to an image
def apply_color_filter(img, color):
    data = img.getdata()
    new_data = []
    for item in data:
        # Apply color filter (tint) to each pixel
        new_data.append(tuple([min(255, max(0, item[i] + color[i])) for i in range(3)]) + (item[3],))
    img.putdata(new_data)
    return img

# Add radio buttons for color tint selection
color_option = st.radio("Choose a color tint:", ["None", "Blue", "Green", "Red"])

# Apply color tint when the button is clicked
if st.button("Apply Tint"):
    if color_option != "None":
        apply_color_tint(color_option)


        

# Display the third GIF with the slider!
gif_img = st.markdown(
    f'<img src="data:image/gif;base64,{base64.b64encode(contents).decode("utf-8")}" alt="cat gif">',
    unsafe_allow_html=True,
)

# Function to apply color tint to the GIF with adjustable intensity
def apply_color_tint_with_intensity(color, intensity):
    # Load the GIF image
    img = Image.open(io.BytesIO(contents))

    # Convert the image to RGBA mode for color adjustments
    img = img.convert("RGBA")

    # Define color values based on selected color
    if color == "Blue":
        color_value = (0, 0, 255)  # Blue tint
    elif color == "Green":
        color_value = (0, 255, 0)  # Green tint
    elif color == "Red":
        color_value = (255, 0, 0)  # Red tint
    else:
        return  # No color tint applied if "None" is selected

    # Apply the color tint with adjustable intensity
    img = apply_color_filter_with_intensity(img, color_value, intensity)

    # Convert the modified image back to GIF format
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='GIF')
    img_byte_arr = img_byte_arr.getvalue()

    # Update the displayed GIF with the new tint using a unique identifier
    unique_gif_img = st.markdown(
        f'<img src="data:image/gif;base64,{base64.b64encode(img_byte_arr).decode("utf-8")}" alt="cat gif">',
        unsafe_allow_html=True,
    )

# Function to apply a color filter to an image with adjustable intensity
def apply_color_filter_with_intensity(img, color, intensity):
    data = img.getdata()
    new_data = []
    for item in data:
        # Apply color filter (tint) to each pixel with adjustable intensity
        new_pixel = tuple([min(255, max(0, item[i] + int(color[i] * intensity))) for i in range(3)]) + (item[3],)
        new_data.append(new_pixel)
    img.putdata(new_data)
    return img

# Generate unique widget IDs using a counter
widget_counter = 0

# Add radio buttons for color selection with a unique key
widget_counter += 1
radio_key = f"radio_{widget_counter}"
color_option = st.radio("Choose a color tint:", ["None", "Blue", "Green", "Red"], key=radio_key)

# Add a slider for adjusting tint intensity (if color tint is selected) with a unique key
if color_option != "None":
    widget_counter += 1
    slider_key = f"slider_{widget_counter}"
    intensity = st.slider("Adjust Tint Intensity", 0.0, 2.0, 1.0, key=slider_key)

# Apply color tint when the button is clicked with a unique key
widget_counter += 1
button_key = f"button_{widget_counter}"
if st.button("Apply Tint", key=button_key):
    if color_option != "None":
        apply_color_tint_with_intensity(color_option, intensity)