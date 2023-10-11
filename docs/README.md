# Math formulas for different shapes
	Functions for fast calculation for different shapes


# Area


## Circle: S = πR²

### Function
	area( par1 ) >> circleArea
	
### Parameters
	(long double) par1
	
### Return Value
	(long double) circleArea


## Rectangle: S = ab

### Function
	area( firstSide, secondSide ) >> rectangleArea
	
### Parameters
	(long double) firstSide
	(long double) secondSide
	
### Return Value
	(long double) rectangleArea


## Square: S = a²

### Function
	area( side ) >> squareArea

### Parameters
	(long double) side

### Return Value
	(long double) squareArea
	
## Area Examples

### Circle
	area( 5 )
	>> 78.540

### Rectangle
	area( 5, 4 )
	>> 20

### Square
	area( 5 )
	>> 25

# Perimeter


## Circle: P = 2πR

### Function
	perimeter( radius ) >> circlePerimeter

### Parameters
	(long double) radius

### Return Value
	(long double) circlePerimeter


## Rectangle: P = 2a + 2b

### Function
	perimeter( firstSide, secondSide ) >> rectanglePerimeter

### Parameters
	(long double) firstSide
	(long double) secondSide

### Return Value
	(long double) rectanglePerimeter

## Square: P = 4a

### Function
	perimeter( side ) >> squarePerimeter

### Parameters
	(long double) side

### Return Value
	(long double) squarePerimeter

## Perimeter Examples

### Circle
	perimeter( 5 )
	>> 31.416

### Rectangle
	perimeter( 5, 4 )
	>> 18

### Square
	perimeter( 5 )
	>> 20

# Commit history

## * commit eaf059f3b71aabe9793e753dbcaa32dc66317d19 (HEAD -> a, main)
	| Author: KonstantinMinecraft <343690@edu.itmo.ru>
	| Date:   Wed Sep 13 14:02:51 2023 +0300
	|
	|     Added triangle.py, Fixed mistake in rectangle.py
	|
## * commit 34b22008c5e3d6b33e9726d4f5e3653a22a9a39e
	| Author: KonstantinMinecraft <343690@edu.itmo.ru>
	| Date:   Wed Sep 13 14:00:03 2023 +0300
	|
	|     Added rectangle.py
	|
