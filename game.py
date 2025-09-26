"""Simple text-based RPG game for the CCTA project.

This module contains a minimal turn-based combat system that can be played in
the terminal. A player character faces a series of enemies and can choose
between attacking, defending, or using potions. The goal is to defeat all
enemies without running out of health.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Character:
    """Base class for the player and enemies."""

    name: str
    max_health: int
    attack_power: int
    defense: int
    health: int = field(init=False)

    def __post_init__(self) -> None:
        self.health = self.max_health

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, amount: int) -> int:
        damage = max(amount - self.defense, 1)
        self.health = max(self.health - damage, 0)
        return damage

    def heal(self, amount: int) -> int:
        new_health = min(self.health + amount, self.max_health)
        healed = new_health - self.health
        self.health = new_health
        return healed


@dataclass
class Player(Character):
    """Player character with limited healing potions."""

    potions: int = 3

    def attack(self) -> int:
        return random.randint(self.attack_power // 2, self.attack_power)

    def use_potion(self) -> int:
        if self.potions <= 0:
            return 0
        self.potions -= 1
        return self.heal(random.randint(15, 25))


@dataclass
class Enemy(Character):
    """Enemy character with a simple AI."""

    def attack(self) -> int:
        return random.randint(self.attack_power // 2, self.attack_power)


class Game:
    """Core game loop for the text-based RPG."""

    def __init__(self) -> None:
        self.player = Player(name="Aeria", max_health=80, attack_power=18, defense=4)
        self.enemies: List[Enemy] = [
            Enemy(name="Goblin", max_health=35, attack_power=12, defense=2),
            Enemy(name="Skeleton", max_health=45, attack_power=15, defense=3),
            Enemy(name="Orc", max_health=55, attack_power=18, defense=4),
            Enemy(name="Shadow Wraith", max_health=65, attack_power=20, defense=5),
        ]

    def play(self) -> None:
        print("Welcome to Aeria's Trial! Defeat all enemies to claim victory.\n")

        for enemy in self.enemies:
            print(f"A wild {enemy.name} approaches!\n")
            while enemy.is_alive() and self.player.is_alive():
                self._print_status(enemy)
                choice = self._prompt_action()
                print()

                if choice == "1":
                    damage = enemy.take_damage(self.player.attack())
                    print(f"You strike the {enemy.name} for {damage} damage!")
                elif choice == "2":
                    heal_amount = self.player.use_potion()
                    if heal_amount > 0:
                        print(f"You drink a potion and recover {heal_amount} health.")
                    else:
                        print("You are out of potions!")
                elif choice == "3":
                    print("You brace for the next attack, reducing incoming damage.")

                if enemy.is_alive():
                    self._enemy_turn(enemy, choice)
                print()

            if not self.player.is_alive():
                break

        if self.player.is_alive():
            print("Congratulations! You have defeated all foes and restored peace to the realm.")
        else:
            print("Your journey ends here. The realm awaits another hero...")

    def _enemy_turn(self, enemy: Enemy, player_choice: str) -> None:
        damage = enemy.attack()
        if player_choice == "3":
            damage //= 2
        actual_damage = self.player.take_damage(damage)
        print(f"The {enemy.name} attacks and deals {actual_damage} damage!")

    def _print_status(self, enemy: Enemy) -> None:
        print("--- Battle Status ---")
        print(f"Player: {self.player.health}/{self.player.max_health} HP | Potions: {self.player.potions}")
        print(f"Enemy:  {enemy.name} - {enemy.health}/{enemy.max_health} HP")

    def _prompt_action(self) -> str:
        print("Choose your action:")
        print("  1) Attack")
        print("  2) Use Potion")
        print("  3) Defend")

        choice = input("Enter the number of your action: ").strip()
        while choice not in {"1", "2", "3"}:
            choice = input("Please enter 1, 2, or 3: ").strip()
        return choice


def main() -> None:
    random.seed()
    Game().play()


if __name__ == "__main__":
    main()
