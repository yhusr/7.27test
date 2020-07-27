pytest中如果想要使用如下命令
pytest.main(["--reruns", "2", "--reruns-delay", "5", "--junitxml=reports/allure.xml"])
需要进行如下安装后方可使用命令："--reruns", "2", "--reruns-delay", "5"
pip install pytest-rerunfailures


@pytest.fixture(scope='class', autouse=True)
@pytest.fixture(scope='class')
@pytest.fixture(scope='class')
以上三个fixture中scope一样的时候，如果设置autouse
那这个fixture就会先执行