# TestTools
## **`使用说明：`**

### **`创建项目：`**
##### 1.CD到项目根目录下（Api目录）。
##### 2.输入命令：python main.py -start 项目名 例如：
```shell script
python main.py -start hengsuan504
```
##### 3.此时，系统会生成几个新的目录，用于管理你的项目，目录结构如下：
>Api
>>locust_dir &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<<<用于存放所有项目的性能测试脚本的目录<br>
>>>HENGSUAN504 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<<<新建的项目文件夹，项目的性能测试脚本就会存在这里<br>

>>test_api_dir &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<<<用于存放所有项目的接口测试脚本的目录<br>
>>>HENGSUAN504 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<<<新建的项目文件夹，项目的接口测试脚本就会存在这里<br>

>>case_dir &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<<<用于存放所有项目的测试用例的目录<br>
>>>HENGSUAN504 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<<<新建的项目文件夹，项目的测试用例就会存在这里

### **`配置项目：`**
##### 1.进入根目录下settings.py文件中
##### 2.编辑 PROJECT_NAME 变量为项目名，例如上一个例子里的新建的项目叫hengsuan504，我现在要使用他，就将他改为**PROJECT_NAME = 'hengsuan504'**
##### 3.编辑 HOST 变量为项目地址，例如：HOST = 'http://10.102.111.117:8093/HCLCNNC/a/'

### **`生成测试脚本：`**
##### 1.正确完成前两部配置后，就可以生成脚本了，首先将脚本的发出请求的json粘贴到Api>getyaml>json文件下，支持Charles直接复制出来的json—text格式和form格式，目录位置:<br>
> Api
>> getyaml
>>> __ init __.py<br>
>>> data_to_json.py<br>
>>> **`json`**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<<<<<在这里<br>
>>> json_to_yaml.py<br>

##### 2.在Api目录下使用命令 python --u 接口地址，也可以使用完整的URL --n 接口名，也可以直接输入@auto关键字自动生成接口名，推荐自动生成 --m 请求方式，一共识别三种请求方式：POST/json，POST/data，GET。例如：
```shell script
python --u http://10.102.111.117:8093/HCLCNNC/a/ --n @auto --m POST/data
```
##### 3.输入完这条命令后，如果此接口名存在在测试用例文件夹中，系统会提示是否覆盖原有的文件，如果没有同名文件，则会弹出选择窗口，根据自己需求可以选择是否将代码追加到脚本中。

### **`使用接口测试脚本：`**
#### **接口测试脚本基于unittest框架，而且需要拆json，生成的只是一小部分，现阶段你们几个就先不要深究，能跑通就行，不需要做断言**
##### 在脚本最后添加如下语句：<br>
```python
if __name__ == '__main__':
    unittest.main(verbosity=2)
```
##### 即可在编辑器内右键 run 执行

### **`使用性能测试脚本：`**
##### 最新版的locust的使用语法变动较大，现正在探索中，基本用法脚本已经实现，可以直接在编辑器中使用右键 run 执行，然后在浏览器中输入127.0.0.1:8089进行性能测试
