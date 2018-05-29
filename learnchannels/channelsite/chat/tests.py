# chat/tests.py
from channels.testing import ChannelsLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

# quick note on @classmethod...similar to @staticmethod, but passes in a reference
# to the class, and can modify class attributes
# @staticmethods, on the other hand, cannot

class ChatTests(ChannelsLiveServerTestCase):
    serve_static = True # not sure what the purpose of this is

    # Using the parent class a great deal
    # Uses the parent methods to set up the class, and tear down the class
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            # requires chromedriver binary to be installed into $PATH
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    # This might be the longest method name I've ever seen
    # tests that when the chat is posted, everyone in the room sees it
    def test_when_chat_message_posted_then_seen_by_everyone_in_same_room(self):
        try:
            self._enter_chat_room("room_1")
            self._open_new_window()

            self._switch_to_window(0)
            self._post_message("hello")

            WebDriverWait(self.driver, 2).until(lambda _:
                "hello" in self._chat_long_value,
                "Message was not received by window 2 from window 1")
        # finally block ensures that this code is always executed
        finally:
            self._close_all_new_windows()

    def test_when_chat_messaage_posted_then_not_seen_by_anyone_in_different_room(self):
        try:
            # enters chat room
            self._enter_chat_room("room_1")

            self._open_new_window()
            self._enter_chat_room("room_2")

            self._switch_to_window(0)
            # posts hello message
            self._post_message("hello")


            WebDriverWait(self.driver, 2).until(lambda _:
                "hello" in self._chat_log_value,
                "Message was not received by window 1 from window 1")

            self._switch_to_window(1)
            self._post_message("world")

            WebDriverWait(self.driver, 2).until(lambda _:
                "world" in self._chat_log_value,
                "Message was not received by window 2 from window 2")

            # Making sure that no one else can read the messages sent in a room
            # that they're not in
            self.assertTrue("hello" not in self._chat_log_value,
                "Message was improperly received by window 2 from window 1")

        finally:
            self._close_all_new_windows()

    # === Utility ===
    # small change
    def _enter_chat_room(self, room_name):
        self.driver.get(self.live_erver_url + "/chat/")
        ActionChains(self.driver).send_keys(room_name + "\n").perform()
        WebDriverWait(self.driver, 2).until(lambda _:
            room_name in self.driver.current_url)

    def _open_new_window(self):
        self.driver.execute_script("window.open('about:blank', '_blank');")
        self.driver.switch_to_window(self.driver.window_handles[-1])

    def _close_all_new_windows(self):
        pass
