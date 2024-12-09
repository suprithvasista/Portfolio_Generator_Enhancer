from google.cloud import bigquery
import os
import base64
import json

def invoke_client():
    encoded_key = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not encoded_key:
        raise ValueError("Environment variable GOOGLE_APPLICATION_CREDENTIALS is not set")

    # Decode and parse the JSON key
    decoded_key = base64.b64decode(encoded_key).decode("utf-8")
    credentials_info = json.loads(decoded_key)
    client = bigquery.Client.from_service_account_info(credentials_info)
    return client


def insert_user_id_map_table(client, email_id) -> object:
    global user_id, valid_email, valid_user_id, valid_email_count

    query_for_val_email = f"""SELECT email_id,user_id FROM `bionic-kiln-443407-m6.authentication_dev.user_id_map` where email_id='{email_id}'"""
    query_job_verify_mail = client.query(query_for_val_email)

    query_for_val_email_count = f"""SELECT count(*) FROM `bionic-kiln-443407-m6.authentication_dev.user_id_map` where email_id='{email_id}'"""
    query_job_verify_mail_count = client.query(query_for_val_email_count)

    for row_count in query_job_verify_mail_count.result():
        valid_email_count=row_count[0]

    for row_1 in query_job_verify_mail.result():
        valid_email=row_1[0]
        valid_user_id=int(row_1[1])

    if int(valid_email_count) == 0 or not valid_email:
        user_id_val = """SELECT count(*) +1 FROM `bionic-kiln-443407-m6.authentication_dev.user_id_map` """
        query_job = client.query(user_id_val)
        for row in query_job.result():
            user_id=int(row[0])
        rows_to_insert = [
            {"user_id": user_id, "email_id": email_id}]

        errors = client.insert_rows_json('bionic-kiln-443407-m6.authentication_dev.user_id_map',
                                         rows_to_insert)  # Make an API request.
        if errors == []:
            print("New rows have been added.")
        else:
            print("Encountered errors while inserting rows: {}".format(errors))
        return user_id
    else:
        return valid_user_id


