# memory/episodic.py

from datetime import datetime


class EpisodicMemory:
    """
    Stores past research sessions.
    """

    def __init__(self):

        self.history = []

    def add_episode(
        self,
        company,
        query,
        tools_used,
        status
    ):

        episode = {

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "company": company,

            "query": query,

            "tools_used": tools_used,

            "status": status

        }

        self.history.append(episode)

    def get_all(self):

        return self.history

    def latest(self):

        if self.history:

            return self.history[-1]

        return None