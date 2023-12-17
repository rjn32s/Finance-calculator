import streamlit as st

def display_animation():
    st.markdown(
        """
        <style>
        @keyframes move {
          0% {left: 0;}
          100% {left: calc(100% - 50px);}
        }

        @keyframes color-change {
          0% {background-color: red;}
          50% {background-color: green;}
          100% {background-color: blue;}
        }

        .animated-element {
          position: absolute;
          top: 50%;
          left: 0;
          width: 50px;
          height: 5px;
          animation: move 9s linear infinite, color-change 6s linear infinite;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="animated-element"></div>', unsafe_allow_html=True)
    st.title("FinCal")
    st.text("By - Rajan Shukla")

    st.markdown(
        """
        <style>
        @keyframes move {
          0% {left: 0;}
          100% {left: calc(100% - 50px);}
        }

        @keyframes color-change {
          0% {background-color: red;}
          50% {background-color: green;}
          100% {background-color: blue;}
        }

        .animated-element {
          position: absolute;
          top: 50%;
          left: 0;
          width: 50px;
          height: 5px;
          animation: move 12s linear infinite, color-change 3s linear infinite;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="animated-element"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        @keyframes move {
          0% {left: 10; width: 50px;}
          100% {left: calc(100% - 50px); width: 200px;}
        }

        @keyframes color-change {
          0% {background-color: red;}
          50% {background-color: green;}
          100% {background-color: blue;}
        }

        .animated-element {
          position: absolute;
          top: 50%;
          left: 0;
          width: 50px;
          height: 5px;
          animation: move 12s linear infinite, color-change 8s linear infinite;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="animated-element"></div>', unsafe_allow_html=True)

# Call the function to display the animated elements, title, and text

