class HtmlElement:
    def __init__(self, tag, text="", children=None, attrs=None):
        self.tag = tag
        self.text = text
        self.children = children or []
        self.attrs = attrs or {}

    def render(self, indent=0):
        # Build attributes string robustly: skip None keys/values and convert to str
        attrs_parts = []
        for k, v in (self.attrs or {}).items():
            if k is None:
                continue
            if v is None:
                # skip attributes with None value
                continue
            attrs_parts.append(f' {str(k)}="{str(v)}"')
        attrs = "".join(attrs_parts)

        spaces = " " * indent
        if not (self.children or []) and not self.text:
            return f"{spaces}<{self.tag}{attrs} />"

        inner = ""
        if self.text:
            inner += str(self.text)

        # Safely render children: skip None entries and objects without a callable render method
        rendered_children = []
        for child in self.children or []:
            if child is None:
                continue
            render_fn = getattr(child, "render", None)
            if not callable(render_fn):
                continue
            rendered_children.append(render_fn(indent + 1))

        if rendered_children:
            inner += "\n" + "\n".join(rendered_children) + "\n" + spaces

        return f"{spaces}<{self.tag}{attrs}>{inner}</{self.tag}>"


class HtmlBuilder:
    def __init__(self, root_tag):
        self._root = HtmlElement(root_tag)

    def add_child(self, tag, text="", **attrs):
        child = HtmlElement(tag, text=text, attrs=attrs)
        self._root.children.append(child)
        return self

    def add_nested(self, tag, **attrs):
        child = HtmlElement(tag, attrs=attrs)
        self._root.children.append(child)
        return HtmlBuilderContext(self, child)

    def build(self):
        return self._root


class HtmlBuilderContext:
    def __init__(self, parent_builder, element):
        self._parent_builder = parent_builder
        self._element = element

    def add_child(self, tag, text="", **attrs):
        child = HtmlElement(tag, text=text, attrs=attrs)
        self._element.children.append(child)
        return self

    def end(self):
        return self._parent_builder


# Usage
page = (
    HtmlBuilder("html")
    .add_child("head")
    .add_nested("body")
    .add_child("h1", "Hello, Builder!")
    .add_child("p", "This page was built step by step.")
    .end()
    .build()
)

print(page.render())
