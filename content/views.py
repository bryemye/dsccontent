from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse
from content.models import ContentPiece, Author
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm


class ContentList(ListView):
    model = ContentPiece
    context_object_name='content_piece'

# edit view
def editContent(request, content_id):

    try:
        content = ContentPiece.objects.get(pk=content_id)
        context = {'content': content}
    except ContentPiece.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'content/edit.html',context)


#the below function attempts to edit an entry in the database.
def editDatabaseEntry(request, content_id):
    content=get_object_or_404(ContentPiece, pk=content_id)
    content.title=request.POST['title']
    content.note=request.POST['note']
    content.author=request.POST['author']
    content.save()
    return HttpResponseRedirect('/content')


#create a new database editDatabaseEntry
def newDatabaseEntry(request):

    content=ContentPiece()
    content.save()
    return HttpResponseRedirect('/content/edit/'+str(content.id), str(content.id))
