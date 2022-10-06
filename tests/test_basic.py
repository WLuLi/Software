import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''
    def test_register_params_check(self):
        content={}
        content['username']='wanglulie123'
        content['password']='wangluli1-W'
        content['nickname']='wangluli'
        content['url']='http://233abc.123.com'
        content['mobile']='+86.123456789010'
        self.assertEqual(register_params_check(content), ("ok", True))


if __name__ == '__main__':
    unittest.main()
