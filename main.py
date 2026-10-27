from engine import GameEngine

if __name__ == "__main__":
    # Инициализируем движок, передавая файл с историей
    game = GameEngine("story.json")
    game.start()