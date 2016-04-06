from .element import Element

class TableHead(Element):
    """Implements the <thead> tag"""

    def __init__(self, cl=None, ident=None, style=None):
        super().__init__(cl=cl, ident=ident, style=style)

    def __repr__(self):
        return "<TableHead>"

    def __str__(self):
        output = [ "<thead" ]

        if self.ident:
            output.append(" id=\"")
            output.append(self.ident)
            output.append("\"")

        if self.cl:
            output.append(" class=\"")
            output.append(self.cl)
            output.append("\"")

        if self.style:
            output.append(" style=\"")
            output.append(self.style)
            output.append("\"")

        output.append(">")

        for child in self.children:
            output.append(str(child))

        output.append("</thead>")

        return "".join(output)
