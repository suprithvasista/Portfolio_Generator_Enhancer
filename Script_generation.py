import time

import streamlit as st
import re
import base64

# Function to validate the input URL
from Llm_prompt import gen_promt
from big_query import final_execution
from git_forker import git_repo_fork, rename_git_repo
from git_modification import git_file_updation
from mail_id_validation import my_dialog
from upload_file import photo_upload
from vercel_api_integration import vercel_project_deployment
import pathlib


# Function to load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load the external CSS
css_path = pathlib.Path("assets/custom_css.css")
load_css(css_path)


def is_valid_github_url(url):
    pattern = r'^https:\/\/github\.com\/.+'
    return re.match(pattern, url) is not None


def is_valid_linkedin_url(url):
    pattern = r'^https:\/\/www\.linkedin\.com\/in\/.+'
    return re.match(pattern, url) is not None


def is_valid_devpost_url(url):
    pattern = r'^https:\/\/devpost\.com\/.+'
    return re.match(pattern, url) is not None


def is_valid_gmail(url):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, url) is not None


def is_valid_medium_url(url):
    pattern = r'^https:\/\/medium\.com\/.+'
    return re.match(pattern, url) is not None


def image_val_upload(uploaded_file):
    # Check if the user has uploaded a file
    if uploaded_file is not None:
        # Display the uploaded image
        # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        # Convert the uploaded image to base64
        image_bytes = uploaded_file.read()  # Read the file in binary mode
        encoded_content = base64.b64encode(image_bytes).decode()  # Base64 encode
        return encoded_content


def ai_enhancer_func():
    if "block_ai_work" not in st.session_state:
        st.session_state.block_ai_work = False
    if "block_ai_hobby" not in st.session_state:
        st.session_state.block_ai_hobby = False
    with st.container(border=True):
        st.subheader("Click to rewrite and refine content")
        st.info("Fill in the project details before using the ai feature")
        if st.session_state.block_ai_work and st.session_state.block_ai_hobby:
            dis_ai_but = False
        else:
            dis_ai_but = True
        if st.button(":material/smart_toy:", key="pulse", help="Ai Assistant", disabled=dis_ai_but):
            st.session_state.final_val_acct = True
            st.session_state.work_proj_val = True
            st.session_state.hobby_proj_val = True
            st.info("Fine tuning in progress..")
            # st.rerun()
        else:
            st.session_state.final_val_acct = False
            st.session_state.work_proj_val = False
            st.session_state.hobby_proj_val = False
            # st.rerun()


def profile_links():
    st.title("Social Media Links")
    with st.container(border=True):
        sns_git_hub = st.text_input("Your Git Profile Link", placeholder="Git profile",
                                    help="eg:- https://github.com/suprithvasista/")
        if sns_git_hub:
            if is_valid_github_url(sns_git_hub.lower()):
                sns_git_hub = '"' + sns_git_hub + '"'
                st.success("Valid GitHub URL!")
            else:
                st.error("Invalid URL! Please enter a URL that starts with 'https://github.com/username'.")
        else:
            sns_git_hub = '"' + "https://github.com/" + '"'

        sns_linkedin = st.text_input("Your Linkedin Profile Link", placeholder="Linkedin profile",
                                     help="eg:- https://www.linkedin.com/in/suprithm1/")

        if sns_linkedin:
            if is_valid_linkedin_url(sns_linkedin.lower()):
                sns_linkedin = '"' + sns_linkedin + '"'
                st.success("Valid Linkedin URL!")
            else:
                st.error("Invalid URL! Please enter a URL that starts with 'https://www.linkedin.com/in/username'.")
        else:
            sns_linkedin = '"' + "https://www.linkedin.com/in/" + '"'

        sns_devpost = st.text_input("Your Devpost Profile Link", placeholder="Devpost profile",
                                    help="eg:- https://devpost.com/suprithvasista829/")

        if sns_devpost:
            if is_valid_devpost_url(sns_devpost.lower()):
                sns_devpost = '"' + sns_devpost + '"'
                st.success("Valid Devpost Profile URL!")
            else:
                st.error("Invalid URL! Please enter a URL that starts with 'https://devpost.com/username'.")
        else:
            sns_devpost = '"' + "https://devpost.com/" + '"'

        sns_gmail = st.text_input("Your Gmail", placeholder="Gmail",
                                  help="eg:- username@domain.com")

        if sns_gmail:
            if is_valid_gmail(sns_gmail):
                sns_gmail = '"' + sns_gmail + '"'
                st.success("Valid Mail!")
            else:
                st.error("Invalid Mail! Please enter a Mail that starts with 'username@gmail.com'.")
        else:
            sns_gmail = '"' + "" + '"'

        sns_medium = st.text_input("Your Medium Profile Link", placeholder="Medium Profile Link",
                                   help="eg:- https://medium.com/@suprithvasista829")

        if sns_medium:
            if is_valid_medium_url(sns_medium):
                sns_medium = '"' + sns_medium + '"'
                st.success("Valid Medium URL!")
            else:
                st.error("Invalid URL! Please enter a URL that starts with 'https://medium.com/username'.")
        else:
            sns_medium = '"' + "https://medium.com/" + '"'

        sns_links = """
        class SnsLinks{\n
          static const String github=""" + sns_git_hub + ";" + """\n
          static const String linkedin=""" + sns_linkedin + ";" + """\n
          static const String devpost=""" + sns_devpost + ";" + """\n
          static const String gmail=""" + sns_gmail + ";" + """\n
          static const String medium=""" + sns_medium + ";" + """\n
        }
        """
        st.session_state.sns_git_hub_val = sns_git_hub
        st.session_state.sns_linkedin_val = sns_linkedin
        st.session_state.sns_devpost_val = sns_devpost
        st.session_state.sns_gmail_val = sns_gmail
        st.session_state.sns_medium_val = sns_medium
        # st.success(sns_links)
        return sns_links


