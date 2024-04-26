def create_HTML(tag,string):
    return "<%s>%s</%s>" % (tag, string, tag)

print(create_HTML('a','b'))