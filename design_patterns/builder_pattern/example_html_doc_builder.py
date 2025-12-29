from typing import List


class HTMLElement:
    def __init__(self, tag: str):
        self.tag = tag
        self.attributes = {}
        self.children = []
        self.text_content = None

    def to_html(self, indent=0):
        indent_str = "  " * indent
        attr_str = ""

        if self.attributes:
            attr_str = " " + " ".join(f'{k}="{v}"' for k, v in self.attributes.items())

        if self.text_content and not self.children:
            return f"{indent_str}<{self.tag}{attr_str}>{self.text_content}</{self.tag}>"

        html = f"{indent_str}<{self.tag}{attr_str}>"

        if self.children:
            html += "\n"
            for child in self.children:
                html += child.to_html(indent + 1) + "\n"
            html += indent_str

        html += f"</{self.tag}>"
        return html


class HTMLDocument:
    def __init__(self):
        self.doctype = "<!DOCTYPE html>"
        self.html_element = HTMLElement("html")
        self.head_element = HTMLElement("head")
        self.body_element = HTMLElement("body")
        self.html_element.children.extend([self.head_element, self.body_element])

    def to_html(self):
        return self.doctype + "\n" + self.html_element.to_html()


class HTMLDocumentBuilder:
    def __init__(self):
        self.document = HTMLDocument()

    def title(self, title: str):
        title_elem = HTMLElement("title")
        title_elem.text_content = title
        self.document.head_element.children.append(title_elem)
        return self

    def meta_charset(self, charset: str = "UTF-8"):
        meta = HTMLElement("meta")
        meta.attributes["charset"] = charset
        self.document.head_element.children.append(meta)
        return self

    def meta(self, name: str, content: str):
        meta = HTMLElement("meta")
        meta.attributes["name"] = name
        meta.attributes["content"] = content
        self.document.head_element.children.append(meta)
        return self

    def stylesheet(self, href: str):
        link = HTMLElement("link")
        link.attributes["rel"] = "stylesheet"
        link.attributes["href"] = href
        self.document.head_element.children.append(link)
        return self

    def script(self, src: str):
        script = HTMLElement("script")
        script.attributes["src"] = src
        self.document.head_element.children.append(script)
        return self

    def add_to_body(self, element: HTMLElement):
        self.document.body_element.children.append(element)
        return self

    def heading(self, level: int, text: str, **attributes):
        h = HTMLElement(f"h{level}")
        h.text_content = text
        h.attributes.update(attributes)
        self.document.body_element.children.append(h)
        return self

    def paragraph(self, text: str, **attributes):
        p = HTMLElement("p")
        p.text_content = text
        p.attributes.update(attributes)
        self.document.body_element.children.append(p)
        return self

    def div(self, **attributes):
        div_elem = HTMLElement("div")
        div_elem.attributes.update(attributes)
        self.document.body_element.children.append(div_elem)
        return div_elem

    def build(self):
        return self.document.to_html()


# Usage
html = (HTMLDocumentBuilder()
        .title("My Website")
        .meta_charset()
        .meta("viewport", "width=device-width, initial-scale=1.0")
        .stylesheet("/css/style.css")
        .script("/js/app.js")
        .heading(1, "Welcome to My Website", id="main-heading")
        .paragraph("This is a paragraph of text.", class_="intro")
        .paragraph("Another paragraph here.")
        .build())

print(html)