import streamlit as st

import makefile
import tools
import fourmeasure
import phrase

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)
    

def main():
    st.header("ピアノ練習システム")
    uploaded_file = st.file_uploader("練習したい曲のファイルをアップロードしてください")
    st.write("default: 'sonatine m.clementi op.36 no.1'")

    st.subheader("Usage:")
    st.write("main: メインページ（現在表示されている画面）です．")
    st.write("step1: 楽譜が4小節ごとに表示されます．楽曲を通す練習に便利です．")
    st.write("step2: 楽譜をフレーズごとに表示します．難しい箇所を練習するのに便利です，")

    tools.init("file")
    if uploaded_file:
        with open("sheet/"+st.session_state.date+".mxl", mode="wb") as f:
            f.write(uploaded_file.getvalue())
        file = "sheet/"+st.session_state.date+".mxl"

        makefile.mxl_ly(file)
        makefile.make_png("file")
        #fourmeasure.addcolor(st.session_state.m)
        #phrase.getphrase(st.session_state.l)
    else:
        file = "sheet/test_file.mxl"





if __name__ == "__main__":
    main()