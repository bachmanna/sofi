from .element import Element

class Deleted(Element):
    """Implements <del> tag"""


    def __init__(self, text=None, cl=None, ident=None, style=None):
        super().__init__(cl=cl, ident=ident, style=style)

        if text:
            self.children.append(text)

    def __repr__(self):
        return "<Deleted>"

    def __str__(self):
        output = [ "<del" ]

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

        output.append("</del>")

        return "".join(output)
