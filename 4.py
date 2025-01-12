import tkinter as tk

class ConvexHullApp:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.points = []
        self.convex_hull = []

        self.canvas.bind("<Button-1>", self.add_point)
        self.button = tk.Button(self.root, text="Build Convex Hull", command=self.build_convex_hull)
        self.button.pack()

    def add_point(self, event):
        x = event.x
        y = event.y
        self.points.append((x, y))
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")

    def build_convex_hull(self):
        self.convex_hull = self.quickhull(self.points)
        self.draw_convex_hull()

    def draw_convex_hull(self):
        self.canvas.delete("convex_hull")
        n = len(self.convex_hull)
        if n > 1:
            for i in range(n):
                x1, y1 = self.convex_hull[i]
                x2, y2 = self.convex_hull[(i+1) % n]
                self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2, tags="convex_hull")

    def quickhull(self, points):
        if len(points) <= 1:
            return points
        else:
            leftmost = min(points, key=lambda p: p[0])
            rightmost = max(points, key=lambda p: p[0])
            convex_hull = [leftmost, rightmost]
            points.remove(leftmost)
            points.remove(rightmost)
            points_left = []
            points_right = []
            for point in points:
                if self.orientation(leftmost, rightmost, point) > 0:
                    points_left.append(point)
                elif self.orientation(leftmost, rightmost, point) < 0:
                    points_right.append(point)
            self.quickhull_recursive(leftmost, rightmost, points_left, convex_hull)
            self.quickhull_recursive(rightmost, leftmost, points_right, convex_hull)
            return convex_hull

    def quickhull_recursive(self, p1, p2, points, convex_hull):
        if len(points) == 0:
            return
        else:
            farthest_point = max(points, key=lambda p: self.distance(p1, p2, p))
            convex_hull.insert(convex_hull.index(p2), farthest_point)
            points.remove(farthest_point)
            points_left = []
            points_right = []
            for point in points:
                if self.orientation(p1, farthest_point, point) > 0:
                    points_left.append(point)
                elif self.orientation(farthest_point, p2, point) > 0:
                    points_right.append(point)
            self.quickhull_recursive(p1, farthest_point, points_left, convex_hull)
            self.quickhull_recursive(farthest_point, p2, points_right, convex_hull)

    def orientation(self, p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def distance(self, p1, p2, p):
        return abs((p2[1] - p1[1]) * p[0] - (p2[0] - p1[0]) * p[1] + p2[0] * p1[1] - p2[1] * p1[0])

    def run(self):
        self.root.mainloop()

app = ConvexHullApp()
app.run()