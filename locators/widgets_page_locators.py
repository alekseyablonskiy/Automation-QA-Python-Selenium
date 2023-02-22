from selenium.webdriver.common.by import By


class AccordianPageLocators:

    FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    THIRD_SECTION = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

