# TestTools
编辑settings.py文件下的HOST全局变量，修改为自己的地址<br>
将json粘贴到json文件<br>
黑窗口cd切换到getyaml目录下<br>
使用命令 python(3) json_to_yaml.py --help可查看帮助<br>
使用命令 python(3) json_to_yaml.py --u json文件中的json的接口地址 --n 接口名，不要重复，没做校验 --m 请求方式，该版本适配三种请求方式：POST/data,POST/json,GET<br>
接口yaml文件会直接进入test_case目录中，文件名为 接口名.yaml 在locust_item/locustfile.py中，会追加写入性能测试方法，在test/test_api.py文件中会追加接口测试方法<br>
locust使用方法：<br>
进入locust目录中 使用命令 locust -f locustfile.py(仅限临时测试使用，服务器部署稳定版需使用docker)<br>
更新日志：<br>
data格式可以直接转换为json格式 <br>
--u参数可以直接传URL 不用手动分割<br> 
可以选择是否添加入代码<br>
接口名自动填充 使用--n @auto命令 可以根据接口地址填充接口名<br>
调用测试用例时可以判断是否已.yaml结尾，并处理<br>
<hr>
2020年5月30日19:53:55<br>
解耦重构代码，入口路径为Api/main<br>
命令改为 python(3) main.py --u 接口地址  --n 接口名(@auto 自动补全) --m 请求方式



<hr>
<p>
<h3>
未实现功能备忘：
</h3>
<s>data和json转换自动判断 2020年05月29日15:09:10 已实现<br></s>
<s>*添加yaml文件时，判断目录中是否存在同名文件，不是直接覆盖<br></s>
<s>*传参--u参数可以直接传URL 不用手动分割 2020年05月29日16:32:46 已完成</s><br>
<s>*可以选择是否添加入代码   2020年5月28日22:51:53 已实现<br></s>
<s>*接口名自动填充 2020年05月29日16:46:36 已完成 使用@auto关键字实现自动填充<br></s>
<s>*判断传入的测试用例名称是否包含.yaml关键字并处理 2020年5月30日16:48:53 已实现<br></s>
根据locust目录和testapi目录生成必要的文件
<p><h2>终极目标：</h2>
<p>使用django重构项目</p>