def color_pickrer(key_val):
    # Display the color picker
    color = st.color_picker(f"Pick A Color {key_val}", "#ff0000", key=key_val)  # Default to red

    # Set the alpha value (0-255, where 255 is fully opaque)
    alpha = 255  # You can adjust this value

    # Convert hex to RGB
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)

    # Create the ARGB format
    argb = f'0x{alpha:02x}{r:02x}{g:02x}{b:02x}'
    st.write(f"ARGB format for {key_val}:", argb)
    return argb


def clor_manager():
    st.title("Background color")
    with st.container(border=True):
        # st.header("Scaffold color")
        scaffloldBg = color_pickrer('scaffloldBg')
        # st.header("background color one")
        bgLight1 = color_pickrer('bgLight1')
        # st.header("background color two")
        bgLight2 = color_pickrer('bgLight2')
        # st.header("textFieldBg color")
        textFieldBg = color_pickrer('textFieldBg')
        # st.header("hintDark color")
        hintDark = color_pickrer('hintDark')
        # st.header("Buttons color primary")
        yellowPrimary = color_pickrer('buttoncolorPrimary')
        # st.header("Buttons color secondary")
        yellowsecondary = color_pickrer('buttoncolorsecondary')
        # st.header("Text color primary")
        whitePrimary = color_pickrer('textcolorPrimary')
        # st.header("Text color secondary")
        whilteSecondary = color_pickrer('textcolorSecondary')

        st.session_state.scaffloldBg_val = scaffloldBg
        st.session_state.bgLight1_val = bgLight1
        st.session_state.bgLight2_val = bgLight2
        st.session_state.textFieldBg_val = textFieldBg
        st.session_state.hintDark_val = hintDark
        st.session_state.yellowPrimary_val = yellowPrimary
        st.session_state.yellowsecondary_val = yellowsecondary
        st.session_state.whitePrimary_val = whitePrimary
        st.session_state.whilteSecondary_val = whilteSecondary

        colors = """import 'dart:ui';\n
        class CustomColor{\n
        static const Color scaffloldBg = Color(""" + scaffloldBg + """);\n
        static const Color bgLight1 = Color(""" + bgLight1 + """);\n
        static const Color bgLight2 = Color(""" + bgLight2 + """ );\n
        static const Color textFieldBg = Color(""" + textFieldBg + """);\n
        static const Color hintDark = Color(""" + hintDark + """);\n
        static const Color yellowsecondary = Color(""" + yellowsecondary + """);\n
        static const Color yellowPrimary = Color(""" + yellowPrimary + """);\n
        static const Color whitePrimary = Color(""" + whitePrimary + """);\n
        static const Color whilteSecondary = Color(""" + whilteSecondary + """);\n 
        }\n"""
        # st.success(colors)
        return colors


def nav_item_func():
    st.title("Navigator Menu Names", help="Pleas Keep Below 10 Characters")
    with st.container(border=True):
        Home = st.text_input("Nav item fisrt header name", max_chars=10, help="eg.Home")
        Skills = st.text_input("Nav item second header name", max_chars=10, help="eg.Skills")
        Projects = st.text_input("Nav item third header name", max_chars=10, help="eg.Projects")
        Contact = st.text_input("Nav item fourth header name", max_chars=10, help="eg.Contact")
        Blog = st.text_input("Nav item fifth header name", max_chars=10, help="eg.Blog")
        if not Home:
            Home = "Home"
        if not Skills:
            Skills = "Skills"
        if not Projects:
            Projects = "Projects"
        if not Contact:
            Contact = "Contact"
        if not Blog:
            Blog = "Blog"
        nav_item_list = '"' + Home + '"' + "," + '"' + Skills + '"' + "," + '"' + Projects + '"' + "," + '"' + Contact + '"' + "," + '"' + Blog + '"'
        nav_item = """import 'package:flutter/material.dart';\n
                    List < String > navtitles = [""" + nav_item_list + """];\n
                    // For mobiles\n
                    List < IconData > navIcons = [\n
                        Icons.home,\n
                        Icons.handyman_outlined,\n
                        Icons.apps,\n
                        Icons.quick_contacts_mail,\n
                        Icons.web,\n
                    ];"""
        # st.success(nav_item)
        st.session_state.nav_item_list_val = nav_item_list
        return nav_item


