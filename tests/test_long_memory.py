from memory.long_term import LongTermMemory

memory = LongTermMemory()

memory.store(

    "MSFT",

    """
Microsoft is a technology company.

Revenue is 281 Billion.

Net Income is 101 Billion.

"""
)

print()

print("Stored Successfully")

print()

print(memory.retrieve("MSFT"))

print()

print(memory.search("Microsoft revenue"))
