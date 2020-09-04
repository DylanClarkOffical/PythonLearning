from PIL import Image
from matplotlib import colors as mcolors

## not a complete program
class WriteMessage:
		cars = ["Hello", "this", "is", "my", "color", "Img", "Generator"]
		for target_list in cars:
				print(target_list)
				pass


class GeneratecolorImg:
		while True:
				try:
						Randval1 = int(input("Enter number 1:  "))
						Randval1 = int(Randval1)
						break
				except ValueError:
						print("Not a valid integer! Please try again ...")
		while True:
				try:
						Randval2 = int(input("Enter number 2:  "))
						break
				except ValueError:
						print("Not a valid integer! Please try again ...")

		while True:
    						colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
						# Sort colors by hue, saturation, value and name.
						by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
														for name, color in colors.items())
						sorted_names = [name for hsv, name in by_hsv
				try:
						colorColor= input("enter a color eg red : ")
						if colorColor in sorted_names:
								print("colorColor in sorted_names: ...")
								pass
				except ValueError:
						print("Not a valid integer! Please try again ...")
Genimg= GeneratecolorImg()
Hworld= WriteMessage()
print(Hworld)
