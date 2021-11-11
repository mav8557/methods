"""
Represents a bug reporting service
"""


def random_string(length):
    """
    Not super relevant, generate a random string
    """
    from random import choice
    from string import ascii_uppercase

    # get a list of random uppercase characters, join() into a string
    return "".join([choice(ascii_uppercase) for x in range(length)])


class Bug:
    __slots__ = ["__description", "__severity", "__software", "__name"]

    def __init__(self, software=None, description=None, severity=None):
        self.__description = description
        self.__software = software
        self.__severity = severity  # number out between 0.0 and 10.0

        # set random name
        self.gen_random_name()

    def gen_random_name(self):
        self.__name = "VULN-" + str(self.__severity) + "-" + random_string(4).upper()

    def get_name(self):
        return self.__name

    def set_desc(self, description):
        self.__description == description

    def get_desc(self):
        return self.__description

    def set_software(self, software):
        self.__software == software

    def get_software(self):
        return self.__software

    def set_severity(self, severity):
        self.__severity = severity

    def get_severity(self):
        return self.__severity


class Discloser:
    """
    A bug disclosure service.
    Lets users create accounts, log in, and disclose bugs
    """

    def __init__(self):
        self.__users = {"michael": "5f4dcc3b5aa765d61d8327deb882cf99"}
        self.__bugs = []  # list of Bug objects

    def _insecure_hash(self, password):
        """
        NOT A SECURE HASH FUNCTION
        """
        from hashlib import md5

        return md5(password.encode()).hexdigest()

    def register_user(self, username, password):
        """
        Register (or overwrite) a user in the database
        """
        self.__users[username] = self._insecure_hash(password)

    def login(self, username, password):
        """
        Log in a user.

        Returns True if the user exists and the
        password is correct.
        """
        # if user is not registered, don't log in.
        if username not in self.__users:
            return False

        pw_hash_on_file = self.__users[username]

        if self._insecure_hash(password) == pw_hash_on_file:
            # user is registered and entered the right password
            # hash(password given) = hash(password registered)
            return True

        return False

    def disclose(self, bug):
        """
        Given a bug object the user forms,
        add it to the list of bugs
        """
        self.__bugs.append(bug)
        print(self.__bugs)

    def get_bugs(self, count):
        return self.__bugs[:count]

    def get_all_bugs(self):
        return self.__bugs

    def pop_latest(self):
        return self.__bugs.pop(0)


if __name__ == "__main__":
    discloser = Discloser()
    discloser.register_user("michael", "password")
    discloser.register_user("testuser", "admin")

    if discloser.login("michael", "password") and discloser.login("testuser", "admin"):
        print("log in is working")

    bug = Bug("Google Chrome", "Buffer Overflow", 2)

    discloser.disclose(bug)

    buglist = discloser.get_all_bugs()
