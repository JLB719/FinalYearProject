from django.test import TestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from reccomenderapp.models import UserPreferences
# Create your tests here.

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent;

sys.path.insert(0, str(BASE_DIR) + '/reccomenderalgorithm')
visitcount = 0

from recomendtvshow import reccomendtvshow

testdata = [[500, 1986, ["English"], ["United States", "United Kingdom"], ["Action", "Adventure", "Crime", "Thriller"],
             ["Animation", "Biography", "Documentary", "Family", "Game-Show"],
             ["13 Reasons Why", "12 Monkeys", "Altered Carbon", "Delete", "Trinkets"],
             ["Arrow", "Babylon", "Dare Me", "The Fall", "The Flash"]]]

testdata2 = [[500, 1986, ["English"], ["United States", "United Kingdom"], ["Action", "Adventure", "Crime", "Thriller"],
              ["Animation", "Biography", "Documentary", "Family", "Game-Show"],
              ["13 Reasons Why", "12 Monkeys", "Altered Carbon", "Delete", "Trinkets"],
              ["Arrow", "Babylon", "Dare Me", "The Fall", "The Flash"]],
             [400, 1987, ["English"], ["United States", "United Kingdom"],
              ["Action", "Comedy", "History", "Horror", "Thriller", "War", "Western"],
              ["Drama", "Fantasy", "Family"], ["Archer", "Deadly Class", "On My Block", "Pacific Rim", "Seinfeld"],
              ["The Umbrella Academy", "Prank Encounters", "Mighty Express", "White Gold", "The Wedding Coach"]]]


