import tkinter as tk
from tkinter import ttk,messagebox
import json
from loguru import logger
from 已完成.小红书爬虫工具.phone_setting_param_tool import setting_param_tool
from 已完成.小红书爬虫工具.craw_part__user_data import craw_part_user_data
from 已完成.小红书爬虫工具.craw_part_article_data import craw_part_article_data

def main_menu_functions():
    logger.info('main_menu_functions running...')
    def transmit_phone_param_():
        # setting_param_tool()

        # with open('phone_setting_param.json', 'rb') as f:
        #     str_format = json.load(f)
        #     phone_necessary_param = {
        #         'automationName': str_format['automationName'],
        #         'platformName': str_format['platformName'],
        #         'deviceName': str_format['deviceName'],
        #         'noReset': str_format['noReset']
        #
        #     }
        phone_necessary_param = {
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
        }

        def function_article():
            def inner_function_article():
                article_searching = str(article_searching_get.get().strip())
                if len(article_searching) == 0:
                    messagebox.showwarning('提示', '输入无效!')
                else:
                    if messagebox.askyesno('提示', '此次输入的内容为:{}\n是否确认?'.format(article_searching)):
                        main_menu_functions_root.withdraw()
                        craw_part_article_data(phone_param_set_here__=phone_necessary_param,
                                               main_article_search_content=article_searching)

            inner_function_article_root = tk.Tk()
            inner_function_article_root.title("参数设置")

            ttk.Label(inner_function_article_root, text='搜索:').grid(row=0, column=0, columnspan=2)
            article_searching_get = tk.Entry(inner_function_article_root)
            article_searching_get.grid(row=0, column=3, columnspan=5)
            ttk.Button(inner_function_article_root, text='开始搜索', command=inner_function_article).grid(row=1,
                                                                                                          column=0,
                                                                                                          columnspan=2)
            inner_function_article_root.mainloop()

        def function_user_data():
            def inner_function_user_data():
                user_search = str(user_search_get.get().strip())
                if len(user_search) == 0:
                    messagebox.showwarning('提示', '输入无效!')
                else:
                    if messagebox.askyesno('提示', '此次输入的内容为:{}\n是否确认?'.format(user_search)):
                        main_menu_functions_root.withdraw()
                        craw_part_user_data(phone_param_setting_here___=phone_necessary_param,
                                            user_name_input____=user_search)

            inner_function_user_data_root = tk.Tk()
            inner_function_user_data_root.title('参数传入')

            ttk.Label(inner_function_user_data_root, text='搜索:').grid(row=0, column=0, columnspan=2)
            user_search_get = tk.Entry(inner_function_user_data_root)
            user_search_get.grid(row=0, column=3, columnspan=5)
            ttk.Button(inner_function_user_data_root, text='传入', command=inner_function_user_data).grid(row=1,
                                                                                                          column=0,
                                                                                                          columnspan=2)
            inner_function_user_data_root.mainloop()

        def quit_main_menu_functions():
            if messagebox.askyesno('提示', '确认退出当前界面?'):
                main_menu_functions_root.destroy()

        main_menu_functions_root = tk.Tk()
        main_menu_functions_root.title('功能主界面')

        ttk.Button(main_menu_functions_root, text='爬取文章', command=function_article).pack()
        ttk.Button(main_menu_functions_root, text='爬取用户主页', command=function_user_data).pack()
        ttk.Button(main_menu_functions_root, text='退出', command=quit_main_menu_functions).pack()

        main_menu_functions_root.mainloop()






    transmit_phone_param_()

