__import__('pandas')

import glob

def file_explorer(file_path, search_txt):
    file_with_txt = []
    for file in file_path:
        with open(file, 'r', encoding ='utf-8') as f:
            content = f.read()
            if search_txt in content:
                file_with_txt.append(file)

    path = 'C:\\Users\\python\\lib\\site-packages\\pandas\\'  
    print(f'파일 경로: {path}')
    print('')
    for file in file_with_txt:  
        with open(file, 'r', encoding='utf-8') as f:
            file_name = file.replace(path, '')  
            print(f"파일 이름: {file_name}")
            print("--" * 40)
            for line in f:
                if search_txt in line:
                    print(' -', line.strip())  
            print('')

search_txt = 'index'
file_path = glob.glob('C:\\Users\\python\\lib\\site-packages\\pandas\\**\\*.py', recursive=True)

print(file_explorer(file_path, search_txt))