from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.FIRST_SECTION,
                          'content': self.locators.FIRST_SECTION_CONTENT},
                     'second':
                         {'title': self.locators.SECOND_SECTION,
                          'content': self.locators.SECOND_SECTION_CONTENT},
                     'third':
                         {'title': self.locators.THIRD_SECTION,
                          'content': self.locators.THIRD_SECTION_CONTENT},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]
