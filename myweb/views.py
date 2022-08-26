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


# def Mypesan(request):
#   if request.method == 'POST':
    

#     nama = Post(nama = request.POST.get('Nama'))
#     # alamat = Post(alamat = request.POST['Alamat'])
#     # pesan = Post(pesan = request.POST['Pesan'])
#     print(nama)
#   else:
#     print('salah')
#     # if nama.is_valid():
#     #   nama.save()
#     # if alamat.is_valid():
#     #   alamat.save()
#     # if pesan.is_valid():
#     #   pesan.save()
    
  
#     return HttpResponseRedirect('/')