class SeleniumTests(TestCase):

    def test_1register(self):
        """
        Testing registration of user
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk')
        signup = selenium.find_element_by_id("signup")
        signup.click()
        assert '<h2>Sign up</h2>' in selenium.page_source
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password1")
        passwordconfirm = selenium.find_element_by_id("id_password2")
        submit = selenium.find_element_by_id("submitbtn")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        passwordconfirm.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        assert '<h2>Log In</h2>' in selenium.page_source

    def test_2nopref(self):
        """
        Testing what is shown when a user hasn't entered any prefrences
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        prefs = selenium.find_element_by_id("userresults")
        prefs.click()
        assert "<h1> You have not entered any preferences therefore cannot display recommendations </h1>" in selenium.page_source

    def test_3login(self):
        """
        Testing the user loggin in
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)

        assert '<h1>How the algorithm works</h1>' in selenium.page_source

    def test_4filloutform(self):
        """
        Testing the filling out of a form and it returning the same recomendations as the algorithm
        Then checking the preferences are matched on the user info page
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        selenium.find_element_by_id("form").click()
        selenium.find_element_by_id("id_oldestyear").send_keys(Keys.CONTROL + "a")
        selenium.find_element_by_id("id_oldestyear").send_keys(Keys.DELETE)
        selenium.find_element_by_id("id_oldestyear").send_keys('1986')
        selenium.find_element_by_id("id_minepisodes").send_keys(Keys.CONTROL + "a")
        selenium.find_element_by_id("id_minepisodes").send_keys(Keys.DELETE)
        selenium.find_element_by_id("id_minepisodes").send_keys('500')
        selenium.find_element_by_id("id_languages_6").click()
        selenium.find_element_by_id("id_orgincountries_50").click()
        selenium.find_element_by_id("id_orgincountries_51").click()
        selenium.find_element_by_id("id_likedgenres_0").click()
        selenium.find_element_by_id("id_likedgenres_1").click()
        selenium.find_element_by_id("id_likedgenres_5").click()
        selenium.find_element_by_id("id_likedgenres_23").click()
        selenium.find_element_by_id("id_dislikedgenres_2").click()
        selenium.find_element_by_id("id_dislikedgenres_3").click()
        selenium.find_element_by_id("id_dislikedgenres_6").click()
        selenium.find_element_by_id("id_dislikedgenres_8").click()
        selenium.find_element_by_id("id_dislikedgenres_10").click()
        selenium.find_element_by_id("submit").click()
        select = Select(selenium.find_element_by_id("id_likedtvshow1"))
        select.select_by_visible_text("13 Reasons Why")
        select2 = Select(selenium.find_element_by_id("id_likedtvshow2"))
        select2.select_by_visible_text("12 Monkeys")
        select3 = Select(selenium.find_element_by_id("id_likedtvshow3"))
        select3.select_by_visible_text("Altered Carbon")
        select4 = Select(selenium.find_element_by_id("id_likedtvshow4"))
        select4.select_by_visible_text("Delete")
        select5 = Select(selenium.find_element_by_id("id_likedtvshow5"))
        select5.select_by_visible_text("Trinkets")
        select6 = Select(selenium.find_element_by_id("id_dislikedtvshow1"))
        select6.select_by_visible_text("Arrow")
        select7 = Select(selenium.find_element_by_id("id_dislikedtvshow2"))
        select7.select_by_visible_text("Babylon")
        select8 = Select(selenium.find_element_by_id("id_dislikedtvshow3"))
        select8.select_by_visible_text("Dare Me")
        select9 = Select(selenium.find_element_by_id("id_dislikedtvshow4"))
        select9.select_by_visible_text("The Fall")
        select10 = Select(selenium.find_element_by_id("id_dislikedtvshow5"))
        select10.select_by_visible_text("The Flash")
        selenium.find_element_by_id("submit").click()
        body_text = selenium.find_element_by_tag_name('body').text
        results = reccomendtvshow(testdata)

        assert results[0] in body_text
        assert results[1] in body_text
        assert results[2] in body_text
        assert results[3] in body_text
        assert results[4] in body_text
        assert results[5] in body_text
        assert results[6] in body_text
        assert results[7] in body_text
        assert results[8] in body_text
        assert results[9] in body_text

    def test_5creategroup(self):
        """
        Testing a user creating a group
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        creategroup = selenium.find_element_by_id("creategroup")
        creategroup.click()
        groupfield = selenium.find_element_by_id("id_groupname")
        groupfield.send_keys("Mytestgroup3")
        submit = selenium.find_element_by_id("submit")
        submit.click()
        assert '<h2>Created Mytestgroup3</h2>' in selenium.page_source

    def test_6join_group(self):
        """
        Testing a user can join a group from the list of groups
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        joingroup = selenium.find_element_by_id("joingroup")
        joingroup.click()
        select = Select(selenium.find_element_by_id("id_grouplistfield"))
        select.select_by_visible_text("private3")
        submit = selenium.find_element_by_id("submit")
        submit.click()
        assert '<h2>Joined private3</h2>' in selenium.page_source

    def test_7join_group_link(self):
        """
        Testing a user can join a group through a group link
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        selenium.get("http://jlb838.uk/groups/modeltest3")
        assert 'Joined modeltest3' in selenium.page_source
        allrecs = selenium.find_element_by_id("userresults")
        allrecs.click()
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'modeltest3' in body_text

    def test_8load_preferences(self):
        """
        Testing a user can see thier prefrences and joined groups on the detailed page
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        selenium.find_element_by_id("userresults").click()
        body_text = selenium.find_element_by_tag_name('body').text
        results = reccomendtvshow(testdata)

        assert results[0] in body_text
        assert results[1] in body_text
        assert results[2] in body_text
        assert results[3] in body_text
        assert results[4] in body_text
        assert results[5] in body_text
        assert results[6] in body_text
        assert results[7] in body_text
        assert results[8] in body_text
        assert results[9] in body_text
        assert 'modeltest3' in body_text
        assert 'private3' in body_text
        assert 'Mytestgroup3' in body_text

    def test_9groupalreadyexist(self):
        """
        Checking that the site reacts appropraitely if a user tries to create a group that already exists
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        creategroup = selenium.find_element_by_id("creategroup")
        creategroup.click()
        groupfield = selenium.find_element_by_id("id_groupname")
        groupfield.send_keys("123")
        submit = selenium.find_element_by_id("submit")
        submit.click()
        assert '<h2>The group already exists</h2>' in selenium.page_source

    def test_agenerate_group_results(self):
        """
        Testing the generation of group results compared to the algorithm processing the input directly
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/accounts/login/')
        username = selenium.find_element_by_id("id_username")
        password = selenium.find_element_by_id("id_password")
        submit = selenium.find_element_by_id("submitbutton")
        username.send_keys('seleniumtest3')
        password.send_keys('helloworld10')
        submit.send_keys(Keys.RETURN)
        selenium.find_element_by_id("selectgroupgenerate").click()
        select = Select(selenium.find_element_by_id("id_groupname"))
        select.select_by_visible_text("modeltest3")
        selenium.find_element_by_id("submit").click()
        body_text = selenium.find_element_by_tag_name('body').text
        results = reccomendtvshow(testdata2)

        assert results[0] in body_text
        assert results[1] in body_text
        assert results[2] in body_text
        assert results[3] in body_text
        assert results[4] in body_text
        assert results[5] in body_text
        assert results[6] in body_text
        assert results[7] in body_text
        assert results[8] in body_text
        assert results[9] in body_text

    def test_load_ballshows(self):
        """
        Testing some of the tv shows in the dataset have been shown
        """
        selenium = webdriver.Chrome()
        selenium.get('http://jlb838.uk/')
        allshows = selenium.find_element_by_id("listall")
        allshows.click()
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'A Perfect Crime' in body_text
        assert 'Altered Carbon' in body_text
        assert 'Dark Net' in body_text
        assert 'Zoo' in body_text
        assert 'X-Men' in body_text
        assert '<h2>All the shows that are in the data set</h2>' in selenium.page_source
        assert '<h4>Click on the title of the show to see more info</h4>' in selenium.page_source


