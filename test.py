import xsa


class String(xsa.Type):
    def check(self, context):
        context.lookup(xsa.START)
        assert context.capsulates(self.symbol)

        context.keep()


class Integer(xsa.Type):
    def check(self, context):
        assert context.call_str("isdigit")

        context.to_type(int)


class Pointer(xsa.Type):
    def check(self, context):
        assert context.parent_type(PointerContext)
        context.lookup(xsa.START)
        assert context.immidiate(self.symbol, ignore=xsa.STDLEX)
