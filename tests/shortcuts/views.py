from django.shortcuts import render, render_to_response
from django.template import Context, RequestContext


def render_to_response_view(request):
    return render_to_response('shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    })


def render_to_response_view_with_multiple_templates(request):
    return render_to_response([
        'shortcuts/no_such_template.html',
        'shortcuts/render_test.html',
    ], {
        'foo': 'FOO',
        'bar': 'BAR',
    })


def render_to_response_view_with_request_context(request):
    return render_to_response('shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    }, context_instance=RequestContext(request))


def render_to_response_view_with_content_type(request):
    return render_to_response('shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    }, content_type='application/x-rendertest')


def render_to_response_view_with_status(request):
    return render_to_response('shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    }, status=403)


def render_to_response_view_with_using(request):
    using = request.GET.get('using')
    return render_to_response('shortcuts/using.html', using=using)


def context_processor(request):
    return {'bar': 'context processor output'}


def render_to_response_with_context_instance_misuse(request):
    context_instance = RequestContext(request, {}, processors=[context_processor])
    # Incorrect -- context_instance should be passed as a keyword argument.
    return render_to_response('shortcuts/render_test.html', context_instance)


def render_view(request):
    return render(request, 'shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    })


def render_view_with_multiple_templates(request):
    return render(request, [
        'shortcuts/no_such_template.html',
        'shortcuts/render_test.html',
    ], {
        'foo': 'FOO',
        'bar': 'BAR',
    })


def render_view_with_base_context(request):
    return render(request, 'shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    }, context_instance=Context())


def render_view_with_content_type(request):
    return render(request, 'shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    }, content_type='application/x-rendertest')


def render_view_with_status(request):
    return render(request, 'shortcuts/render_test.html', {
        'foo': 'FOO',
        'bar': 'BAR',
    }, status=403)


def render_view_with_using(request):
    using = request.GET.get('using')
    return render(request, 'shortcuts/using.html', using=using)
