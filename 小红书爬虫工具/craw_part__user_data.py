from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger
import time
import tkinter as tk
from tkinter import ttk,messagebox




def craw_part_user_data(phone_param_setting_here___,user_name_input____):
    local_time = time.asctime(time.localtime(time.time()))

    search_user_general_describe_list = []

    options = UiAutomator2Options()
    options.load_capabilities(phone_param_setting_here___)
    user_data_android_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(user_data_android_driver, 20)

    def open_application():
        logger.info('open_application running...')
        try:
            red_book_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="小红书"]')))
            red_book_button.click()

        except Exception as e:
            logger.error(f'小红书启动失败:{e}')

    def search_user(input_user_name):
        logger.info('search_user running...')
        try:
            red_book_search_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.Button[@content-desc="搜索"]')))
            red_book_search_button.click()

            red_book_search_input = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="搜索, "]')))
            red_book_search_input.click()
            red_book_search_input.send_keys(input_user_name)

            time.sleep(2)
            red_book_ensure_searching = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="搜索"]')))
            red_book_ensure_searching.click()

            account_option_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="账号"]')))
            account_option_button.click()

            for i in list(range(1, 9)):
                sample_xpath = f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[{i}]/android.view.ViewGroup[1]'
                user_general_describe = wait.until(
                    e_conditions.presence_of_element_located((AppiumBy.XPATH, sample_xpath))).get_attribute(
                    'content-desc')
                search_user_general_describe_list.append(user_general_describe)
                logger.info(f'第{i}行: 用户:{user_general_describe}')
            return search_user_general_describe_list
        except Exception as e:
            logger.error(f'搜索用户出错:{e}')


    def select_witch_one():
        logger.info('select_witch_one running...')
        def showing_users():   #不封装,按流程运行.....
            show_text.insert(tk.END,f'当前时间为:{local_time}...\n')
            show_root.update_idletasks()
            time.sleep(1)

            show_text.insert(tk.END,'以下为爬取到的用户信息,查看后退出该界面,并在后续页面输入对应的序号进行相对应用户的详细爬取....\n')
            show_root.update_idletasks()
            time.sleep(1)

            show_text.insert(tk.END,'tip:序号从1起计数....\n')
            show_root.update_idletasks()
            time.sleep(1)

            for i in search_user_general_describe_list:
                show_text.insert(tk.END, f'{i}\n')
                show_root.update_idletasks()
                time.sleep(1)

            def quit_showing_users():
                if messagebox.askyesno('提示', '确认退出当前页面?'):
                    show_root.destroy()

            start_show.config(text='已完成检索,点击下方退出')
            ttk.Button(show_root,text='点击退出以继续',command=quit_showing_users).pack()

        show_root = tk.Tk()
        show_root.title('爬取用户一览')

        show_text = tk.Text(show_root)
        show_text.pack()

        start_show = ttk.Button(show_root,text='开始检索',command=showing_users)
        start_show.pack()
        show_root.mainloop()
        
        def to_select_witch_one():
            column_number = str(column_number_get.get().strip())
            if len(column_number) == 0:
                messagebox.showwarning('错误','输入无效!')
            else:
                if messagebox.askyesno('提示','当前操作的对象序号为{}\n是否继续?'.format(column_number)):
                    ######手机后续操作#####
                    try:
                        sample_here = f'//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[{column_number}]/android.view.ViewGroup[1]'

                        click_user_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH, sample_here)))
                        click_user_button.click()
                        #####????????无后续,可跳过........
                        #####????????无后续,可跳过........
                        #####????????无后续,可跳过........
                    except Exception as e:
                        logger.error(f'手机后续操作出错 : {e}')

        def quit_select_witch_one():
            if messagebox.askyesno('提示', '确认退出当前页面?'):
                select_root.destroy()

        select_root = tk.Tk()
        select_root.title('爬取用户操作')

        ttk.Label(select_root,text='序号:').grid(row=0, column=0,columnspan=2)
        column_number_get = tk.Entry(select_root)
        column_number_get.grid(row=0,column=3,columnspan=5)

        ttk.Button(select_root,text='开始爬取',command=to_select_witch_one).grid(row=1,column=0,columnspan=2)
        ttk.Button(select_root,text='退出',command=quit_select_witch_one).grid(row=1,column=3)
        select_root.mainloop()

    def quit_user_data_driver():
        logger.info('quit_user_data_driver running...')
        for i in list(range(0, 7)):
            logger.info('这是小红书的第{}次退出....'.format(i))
            user_data_android_driver.back()

        user_data_android_driver.quit()

    open_application()
    search_user(input_user_name=user_name_input____)
    select_witch_one()
    quit_user_data_driver()

if __name__ == '__main__':
    phone_____ = {
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    }
    craw_part_user_data(phone_param_setting_here___=phone_____,user_name_input____='')######.......

