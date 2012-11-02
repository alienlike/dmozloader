from models.dmoz_topic import DmozTopic

class TopicHandler:

    def __init__(self, session):
        self.session = session
        self.ct = 0

    def topic(self, topic):

        entry = DmozTopic(topic)
        self.session.add(entry)
        self.ct += 1

        if not self.ct % 10000:
            self.session.commit()
        elif not self.ct % 100:
            self.session.flush()

    def finish(self):
        self.session.commit()
        self.session.close()