from _ast import Call, Name, Load, keyword

from macropy.core.macros import Macros

macros = Macros()


@macros.expr
def grab(tree, **kw):
    keywords = [
        keyword(k.id, Name(k.id, Load()))
        for k in tree.elts
    ]

    return Call(
        Name('dict', Load()),
        [],
        keywords,
    )
