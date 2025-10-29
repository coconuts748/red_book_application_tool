import tkinter as tk
from tkinter import ttk,messagebox
from loguru import logger
import time
from 已完成.小红书爬虫工具.cite_part_xiao_hong_shu import creat_json,encryption_something
from 已完成.小红书爬虫工具.main_menu_functions import main_menu_functions


local_time = time.asctime(time.localtime(time.time()))

class AccountCode:
    def __init__(self):
        self.lib = {}
        default_name = encryption_something(encrypt_content='default_name')
        default_code = encryption_something(encrypt_content='default_code')
        default_account = {
            default_name : default_code
        }
        try:
            creat_json(str(default_account),file_name='accounts_lib')
        except Exception as e:
            logger.error(f'json文件写入失败:{e}')

    def add__new_account(self,account_name,account_code):
        if len(account_name) is None or len(account_code) is None:
            messagebox.showwarning('错误','注册账号无效!')
        else:
            if messagebox.askyesno('注册提醒',f'注册信息为:\n帐:{account_name}\n密:{account_code}\n是否确认注册?'):
                account_name_ = encryption_something(encrypt_content=account_name)
                account_code_ = encryption_something(encrypt_content=account_code)
                self.lib[account_name_] = account_code_
                messagebox.showinfo('注册结果','注册成功！')
                return self.lib

    def load_database(self,check_name,check_code):
        if check_name is None or check_code is None:
            messagebox.showwarning('错误', '查询无效!')
        else:
            if messagebox.askyesno('查找提醒', f'登录信息为:\n帐:{check_name}\n密:{check_code}\n是否确认登录?'):
                check_name_ = encryption_something(encrypt_content=check_name)
                check_code_ = encryption_something(encrypt_content=check_code)
                if self.lib[check_name_] == check_code_:
                    return 'right'
                else:
                    return 'false'

test = AccountCode()
test.add__new_account(account_name='a1',account_code='a1')


def main_menu():
    logger.info('main_menu running....')
    def menu_step_one():
        def first_introduce_page():
            introduce_text.insert(tk.END, '如有账号先账密登录,无账号则需注册....\n')
            first_introduce_root.update_idletasks()
            time.sleep(2)

            introduce_text.insert(tk.END, '此工具功能有: 爬取搜索相关内容数据, 爬取用户主页信息....\n')
            first_introduce_root.update_idletasks()
            time.sleep(2)

            introduce_text.insert(tk.END, '点击退出以继续下一进程....\n')
            first_introduce_root.update_idletasks()
            time.sleep(2)

            def first_quit_page():
                if messagebox.askyesno('提示', '确认退出当前页面以进行后续?'):
                    first_introduce_root.destroy()

            ttk.Button(first_introduce_root, text='退出', command=first_quit_page).pack()

        first_introduce_root = tk.Tk()
        first_introduce_root.title('介绍界面')

        introduce_text = tk.Text(first_introduce_root)
        introduce_text.pack()

        ttk.Button(first_introduce_root, text='开始使用', command=first_introduce_page).pack()
        first_introduce_root.mainloop()

    def menu_step_two():
        def second_login_or_registrate():
            def login_login_option():
                def if_login():
                    login_account = str(login_account_input.get().strip())
                    login_password = str(login_password_input.get().strip())
                    try:
                        if login_account is None or login_password is None:
                            messagebox.showwarning('提示', '输入无效!')
                        else:
                            if messagebox.askyesno('提示',
                                                   f'输入的账密为:\n帐:{login_account}\n密:{login_password}\n是否确认登录?'):
                                try:
                                    if test.load_database(login_account, login_password) == 'right':
                                        login_root.withdraw()
                                        login_or_registrate_root.withdraw()
                                        #########功能主界面#######
                                        main_menu_functions()
                                        #########功能主界面#######
                                except Exception:
                                    messagebox.showwarning('错误', '账密有错!')
                    except Exception as e:
                        logger.error(e)

                def quit_login_page():
                    if messagebox.askyesno('提示', '确认退出?'):
                        login_root.destroy()

                login_root = tk.Tk()
                login_root.title('登录界面')

                ttk.Label(login_root, text='账号:').grid(row=1, column=0, columnspan=2)
                login_account_input = ttk.Entry(login_root)
                login_account_input.grid(row=1, column=3, columnspan=5)

                ttk.Label(login_root, text='密码:').grid(row=2, column=0, columnspan=2)
                login_password_input = ttk.Entry(login_root)
                login_password_input.grid(row=2, column=3, columnspan=5)

                ttk.Button(login_root, text='确认登录', command=if_login).grid(row=3, column=0, columnspan=2)
                ttk.Button(login_root, text='退出', command=quit_login_page).grid(row=3, column=3, columnspan=2)
                login_root.mainloop()

            def registrate_registrate_option():
                def if_registrate():
                    registrate_account = str(registrate_account_input.get().strip())
                    registrate_password = str(registrate_password_input.get().strip())
                    try:
                        test.add__new_account(registrate_account, registrate_password)
                    except Exception as e:
                        logger.error(e)

                def quit_registrate_page():
                    if messagebox.askyesno('提示', '确认退出?'):
                        registrate_root.destroy()

                registrate_root = tk.Tk()
                registrate_root.title("注册页面")

                ttk.Label(registrate_root, text='账号:').grid(row=1, column=0, columnspan=2)
                registrate_account_input = ttk.Entry(registrate_root)
                registrate_account_input.insert(0, '删除此内容以输入..')
                registrate_account_input.grid(row=1, column=3, columnspan=5)

                ttk.Label(registrate_root, text='密码:').grid(row=2, column=0, columnspan=2)
                registrate_password_input = ttk.Entry(registrate_root)
                registrate_password_input.insert(0, '删除此内容以输入..')
                registrate_password_input.grid(row=2, column=3, columnspan=5)

                ttk.Button(registrate_root, text='确认注册', command=if_registrate).grid(row=3, column=0, columnspan=2)
                ttk.Button(registrate_root, text='退出', command=quit_registrate_page).grid(row=3, column=3,
                                                                                            columnspan=2)
                registrate_root.mainloop()

            def quit_login_or_registrate_option():
                if messagebox.askyesno('提示','确认退出?'):
                    login_or_registrate_root.destroy()

            login_or_registrate_root = tk.Tk()
            login_or_registrate_root.title('账号信息管理界面')

            ttk.Button(login_or_registrate_root,text='去登录',command=login_login_option).pack()
            ttk.Button(login_or_registrate_root,text='去注册',command=registrate_registrate_option).pack()
            ttk.Button(login_or_registrate_root,text='退出',command=quit_login_or_registrate_option).pack()
            login_or_registrate_root.mainloop()

        second_login_or_registrate()


    menu_step_one()
    menu_step_two()

if __name__ == '__main__':
    main_menu()
