*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Test Cases ***

Search On Google Page and Verify
    Open Browser     https://google.co.in    chrome
    Input text       name=q      robotframework
    click element    name=btnk


*** Keywords ***
