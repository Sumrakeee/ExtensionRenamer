import os

def main():
	path = input('Путь: ').replace('"','')
	file_extension = input('Расширение файла (Например ".docx"): ')
	files = os.listdir(path)

	for i in files:
		if i != 'Thumbs.db':
			try:
				os.rename(path + '\\' + i, path + '\\' + i.split('.')[0] + file_extension)
				print(str(i) + '\t=====>\t' + i.split('.')[0] + file_extension)
			except:
				print('\nПереименование невозможно. Файл с этим именем уже находится в данной папке.\nУдаление файла...\n')
				os.remove(path + '\\' + i)
		else:
			print('Thumbs.db =====> PASS')

	print('\nОбработано\n')

if __name__ == '__main__':
	while True:
		main()
