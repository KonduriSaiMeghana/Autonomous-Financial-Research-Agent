# memory/long_term.py

import chromadb


class LongTermMemory:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="memory/chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="financial_reports"
        )

    def store(self, company, report):

        self.collection.add(

            ids=[company],

            documents=[report]

        )

    def retrieve(self, company):

        results = self.collection.get(ids=[company])

        return results

    def search(self, query, n_results=3):

        results = self.collection.query(

            query_texts=[query],

            n_results=n_results

        )

        return results