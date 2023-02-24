import random

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_cur_addr
            assert permanent_address == output_per_addr

    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_checkbox(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            assert output_yes == 'Yes'
            assert output_impressive == 'Impressive'

    @allure.feature('TestWebTable')
    class TestWebTable:
        @allure.title('Check to add person to the table')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_added_person()
            assert new_person in table_result

        @allure.title('Check to search person in the table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person(key_word)
            table_result = web_table_page.check_searched_person()
            assert key_word in table_result

        @allure.title('Check to update person in the table')
        def test_web_table_update_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person(lastname)
            age = web_table_page.update_person()
            row = web_table_page.check_searched_person()
            assert age in row

        @allure.title('Check to delete person from the table')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted_person()
            assert text == 'No rows found'

    @allure.feature('Buttons')
    class TestButtons:
        @allure.title('Check Buttons')
        def test_different_click_on_buttons(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_buttons('double')
            right = button_page.click_on_different_buttons('right')
            click = button_page.click_on_different_buttons('click')
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert click == 'You have done a dynamic click'

    @allure.feature('Links')
    class TestLinks:
        @allure.title('Check Link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url

        @allure.title('Check Broken Link')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400

    @allure.feature('UploadDownload')
    class TestUploadDownload:
        @allure.title('Check UploadDownload file')
        def test_upload_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            path = upload_download_page.upload_file()
            assert path == r'C:\fakepath\picture.jpeg'

    @allure.feature('Dynamic Properties')
    class TestDynamicProperties:
        @allure.title('Check enable button')
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True

        @allure.title('Check change button color')
        def test_change_color_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_before != color_after

        @allure.title('Check button appear')
        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True

