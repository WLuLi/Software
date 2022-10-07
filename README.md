### run for dev

```bash
pip install virtualenv
virtualenv venv
# 安装依赖
pip install -r requirements.txt
# 编辑配置
vim config.yaml 
# 启动 flask 应用
python manage.py init_db
python manage.py runserver
# 启动单元测试
python manage.py test -f test_basic
# 启动集成测试
python manage.py test -f test_api
# 启动端到端测试
python manage.py test -f test_e2e
```
