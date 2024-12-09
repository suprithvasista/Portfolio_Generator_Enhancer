import streamlit as st
import time
import re
from mail_dellivery_otp import verify_otp, generate_otp, send_otp


def is_valid_gmail(url):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, url) is not None

def disable_text_box():
    st.session_state.disable_text = False

@st.dialog("Verify Otp")
def my_dialog():
    print("frist")
    if "disable_text" not in st.session_state:
        st.session_state.disable_text = True
    email_id=st.text_input("Enter valida email id.",key="email_id",help="eg:- user_name@gmail.com")
    if is_valid_gmail(email_id):
        st.info("Mail id entered is correct")
        dis_val=False
    else:
        if len(email_id)>0:
            st.error("Mail id entered is not in correct format")
        dis_val=True
    user_input = st.text_input("Enter otp send to mail.", max_chars=6, type='password', help="Enter Otp Sent to mail",
                               disabled=st.session_state.disable_text)

    if st.button('verify',disabled=dis_val, on_click=disable_text_box):
        otp_val=generate_otp()
        st.session_state.otp_value=otp_val
        time.sleep(1)
        send_otp(email_id,otp_val)
        st.info(f"Otp sent to mail: {email_id}")

    if len(user_input) ==6:
        if verify_otp(user_input,st.session_state.otp_value):
            st.success("Otp Validated Successfully")
            st.success("Redirecting to Deployment")
            st.session_state.disable_text = True
            time.sleep(1.5)
            st.session_state.email_id_for_conf=email_id
            st.session_state.mail_authentication_val=True
            st.rerun()
        else:
            st.session_state.mail_authentication_val = False
            st.error(f"Wrong otp Entered.")