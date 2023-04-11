class RedisConfig:

    def __init__(self, files) -> None:
        self.files = files

    def get(self, key):
        with open(self.files, 'r', encoding='utf-8') as file: # encoding='utf-8' это для того чтобы он распознавал русские буквы
            for line in file:
                if line.startswith(key):
                    return line.strip().split(' = ')
                
        return None
    
    def set(self, key, value):
        with open(self.files, 'a', encoding='utf-8') as file:
            file.write(f'{key}={value}\n')

    def delete(self, key):
        lines = []
        with open(self.files, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(self.files, 'w', encoding='utf-8') as file:
            for line in lines:
                if not line.startwitch(key):
                    file.write(line)

