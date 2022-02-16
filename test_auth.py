from AuthPage import AuthPage
from GamePage import GamePage, GamePageLocators


def test_correct_auth(browser):
   auth_page = AuthPage(browser)
   auth_page.go_to_site()
   auth_page.fill_login('xennox2004@yandex.ru')
   auth_page.fill_password("Chpoker032")
   auth_page.click_login_button()
   game_page = GamePage(browser)
   game_page.find_lk_button()

def test_authorization_error_login_empty_error_password_empty(browser):
   auth_page = AuthPage(browser)
   auth_page.go_to_site()
   auth_page.fill_login("")
   auth_page.fill_password("")
   auth_page.click_login_button()
   element_email_error = auth_page.find_alert_email()
   email_error_text = element_email_error.text
   assert email_error_text == 'Неправильный e-mail'
   auth_page.find_alert_password()

def test_google_auth(browser):
   auth_page = AuthPage(browser)
   auth_page.go_to_site()
   auth_page.click_google_button()

