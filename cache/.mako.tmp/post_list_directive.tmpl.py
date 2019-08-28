# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1566986587.7538445
_enable_loop = True
_template_filename = '/home/aubreymoore/.virtualenvs/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_list_directive.tmpl'
_template_uri = 'post_list_directive.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        lang = context.get('lang', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        post_list_id = context.get('post_list_id', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        lang = context.get('lang', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        post_list_id = context.get('post_list_id', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!-- Begin post-list ')
        __M_writer(str(post_list_id))
        __M_writer(' -->\n<div id="')
        __M_writer(str(post_list_id))
        __M_writer('" class="post-list">\n')
        if posts:
            __M_writer('    <ul class="post-list">\n')
            for post in posts:
                __M_writer('            <li class="post-list-item">\n            ')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('\n            &nbsp;\n            <a href="')
                __M_writer(str(post.permalink(lang)))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.title(lang))))
                __M_writer('</a>\n            </li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</div>\n<!-- End post-list ')
        __M_writer(str(post_list_id))
        __M_writer(' -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "post_list_directive.tmpl", "filename": "/home/aubreymoore/.virtualenvs/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_list_directive.tmpl", "source_encoding": "utf-8", "line_map": {"64": 17, "65": 17, "71": 65, "16": 0, "31": 18, "37": 2, "47": 2, "48": 3, "49": 3, "50": 4, "51": 4, "52": 5, "53": 6, "54": 7, "55": 8, "56": 9, "57": 9, "58": 11, "59": 11, "60": 11, "61": 11, "62": 14, "63": 16}}
__M_END_METADATA
"""
