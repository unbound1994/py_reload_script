from selenium.webdriver.common.by import By
from actions import find_elem, waiter, open_page, refresh, closeWindow


def test_page():
    LOGIN = (By.CLASS_NAME, "MuiInputBase-input.MuiFilledInput-input.css-2bxn45")
    PASSWD = (By.CLASS_NAME, "MuiInputBase-input.MuiFilledInput-input.MuiInputBase-inputAdornedEnd.css-ftr4jk")
    BUTTON = (By.CSS_SELECTOR, "#login > div > div > div.jss4 > div > div > form > div.jss22 > button")

    url = 'https://edu.21-school.ru/projects/code-review'
    open_page(url)

    find_elem(LOGIN).send_keys(234234)
    find_elem(PASSWD).send_keys(234234)

    waiter(1)

    print("Ready for login!")
    find_elem(BUTTON).click()

    LOGIN_CHECK = (By.XPATH, '//*[text() = \'Invalid login and/or password\']')

    if find_elem(LOGIN_CHECK):
        print('Incorrect Login/Passwd')
        closeWindow()
        return False

    CHECK = (By.XPATH, '//*[text() = \'You have no projects for review\']')
    SECOND_CHECK = (By.XPATH, '//*[text() = \'Available for code review\']')

    flag_checker = True
    waitTime = 0

    # нейронка, не иначе
    try:
        while flag_checker:
            if not find_elem(SECOND_CHECK):
                refresh()
                waitTime = 4
                waiter(waitTime)
                flag_checker = True
            elif not find_elem(CHECK):
                if find_elem(SECOND_CHECK):
                    flag_checker = False
            elif not find_elem(CHECK):
                if not find_elem(SECOND_CHECK):
                    refresh()
                    waitTime = 4
                    waiter(waitTime)
                    flag_checker = True
            else:
                print('Some shit')
                break
    except Exception as e:
        print('Вообще херня произошла, которая никак не учитывается.\n')
        print(e)


test_page()
