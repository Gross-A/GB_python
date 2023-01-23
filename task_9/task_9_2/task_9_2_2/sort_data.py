from operator import itemgetter, attrgetter

# data = [['нб', 'fgfh'],['сдо', 'fdd', 'dff'], ['мо', 'fhfh']]
def sort_data(data, key_item):
    return sorted(data, key = itemgetter(key_item)) #сортируем список по фамилии в алф порядке

