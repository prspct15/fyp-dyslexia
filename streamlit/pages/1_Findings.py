import streamlit as st

def run():
    st.set_page_config(
        page_title="About Project",
        page_icon="💻",
    )

    st.title("About Project")
    st.sidebar.title("CS259 Final Year Project")

    st.write("The experiments ran and has returned these results:")

    st.write("## Accuracy")

    st.image("./images/acc-sep.png", caption="Accuracy Graph", use_column_width=True)

    st.write("Throughout 18 epochs, the training accuracy of the model has reported an impressive 97.5%, while for the validation accuracy, it has reported an accuracy of 85%, which is 12.5% off the training accuracy.")

    st.write("## Loss")

    st.image("./images/loss-sep.png", caption="Loss Graph", use_column_width=True)

    st.write("The loss graph shows that the model has obtained an impressively low training loss value at 2.5%, however, test loss shows concerning values, as it is approximately 30% off target, which may show signs of overfitting.")

    st.write("## Confusion Matrix")

    st.image("./images/conf-matrix.png", caption="Confusion Matrix", use_column_width=True)

    st.write("The confusion matrix shows that the model has a significantly lower accuracy for non-dyslexic handwriting in contrast to its dyslexic counterpart. This may be due to the fact that the model has been trained on a significantly higher amount of dyslexic handwriting samples in comparison to non-dyslexic samples. This may be resolved by training the model on a more balanced dataset.")


if __name__ == "__main__":
    run()