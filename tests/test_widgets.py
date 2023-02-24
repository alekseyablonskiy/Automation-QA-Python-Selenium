import time

import allure

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite('Widgets')
class TestWidgets:
    @allure.feature('Accordian page')
    class TestAccordianPage:
        @allure.title('Check accordian')
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    @allure.feature('AutoComplete page')
    class TestAutoCompletePage:
        @allure.title('Check fill multi autocomplete')
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result

        @allure.title('Check remove value from multi')
        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            autocomplete_page.remove_value_from_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        @allure.title('Check fill single autocomplete')
        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result

    @allure.feature('DatePicker page')
    class TestDatePickerPage:
        @allure.title('Check change date')
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after

        @allure.title('Check change date and time')
        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after

    @allure.feature('Slider page')
    class TestSliderPage:
        @allure.title('Check slider')
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page. change_slider_value()
            assert before != after

    @allure.feature('ProgressBar page')
    class TestProgressBarPage:
        @allure.title('Check progress bar')
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.change_progress_bar_value()
            assert before != after

    @allure.feature('Tabs page')
    class TestTabsPage:
        @allure.title('Check tabs')
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_button, what_content = tabs_page.check_tabs('what')
            origin_button, origin_content = tabs_page.check_tabs('origin')
            use_button, use_content = tabs_page.check_tabs('use')
            assert what_button == 'What' and what_content == 574
            assert origin_button == 'Origin' and origin_content == 1059
            assert use_button == 'Use' and use_content == 613

    @allure.feature('ToolTips page')
    class TestToolTipsPage:
        @allure.title('Check tool tips')
        def test_tool_tips(self, driver):
            tool_tips = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips.open()
            button_text, section_text, field_text, contrary_text = tool_tips.check_tool_tips()
            assert button_text == 'You hovered over the Button'
            assert field_text == 'You hovered over the text field'
            assert contrary_text == 'You hovered over the Contrary'

    @allure.feature('Menu page')
    class TestMenuPage:
        @allure.title('Check menu')
        def test_menu(self, driver):
            menu = MenuPage(driver, 'https://demoqa.com/menu')
            menu.open()
            data = menu.check_menu()
            assert len(data) == 8

