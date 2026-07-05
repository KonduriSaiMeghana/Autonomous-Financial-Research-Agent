from memory.short_term import ShortTermMemory

memory = ShortTermMemory()

memory.store("company", "Microsoft")

memory.store("revenue", "281 Billion")

print(memory.retrieve("company"))

print(memory.retrieve_all())

memory.clear()

print(memory.retrieve_all())