def footer_code():
    st.title("Footer String")
    with st.container(border=True):
        footer_string = st.text_input("Enter Footer String", help="eg:-Made by Suprith M with Flutter 3.1.0")
        footer = """import 'package:flutter/material.dart';\n
        import '../constants/colors.dart';\n
        \n
        class Footer extends StatelessWidget {\n
        const Footer({Key? key}): super(key: key\n
        );\n
        @override\n
        Widget\n
        build(BuildContext\n
        context) {\n
        return Container(\n
            padding: const\n
        EdgeInsets.symmetric(vertical: 20),\n
        width: double.maxFinite,\n
        alignment: Alignment.center,\n
        child: const\n
        Text(""" + '"' + footer_string + " Credit @Suprith M" + '"' + """,\n
             style: TextStyle(fontWeight: FontWeight.w400,\n
                                          color: CustomColor.whilteSecondary,\n
        ),\n
        ),\n
        );\n
        }\n
        }\n"""
        # st.success(footer)
        st.session_state.footer_string_val = footer_string
        return footer


def main_code():
    st.title("Main Icon Name")
    with st.container(border=True):
        main_string = st.text_input("Main screen tab logo", help='eg;-Suprith M')
        st.session_state.main_string_val = main_string
        if not main_string:
            main_string = "FlutterPortfolio"
        main = """import 'package:flutter/material.dart';\n
        import'package:porfoliojob/pages/home_page.dart';\n
        void main()\n
        {\n
            runApp(const\n
        MyApp());\n
        }\n

        class MyApp extends StatelessWidget {\n
        const MyApp({super.key});\n
        \n
        // This widget is the root of your application.\n
        @ override\n
        Widget build(BuildContext context) {\n
        \n
        return MaterialApp(\n
            debugShowCheckedModeBanner: false,\n
                                        theme: ThemeData.dark(),\n
        title: '""" + main_string + """',\n
        home: const\n
        HomePage(),\n
        );\n
        }\n
        }\n"""

        # st.success(main)
        return main


