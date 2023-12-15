{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c28cef12",
   "metadata": {},
   "source": [
    "# Start off by importing the turtle module (built in with python 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73092f68",
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "655811fd",
   "metadata": {},
   "source": [
    "# Now some simple code that uses it to draw"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ef6e9cc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def christmas_tree():\n",
    "    # Setup drawing screen\n",
    "    screen = turtle.Screen()\n",
    "    screen.setup(900,870)\n",
    "\n",
    "    # Create circle object\n",
    "    circle = turtle.Turtle()\n",
    "    circle.shape('circle')\n",
    "    circle.color('red')\n",
    "    circle.speed('fastest')\n",
    "    circle.up()\n",
    "\n",
    "    # Create square object\n",
    "    square = turtle.Turtle()\n",
    "    square.shape('square')\n",
    "    square.color('green')\n",
    "    square.speed('fastest')\n",
    "    square.up()\n",
    "\n",
    "    # Start at the top and draw first red circle\n",
    "    circle.goto(0,280)\n",
    "    circle.stamp()\n",
    "\n",
    "    k = 0\n",
    "    # Iterate to create rows 1 - 16\n",
    "    for i in range(1, 17):\n",
    "        # Every iteration, go 30 pixels down\n",
    "        y = 30*i\n",
    "        \n",
    "        # Draw green squares, width is iteration minus k-variable\n",
    "        for j in range(i-k):\n",
    "            x = 30*j\n",
    "            square.goto(x,-y+280)\n",
    "            square.stamp()\n",
    "            square.goto(-x,-y+280)\n",
    "            square.stamp()\n",
    "\n",
    "        # Draw red circles once every 4 rows, starting at 0\n",
    "        if i % 4 == 0:\n",
    "            x =  30*(j+1)\n",
    "            circle.color('red')\n",
    "            circle.goto(-x,-y+280)\n",
    "            circle.stamp()\n",
    "            circle.goto(x,-y+280)\n",
    "            circle.stamp()        \n",
    "            # After every row with a red circle, decrease tree width with two\n",
    "            k += 2\n",
    "\n",
    "        # Draw yellow circles once every 4 rows, starting at 3\n",
    "        if i % 4 == 3:\n",
    "            x =  30*(j+1)\n",
    "            circle.color('yellow')\n",
    "            circle.goto(-x,-y+280)\n",
    "            circle.stamp()\n",
    "            circle.goto(x,-y+280)\n",
    "            circle.stamp() \n",
    "    \n",
    "    # Create trunk in rows 17 - 19\n",
    "    square.color('brown')\n",
    "    for i in range(17,20):\n",
    "        y = 30*i\n",
    "        for j in range(3):    \n",
    "            x = 30*j\n",
    "            square.goto(x,-y+280)\n",
    "            square.stamp()\n",
    "            square.goto(-x,-y+280)\n",
    "            square.stamp()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37100ff5",
   "metadata": {},
   "source": [
    "# Now run the code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "98df5969",
   "metadata": {},
   "outputs": [],
   "source": [
    "christmas_tree()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45aecf90",
   "metadata": {},
   "source": [
    "# Finally, close the window"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b35c1834",
   "metadata": {},
   "outputs": [],
   "source": [
    "turtle.bye()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
