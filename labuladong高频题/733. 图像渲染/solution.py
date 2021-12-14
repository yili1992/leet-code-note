class Solution:
    def inArea(self, x, y, image):
        if x < 0 or x > len(image) -1:
            return False
        if y < 0 or y > len(image[0]) -1 :
            return False
        return True

    def do_fill(self, image, x, y, org_color, new_color):
        if not self.inArea(x, y, image):
            return
        print(x, y)
        if image[x][y] != org_color:
            return
        if image[x][y] == -1:
            return
        image[x][y] = -1
        self.do_fill(image, x, y - 1, org_color,  new_color)
        self.do_fill(image, x, y + 1, org_color,  new_color)
        self.do_fill(image, x - 1, y, org_color, new_color)
        self.do_fill(image, x + 1, y, org_color, new_color)
        image[x][y] = new_color

    def floodFill(self, image, sr: int, sc: int, newColor: int):
        org_color = image[sr][sc]
        self.do_fill(image, sr, sc, org_color, newColor)
        return image


s = Solution()
image =[[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
print(s.floodFill(image, sr, sc, newColor))