def main_mobile_code():
    st.title("Main Information")
    if "resume_pdf_bytes" not in st.session_state:
        st.session_state.resume_pdf_bytes = ""
    if "photo_portfolio_val" not in st.session_state:
        st.session_state.photo_portfolio_val = ""
    with st.container(border=True):
        resume_name = st.text_input("Cv Name When Downloaded", help="suprith_m_resume")
        st.session_state.resume_name_val = resume_name
        Resume_CV = st.file_uploader("Upload Your Resume Here", accept_multiple_files=False, type=['pdf'], key="Resume")
        tag_line_about_you = st.text_input("Tag Line about Your Self", help="Hi I am Suprith M AKA Data Engineer.")
        st.session_state.tag_line_about_you_val = tag_line_about_you
        photo_portfolio = st.file_uploader("Photo of you to display in the portfolio", accept_multiple_files=False,
                                           type=['png', 'jpg'], key="Photo")
        if Resume_CV and st.session_state.submit_git == 'submit_git_value':
            resume_pdf = image_val_upload(Resume_CV)
            st.session_state.resume_pdf_bytes = resume_pdf
            photo_upload(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                         st.session_state.project_name_git,
                         'public/' + resume_name + '.pdf', resume_pdf)

        if photo_portfolio and st.session_state.submit_git == 'submit_git_value':
            photo_portfolio_photo = image_val_upload(photo_portfolio)
            st.session_state.photo_portfolio_val = photo_portfolio_photo
            photo_upload(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                         st.session_state.project_name_git,
                         'assets/' + photo_portfolio.name if photo_portfolio else 'default_profile.png',
                         photo_portfolio_photo)
        if photo_portfolio:
            photo_portfolio_name = photo_portfolio.name
        else:
            photo_portfolio_name = 'default_profile.png'
            # https://github.com/sumanthvasista107/testRepo_test/blob/main/public/Test.pdf
        main_moblie_code = """\n
        import 'package:flutter/material.dart';\n
        import 'dart:html' as html; // Import for web downloads\n
        import '../constants/colors.dart';\n
        \n
        class MainMobile extends StatelessWidget {\n
        const MainMobile({super.key, required this.onNavItemTapSocialMobile});\n
        final Function(int) onNavItemTapSocialMobile;\n
        \n
        // Function to download PDF from the local files in the web directory\n
        void downloadPDF() {\n
        const url = 'https://github.com/""" + st.session_state.submit_git_cred_user_name + "/" + st.session_state.project_name_git + """/blob/main/public/""" + resume_name + """.pdf?raw=true'; // The relative path to your PDF in the web directory\n
        final anchor = html.AnchorElement(href: url)\n
        ..setAttribute('download', '""" + resume_name + """.pdf') // Name of the downloaded file\n
            ..click();\n
        }\n
        \n
        @override\n
        Widget build(BuildContext context) {\n
            final screenSize = MediaQuery.of(context).size;\n
            final screenWidth = screenSize.width;\n
            final screenHeight = screenSize.height;\n
        \n
        return Container(\n
            margin: const EdgeInsets.symmetric(horizontal: 40.0, vertical: 30.0),\n
            height: screenHeight,\n
            constraints: const BoxConstraints(\n
            minHeight: 560.0,\n
        ),\n
        child: Column(\n
            mainAxisAlignment: MainAxisAlignment.start,\n
                               crossAxisAlignment: CrossAxisAlignment.center,\n
        children: [\n
                  // Avatarimage\n
        ShaderMask(\n
            shaderCallback: (bounds)\n
        {\n
        return LinearGradient(colors: [\n
            CustomColor.scaffloldBg.withOpacity(0.6),\n
            CustomColor.scaffloldBg.withOpacity(0.6),\n
        ]).createShader(bounds);\n
        },\n
        blendMode: BlendMode.srcATop,\n
        child: Image.asset(\n
        """ + '"assets/' + photo_portfolio_name + '"' + """,\n
        width: screenWidth / 2,\n
        ),\n
        ),\n
        const SizedBox(height: 30.0),\n
        const Align(\n
            alignment: Alignment.topLeft,\n
        child: Text(\n
        """ + '"' + tag_line_about_you + '"' + """,\n
        style: TextStyle(\n
            fontSize: 24.0,\n
                      height: 1.5,\n
        fontWeight: FontWeight.bold,\n
        color: CustomColor.whitePrimary,\n
        ),\n
        ),\n
        ),\
        const SizedBox(height: 15),\n
        Align(\n
            alignment: Alignment.topLeft,\n
        child: SizedBox(\n
        width: 180.0,\n
        child: ElevatedButton(\n
            onPressed: ()\n
        {\n
            onNavItemTapSocialMobile(3);\n
        },\n
        style: ElevatedButton.styleFrom(\n
            shape: RoundedRectangleBorder(\n
            borderRadius: BorderRadius.circular(20.0),\n
        ),\n
        backgroundColor: CustomColor.yellowPrimary,\n
        ),\n
        child: const\n
        Text("Get in touch", style: TextStyle(color: CustomColor.whitePrimary), ),\n
        ),\n
        ),\n
        ),\n
        const SizedBox(height: 15), // Add some spacing\n
        Align(\n
            alignment: Alignment.topLeft,\n
        child: SizedBox(\n
        width: 180.0,\n
        child: ElevatedButton(\n
            onPressed: downloadPDF, // Call the download function\n
        style: ElevatedButton.styleFrom(\n
            shape: RoundedRectangleBorder(\n
            borderRadius: BorderRadius.circular(20.0),\n
        ),\n
        backgroundColor: CustomColor.yellowPrimary,\n
        ),\n
        child: const\n
        Text("Download Resume", style: TextStyle(color: CustomColor.whitePrimary), ),\n
        ),\n
        ),\n
        ), // Download PDF buttoN\n
        ],\n
        ),\n
        );\n
        }\n
        }\n"""
        main_desktop_code = """
        import 'package:flutter/material.dart';\n
        import 'dart:html' as html; // Import for web downloads\n
        import '../constants/colors.dart';\n
        
        class MainDesktop extends StatelessWidget {\n
          const MainDesktop({super.key, required this.onNavItemTapSocial});\n
          final Function(int) onNavItemTapSocial;\n
          \n        
          // Function to download PDF from the local files in the web directory\n
          void downloadPDF() {\n
            const url = 'https://github.com/""" + st.session_state.submit_git_cred_user_name + "/" + st.session_state.project_name_git + """/blob/main/public/""" + resume_name + """.pdf?raw=true'; // The relative path to your PDF in the web directory\n
            final anchor = html.AnchorElement(href: url)\n
              ..setAttribute('download', '""" + resume_name + """.pdf') // Name of the downloaded file\n
              ..click();\n
          }\n
          \n
          @override\n
          Widget build(BuildContext context) {\n
            final screenSize = MediaQuery.of(context).size;\n
            final screenWidth = screenSize.width;\n
            final screenHeight = screenSize.height;\n
            \n
            return Container(\n
              margin: const EdgeInsets.symmetric(horizontal: 20.0),\n
              height: screenHeight / 1.2,\n
              constraints: const BoxConstraints(\n
                minHeight: 350.0,\n
              ),\n
              child: Row(\n
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,\n
                children: [\n
                  Column(\n
                    mainAxisAlignment: MainAxisAlignment.center,\n
                    children: [\n
                      const Text(\n
                        """ + '"' + tag_line_about_you + '"' + """,\n
                        style: TextStyle(\n
                          fontSize: 30.0,\n
                          height: 1.5,\n
                          fontWeight: FontWeight.bold,\n
                          color: CustomColor.whitePrimary,\n
                        ),\n
                      ),\n
                      const SizedBox(height: 15),\n
                      SizedBox(\n
                        width: 250,\n
                        child: ElevatedButton(\n
                          onPressed: () {\n
                            onNavItemTapSocial(3);\n
                          },\n
                          style: ElevatedButton.styleFrom(\n
                            shape: RoundedRectangleBorder(\n
                              borderRadius: BorderRadius.circular(10.0),\n
                            ),\n
                            backgroundColor: CustomColor.yellowPrimary,\n
                          ),\n
                          child: const Text("Get in touch",style: TextStyle(color: CustomColor.whitePrimary),),\n
                        ),\n
                      ),\n
                      const SizedBox(height: 15), // Add spacing between buttons\n
                      SizedBox(\n
                        width: 250,\n
                        child: ElevatedButton(\n
                          onPressed: downloadPDF, // Call the download function\n
                          style: ElevatedButton.styleFrom(\n
                            shape: RoundedRectangleBorder(\n
                              borderRadius: BorderRadius.circular(10.0),\n
                            ),\n
                            backgroundColor: CustomColor.yellowPrimary,\n
                          ),\n
                          child: const Text("Download Resume",style: TextStyle(color: CustomColor.whitePrimary),),\n
                        ),\n
                      ),\n
                    ],\n
                  ),\n
                  Image.asset(\n
                    """ + '"assets/' + photo_portfolio_name + '"' + """,\n
                    width: screenWidth / 4,\n
                  ),\n
                ],\n
              ),\n
            );\n
          }\n
        }\n
        """

        # st.success(main_moblie_code)
        # st.success(main_desktop_code)
        return [main_moblie_code, main_desktop_code]


