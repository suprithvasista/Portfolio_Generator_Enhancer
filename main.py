import streamlit as st
from streamlit_option_menu import option_menu

from Script_generation import *
from big_query import port_list_extra
import requests

selected = option_menu(
        menu_title=None,
        options=["Home","Projects","Info-Hub"],
        icons=["house","book","info-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

if selected == "Home":
        side_bar_fun()
        ai_enhancer_func()
        main_class_value = main_code()
        main_code_string = main_mobile_code()
        color_man_value = clor_manager()
        nav_items_value = nav_item_func()
        skill_value = skill_item()
        hobby_work = hobby_work_project()
        profile_value = profile_links()
        footer_value = footer_code()

        if "mail_authentication_val" not in st.session_state:
                st.session_state.mail_authentication_val = False

        if st.button("Submit") or st.session_state.mail_authentication_val:
                if not st.session_state.mail_authentication_val:
                        my_dialog()
                if st.session_state.mail_authentication_val:
                        print("Inside of authen")
                        st.session_state['submit_git'] = 'submit_git_value'
                        st.session_state.mail_authentication_val = False
                else:
                        st.session_state['submit_git'] = 'not_submit_git_value'
                        if "deploy_git_vercel" not in st.session_state:
                                st.session_state['deploy_git_vercel'] = 'not_deploy_git_vercel'
        else:
                st.session_state['submit_git'] = 'not_submit_git_value'
                if "deploy_git_vercel" not in st.session_state:
                        st.session_state['deploy_git_vercel'] = 'not_deploy_git_vercel'
                else:
                        print("vercel no deploy")

        if st.session_state.submit_git == 'submit_git_value':
                rename_git_repo(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                st.session_state.project_name_git)
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git, 'lib/widgets/mian_mobile.dart',
                                  main_code_string[0])
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/widgets/main_desktop.dart', main_code_string[1])
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/main.dart', main_class_value)
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/constants/colors.dart', color_man_value)
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/constants/nav_items.dart', nav_items_value)
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/constants/skills_item.dart', skill_value)
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/utils/project_utils.dart', hobby_work)
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/constants/sns_links.dart', profile_value)
                git_file_updation(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                  st.session_state.project_name_git,
                                  'lib/widgets/footer.dart', footer_value)
                st.session_state['deploy_git_vercel'] = 'deploy_git_vercel'
                # st.session_state['submit_git'] = 'not_submit_git_value'
                st.rerun()

        if st.session_state.deploy_git_vercel == "deploy_git_vercel":
                ret_val = vercel_project_deployment(st.session_state.submit_vercel_token,
                                                    st.session_state.submit_git_cred_user_name + "/" + st.session_state.project_name_git,
                                                    st.session_state.project_name_git)
                if ret_val[0] != 1:
                        st.success(f"Successfully deployed application access link: {ret_val[1]}")
                        # st.write(st.session_state.email_id_for_conf)
                        final_execution(st.session_state.email_id_for_conf, ret_val[1],
                                        st.session_state.skills_list_val, "",
                                        st.session_state.platform_list_val,
                                        st.session_state.submit_git_cred_user_name,
                                        st.session_state.project_name_git, st.session_state.main_string_val,
                                        st.session_state.resume_name_val,
                                        st.session_state.resume_pdf_bytes, st.session_state.tag_line_about_you_val,
                                        st.session_state.photo_portfolio_val,
                                        st.session_state.scaffloldBg_val, st.session_state.bgLight1_val,
                                        st.session_state.bgLight2_val,
                                        st.session_state.textFieldBg_val,
                                        st.session_state.hintDark_val, st.session_state.yellowPrimary_val,
                                        st.session_state.yellowsecondary_val, st.session_state.whitePrimary_val,
                                        st.session_state.whilteSecondary_val, st.session_state.nav_item_list_val, "",
                                        "",
                                        "", "", st.session_state.sns_git_hub_val, st.session_state.sns_linkedin_val,
                                        st.session_state.sns_devpost_val, st.session_state.sns_gmail_val,
                                        st.session_state.sns_medium_val, st.session_state.footer_string_val,
                                        "", "", st.session_state.final_hobby_string_list_val,
                                        st.session_state.final_work_string_list_val,
                                        "", "",
                                        "", "", "", "", "")
                else:
                        st.error(ret_val[1])
                        st.error("Deployment error please check with admin.")
                st.session_state['submit_git'] = 'not_submit_git_value'
                st.session_state['deploy_git_vercel'] = 'not_deploy_git_vercel'
        else:
                print("Project not yet inserted.")

if selected == "Projects":
        if st.button("",icon=":material/refresh:",help="Refreshes Records"):
            st.session_state.data_extract_prof = True
            st.session_state.final_val_list_user_port_link = True
        if "data_extract_prof" not in st.session_state:
            st.session_state.data_extract_prof = True
        st.title("People Deployments",help="Just Gives Masked Names")
        if "final_val_list_user_port_link" not in st.session_state:
            st.session_state.final_val_list_user_port_link=True
        if "final_val_list_user_port_link_val" not in st.session_state:
            st.session_state.final_val_list_user_port_link_val=""

        if st.session_state.data_extract_prof:
            if st.session_state.final_val_list_user_port_link:
                with st.spinner():
                    removal=st.empty()
                    removal.info("Fetching project deployments")
                    time.sleep(3)
                    removal.empty()
                    removal.success("Fetched Project Details")
                    time.sleep(2)
                    removal.empty()
                final_val_list=port_list_extra()
            else:
                final_val_list=st.session_state.final_val_list_user_port_link_val
            if final_val_list:
                st.session_state.final_val_list_user_port_link_val=final_val_list
                # Create columns dynamically based on the input number
                conn = st.container(border=True)
                for row in final_val_list.result():
                    project_id_user_name = row[0]
                    project_id_user_url = row[1]
                    #st.success(project_id_user_url)
                    with conn:
                        col1 = st.columns(1)[0]
                        with col1:
                            st.link_button(project_id_user_name,url="https://"+project_id_user_url,use_container_width=True)
                #st.session_state.data_extract_prof=False
                st.session_state.final_val_list_user_port_link=False
            else:
                #st.session_state.data_extract_prof = False
                st.session_state.final_val_list_user_port_link = False
                st.error("Error fetching records")
if selected == "Info-Hub":
        st.title("Guidelines")
        st.header("Step 1")
        with st.container(border=True):
            st.header("Creating Git token Guide")
            VIDEO_URL = "https://www.youtube.com/watch?v=J-CSiw5CFWE"
            st.video(VIDEO_URL)
            st.write("""
            Link: https://github.com/settings/tokens\n
            To generate a personal access token (PAT) for GitHub, you can do the following:\n
            1.Log in to your GitHub account\n
            2.Click your profile photo in the upper-right corner and select Settings\n 
            3.Click Developer settings in the left sidebar\n
            4.Under Personal access tokens, click Generate new token\n 
            5.Enter a name for the token\n
            6.Select an expiration for the token\n 
            7.Select the scopes or permissions you want to grant the token\n 
            8.Click Generate token\n
            9.Copy and store the token in a safe place\n""")
        st.header("Step 2")
        with st.container(border=True):
            st.header("Creating Vercel token Guide")
            video_file = "https://raw.githubusercontent.com/suprithvasista/VercelTokenGeneration/main/Vercel_token_generation.mov"
            st.video(video_file)
            st.write("""
                    Link: https://vercel.com/account/settings/tokens\n
                    1.Click Create to open the create token modal.\n
                    2.Enter a descriptive name and click Create Token.\n
                    3.Choose the scope of access for the token from the dropdown.\n
                    4.Make a note of the token created as it will not be shown again.\n""")

        st.header("Demo Video")
        with st.container(border=True):
            st.video("https://www.youtube.com/watch?v=DaCe4OgAmyQ")
            # try:
            #     response = requests.get("https://github.com/suprithvasista/SuprithM_Portfolio/blob/main/assets/DataBricks.png?raw=true")
            #     response.raise_for_status()
            #     data = response.content,
            #     file_name = "pdf",
            #     st.download_button(":material/download:",data,file_name)
            # except requests.exceptions.RequestException as e:
            #     st.error(f"Error fetching the file: {e}")
            # col1, col2 = st.columns([10, 1], gap="medium", vertical_alignment="center")
            # file_paths=["PortfolioGenration_Doc.pdf","Portfolio_Generator_Presentation.pptx"]
            # for i in file_paths:
            #     with col1:
            #         st.markdown("""
            #         <style>
            #             write {
            #                 height:5px;
            #             }
            #         </style>
            #         """, unsafe_allow_html=True)
            #         st.write(':page_facing_up:', i)
            #     with col2:
            #         a = st.download_button(':material/download:', key=i, use_container_width=False)
                    # if a:
                    #     call_back_values(j)
                    #     st.rerun()