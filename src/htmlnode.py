from email.policy import default


class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError('not implemented')

    def props_to_html(self):
        if self.props:
            result=''
            for prop_key,prop_value in self.props.items():
                result+= f' {prop_key}=\"{prop_value}\"'


            return result

        return ''


    def __eq__(self,other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True

        return False



    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.props_to_html()})'




class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag,value,None,props)


    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")

        if not self.tag:
            return f'{self.value}'

        result = ''
        if not self.props:
            result += f'<{self.tag}>{self.value}</{self.tag}>'

        elif self.props:
            html_prop=self.props_to_html()
            result += f'<{self.tag}{html_prop}>{self.value}</{self.tag}>'

        return result


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None,children,props)



    def to_html(self):
        if not self.tag:
            raise ValueError("Parent nodes must have a tag")

        if not self.children:
            raise ValueError("Parent nodes must have children")


        props_to_html=self.props_to_html()
        opening_tag = f'<{self.tag}{props_to_html}>'
        closing_tag = f'</{self.tag}>'

        children_html =''
        for child in self.children:
            children_html += child.to_html()

        return opening_tag + children_html + closing_tag





