def hobby_work_project():
    if "final_val_acct" not in st.session_state:
        st.session_state.final_val_acct = False

    if "value_in_str_brief" not in st.session_state:
        st.session_state.value_in_str_brief = []

    if "value_in_str_desc" not in st.session_state:
        st.session_state.value_in_str_desc = []

    if "hobby_value_in_str_brief" not in st.session_state:
        st.session_state.hobby_value_in_str_brief = []

    if "hobby_value_in_str_desc" not in st.session_state:
        st.session_state.hobby_value_in_str_desc = []

    api_vertex = ""
    st.title("Project Description")
    final_hobby_string_list = []
    final_work_string_list = []
    with st.container(border=True):
        number = st.number_input(
            "Number of Work Projects", value=None, min_value=1, step=1, placeholder="Type a number..."
        )
        if not number:
            number = 0
        try:
            if number == 0:
                st.session_state.value_in_str_brief.pop()
                st.session_state.value_in_str_desc.pop()
        except:
            print()
        st.session_state.work_proj_number = number
        for i in range(number):
            st.header("Work Project " + str(i + 1))
            with st.container(border=True):
                image_project = st.file_uploader("Upload Project photo",
                                                 accept_multiple_files=False, type=['png', 'jpg'],
                                                 help="Upload project image", key="image_project_" + str(i))
                if image_project and st.session_state.submit_git == 'submit_git_value':
                    image_project_content = image_val_upload(image_project)
                    photo_upload(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                 st.session_state.project_name_git,
                                 'assets/projects/' + image_project.name if image_project else 'default_project.png',
                                 image_project_content)
                title_project = st.text_input("Enter the project title", max_chars=30,
                                              key="project_title_" + str(i))
                project_def_brief_empty = st.empty()
                project_description_empty = st.empty()
                if len(st.session_state.value_in_str_brief) == int(i + 1) and len(
                        st.session_state.value_in_str_desc) == int(i + 1):
                    print("All values are matching")

                if len(st.session_state.value_in_str_brief) < int(i + 1):
                    st.session_state.value_in_str_brief.append("")
                if len(st.session_state.value_in_str_desc) < int(i + 1):
                    st.session_state.value_in_str_desc.append("")
                if len(st.session_state.value_in_str_brief) > len(range(number)):
                    st.session_state.value_in_str_brief.pop()
                if len(st.session_state.value_in_str_desc) > len(range(number)):
                    st.session_state.value_in_str_desc.pop()

                project_def_brief = project_def_brief_empty.text_input("Enter project brief definition",
                                                                       st.session_state.value_in_str_brief[i],
                                                                       max_chars=150,
                                                                       key="project_definition_" + str(i))
                project_description = project_description_empty.text_area("Enter project description",
                                                                          st.session_state.value_in_str_desc[i],
                                                                          key="project_description_" + str(i))

                # if project_def_brief:
                #     st.session_state.value_in_str_brief[i] = project_def_brief
                # if project_description:
                #     st.session_state.value_in_str_desc[i] = project_description

                if st.session_state.final_val_acct and st.session_state.work_proj_val:
                    try:
                        final_value_desc_proj = gen_promt(api_vertex,
                                                          "Make the text professional without adding or appending any content no special caharacters and quotes " +
                                                          project_description)
                    except:
                        st.error("Quota Expired Out of Free limit for api calls")

                    time.sleep(22)

                    try:
                        final_val_brief_desc_proj = gen_promt(api_vertex,
                                                              "Make the text professional without adding or appending any content do not exceed 150 characters and no special caharacters and quotes " +
                                                              project_def_brief)
                    except:
                        st.error("Quota Expired Out of Free limit for api calls")

                    time.sleep(22)
                    st.session_state.value_in_str_brief[i] = final_val_brief_desc_proj
                    st.session_state.value_in_str_desc[i] = final_value_desc_proj

                    if i == len(range(number - 1)):
                        st.info(f"{i} in {len(range(number - 1))}")
                        st.session_state.work_proj_val = False
                        #st.rerun()

                    # project_def_brief = project_def_brief_empty.text_input("Enter project brief definition",
                    #                                                        st.session_state.value_in_str_brief[i],
                    #                                                        max_chars=150,
                    #                                                        key="project_definition_ai" + str(i))
                    # project_description = project_description_empty.text_area("Enter project description",
                    #                                                           st.session_state.value_in_str_desc[i],
                    #                                                           key="project_description_ai" + str(i))
                project_verifier_link = st.text_input("Enter profile link of project verifier",
                                                      key="project_verifier_link_" + str(i))
                display_project_footer = "Verified by"
                work_string = 'image: ' + "'assets/projects/" + image_project.name + "',\n" if image_project else "image: 'assets/projects/default_project.png ',\n"
                work_string += "\ntitle: '" + title_project.replace("'", "").replace('"', "") + "',\n" + "\nsubtitle: '" \
                               + " ".join([line for line in project_def_brief.replace("'", "").replace('"', "").splitlines() if line.strip()]) + "',\n" + "\nfullcontent: '" + " ".join([line for line in project_description.replace("'", "").replace('"', "").splitlines() if line.strip()])+ "',\n"
                work_string += "\n" "verifierLink: '" + project_verifier_link + "'," + "\n" if project_verifier_link else "verifierLink: 'https://www.linkedin.com/in/'"
                work_string += "\ndisplayFooter: '" + display_project_footer + "',\n"
                final_work_string = """ProjectUtils(\n""" + work_string + """  ), """
                final_work_string_list.append(final_work_string)
                # st.success(final_work_string)
    with st.container(border=True):
        number = st.number_input(
            "Number of Hobby Projects", value=None, min_value=1, step=1, placeholder="Type a number..."
        )
        if not number:
            number = 0
        try:
            if number == 0:
                st.session_state.hobby_value_in_str_brief.pop()
                st.session_state.hobby_value_in_str_desc.pop()
        except:
            print()
        st.session_state.hobby_proj_number = number
        for i in range(number):
            st.header("Hobby Project " + str(i + 1))
            with st.container(border=True):
                hobby_image_project = st.file_uploader("Upload Project photo",
                                                       accept_multiple_files=False, type=['png', 'jpg'],
                                                       help="Upload project image", key="image_project_hobby_" + str(i))
                if hobby_image_project and st.session_state.submit_git == 'submit_git_value':
                    hobby_image_project_content = image_val_upload(hobby_image_project)
                    photo_upload(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                                 st.session_state.project_name_git,
                                 'assets/projects/' + hobby_image_project.name if hobby_image_project else 'default_project.png',
                                 hobby_image_project_content)
                    if i == len(range(number - 1)):
                        print("Reversing to not submit git value")
                        st.session_state['submit_git'] = 'not_submit_git_value'
                hobby_title_project = st.text_input("Enter the project title", max_chars=30,
                                                    key="project_title_hobby_" + str(i))
                hobby_project_def_brief_empty = st.empty()
                hobby_project_description_empty = st.empty()

                if len(st.session_state.hobby_value_in_str_brief) == int(i + 1):
                    print("All values are matching")
                if len(st.session_state.hobby_value_in_str_desc) == int(i + 1):
                    print("All values are matching")
                if len(st.session_state.hobby_value_in_str_brief) < int(i + 1):
                    st.session_state.hobby_value_in_str_brief.append("")
                if len(st.session_state.hobby_value_in_str_desc) < int(i + 1):
                    st.session_state.hobby_value_in_str_desc.append("")

                if len(st.session_state.hobby_value_in_str_brief) > len(range(number)):
                    st.session_state.hobby_value_in_str_brief.pop()
                if len(st.session_state.hobby_value_in_str_desc) > len(range(number)):
                    st.session_state.hobby_value_in_str_desc.pop()

                hobby_project_def_brief = hobby_project_def_brief_empty.text_input("Enter project brief definition",
                                                                                   st.session_state.hobby_value_in_str_brief[
                                                                                       i], max_chars=150,
                                                                                   key="project_definition_hobby_" + str(
                                                                                       i))
                hobby_project_description = hobby_project_description_empty.text_area("Enter project description",
                                                                                      st.session_state.hobby_value_in_str_desc[
                                                                                          i],
                                                                                      key="project_description_hobby_" + str(
                                                                                          i))

                # if hobby_project_def_brief:
                #     st.session_state.hobby_value_in_str_brief[i] = hobby_project_def_brief
                # if hobby_project_description:
                #     st.session_state.hobby_value_in_str_brief[i] = hobby_project_description

                if st.session_state.final_val_acct and st.session_state.hobby_proj_val:
                    try:
                        hobby_final_value_desc_proj = gen_promt(api_vertex,
                                                                "Make the text professional without adding or appending any content and  no special caharacters and quotes " +
                                                                hobby_project_description)
                    except:
                        st.error("Error Out of quota limit.")

                    time.sleep(20)
                    try:
                        hobby_final_val_brief_desc_proj = gen_promt(api_vertex,
                                                                    "Make the text professional without adding or appending any content do not exceed 150 characters and  no special caharacters and quotes " +
                                                                    hobby_project_def_brief)
                    except:
                        st.error("Error Out of quota limit.")
                    time.sleep(20)
                    st.session_state.hobby_value_in_str_brief[i] = hobby_final_val_brief_desc_proj
                    st.session_state.hobby_value_in_str_desc[i] = hobby_final_value_desc_proj

                    if i == len(range(number - 1)):
                        st.info(f"{i} in {len(range(number - 1))}")
                        st.session_state.final_val_acct = False
                        st.session_state.hobby_proj_val = False
                        st.rerun()
                    # hobby_project_def_brief = hobby_project_def_brief_empty.text_input("Enter project brief definition",
                    #                                                                    st.session_state.hobby_value_in_str_brief[
                    #                                                                        i], max_chars=150,
                    #                                                                    key="project_definition_hobby_ai" + str(
                    #                                                                        i))
                    # hobby_project_description = hobby_project_description_empty.text_area("Enter project description",
                    #                                                                       st.session_state.hobby_value_in_str_desc[
                    #                                                                           i],
                    #                                                                       key="project_description_hobby_ai" + str(
                    #                                                                           i))

                hobby_project_available_link_android = st.text_input("Enter play store link if available",
                                                                     key="project_available_link_hobby_android_" + str(
                                                                         i))
                hobby_project_available_link_ios = st.text_input("Enter App store link if available",
                                                                 key="project_available_link_hobby_ios_" + str(i))
                hobby_project_available_link_web = st.text_input("Enter any web links",
                                                                 key="project_available_link_hobby_web_" + str(i))
                hobby_project_available_link_pypi = st.text_input("Enter pypi repo links",
                                                                  key="project_available_link_hobby_pypi_" + str(i))
                hobby_project_available_link_git = st.text_input("Enter git repo link",
                                                                 key="project_available_link_hobby_git_" + str(i))
                hobby_display_project_footer = "Available on"
                if hobby_project_available_link_android:
                    hobby_android = "androidLink: '" + hobby_project_available_link_android + "',\n"
                if hobby_project_available_link_ios:
                    hobby_ios = "iosLink: '" + hobby_project_available_link_ios + "',\n"
                if hobby_project_available_link_web:
                    hobby_weblink = "webLink: '" + hobby_project_available_link_web + "',\n"
                if hobby_project_available_link_pypi:
                    hobby_git = "gitLink: '" + hobby_project_available_link_pypi + "',\n"
                if hobby_project_available_link_git:
                    hobby_pypi = "pypiLink: '" + hobby_project_available_link_git + "',\n"
                hobby_string = 'image: ' + "'assets/projects/" + hobby_image_project.name + "',\n" if hobby_image_project else "image: 'assets/projects/default_project.png ',\n"
                hobby_string += "\ntitle: '" + hobby_title_project.replace("'", "").replace('"', "") + "',\n" + "\nsubtitle: '" \
                                + " ".join([line for line in hobby_project_def_brief.replace("'", "").replace('"', "").splitlines() if line.strip()]) + "',\n" + "\nfullcontent: '" + " ".join([line for line in hobby_project_description.replace("'", "").replace('"', "").splitlines() if line.strip()]) + "',\n"
                hobby_string += "\n" + hobby_android + "\n" if hobby_project_available_link_android else ''
                hobby_string += hobby_ios + "\n" if hobby_project_available_link_ios else ''
                hobby_string += hobby_weblink + "\n" if hobby_project_available_link_web else ''
                hobby_string += hobby_git + "\n" if hobby_project_available_link_pypi else ''
                hobby_string += hobby_pypi + "\n" if hobby_project_available_link_git else ''
                hobby_string += "displayFooter: '" + hobby_display_project_footer + "',\n"
                # st.success(hobby_string)
                final_hobby_string = """ProjectUtils(\n""" + hobby_string + """  \n),\n """
                final_hobby_string_list.append(final_hobby_string)

    string_code_proj_util = """
    class ProjectUtils {\n
      final String image;\n
      final String title;\n
      final String subtitle;\n
      final String fullcontent;\n
      final String? androidLink;\n
      final String? iosLink;\n
      final String? webLink;\n
      final String? gitLink;\n
      final String? pypiLink;\n
      final String? verifierLink;\n
      final String displayFooter;\n
    \n
      ProjectUtils({\n
        required this.image,\n
        required this.title,\n
        required this.subtitle,\n
        required this.fullcontent,\n
        this.androidLink,\n
        this.iosLink,\n
        this.webLink,\n
        this.gitLink,\n
        this.pypiLink,\n
        this.verifierLink,\n
        required this.displayFooter,\n
      });\n
    }\n
    List < ProjectUtils > hobbyProjectUtils = [\n
    """ + ' '.join(final_hobby_string_list) + """ \n];\n
    List<ProjectUtils> workProjectUtils = [\n """ + ' '.join(final_work_string_list) + """ \n];\n
    """
    # st.success(string_code_proj_util)
    st.session_state.final_hobby_string_list_val = ''.join(final_hobby_string_list)
    st.session_state.final_work_string_list_val = ''.join(final_work_string_list)
    st.session_state.final_val_acct = False
    if st.session_state.work_proj_number > 0 and st.session_state.hobby_proj_number > 0 and not st.session_state.block_ai_hobby and not st.session_state.block_ai_work:
        st.session_state.block_ai_work = True
        st.session_state.block_ai_hobby = True
        # st.success("Inside true")
        st.rerun()
    if (st.session_state.work_proj_number == 0 or st.session_state.hobby_proj_number == 0) and (
            st.session_state.block_ai_hobby or st.session_state.block_ai_work):
        st.session_state.block_ai_work = False
        st.session_state.block_ai_hobby = False
        # st.success("Inside false")
        st.rerun()
    return string_code_proj_util


