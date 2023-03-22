import sys
import unittest

class Test(unittest.TestCase):
    def test_p1(self):
        import p1
        self.assertEqual(p1.f(0), "")
        self.assertEqual(p1.f(6), "//////")
        self.assertEqual(p1.f(74), "+++++++////")
        self.assertEqual(p1.f(203), "**///")
        self.assertEqual(p1.f(345), "***++++/////")

    def test_p2(self):
        import p2
        self.assertEqual(p2.f([8,3,7,7,5,9,2,1,9,6],[6,10]), 6)
        self.assertEqual(p2.f([1,3,7],[1,5]), 2)

    def test_p3(self):
        import p3
        self.assertEqual(p3.f("KW425"),True)
        self.assertEqual(p3.f("K42561"),True)
        self.assertEqual(p3.f("KY123456"),False)
        self.assertEqual(p3.f("K123K"),False)

    def test_p4(self):
        import p4
        self.assertEqual(p4.f({"BA6":51,"DGX338":6,"TWA88":142},85),"TWA88")
        self.assertEqual(p4.f({"BA6":51,"DGX338":6,"TWA88":142},20),"BA6,TWA88")

    def test_p5(self):
        import p5
        self.assertEqual(p5.C("Robin","Williams",38,2).__str__(),"WILLIAMSR2")
        self.assertEqual(p5.C("Sofie","Pratt",16,6).__str__(),"pratts6")

    def test_p6(self):
        import p6
        self.assertEqual(p6.C([[2,4],[-2,1],[2,-2],[4,2],[2,4],[4,4],[2,-4]]).m(3),True)
        self.assertEqual(p6.C([[2,4],[-2,1],[2,-2],[4,2],[2,4],[4,4],[2,-4]]).m(5),False)

    def test_p7(self):
        import p7
        self.assertEqual(p7.C.m(123455667788),True)
        self.assertEqual(p7.C.m(12341234),False)

    def test_p8(self):
        import p8
        self.s1 = p8.C({"X":50,"Y":70,"Z":90,"B":110})
        self.assertEqual(self.s1.m2("WZ"),90)
        self.s1.m1("Y",170)
        self.assertEqual(self.s1.m2("YZ"),260)
        self.s1.m1("K",10)
        self.assertEqual(self.s1.m2("KYZ"),270)

if __name__ == '__main__':
    sys.stderr = open('test_results.txt', 'w', encoding="utf-8")
    unittest.main(verbosity=2)