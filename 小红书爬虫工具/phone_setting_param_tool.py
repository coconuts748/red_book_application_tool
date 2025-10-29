import tkinter as tk
from tkinter import ttk,messagebox
from 已完成.小红书爬虫工具.cite_part_xiao_hong_shu import creat_json_for_build_param
from loguru import logger

def setting_param_tool():
    def get_setting_param():
        automation_name = str(get_automation_name.get().strip())
        platform_name = str(get_platform_name.get().strip())
        device_name =str(get_device_name.get().strip())
        if len(automation_name) ==0 or len(platform_name) ==0 or len(device_name) ==0:
            messagebox.showwarning('错误','输入无效!')
        else:
            if messagebox.askyesno('提示',f'当前输入为:\n驱动:{automation_name}\n系统:{platform_name}\n设备:{device_name}'):
                try:
                    json_content = {
                        'automationName': automation_name,
                        'platformName': platform_name,
                        'deviceName': device_name,
                        'noReset': True
                    }
                    creat_json_for_build_param(json_content=json_content, file_name='phone_setting_param')
                    messagebox.showinfo('提示','已生成成功,现可查看！')
                    if messagebox.askyesno('提示','是否退出当前？'):
                        setting_root.destroy()
                except Exception as e:
                    logger.error(f'手机配置参数生成失败:{e}')
    def quit_get_setting_param():
        if messagebox.askyesno('提示','确认退出当前页面?'):
            setting_root.destroy()


    setting_root = tk.Tk()
    setting_root.title('参数生成')

    ttk.Label(setting_root,text='命令符输入appium即可查看相关参数').grid(row=0,column=0,columnspan=5)
    ttk.Label(setting_root,text='驱动名可参考里面参数介绍').grid(row=1,column=0,columnspan=5)
    ttk.Label(setting_root,text='系统名根据自己手机系统来定(Android or Ios)').grid(row=2,column=0,columnspan=5)
    ttk.Label(setting_root,text='设备名参考“adb devices” 反馈的参数').grid(row=3,column=0,columnspan=5)

    ttk.Label(setting_root,text='驱动名:').grid(column=0, row=5,columnspan=3)
    get_automation_name = tk.Entry(setting_root)
    get_automation_name.grid(column=4, row=5,columnspan=5)

    ttk.Label(setting_root,text='系统名:').grid(column=0, row=7,columnspan=3)
    get_platform_name = tk.Entry(setting_root)
    get_platform_name.grid(column=4, row=7,columnspan=5)

    ttk.Label(setting_root,text='设备名:').grid(column=0, row=9,columnspan=3)
    get_device_name = tk.Entry(setting_root)
    get_device_name.grid(column=4, row=9,columnspan=5)

    ttk.Button(setting_root,text='生成配置参数',command=get_setting_param).grid(row=11,column=0,columnspan=2)
    ttk.Button(setting_root,text='退出',command=quit_get_setting_param).grid(row=11,column=3,columnspan=2)
    setting_root.mainloop()

# setting_param_tool()

