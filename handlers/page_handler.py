from models.dmoz_page import DmozPage

class PageHandler:

    def __init__(self, session):
        self.session = session
        self.ct = 0

    def page(self, page, content):

        entry = DmozPage(page, content)
        self.session.add(entry)
        self.ct += 1

        if not self.ct % 10000:
            self.session.commit()
        elif not self.ct % 100:
            self.session.flush()

    def finish(self):
        self.session.commit()
        self.session.close()