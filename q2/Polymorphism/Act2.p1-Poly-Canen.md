a. What is duck typing, as explained in the video?
  Ans: Duck typing is a programming concept where Python cares more about what methods an object has rather than what class it belongs to. The idea comes from the saying: "If it walks like a duck and quacks like a duck, it's a duck."

b. What did the Car class need to have so it could work inside the same loop as Dog and
Cat, even if it does not inherit from the Animal class?
  Ans: The Car class just needed to have the exact same method name (catch() or move()) with the same signature so that Python could run it inside the loop without throwing an error, even without inheriting from Animal.