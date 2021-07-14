import streamlit as st
from PIL import Image
from summarization import summarize
from transformers import MBartTokenizer, MBartForConditionalGeneration

image = Image.open('images/clvr_logo3.png')
st.image(image, use_column_width=False)
st.header('Выделение из новости наиболее важной информации')


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_model(model_name='IlyaGusev/mbart_ru_sum_gazeta'):
    st.write("Download model")
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model


article_text = st.text_area("Введите текст ниже:", height=250)

if st.button('Преобразовать'):
    gif_runner = st.image('images/wait2.gif')
    tokenizer, model = load_model()
    summary = summarize(article_text, tokenizer, model)
    gif_runner.empty()
    st.write(summary)
