import streamlit as st
from style import global_page_style2


if __name__ == "__main__":
    global_page_style2()
        # Create 5 columns  
    col1, col2, col3, col4, col5, col6 = st.columns(6)  
      
    # Place the image in the middle column (col3) and ensure it retains its original size  
    with col3:  
        st.image('./images/logo.png', use_column_width=False)   
    st.title("Overview: Ice Cream Bot")
    st.warning("Coming soon...")