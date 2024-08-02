import streamlit as st
import pandas as pd
from PIL import Image
import base64
import matplotlib.pyplot as plt

def stream():
    st.title("STRAY KIDS HOO!")

    st.header("HELLAVATOR")
    st.subheader("STRAY KIDS")

    st.write("STRAY KIDS EVERYWHERE ALL AROUND THE WORLD")#---------DATATYPE DEKHTA HAI SHAYAD
    st.write(143)

    st.markdown("_BANGCHAN_")#-----------------------FORMAT DEKHTA HAI
    st.markdown("""
    | col1 | col2 |
    |------|------|
    |   1  |   3  |
    |   2  |   4  |
    """)
     
    st.sidebar.write(pd.DataFrame({'A':[1,2,3], 'B':[4,5,6]}))

    st.code("wwww.google.com")


    a = st.button("MAR TU")
    if a:
        st.write("Your sins are......loading........")
        st.write("Click checkbox")

    b = st.checkbox("Dead?")
    if b:
        st.write("...Infinite")
    
def visualize():

    uploaded_file = st.file_uploader("Choose a file", type = ["pdf","jpg","png"])

    c = st.button("submit")
    if c:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption = "Uploaded Image." , use_column_width = True)
            st.write("Image uploaded successfully.")

        else:
            st.write("Please upload an image file.")  
    data = {
        'A': [5,7,8,5,6,7,8,7,6,5],
        'B': [10,20,15,20,10,15,20,10,15,10]
    }
    df = pd.DataFrame(data)

    st.write("Sample DataFrame: ")
    st.dataframe(df)

    plt.figure(figsize=(10,5))
    plt.hist(df["A"], bins = 5, alpha = 0.75)
    plt.title("SWARA KA HISTOGRAM")
    plt.xlabel("value")
    plt.ylabel("frequency")
    
    st.pyplot(plt)

st.sidebar.title('sidebar')   
ch = st.sidebar.selectbox("Choose penalty: ",{1:"Add your sins to stuti's sins and become sin free", 2:"Reincarnate as a cockroach"})
print(ch)
if ch == 1:
    stream()
elif ch == 2:
    visualize()

# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#         print(data)
#         #print(base64.b64encode(data).decode())
#     return base64.b64encode(data).decode()

# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#     <style>
#     .stApp {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)
# set_background('Screenshot 2024-03-26 162959.png')

