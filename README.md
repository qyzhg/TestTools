# TestTools
编辑settings.py文件下的HOST全局变量，修改为自己的地址<br>
将json粘贴到json文件<br>
黑窗口cd切换到getyaml目录下<br>
使用命令 python(3) json_to_yaml.py --help可查看帮助<br>
使用命令 python(3) json_to_yaml.py --u json文件中的json的接口地址 --n 接口名，不要重复，没做校验 --m 请求方式，该版本适配三种请求方式：POST/data,POST/json,GET<br>
接口yaml文件会直接进入test_case目录中，文件名为 接口名.yaml 在locust_item/locustfile.py中，会追加写入性能测试方法，在test/test_api.py文件中会追加接口测试方法<br>
locust使用方法：<br>
进入locust目录中 使用命令 locust -f locustfile.py(仅限临时测试使用，服务器部署稳定版需使用docker)<br>
<hr>
<p>
<h3>
未实现功能备忘：
</h3></p>
<s>data和json转换自动判断 2020年05月29日15:09:10 已实现<br></s>
*添加yaml文件时，判断目录中是否存在同名文件，不是直接覆盖<br>
<s>*可以选择是否添加入代码   2020年5月28日22:51:53 已实现<br></s>
*判断传入的测试用例名称是否包含.yaml关键字并处理<br>
<p><h2>终极目标：</h2></p>
<p>使用django重构项目</p>
