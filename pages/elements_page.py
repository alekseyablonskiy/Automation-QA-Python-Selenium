import random
import time

import requests

from utils.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonPageLocators, LinksPageLocators, UploadDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage
from utils import path_to_file


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element('xpath', self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('.doc', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_searched_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text


class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    def click_on_different_buttons(self, type_click):
        if type_click == 'double':
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_button(self.locators.SUCCESS_DOUBLE)

        if type_click == 'right':
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_button(self.locators.SUCCESS_RIGHT)

        if type_click == 'click':
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.elements_are_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()

    def upload_file(self):
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path_to_file.generate_path_upload('picture.jpeg'))
        text = self.element_is_present(self.locators.UPLOADED_FILE_PATH).text
        return text


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)
        except TimeoutError:
            return False
        return True

    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_before_button = color_button.value_of_css_property('color')
        time.sleep(5)
        color_after_button = color_button.value_of_css_property('color')
        return color_before_button, color_after_button

    def check_appear_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        except TimeoutError:
            return False
        return True





