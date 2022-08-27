from django.shortcuts import render
from django.http import HttpResponseRedirect


from mypesan.models import Post


def index(request):
  


  pesanku = Post.objects.all()
  if request.method == 'POST':
    Post.objects.create(
      nama = request.POST.get('Nama'),
      alamat = request.POST.get('Alamat'),
      pesan = request.POST.get('Pesan'),
    )
    return HttpResponseRedirect('/#pesanku')

  context = {
    'pesan' : pesanku,
  }

  return render(request, 'index.html', context)



