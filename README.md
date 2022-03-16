# Localization-testing
Homework for QA automation course on https://stepik.org/course/575/info.  
Step 3.6.9. Checking the possibility to choose the language  
by passing the argument via command line.  
 
Repo contains:  
1. Python script **test_items.py** with test for checking the button  
existance on page.
2. Configuration file **conftest.py** for scripts that are run via  
pytest. Allows to launch a specific browser with a specific language  
preference.  
Arguments that are passed via command line:  
    - browser name (Chrome and Firefox are available),
    - language preference for HTTP request.