def insert_user_id_por_link_map(client, user_id, portfolio_link):

    global project_id
    project_id_num = f"""SELECT count(*) +1 FROM `bionic-kiln-443407-m6.authentication_dev.user_id_por_link_map` where user_id={user_id}"""
    query_job = client.query(project_id_num)
    for row in query_job.result():
        project_id=int(row[0])

    rows_to_insert = [
        {"user_id": user_id, "port_link": portfolio_link ,"project_id":project_id}]

    errors = client.insert_rows_json('bionic-kiln-443407-m6.authentication_dev.user_id_por_link_map',
                                     rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
    return project_id

def insert_skills_tech_data(client, user_id, projtect_id_num,skills_tech_indi_val,upload_icon_tech_data_val,platform_titile_val):
    rows_to_insert = [
        {"user_id": user_id, "project_id": projtect_id_num, "skills_tech_indi": skills_tech_indi_val, "upload_icon_tech_data": upload_icon_tech_data_val, "platform titile": platform_titile_val}]

    errors = client.insert_rows_json('bionic-kiln-443407-m6.authentication_dev.skills_tech_data',
                                     rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def insert_user_portfolio_data_map(client, user_id,git_user_name_val,
                                   project_name_git_vercel_val,main_icon_tab_logo_name_val,
                                   Cv_name_dowloaded_val,resume_data_bytes_val,
                                   main_screen_tag_line_val,main_user_photo_logo_val,
                                   color_bg_scaffold_val,back_ground_color1_val,
                                   back_ground_color2_val,text_field_color_bg_val,
                                   background_hint_black_val,bt_color_primary_val,
                                   bt_color_secondary_val,text_color_primary_val,
                                   text_color_secondary_val,nav_bar_name1_val,
                                   nav_bar_name2_val,nav_bar_name3_val,nav_bar_name4_val,
                                   nav_bar_name5_val,git_prof_link_val,link_prof_link_val,
                                   devpost_link_val,gmail_id_val,medium_profile_link_val,
                                   footer_string_val,project_number_val):
    rows_to_insert = [
        {"user_id": user_id, "git_user_name": git_user_name_val, "project_name_git_vercel": project_name_git_vercel_val, "main_icon_tab_logo_name": main_icon_tab_logo_name_val, "Cv_name_dowloaded": Cv_name_dowloaded_val, "resume_data_bytes": resume_data_bytes_val, "main_screen_tag_line": main_screen_tag_line_val, "main_user_photo_logo": main_user_photo_logo_val,
         "color_bg_scaffold": color_bg_scaffold_val,"back_ground_color1": back_ground_color1_val, "back_ground_color2": back_ground_color2_val,
         "text_field_color_bg": text_field_color_bg_val, "background_hint_black": background_hint_black_val,
         "bt_color_primary": bt_color_primary_val,"bt_color_secondary": bt_color_secondary_val,
         "text_color_primary": text_color_primary_val, "text_color_secondary": text_color_secondary_val,
         "nav_bar_name1": nav_bar_name1_val, "nav_bar_name2": nav_bar_name2_val, "nav_bar_name3": nav_bar_name3_val,
         "nav_bar_name4":nav_bar_name4_val,"nav_bar_name5": nav_bar_name5_val,"git_prof_link": git_prof_link_val,
         "link_prof_link": link_prof_link_val, "devpost_link": devpost_link_val,
         "gmail_id": gmail_id_val, "medium_profile_link": medium_profile_link_val, "footer_string": footer_string_val,
         "project_number": project_number_val}]

    errors = client.insert_rows_json('bionic-kiln-443407-m6.authentication_dev.user_portfolio_data_map',
                                     rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def insert_work_hobby_table(client, user_id, upload_image_val, project_title_val,
                            project_brief_desc_val,project_full_desc_val,
                            project_verfier_link_val,project_identifier_flag_val,
                            play_store_link_val,app_store_link_val,web_link_val,
                            pypi_link_val,git_repo_val,project_id_val):
    rows_to_insert = [
        {"user_id": user_id, "upload_image": upload_image_val,
         "project_title": project_title_val,"project_brief_desc": project_brief_desc_val,
         "project_full_desc": project_full_desc_val,"project_verfier_link": project_verfier_link_val,
         "project_identifier_flag": project_identifier_flag_val,"play_store_link": play_store_link_val,
         "app_store_link": app_store_link_val,"web_link": web_link_val,
         "pypi_link": pypi_link_val,"git_repo": git_repo_val, "project_id": project_id_val}]

    errors = client.insert_rows_json('bionic-kiln-443407-m6.authentication_dev.work_hobby_table',
                                     rows_to_insert)  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

def port_list_extra():
    cl_val_link = invoke_client()
    project_id_num_port_link = f"""SELECT "Name_" || user_id ||"_" || project_id, port_link FROM `bionic-kiln-443407-m6.authentication_dev.user_id_por_link_map` order by user_id ,project_id"""
    try:
        query_job_res_link = cl_val_link.query(project_id_num_port_link)
        return query_job_res_link
    except:
        return False


def final_execution(emial_id,portLink,skills_tech_indi_val,upload_icon_tech_data_val,platform_titile_val,git_user_name_val,
                    project_name_git_vercel_val,main_icon_tab_logo_name_val,Cv_name_dowloaded_val,resume_data_bytes_val,main_screen_tag_line_val,main_user_photo_logo_val,
                    color_bg_scaffold_val, back_ground_color1_val,back_ground_color2_val, text_field_color_bg_val,
                    background_hint_black_val, bt_color_primary_val,bt_color_secondary_val, text_color_primary_val,
                    text_color_secondary_val, nav_bar_name1_val,nav_bar_name2_val, nav_bar_name3_val, nav_bar_name4_val,
                    nav_bar_name5_val, git_prof_link_val, link_prof_link_val,devpost_link_val, gmail_id_val, medium_profile_link_val,footer_string_val,
                    upload_image_val, project_title_val,project_brief_desc_val, project_full_desc_val,project_verfier_link_val, project_identifier_flag_val,
                    play_store_link_val, app_store_link_val, web_link_val,pypi_link_val, git_repo_val):

    cl_val = invoke_client()
    user_id_ret=insert_user_id_map_table(cl_val, emial_id)
    project_id_ret=insert_user_id_por_link_map(cl_val,user_id_ret,portLink)
    insert_skills_tech_data(cl_val, user_id_ret, project_id_ret,skills_tech_indi_val,upload_icon_tech_data_val,platform_titile_val)
    insert_user_portfolio_data_map(cl_val,user_id_ret,git_user_name_val,
                                   project_name_git_vercel_val,main_icon_tab_logo_name_val,Cv_name_dowloaded_val,resume_data_bytes_val,
                                   main_screen_tag_line_val,main_user_photo_logo_val,color_bg_scaffold_val,back_ground_color1_val,
                                   back_ground_color2_val,text_field_color_bg_val,background_hint_black_val,bt_color_primary_val,
                                   bt_color_secondary_val,text_color_primary_val,text_color_secondary_val,nav_bar_name1_val,
                                   nav_bar_name2_val,nav_bar_name3_val,nav_bar_name4_val,nav_bar_name5_val,git_prof_link_val,link_prof_link_val,
                                   devpost_link_val,gmail_id_val,medium_profile_link_val,footer_string_val,project_id_ret)
    insert_work_hobby_table(cl_val, user_id_ret, upload_image_val, project_title_val,
                            project_brief_desc_val, project_full_desc_val,project_verfier_link_val, project_identifier_flag_val,
                            play_store_link_val, app_store_link_val, web_link_val,pypi_link_val, git_repo_val, project_id_ret)