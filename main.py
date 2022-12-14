import streamlit as st
import xml.etree.ElementTree as ET

import makefile
import tools
import music21

st.set_page_config(
    page_title="ピアノ練習システム",
    layout="wide",
    initial_sidebar_state="expanded"
)
    

def main():
    st.header("ピアノ練習システム")
    uploaded_file = st.file_uploader("練習したい曲のファイルをアップロードしてください ＊まだ未完成＊")
    st.write("default: 'sonatine m.clementi op.36 no.1'")

    st.subheader("Usage:")
    st.write("main: メインページ（現在表示されている画面）です．")
    st.write("step1: 楽譜が4小節ごとに表示されます．楽曲を通す練習に便利です．")
    st.write("step2: 楽譜をフレーズごとに表示します．難しい箇所を練習するのに便利です，")

    tools.init("")
    if uploaded_file:
        with open("sheet/file.mxl", mode="wb") as f:
            f.write(uploaded_file.getvalue())
        makefile.mxl_ly("sheet/file.mxl")
        makefile.makesvg("file")

    else:
        file = "sheet/test_file.mxl"
        makefile.mxl_ly(file)



        
    


if __name__ == "__main__":
    main()