class TestUnit(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creates a sample model to test
        """
        UserPreferences.objects.create(username="James", maxyear=1990, numberofepisodes=100, languages="English",
                                       origincountries="United States, United Kingdom", likedgenres="Action,Horror",
                                       dislikedgenres="Animation,Comedy", likedshows="1984, The 100, Yesman, Jamesshow",
                                       dislikedshows="Percent, 50, hello, bye, ja")

    def testusername(self):
        """
        Tests the type of the username and the actual username matches
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.username, str)
        self.assertEqual(user.username, "James")

    def testmaxyear(self):
        """
        Tests the type and year matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.maxyear, int)
        self.assertEqual(user.maxyear, 1990)

    def testmaxepisodes(self):
        """
        Tests the type and number of episodes matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.numberofepisodes, int)
        self.assertEqual(user.numberofepisodes, 100)

    def testlanguages(self):
        """
        Tests the type and language matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.languages, str)
        self.assertEqual(user.languages, "English")

    def testorigincountries(self):
        """
        Tests the type and origin countries matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.origincountries, str)
        self.assertEqual(user.origincountries, "United States, United Kingdom")

    def testlikedgenres(self):
        """
        Tests the type and liked genres matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.likedgenres, str)
        self.assertEqual(user.likedgenres, "Action,Horror")

    def testdislikedgenres(self):
        """
        Tests the type and disliked genres matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.dislikedgenres, str)
        self.assertEqual(user.dislikedgenres, "Animation,Comedy")

    def testlikedshows(self):
        """
        Tests the type and likedshows matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.likedshows, str)
        self.assertEqual(user.likedshows, "1984, The 100, Yesman, Jamesshow")

    def testdislikedshows(self):
        """
        Tests the type and dislikedtvshows matches the expected value
        """
        user = UserPreferences.objects.get(id=1)
        self.assertIsInstance(user.dislikedshows, str)
        self.assertEqual(user.dislikedshows, "Percent, 50, hello, bye, ja")
