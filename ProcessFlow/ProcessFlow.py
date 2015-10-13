class Node(object):
    def __init__(self, label=None, **attrs):
        self.label = label
        self.id = label
        for attr in ['size', 'color', 'font', 'fontcolor', 'fontsize']:
            setattr(self, attr, attrs.get(attr, None))
        self._set_shape()
        
class Condition(Node):
    def _set_shape(self):
        self.shape = 'diamond'
        self.style = 'filled'
        self.fillcolor = 'purple'
        self.fontcolor = 'white'
        
class Input(Node):
    def _set_shape(self):
        self.shape = 'parallelogram'
        self.style = 'filled'
        self.fillcolor = 'blue'
        self.fontcolor = 'gold'
        
class Process(Node):
    def _set_shape(self):
        self.shape = 'box'
        self.style = 'filled'
        self.fillcolor = 'cornflowerblue'
        self.fontcolor = 'black'
        
class End(Node):
    def _set_shape(self):
        self.shape = 'invtriangle'
        self.style = 'filled'
        self.fillcolor = 'blue'
        self.fontcolor = 'gold'
        
class ProcessFlow(object):
    import pygraphviz as _pgv
    from StringIO import _StringIO
    
    def __init__(self, label=None):
        self._G = self._pgv.AGraph(label=label, id=label, directed=True, splines='ortho')
        
    def add_edge(self, u, v, label=''):
        if isinstance(u, Condition):
            assert  isinstance(label, bool), ValueError(
            'Parameter, "label", must be boolean for Conditional edges')
        self._add_node(u)
        self._add_node(v)
        self._G.add_edge(u.label, v.label, None, xlabel=label, id=u.label+'_'+v.label)
        
    def _add_node(self, node):
        if node.label not in self._G:
            attr = {}
            for key in node.__dict__:
                if node.__dict__[key] != None:
                    attr[key] = node.__dict__[key]
            self._G.add_node(node.label, **attr)
               
    def draw(self, format='svg', prog='dot'):
        output = self._StringIO()
        self._G.draw(output, format=format, prog=prog)
        return output.getvalue()