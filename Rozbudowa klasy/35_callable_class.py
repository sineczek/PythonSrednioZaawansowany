class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list

    def __call__(self, item):
        self.list_of_items.append(item)

mem = MemoryClass([])
print('List of items in memory', mem.list_of_items)

mem.list_of_items.append('buy sugar')
print('List of items in memory', mem.list_of_items)

mem('buy coffee')
mem('buy milk')
print('List of items in memory', mem.list_of_items)
print('List of items in memory', mem.list_of_items)

print('This class is callable: ', callable(MemoryClass)) #obiekt wywoływalny
print('This class is callable: ', callable(mem)) #zanim powstało __call__ w classie nie była wywoływalna, po już jest





