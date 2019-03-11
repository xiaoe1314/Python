"""
    Created by 朝南而行 2019/3/11 15:15
"""
from projects.App import unitTestAppium
import unittest

# 一个类里面的多个测试用例 (有数据驱动不可以用这种方法)
# mySuite = unittest.TestSuite()
# mySuite.addTest(unitTestAppium.MyTestCase('test_anything'))
# mySuite.addTest(unitTestAppium.MyTestCase('test_something'))

# 直接测试一个类的用例 (有数据驱动可以用这种方法)
cases = unittest.TestLoader().loadTestsFromTestCase(unitTestAppium.MyTestCase)
mySuite = unittest.TestSuite([cases])

myRunner = unittest.TextTestRunner(verbosity=2)
myRunner.run(mySuite)

