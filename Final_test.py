# import time
#
# import streamlit as st
#
# from Llm_prompt import gen_promt
# import pathlib
#
#
# # Function to load CSS from the 'assets' folder
# def load_css(file_path):
#     with open(file_path) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#
#
# # Load the external CSS
# css_path = pathlib.Path("assets/custom_css.css")
# load_css(css_path)
#
#
# def change_text(final_val):
#     chag_txt="Change Text with Ai broooooooooooo" + final_val
#     return chag_txt
# # creating a placeholder for the fixed sized textbox
# if "final_val_acct" not in st.session_state:
#     st.session_state.final_val_acct = False
# if "value_in_str" not in st.session_state:
#     st.session_state.value_in_str = []
# if "value_in_str_2" not in st.session_state:
#     st.session_state.value_in_str_2 = []
#
# j=0
# with st.container(border=True):
#     num_boxes = st.number_input("Enter the number of text boxes:", max_value=10, step=1)
#     if num_boxes == 0:
#         st.session_state.value_in_str.pop()
#         st.session_state.value_in_str_2.pop()
#     for i in range(num_boxes):
#         #st.success(f"First {i}")
#         st.success(range(num_boxes))
#         j=j+1
#         #st.success(f"final value {j}")
#         with st.container():
#             logtxtbox = st.empty()
#             logtxtbox_1 = st.empty()
#
#             # if "value_desc" not in st.session_state:
#             #     st.session_state.value_desc=[""]
#            # st.error(i)
#             #st.success(len(st.session_state.value_in_str))
#             if len(st.session_state.value_in_str) == int(i+1):
#                 print("All values are macthing")
#             if len(st.session_state.value_in_str)<int(i+1):
#                 st.session_state.value_in_str.append("")
#
#             if len(st.session_state.value_in_str)>len(range(num_boxes)):
#                 st.info(len(st.session_state.value_in_str))
#                 #st.info(f"I value for pop {i+1}")
#                 st.session_state.value_in_str.pop()
#
#             if len(st.session_state.value_in_str_2) == int(i+1):
#                 print("All values are macthing")
#             if len(st.session_state.value_in_str_2)<int(i+1):
#                 st.session_state.value_in_str_2.append("")
#
#             if len(st.session_state.value_in_str_2)>len(range(num_boxes)):
#                 st.info(len(st.session_state.value_in_str_2))
#                 st.info(f"I value for pop {i+1}")
#                 st.session_state.value_in_str_2.pop()
#             #st.success(st.session_state.value_in_str)
#
#             # if st.session_state.value_in_str[i]:
#             #     #st.success(st.session_state.value_in_str)
#             #     st.session_state.value_in_str[i] = st.session_state.value_in_str[i]
#             #     #st.success("value str " + str(st.session_state.value_in_str))
#             #     #st.success(st.session_state.value_in_str)
#             # if st.session_state.value_in_str_2[i]:
#             #     with st.spinner():
#             #         st.success(f"Value of b is {st.session_state.value_in_str_2[i]} for i value {i}")
#             #         time.sleep(5)
#             #     st.session_state.value_in_str_2[i] = st.session_state.value_in_str_2[i]
#                 #st.success("Value str 2 " + str(st.session_state.value_in_str_2))
#             a=logtxtbox.text_area("Logging: ",st.session_state.value_in_str[i] ,key="logtxtbox_"+str(i))
#             b = logtxtbox_1.text_input("Logging: input ", st.session_state.value_in_str_2[i], key="logtxtbox_input" + str(i))
#             #st.session_state.value_in_str[i]=a
#             #st.success(a)
#             #b=logtxtbox_1.text_input("Next level ",st.session_state.value_desc[i-1],key="logtxtbox_1_"+str(i))
#             api_vertex="AIzaSyAnW5TaAl2WG2QmtsEiKifTtnpAHKiiIVI"
#             if st.session_state.final_val_acct:
#                 st.success(st.session_state.value_in_str)
#                 st.success(st.session_state.value_in_str_2)
#                 #final_value =  "Make the text professional without adding or appending any content " + a #gen_promt(api_vertex,)
#                 next_level = "1 " + a #gen_promt(api_vertex,#)
#                 next_level_1 = "2 " + b
#                 #st.success(next_level+ "value :" + str(i))
#                 st.session_state.value_in_str[i] = next_level
#                 st.session_state.value_in_str_2[i] = next_level_1
#                 if i == len(range(num_boxes-1)):
#                     st.info(f"{i} in {len(range(num_boxes-1))}")
#                     st.session_state.final_val_acct=False
#                     st.rerun()
#                 #st.session_state.value_desc.append(final_value)
#                 #st.session_state.value_in_str[i+1]=next_level
#                 #a=logtxtbox.text_area("Logging: ", st.session_state.value_in_str[i],key="logtxtbox_1_ai"+str(i))#st.session_state.value_brief[i-1],)
#                 #b=logtxtbox_1.text_input("Logging: inpiut ", st.session_state.value_in_str_2[i],key="logtxtbox_12_ai"+str(i))
#                 #st.rerun()
#
# if "final_val_acct" not in st.session_state:
#     st.session_state.final_val_acct = False
#             #Make the text professional without adding or appending any content
#             #"Make the text professional don't add anything in at start of text and don't  give any text after providing changes and also no special characters "
# if st.button(":material/smart_toy:",key="pulse",help="Ai Assistant"):
#     st.session_state.final_val_acct=True
#     st.rerun()
# else:
#     st.session_state.final_val_acct = False
# # if 'my_list' not in st.session_state:
# #     st.session_state.my_list = []
# #
# # # Append a new item to the list
# # new_item = "New Item"
# # st.session_state.my_list.append(new_item)
#
# # """import streamlit as st
# #
# # # Function to simulate the text transformation
# # def gen_promt(api_key, text):
# #     # Replace this with actual API call logic
# #     return "Processed: " + text
# #
# # # Input for the number of text boxes
# # num_boxes = st.number_input("Enter the number of text boxes:", min_value=1, max_value=10, step=1, value=1)
# #
# # # Placeholder for dynamic text boxes
# # text_boxes = [st.empty() for _ in range(num_boxes)]
# # text_inputs = [st.empty() for _ in range(num_boxes)]
# #
# # # Dictionary to hold user inputs
# # user_inputs = ""
# # st.success(text_inputs)
# # # Display the dynamic text boxes
# # for i in range(num_boxes):
# #     user_inputs_0 = text_boxes[i].text_area(f"Logging {i+1}:", user_inputs, height=100)
# #     user_inputs_1 = text_inputs[i].text_input(f"Next Level {i+1}:", user_inputs)
# #
# # api_vertex = "AIzaSyAnW5TaAl2WG2QmtsEiKifTtnpAHKiiIVI"
# #
# # if st.button("Submit"):
# #     processed_results = {}
# #     for i in range(num_boxes):
# #         # Process each text box's input
# #         final_value = gen_promt(api_vertex, "Make the text professional without adding or appending any content " + user_inputs[i])
# #         next_level = gen_promt(api_vertex, "Make the text professional without adding or appending any content do not exceed 150 characters " + user_inputs[f"next_level_{i}"])
# #
# #         # Update the placeholders with processed results
# #         text_boxes[i].text_area(f"Logging {i+1}:", final_value, height=100)
# #         text_inputs[i].text_input(f"Next Level {i+1}:", next_level)
# # """

import os
import base64
import json
from google.cloud import bigquery

# Retrieve and decode the base64-encoded JSON key
from mail_dellivery_otp import send_otp

encoded_key = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not encoded_key:
    raise ValueError("Environment variable GOOGLE_APPLICATION_CREDENTIALS is not set")

# Decode and parse the JSON key
decoded_key = base64.b64decode(encoded_key).decode("utf-8")
credentials_info = json.loads(decoded_key)

# Authenticate using from_service_account_info
client = bigquery.Client.from_service_account_info(credentials_info)

# Now you can use the client
query = "SELECT CURRENT_TIMESTAMP() as current_time"
query_job = client.query(query)
result = query_job.result()

for row in result:
    print(f"Current time: {row['current_time']}")


send_otp("suprithvasista829@gmail.com","1234")