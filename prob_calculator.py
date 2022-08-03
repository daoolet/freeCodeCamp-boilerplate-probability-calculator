import copy
import random
# Consider using the modules imported above.

class Hat:
	def __init__(self, **balls):

		self.contents = []

		for key, value in balls.items():
			for _ in range(value):
				self.contents.append(key)

		# print(f"List of contetns: {self.contents}, Length: {len(self.contents)}")

	def draw(self, amount):

		draw_list = []

		if amount >= len(self.contents):
			# print(f"Amount greater than contents, so: {self.contents}")
			return self.contents

		for _ in range(amount):
			x = self.contents.pop(random.randrange(len(self.contents)))
			draw_list.append(x)

		# print(f"The draw list: {draw_list}")
		return draw_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	count = 0

	for _ in range(num_experiments):
		copy_hat = copy.deepcopy(hat)
		drawed_list = copy_hat.draw(num_balls_drawn)
		success = True

		for k, v in expected_balls.items():
			if drawed_list.count(k) < v:
				success = False
				break

		if success:
			count += 1

	return count/num_experiments
