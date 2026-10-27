import json
import random
from characters import Player, Enemy

class GameEngine:
    """Main engine class for the Text RPG"""
    def __init__(self, story_filename):
        self.story_filename = story_filename
        self.story_data = self.load_story()
        self.player = None

    def load_story(self):
        """Loads the story data from a JSON file"""
        try:
            with open(self.story_filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The story file '{self.story_filename}' was not found!")
            return None

    def start(self):
        """Starts the game flow"""
        if not self.story_data:
            return

        print("==========================================")
        print("     WELCOME TO TEXT RPG ENGINE           ")
        print("==========================================")
        
        player_name = input("Enter your hero's name: ").strip()
        if not player_name:
            player_name = "Wanderer"
            
        self.player = Player(player_name)
        print(f"\nHero {self.player.name} is ready for adventure!\n")

        # Get the starting scene from JSON
        current_scene_key = self.story_data.get("start_scene", "intro")
        self.play_scene(current_scene_key)

    def play_scene(self, scene_key):
        """Main scene loop handler"""
        scenes = self.story_data.get("scenes", {})
        
        while self.player.is_alive():
            scene = scenes.get(scene_key)
            if not scene:
                print("\n[Error]: Scene not found in the story file.")
                break

            print("\n" + "="*40)
            print(scene["text"])
            print("="*40)

            # Check if there is an item in the scene
            if "item" in scene:
                item = scene["item"]
                if item not in self.player.inventory:
                    self.player.inventory.append(item)
                    print(f"🎁 You found an item: {item}!")

            # Check if there is an enemy in the scene (combat logic)
            if "enemy" in scene:
                enemy_info = scene["enemy"]
                enemy = Enemy(enemy_info["name"], enemy_info["health"], enemy_info["attack"])
                print(f"\n⚠️ Warning! An enemy appears: {enemy.name} (Health: {enemy.health})")

                # Combat loop
                while enemy.is_alive() and self.player.is_alive():
                    print(f"\nYour Health: {self.player.health} | Enemy Health: {enemy.health}")
                    action = input("Action: [1] Attack [2] Parry [3] Status: ").strip()
                    
                    if action == "1":
                        enemy.take_damage(self.player.attack_power)
                        print(f"⚔️ You attacked {enemy.name} and dealt {self.player.attack_power} damage.")
                        if enemy.is_alive():
                            self.player.take_damage(enemy.attack_power)
                            print(f"💥 {enemy.name} strikes back and deals {enemy.attack_power} damage to you!")
                            
                    elif action == "2":
                        # Parry mechanic (50% success chance)
                        print("🛡️ You take a defensive stance...")
                        if random.random() < 0.5:
                            print(f"✨ Perfect Parry! You completely block {enemy.name}'s attack and counterattack!")
                            enemy.take_damage(self.player.attack_power)
                            print(f"You dealt counterattack damage: {self.player.attack_power}!")
                        else:
                            print(f"❌ You failed to react in time. {enemy.name} breaks through your defense!")
                            self.player.take_damage(enemy.attack_power)
                            print(f"You took {enemy.attack_power} damage.")
                            
                    elif action == "3":
                        self.player.show_status()
                    else:
                        print("⚠️ Invalid input, please try again.")

                if not self.player.is_alive():
                    print("\n💀 You have perished in battle... Game Over.")
                    return
                else:
                    print(f"\n🎉 Victory! You defeated {enemy.name}.")

            # Choice selection
            choices = scene.get("choices", [])
            if not choices:
                print("\nGame Over. Thank you for playing!")
                break

            print("\nWhere would you like to go?")
            for index, choice in enumerate(choices, 1):
                print(f"[{index}] {choice['text']}")

            # Protected input loop to prevent infinite re-rendering / spam
            while True:
                choice_idx = input("\nMake a choice (enter number): ").strip()
                
                if choice_idx.isdigit() and 1 <= int(choice_idx) <= len(choices):
                    selected_choice = choices[int(choice_idx) - 1]
                    scene_key = selected_choice["next_scene"]
                    break
                else:
                    print("⚠️ Invalid choice. Please enter a valid option number.")