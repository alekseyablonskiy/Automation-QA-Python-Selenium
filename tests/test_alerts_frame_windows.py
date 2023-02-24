import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, NestedFramesPage, ModalDialogPage


@allure.suite('AlertsFrameWindows')
class TestAlertsFrameWindows:
    @allure.feature('BrowserWindows Page')
    class TestBrowserWindowsPage:
        @allure.title('Check new tab')
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_opened_tab()
            assert text_result == 'This is a sample page'

        @allure.title('Check new window')
        def test_new_window(self, driver):
            new_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open()
            text_result = new_window_page.check_opened_window()
            assert text_result == 'This is a sample page'

    @allure.feature('Alerts Page')
    class TestAlertsPage:
        @allure.title('Check see alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title('Check alert appear in 5 sec')
        def test_alert_appear_in_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_in_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title('Check confirm alert')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        @allure.title('Check prom alert')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert alert_text == f'You entered {text}'

    @allure.feature('Frame Page')
    class TestFramePage:
        @allure.title('Check frames')
        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px']
            assert result_frame2 == ['This is a sample page', '100px', '100px']

    @allure.feature('NestedFrame Page')
    class TestNestedFramePage:
        @allure.title('Check nested frames')
        def test_nested_frame(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame'
            assert child_text == 'Child Iframe'

    @allure.feature('ModalDialogs Page')
    class TestModalDialogsPage:
        @allure.title('Check modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1]
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'