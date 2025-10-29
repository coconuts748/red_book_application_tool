from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
import time
from loguru import logger
import textwrap
import tkinter as tk
from tkinter import ttk,messagebox


def craw_part_article_data(phone_param_set_here__,main_article_search_content):
    logger.info('craw_part_article_data running....')
    all_article_content = []
    article_title_list = []

    options = UiAutomator2Options()
    options.load_capabilities(phone_param_set_here__)

    article_android_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(article_android_driver, 20)

    def open_red_book_application():
        logger.info('open_red_book_application running....')
        try:
            red_book_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@text="小红书"]')))
            red_book_button.click()

        except Exception as e:
            logger.error(f'小红书启动失败:{e}')

    def search_something(input_here):   #contain store function........

        logger.info('search_something running....')
        try:
            enter_search_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@content-desc="搜索"]')))
            enter_search_button.click()

            search_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,'//android.widget.EditText[@text="搜索, "]')))
            search_button.click()
            search_button.send_keys(input_here)

            ensure_search_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,'//android.widget.Button[@text="搜索"]')))
            ensure_search_button.click()

            solid_list = [3,5,7,8]
            def article_title():
                try:
                    for i in solid_list:
                        build_xpath_source = f'(//android.widget.FrameLayout[@resource-id="com.xingin.xhs:id/0_resource_name_obfuscated"])[{i}]/android.widget.RelativeLayout/android.widget.TextView'
                        try:
                            article_general_description = wait.until(e_conditions.presence_of_element_located(
                                (AppiumBy.XPATH, build_xpath_source))).get_attribute("text")
                            better_article_general_description = textwrap.wrap(str(article_general_description))
                            logger.info(better_article_general_description)
                            article_title_list.append(better_article_general_description)

                        except Exception as r:
                            logger.error(r)
                            pass
                    return article_title_list

                except Exception as r:
                    logger.error(r)  # 辅助格式

            def article_content():
                try:
                    for t in solid_list:
                        cite_object = f'(//android.widget.FrameLayout[@resource-id="com.xingin.xhs:id/0_resource_name_obfuscated"])[{t}]/android.widget.RelativeLayout/android.widget.TextView'
                        try:
                            enter_article_button = wait.until(
                                e_conditions.presence_of_element_located((AppiumBy.XPATH, cite_object)))
                            enter_article_button.click()

                            content_location = '(//android.widget.FrameLayout[@resource-id="com.xingin.xhs:id/0_resource_name_obfuscated"])[8]/android.widget.LinearLayout/android.widget.TextView[2]'
                            content = wait.until(e_conditions.presence_of_element_located(
                                (AppiumBy.XPATH, content_location))).get_attribute("text")
                            logger.info(content)
                            all_article_content.append(content)

                            time.sleep(1)
                            article_android_driver.back()

                        except Exception as c:
                            logger.error(c)
                            pass
                    return all_article_content

                except Exception as y:
                    logger.error(y)

            ########################
            article_title()
            article_content()
            #######################

        except Exception as e:
            logger.error(f'搜索流程出错:{e}')
    def show_article_title_and_content():
        logger.info('show_article_title_and_content running....')
        def inner_show_article_title_and_content():
            try:
                for u in list(range(0,len(article_title_list)+1)):
                    show_article_title_and_content_text.insert(tk.END, f'{str(article_title_list[u])}:\n')
                    show_article_title_and_content_root.update_idletasks()
                    time.sleep(1)
                    show_article_title_and_content_text.insert(tk.END,f'{str(all_article_content[u])}\n')
                    show_article_title_and_content_root.update_idletasks()

            except Exception as e:
                logger.error(e)
                pass

        def quit_show_article_title_and_content():
            if messagebox.askyesno('提示', '确认退出当前页面?'):
                show_article_title_and_content_root.destroy()

        show_article_title_and_content_root = tk.Tk()
        show_article_title_and_content_root.title("爬取结果展示")

        show_article_title_and_content_text = tk.Text(show_article_title_and_content_root)
        show_article_title_and_content_text.pack()

        ttk.Button(show_article_title_and_content_root,text='start',command=inner_show_article_title_and_content).pack()
        ttk.Button(show_article_title_and_content_root, text='quit', command=quit_show_article_title_and_content).pack()

        show_article_title_and_content_root.mainloop()

    def quit_article_android_driver():
        logger.info('quit_article_android_driver running....')

        for k in list(range(0,6)):
            logger.info('这是小红书的第{}次退出'.format(k))
            article_android_driver.back()
        article_android_driver.quit()


    open_red_book_application()
    search_something(input_here=main_article_search_content)
    show_article_title_and_content()
    quit_article_android_driver()


if __name__ == '__main__':
    phone_param_set_here = {
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    }
    craw_part_article_data(phone_param_set_here__=phone_param_set_here,main_article_search_content='')######...