import flet as fl
import subprocess
def main(page: fl.Page):
    page.title = "scrcpy-gui"
    page.window_height = 270
    page.window_width = 400
    page.window_resizable = False
    def start_menu():
        try:
            subprocess.run(["taskkill","/f","/im","adb.exe"])
        except:
            print("未有开启adb")
        finally:
            print('adb应用已杀死')
        page.add(start_text,start_redio_buttons,start_button)
        page.update()
    def hide_start_menu(e):
        start_text.visible=False
        start_redio_buttons.visible=False
        start_button.visible=False
        page.update()
    def start_button(e):
        if ((f"{start_redio_buttons.value}") == "1"):
            hide_start_menu(e)
            mode_1(e)
        elif ((f"{start_redio_buttons.value}") == "2"):
            hide_start_menu(e)
            mode_2(e)
        else:
            page.banner.open = True
            page.update()
    def close_bannner(e):
        page.banner.open = False
        page.update()
    def open_banner(e):
        page.banner.open = True
        page.update()
    def adb_connect_script(e):
        ip = ip_tf.value
        port = port_tf.value
        if (ip == ""):
            page.banner=fl.Banner(bgcolor=fl.colors.AMBER_100,leading=fl.Icon(fl.icons.WARNING_AMBER_ROUNDED, color=fl.colors.AMBER, size=40),content=fl.Text("IP未输入！"),actions=[fl.ElevatedButton(text="明白！",on_click=close_bannner)])
            open_banner(e)
        elif (port == ""):
            page.banner=fl.Banner(bgcolor=fl.colors.AMBER_100,leading=fl.Icon(fl.icons.WARNING_AMBER_ROUNDED, color=fl.colors.AMBER, size=40),content=fl.Text("未输入端口！"),actions=[fl.ElevatedButton(text="明白！",on_click=close_bannner)])
            open_banner(e)
        elif not (0 < int(port) <= 65536):
            page.banner=fl.Banner(bgcolor=fl.colors.AMBER_100,leading=fl.Icon(fl.icons.WARNING_AMBER_ROUNDED, color=fl.colors.AMBER, size=40),content=fl.Text("错误的端口！"),actions=[fl.ElevatedButton(text="明白！",on_click=close_bannner)])
            open_banner(e)
        else:
            ip_port=ip+":"+port
            try:
                subprocess.run(["./adb.exe","connect",f"{ip_port}"])
            except:
                page.banner=fl.Banner(bgcolor=fl.colors.AMBER_100,leading=fl.Icon(fl.icons.WARNING_AMBER_ROUNDED, color=fl.colors.AMBER, size=40),content=fl.Text("连接失败！"),actions=[fl.ElevatedButton(text="明白！",on_click=close_bannner)])
                open_banner(e)
            finally:
                page.update()
    def scrcpy_qidong(e):
        try:
            subprocess.run(["./scrcpy.exe"])
        except:
                page.banner=fl.Banner(bgcolor=fl.colors.AMBER_100,leading=fl.Icon(fl.icons.WARNING_AMBER_ROUNDED, color=fl.colors.AMBER, size=40),content=fl.Text("连接失败！"),actions=[fl.ElevatedButton(text="明白！",on_click=close_bannner)])
                open_banner(e)
        finally:
            page.update()
        
    def mode_1(e):
        page.add(fl.ElevatedButton(text="启动scrcpy",width=200,height=50,on_click=scrcpy_qidong))
        page.update()
    def mode_2(e):
        page.add(ip_tf,port_tf,adb_connect_button,conect_button)
        page.update()
    ip_tf=fl.TextField(label="输入设备ip地址")
    port_tf=fl.TextField(label="请输入设备无线调试端口1-65536")
    conect_button=fl.ElevatedButton(text="启动scrcpy",on_click=scrcpy_qidong)
    adb_connect_button=fl.ElevatedButton(text="启动adb无线连接",on_click=adb_connect_script)
    back_button=fl.ElevatedButton(text="返回",)
    start_text=fl.Text("请选择工作模式:",size=20)
    start_redio_buttons=fl.RadioGroup(content=fl.Column([fl.Radio(value="1",label="有线连接"),(fl.Radio(value="2",label="无线连接"))]))
    start_button=fl.ElevatedButton(text="请选择工作模式",width=200,height=50,on_click=start_button)
    page.banner=fl.Banner(bgcolor=fl.colors.AMBER_100,leading=fl.Icon(fl.icons.WARNING_AMBER_ROUNDED, color=fl.colors.AMBER, size=40),content=fl.Text("没有选择任何工作模式！"),actions=[fl.ElevatedButton(text="明白！",on_click=close_bannner)])
    start_menu()
fl.app(target=main)