def skill_item():
    platform_list = []
    skills_list = []
    st.title("Your Skills and technology")
    with st.container(border=True):
        number_platform = st.number_input(
            "Number of platforms or domains", value=None, min_value=1, step=1, placeholder="Type a number..."
        )
        if not number_platform:
            number_platform = 0
        for i in range(number_platform):
            st.header("Technologies or Domains " + str(i + 1))
            tech_plat_form_photo = st.file_uploader("Upload technology icon",
                                                    accept_multiple_files=False, type=['png', 'jpg'],
                                                    help="Upload technology icon", key="image_tech_icon_" + str(i))
            if tech_plat_form_photo and st.session_state.submit_git == 'submit_git_value':
                tech_plat_form_photo_content = image_val_upload(tech_plat_form_photo)
                photo_upload(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                             st.session_state.project_name_git,
                             'assets/' + tech_plat_form_photo.name if tech_plat_form_photo else 'default_project.png',
                             tech_plat_form_photo_content)
            title_platform = st.text_input("Enter the platform title", max_chars=20, help="eg:- Big Data",
                                           key="title_platform_domain" + str(i))

            platform_string = "{ \n" + '\n"img" :' + '"assets/' + tech_plat_form_photo.name + '",\n' if tech_plat_form_photo else '{\n' + '\n"img": ' + '"defaut_platform.png",\n'
            platform_string += '\n"title": "' + title_platform + '",\n },'
            platform_list.append(platform_string)
            # st.success(platform_string)

    with st.container(border=True):
        number_platform = st.number_input(
            "Number of skills", value=None, min_value=1, step=1, placeholder="Type a number..."
        )
        if not number_platform:
            number_platform = 0
        for i in range(number_platform):
            st.header("Skills " + str(i + 1))
            tech_skills_photo = st.file_uploader("Upload Skills icon",
                                                 accept_multiple_files=False, type=['png', 'jpg'],
                                                 help="Upload skills icon", key="image_skills_icon_" + str(i))

            if tech_skills_photo and st.session_state.submit_git == 'submit_git_value':
                tech_skills_photo_content = image_val_upload(tech_skills_photo)
                photo_upload(st.session_state.submit_git_token, st.session_state.submit_git_cred_user_name,
                             st.session_state.project_name_git,
                             'assets/' + tech_skills_photo.name if tech_skills_photo else 'default_project.png',
                             tech_skills_photo_content)

            title_skills = st.text_input("Enter the platform title", max_chars=20, help="eg:- Python",
                                         key="title_skills_" + str(i))

            skills_string = "{ \n" + '\n"img" :' + '"assets/' + tech_skills_photo.name + '",\n' if tech_skills_photo else '{\n' + '\n"img": ' + '"defaut_platform.png",\n'
            skills_string += '\n"title": "' + title_skills + '",\n },'
            skills_list.append(skills_string)
            # st.success(skills_string)
    skills_string_final = \
        """const List<Map> platformItems = [ \n """ + ' '.join(
            platform_list) + "\n];\n" + """\n const List<Map> skillItem = [ \n """ + ' '.join(
            skills_list) + """\n]; \n"""
    # st.success(skills_string_final)
    st.session_state.platform_list_val = ''.join(platform_list)
    st.session_state.skills_list_val = ''.join(skills_list)
    return skills_string_final


def side_bar_fun():
    st.sidebar.title("Credentials")
    with st.sidebar.form("Credentials"):
        user_name_git = st.text_input("Git user name")
        project_name = st.text_input("Project Name for deployments", help="eg:- suprith-m-portfolio")
        if project_name:
            st.session_state['project_name_git'] = project_name
        else:
            st.session_state['project_name_git'] = "project_name"
        user_git_token = st.text_input("Git token",type="password")
        user_vercel_token = st.text_input("Vercel token",type="password")
        if st.form_submit_button("Submit"):  # sidebar.
            st.session_state['submit_git_cred_user_name'] = user_name_git
            st.session_state['submit_git_token'] = user_git_token
            st.session_state['submit_vercel_token'] = user_vercel_token
            if git_repo_fork(st.session_state.submit_git_token, st.session_state.project_name_git):
                # if wait_for_fork_ready(st.session_state.submit_git_token,st.session_state.submit_git_cred_user_name):
                st.success("Validated")
            else:
                st.error("Wrong Credentials")
        else:
            print("no valid loop")
            if "submit_git_cred_user_name" not in st.session_state:
                st.session_state['submit_git_cred_user_name'] = "user_name_git"
            else:
                print("user name already provided")
