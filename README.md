# M5Cloud

## 快速开始

### 1. 烧录固件
#### Windows烧录
Windows使用Espressif提供Flash Download Tools工具烧录([点击下载](http://espressif.com/sites/default/files/tools/flash_download_tools_v3.6.2.2_0.rar))，设置如下(先擦除再烧录)：
  ![image](docs/img/windows_esptool.png)


#### MacOS/Linux烧录
- 使用pip安装esptool：

    ```pip install esptool```

- 烧录bin文件:

    ``` esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 firmware.bin ```

### 2. 让设备WiFi接入网络
- **方法1:** 使用热点接入，通过Web配置网络
  - 手机或电脑连接M5Stack Core屏幕提示的WiFi热点
  ![image](docs/img/img_startup_ap.JPG)

    连接M5Stack Core WiFi：

    ![image](docs/img/wificonnect.png)
  - 打开浏览器登陆 192.168.4.1填入WiFi的SSID和密码
- **方法2:** 通过串口配置WiFi密码

    通过串口REPL或者上传工具在设备根目录下创建一个名字为：config.json的文件，文件内wifi的配置参数JSON格式如下：
    ```
    {
        "wifi":{
            "ssid":"MasterHax_2.4G",
            "password":"12345678"
        }
    }
    ```
- **方法3:** 通过微信扫描二维码Airkiss接入

  TODO

### 3. 绑定设备
  登陆 http://io.m5cloud.com 注册账号,添加设备：

  ![image](docs/img/add.jpg)

  将M5Stack Core屏幕显示的Check Code填入绑定设备
  
  ![image](docs/img/img_conncet-suc.JPG)
  
  ![image](docs/img/checkcode.jpg)



### 4. 开始编程
![image](docs/img/ide_uploads.jpg)

### 常见问题
