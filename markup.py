from django_markup.markup import formatter
# from django_markup.filter.creole_filter import CreoleMarkupFilter

# MARKUP_FILTER = {
#     'creole': CreoleMarkupFilter,
#     'linebreaks': LinebreaksMarkupFilter,
#     'markdown': MarkdownMarkupFilter,
#     'none': NoneMarkupFilter,
#     'restructuredtext': RstMarkupFilter,
#     'smartypants': SmartyPantsMarkupFilter,
#     'textile': TextileMarkupFilter,
# }

with open("README.md", 'r') as myfile:
   data = formatter(myfile.read(), filter_name='markdown', safe_mode=False)
   print(data)
