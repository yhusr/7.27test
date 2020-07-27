pytest中如果想要使用如下命令
pytest.main(["--reruns", "2", "--reruns-delay", "5", "--junitxml=reports/allure.xml"])
需要进行如下安装后方可使用命令："--reruns", "2", "--reruns-delay", "5"
pip install pytest-rerunfailures