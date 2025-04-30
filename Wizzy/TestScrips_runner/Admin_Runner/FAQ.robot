

from Modules.Admin_Panel import FAQ.py

*** Settings ***
Library    Modules/Admin_Panel/FAQ.py
Library    BuiltIn

*** Variables ***
${faq}  "data"



*** Test Cases ***


Verify Login
    Log    "hello"
    ${faq}    FAQ   # Create an object of FAQ
    ${faq}.create_FAQ    ${data}  # Call the create_FAQ method with data





