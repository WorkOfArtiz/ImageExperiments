# here to clean shit

build :
	python img.py
	convert -delay 5 -loop 0 img-*.png animated.gif

clean :
	rm -rf animated.gif img-*.png
