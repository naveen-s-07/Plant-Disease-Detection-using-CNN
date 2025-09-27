import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import os
from PIL import Image

# Load and preprocess the image
def model_predict(image_path):
    model = tf.keras.models.load_model(r"C:/Users/Karan S/Downloads/CNN_plant_disease_detection_model.keras")
    img = cv2.imread(image_path)  # read the file and convert into array
    H, W, C = 224, 224, 3
    img = cv2.resize(img, (H, W))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array(img)
    img = img.astype("float32")
    img = img / 255.0  # rescaling
    img = img.reshape(1, H, W, C)  # reshaping

    prediction = np.argmax(model.predict(img), axis=-1)[0]
    return prediction

# Sidebar
st.sidebar.title("🌿 Plant Detection System")
app_mode = st.sidebar.selectbox("Choose Section", ["Overview", "Detect Disease", "Plant Health Tips", "About Project"])

# Header style
st.markdown(
    """
    <style>
        .main {
            background-color: #e0f7fa;
        }
        .sidebar .sidebar-content {
            background-color: #004d40;
        }
        .stButton button {
            background-color: #00796b;
            color: white;
        }
        h1, h2, h3 {
            color: #004d40;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Overview Section
if app_mode == "Overview":
    
    st.title("**🌱 Plant Detection System for Sustainable Agriculture**")
    
    st.image(
        Image.open(r"C:/Users/Karan S/Downloads/Plant-Disease-analysis.jpg"),
        caption="Enhancing Agriculture with AI",
        use_container_width=True,
    )

    
    st.write(
        """
        **PROJECT OVERVIEW**
        
This system leverages advanced AI to detect plant diseases, aiding farmers and gardeners in maintaining healthy crops.
Explore the features to understand plant health, detect diseases, and get useful tips for sustainable agriculture.
Disease Detection

**Image Analysis**: Upload images of your plants, and the system will analyze them to detect signs of disease.

**Symptom Matching**: Compare observed symptoms with an extensive database to identify potential issues.
Plant Health Monitoring

**Growth Tracking**: Monitor the growth and development of your plants over time to ensure they are thriving.

**Environmental Factors**: Get insights into how temperature, humidity, and soil conditions affect plant health.
Sustainable Farming Tips

**Pest Management**: Learn about eco-friendly pest control methods to protect your crops without harming the environment.

**Soil Health**: Receive advice on maintaining soil fertility through natural composting and crop rotation techniques.
Expert Recommendations

**Personalized Advice**: Based on the detected diseases and environmental conditions, receive tailored recommendations to improve plant health.

**Resource Library**: Access a wealth of information on plant care, disease prevention, and sustainable farming practices.
        """
    )
    

# Detect Disease Section
elif app_mode == "Detect Disease":
    st.title("🔍 Detect Plant Disease")
    test_image = st.file_uploader("Upload a plant image", type=["jpg", "png", "jpeg"])
        
    if test_image is not None:
        if(st.button("Display Image")):
            st.image(test_image,width=4,use_container_width=True)
          
        
        # Define the save path
        save_path = os.path.join(os.getcwd(), test_image.name)
        print(save_path)
        # Save the file to the working directory
        with open(save_path, "wb") as f:
            f.write(test_image.getbuffer())
 

        if st.button("Detect Disease"):
            st.info("Processing the image, please wait...")
            result_index = model_predict(save_path)

            class_name = [
                'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
                'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
                'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
                'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
                'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
                'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
                'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
                'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
                'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                'Tomato___healthy'
            ]

            st.success(f"Detected Disease: {class_name[result_index]}")

# Plant Health Tips Section
elif app_mode == "Plant Health Tips":
    st.title("💡 Plant Health Tips")
    st.write(
        """
        ## Tips for Keeping Your Plants Healthy:
        - Regularly check plants for early signs of disease.
        - Ensure proper watering techniques to avoid overwatering or underwatering.
        - Use disease-resistant plant varieties when available.
        - Rotate crops to prevent soil-borne diseases.
        - Maintain proper plant spacing to allow good air circulation.
        """
    )
    st.image(
        Image.open(r"C:/Users/Karan S/Downloads/Prevention_Tips.webp"),
        caption="Healthy Plants Lead to Sustainable Agriculture",
        use_container_width=True,
    )

# About Project Section
elif app_mode == "About Project":
    st.title("📚 About the Project")
    st.write(
        """
        The ***Plant Detection System for Sustainable Agriculture*** is an exciting project that uses cutting-edge artificial intelligence (AI) to transform how farmers care for their crops. The heart of this system is its ability to spot plant diseases early, giving farmers a head start in tackling problems before they spread. This not only helps keep crops healthier but also boosts yields, making farming more productive and sustainable.

**Why It Matters**

**Early Disease Detection**: Catching plant diseases early means farmers can act quickly to limit damage. This reduces the need for heavy pesticide use, which is better for the plants and the environment.
**Sustainable Farming Practices**: By encouraging early action, the system helps promote eco-friendly farming practices. This reduces environmental impact and helps preserve the delicate balance of biodiversity.
**Better Crop Management**: With accurate information about plant health, farmers can make smarter decisions about managing their crops, leading to better use of resources and healthier harvests.

***How It Works***

**Image Analysis**: Farmers simply upload photos of their crops, and the AI system does the rest. It analyzes the images to detect any signs of disease, using sophisticated algorithms to achieve high accuracy.

**Symptom Matching**: The system checks the detected symptoms against a vast database of plant diseases, helping farmers pinpoint exactly what's wrong with their crops.

**Environmental Insights**: Beyond just identifying diseases, the system also provides valuable information on factors like soil quality, temperature, and humidity, which all play a role in plant health.

***Benefits for Farmers***

**Timely Interventions**: By identifying problems early, farmers can act before issues get out of hand, saving time and resources.

**Reduced Chemical Use**: Early detection means less reliance on pesticides, leading to safer produce and a healthier environment.

**Economic Savings**: Healthier crops lead to bigger, better-quality harvests, which means better profits for farmers.

**A Sustainable Future**

The Plant Detection System for Sustainable Agriculture is a great example of how technology can work hand-in-hand with nature. By cutting down on harmful practices and helping farmers tackle issues early, this project supports a more sustainable approach to farming. It’s a step forward for farmers, the environment, and the future of food production.
        """
    )
    st.image(
        Image.open(r"C:/Users/Karan S/Downloads/About_Project.jpg"),
        caption="AI in Agriculture: A Step Towards Sustainability",
        use_container_width=True,
    )
