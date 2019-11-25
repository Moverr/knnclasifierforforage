import graphiz
with open("tree.dot") as f:
    dot_grapgh = f.read()

graphiz.source(dot_grapgh)