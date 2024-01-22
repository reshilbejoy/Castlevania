import os
import pygame
from Constants.window_constants import size, length_ratio, height_ratio, height, length, background_length

#I should have ju;st used json: the script
class Parser:
    def __init__(self):
        self.key = {}
        self.meta = {}
        self.map_data = []
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.curr_x = 0
        self.curr_y = 0
        self.width = 60 
        self.height_s = 40
        self.built = []

    def load_tilemap(self):
        level_path = os.path.join(self.path, '..', 'Levels', 'dungeon_1.level')

        print(level_path)
        with open(level_path, 'r') as file:
            content = file.read()
            print(content)

        sections = content.split('Key:')
        if len(sections) < 2:
            print("Failure")
        key_section, rest = sections[1].split('Meta:')
        self.parse_key_section(key_section)
        meta_section, map_section = rest.split('Map:')

        self.parse_meta_data(meta_section)
        self.parse_map_section(map_section)
     

    def parse_key_section(self, key_section):
        key_lines = key_section.split('\n')
        for line in key_lines:
            if line.strip() and ':' in line:
                key, value = line.split(':')
                key = key.strip()
                value = value.strip().rstrip(',')  
                if value and value[0] == '{' and value[-1] == '}':
                    value = value[1:-1].strip() 
                self.key[key] = value
        print("dict " + str(self.key))

    def parse_meta_data(self, meta_section):
        # Implement parsing of meta data if needed
        pass


    def parse_map_section(self, input_str):
   
        lines = input_str.strip().split('\n')
        print(lines)

        lines = [line for line in lines if not line.startswith('{') and not line.startswith('}')]
        print(lines)
        max_length = max(len(line) for line in lines)

        result = [[' ' for _ in range(max_length)] for _ in range(len(lines))]
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                result[i][j] = char
        
        self.map_data = result


    def build_level(self):
        print(self.map_data)
        for x in self.map_data:
            for y in x:
                curr_list = [] 
                if y == 'x':
         
                    image = [pygame.transform.scale(pygame.image.load('Assets/Sprites/Platform/' + self.key[y]), (60, (40)))]
                    #platform = pygame.image.load('Assets/Sprites/Platform/' + self.key[y])
                    #print(platform.wid)
                    image = [pygame.transform.scale((pygame.image.load('Assets/Sprites/Platform/' + self.key[y])), (60, (40)))]
                    
                    rect = pygame.Rect(self.curr_x, self.curr_y, self.width, self.height_s)
                    platform_type = 1
                    curr_list.append(image)
                    curr_list.append(rect)
                    curr_list.append(platform_type)
                    self.built.append(curr_list)
                if y == "o":
                    image = [pygame.transform.scale((pygame.image.load('Assets/Sprites/Additional_sprites/Candle/1.png')), (60, (40)))]
                    rect = pygame.Rect(self.curr_x, self.curr_y, self.width, self.height_s)
                    curr_list.append(image)
                    curr_list.append(rect)
                    curr_list.append(1)
                    self.built.append(curr_list)
                
                curr_list = []
                self.curr_x += 60

            self.curr_y += 50
            self.curr_x=0
        result_rects = [entry[1] for entry in self.built]
        print(result_rects)
        

    def test_map(self):
        for row in self.map_data:
            print(''.join(row))

