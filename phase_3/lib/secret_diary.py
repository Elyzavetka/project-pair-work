class SecretDiary:
    def __init__(self, diary):
        # diary is an instance of Diary
        self._diary = diary
        self._locked = True

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self._locked:
            raise Exception("No access")
        else:
            return self._diary.read()


    def lock(self):
        # Locks the diary
        # Returns nothing
        self._locked = True

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self._locked = False