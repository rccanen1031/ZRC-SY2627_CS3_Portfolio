1. What do all the methods (move(), special_move(), use()) in the previous activities have in
common?
  Ans: They all share the exact same method names across different classes (like move(), special_move(), or use()), but each class writes its own print action inside that method.

2. How does this activity show polymorphism in a gaming context?
  Ans: It lets us treat different game items or characters using the same general command (like calling .use() or .special_move()). We don't have to write different functions for every single class; Python automatically knows which character or item action to execute.

3. Can you think of other examples where the same action behaves differently depending on
the character or item?
  Ans: 
      attack() in a game: A Knight does a sword slash, a Wizard shoots a fireball, and a Gunner shoots a pistol.

      open() in an inventory: Opening a treasure chest grants loot, opening a door moves you to a new room, and opening a mystery box gives a random reward.
  