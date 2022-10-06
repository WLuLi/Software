import unittest

from app.checkers.user import register_params_check


class BasicTestCase(unittest.TestCase):
    '''
    TODO: 在这里补充注册相关测试用例
    '''

    # python manage.py test -f test_basic

    # nonetype
    def test_register_params_check_00(self):
        self.assertEqual(register_params_check(None), ("ok", True))
    
    # empty
    def test_register_params_check_01(self):
        content = {}
        self.assertEqual(register_params_check(content), ("ok", True))

    # lack username
    def test_register_params_check_02(self):
        content = {}
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # lack password
    def test_register_params_check_03(self):
        content = {}
        content['username'] = 'wangqj20'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))    

    # lack nickname
    def test_register_params_check_04(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True)) 

    # lack url
    def test_register_params_check_05(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True)) 

    # lack mobile
    def test_register_params_check_06(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        self.assertEqual(register_params_check(content), ("ok", True))

    # username err: short  
    def test_register_params_check_07(self):
        content = {}
        content['username'] = 'wa20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # username err: long
    def test_register_params_check_08(self):
        content = {}
        content['username'] = 'wangqj20fromsoftwareengineering'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # username err: no letter
    def test_register_params_check_09(self):
        content = {}
        content['username'] = '2020010971'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # username err: no number
    def test_register_params_check_10(self):
        content = {}
        content['username'] = 'wangqj'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # username err: sequence
    def test_register_params_check_11(self):
        content = {}
        content['username'] = '20wangqj'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # password err: short
    def test_register_params_check_12(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-H'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # password err: long
    def test_register_params_check_13(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHAHAHAHAHAHAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # password err: lack type
    def test_register_params_check_14(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-haha'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # password err: illegal symbol
    def test_register_params_check_15(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha@HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # mobile err: erea short
    def test_register_params_check_16(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+8.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # mobile err: erea long
    def test_register_params_check_17(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+886.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # mobile err: number short
    def test_register_params_check_18(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.18970048533'
        self.assertEqual(register_params_check(content), ("ok", True))

    # mobile err: number long
    def test_register_params_check_19(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.1897004853322'
        self.assertEqual(register_params_check(content), ("ok", True))

    # mobile err: lack point
    def test_register_params_check_20(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+861897004853322'
        self.assertEqual(register_params_check(content), ("ok", True))

    # url err: protocol
    def test_register_params_check_21(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'hop://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # url err: domain symbol
    def test_register_params_check_22(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20-.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # url err: number top domain
    def test_register_params_check_23(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.114514'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # url err: http long
    def test_register_params_check_24(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn.wangqj20.mails.tsinghua.edu'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # url err: https long
    def test_register_params_check_25(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'https://wangqj20.mails.tsinghua.edu.cn.wangqj20.mails.tsinghua.ed'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # url err: other symbol
    def test_register_params_check_26(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20@mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
        
    # url err: no point
    def test_register_params_check_27(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20mailstsinghuaeducn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))
    
    # magic number err: negative
    def test_register_params_check_28(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        content['magic_number'] = -1
        self.assertEqual(register_params_check(content), ("ok", True))

    # ok
    def test_register_params_check_ok(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'http://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

    # ok2
    def test_register_params_check_ok2(self):
        content = {}
        content['username'] = 'wangqj20'
        content['password'] = '233ha-HAHA'
        content['nickname'] = 'wangluli'
        content['url'] = 'https://wangqj20.mails.tsinghua.edu.cn'
        content['mobile'] = '+86.189700485332'
        self.assertEqual(register_params_check(content), ("ok", True))

if __name__ == '__main__':
    unittest.main()
