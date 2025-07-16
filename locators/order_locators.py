from selenium.webdriver.common.by import By


class OrderLocators:

    # Кнопка "Заказать"
    ORDER_BUTTON_HEADER = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    ORDER_CENTER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]

    # Данные пользователя
    NAME = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    LAST_NAME = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    ADDRESS = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    METRO = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]
    LIST_STATION = [By.XPATH, "//li[@data-index='0']"]
    NUMBER = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    # Окно Про аренду
    DATE_DELIVERY = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENT_TIME = [By.XPATH, '//div[text()="* Срок аренды"]']
    SELECT_RENT_TIME = [By.XPATH, '//div[text()="{}"]']
    BLACK_COLOR_CHECKBOX = [By.XPATH, '//label[@for="black"]']
    GREY_COLOR_CHECKBOX = [By.XPATH, '//label[@for="grey"]']
    COMMENT = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]

    # Кнопка Да в сплывающем окне заказа подтверждения
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    # Текс окна "Заказ оформлен"
    ORDER_COMPLETED = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]