"""Fractal."""
from PIL import Image


class Fractal:
    """Fractal."""

    def __init__(self, size, scale, computation):
        """Constructor.

        Arguments:
        size -- the size of the image as a tuple (x, y)
        scale -- the scale of x and y as a list of 2-tuple
                 [(minimum_x, minimum_y), (maximum_x, maximum_y)]
        computation -- the function used for computing pixel values as a function
        """
        self.size = size
        self.scale = scale
        self.computation = computation
        self.img = Image.new("RGB", (size[0], size[1]))

    def compute(self):
        """Create the fractal by computing every pixel value."""
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                i = self.pixel_value((x, y))[0]
                quotient = i / 1000
                color = int(max(0.0, min(quotient, 1.0)) * 255.999)

                if quotient > 0.5:
                    self.img.putpixel((x, y), (color, 255, color))
                else:
                    self.img.putpixel((x, y), (0, color, 0))

    def pixel_value(self, pixel):
        """
        Return the number of iterations it took for the pixel to go out of bounds.

        Arguments:
        pixel -- the pixel coordinate (x, y)

        Returns:
        the number of iterations of computation it took to go out of bounds as integer.
        """
        x = (pixel[0] / self.size[0]) * (self.scale[1][0] - self.scale[0][0]) + self.scale[0][0]
        y = (pixel[1] / self.size[1]) * (self.scale[1][1] - self.scale[0][1]) + self.scale[0][1]
        return self.computation((x, y))[0], x, y

    def save_image(self, filename):
        """
        Save the image to hard drive.

        Arguments:
        filename -- the file name to save the file to as a string.
        """
        self.img.save(filename)


if __name__ == "__main__":
    def mandelbrot_computation(pixel):
        """Return integer -> how many iterations it takes for the pixel to escape the mandelbrot set."""
        c = complex(pixel[0], pixel[1])
        z = 0
        iterations = 0

        for i in range(1000):
            if abs(z) >= 2.0:
                break
            z = z ** 2 + c
            iterations += 1

        return iterations, z

    mandelbrot = Fractal((1000, 1000), [(-2, -2), (2, 2)], mandelbrot_computation)
    mandelbrot.compute()
    mandelbrot.save_image("mandelbrot.png")
    # mandelbrot2 = Fractal((1000, 1000), [(-0.74877, 0.065053), (-0.74872, 0.065103)], mandelbrot_computation)
    # mandelbrot2.compute()
    # mandelbrot2.save_image("mandelbrot2.png")
