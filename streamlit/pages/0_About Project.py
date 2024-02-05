import streamlit as st
import os
from pathlib import Path

def run():
    st.set_page_config(
        page_title="About Project",
        page_icon="💻",
    )

    st.title("About Project")
    st.sidebar.title("CS259 Final Year Project")

    st.write("## Project Overview")

    st.markdown(
        """
        The project was developed on a x86_64 PC running Ubuntu 20.04 through the WSL2 protocol. The specifications of the PC are as follows:\\
        \\
            - CPU: AMD Ryzen 3700X\\
            - RAM: 16GB DDR4\\
            - GPU: NVIDIA RTX 3060 12GB\\
            \\
            The project was developed using Python 3.10.2 and the following libraries:\\
            \\
            - Tensorflow\\
            - Keras\\
            - Matplotlib\\
            - Numpy\\
            - Scikit-learn\\
            - Streamlit\\
            \\
            The model structure is laid out as follows:
    """
    )

    st.write("## Model Structure")

    st.write("This model is based off a modified version of Lenet-5, which can be seen its structure below:")

    st.image("pages/images/structure.png", caption="Model Structure", use_column_width=True)

    # use Path to get image from pages/images/structure.png




    




if __name__ == "__main__":
    run()