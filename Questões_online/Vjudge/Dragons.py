'''Kirito is stuck on a level of the MMORPG he is playing now. To move on in the game, he's got to defeat all n dragons that live on this level. Kirito and the dragons have strength, which is represented by an integer. In the duel between two opponents the duel's outcome is determined by their strength. Initially, Kirito's strength equals s.

If Kirito starts duelling with the i-th (1 ≤ i ≤ n) dragon and Kirito's strength is not greater than the dragon's strength xi, then Kirito loses the duel and dies. But if Kirito's strength is greater than the dragon's strength, then he defeats the dragon and gets a bonus strength increase by yi.

Kirito can fight the dragons in any order. Determine whether he can move on to the next level of the game, that is, defeat all dragons without a single loss.'''
you_power, dragon_number = map(int, input().split())
list_dragon, list_bonus= [], []
for i in range (dragon_number):
	dragon_power = None	
	dragon_power, you_bonus = map(int, input().split())
	list_bonus.append(you_bonus)
	list_dragon.append(dragon_power)
for s in range (dragon_number):
	if you_power>min(list_dragon):
		index_ = list_dragon.index(min(list_dragon))
		you_power+=list_bonus[index_]
		list_bonus.pop(index_)
		list_dragon.pop(index_)
if len(list_dragon) == 0:
	print ("YES")
else:
	print("NO")