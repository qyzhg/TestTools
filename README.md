# TestTools
编辑settings.py文件下的HOST全局变量，修改为自己的地址<br>
将json粘贴到json文件<br>
黑窗口cd切换到getyaml目录下<br>
使用命令 python(3) json_to_yaml.py --help可查看帮助<br>
使用命令 python(3) json_to_yaml.py --u json文件中的json的接口地址 --n 接口名，不要重复，没做校验 --m 请求方式，该版本适配三种请求方式：POST/data,POST/json,GET<br>
接口yaml文件会直接进入test_case目录中，文件名为 接口名.yaml 在locust_item/locustfile.py中，会追加写入性能测试方法，在test/test_api.py文件中会追加接口测试方法<br>